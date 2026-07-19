from pathlib import Path
import shutil

def archive_file(file):

    destination = Path("./archive") / file.name

    shutil.move(file, destination)
