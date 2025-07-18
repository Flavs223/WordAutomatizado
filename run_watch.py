#Codigo para refrescar la pantalla
import subprocess
import time
import os
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

RUTA_MAIN = "main.py"

# Mata cualquier instancia previa de main.py
def kill_existing_main():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and RUTA_MAIN in ' '.join(proc.info['cmdline']):
                print(f"🛑 Terminando proceso anterior (PID {proc.pid})")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        kill_existing_main()
        self.process = subprocess.Popen(["python", RUTA_MAIN])

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔄 Cambio detectado en: {event.src_path}")
            if self.process.poll() is None:
                self.process.kill()
            time.sleep(0.5)
            self.process = subprocess.Popen(["python", RUTA_MAIN])

if __name__ == "__main__":
    command = f"python {RUTA_MAIN}"
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print("👀 Esperando cambios en el código...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
