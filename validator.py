def validate(file_path):

    if file_path.suffix != ".csv":

        return False, "Only CSV file allowed"

    return True, ""
