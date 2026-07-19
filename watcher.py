from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time

from processor import process_file


class FileWatcher(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file = Path(event.src_path)

        process_file(file)


def start_watcher():

    observer = Observer()

    observer.schedule(FileWatcher(), "./input", recursive=False)

    observer.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
