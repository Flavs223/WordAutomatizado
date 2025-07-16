#Este código me permite crear un manera de actualizar la ventana de la aplicación sin necesidad de guardar
#Instalar la libería:   pip install watchdog
#Esto desde el bash
# Esto para actualizar la version en que caso de que lo solicite  python.exe -m pip install --upgrade pip

import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print("🔄 Código modificado, reiniciando...")
            self.process.kill()
            time.sleep(0.5)
            self.process = subprocess.Popen(self.command, shell=True)

if __name__ == "__main__":
    command = "python main.py"  # 👈 Asegúrate que es tu punto de entrada
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print("👀 Esperando cambios en tu proyecto...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
