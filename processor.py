from validator import validate

from archive import archive_file

from logger import write_log


def process_file(file):

    write_log(f"Processing {file.name}")

    valid, reason = validate(file)

    if not valid:

        write_log(reason)

        return

    write_log("Validation Success")

    archive_file(file)

    write_log("Completed")
