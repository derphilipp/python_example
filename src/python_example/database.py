import csv
import os


FILENAME = "database.csv"


def append_to_database(number, result, iteration) -> None:
    """
    This DB would consist of only one simple table with 3 columns:
    The integer used as input to calculate the palindrome,
    the resulting palindrome and the number
    of cycles needed to calculate the palindrome.
    """
    # Check if file exists and open in appropriate mode
    file_exists = os.path.isfile(FILENAME)
    mode = "a" if file_exists else "w"

    # Open the file and write/append the data
    with open(FILENAME, mode, newline="") as file:
        writer = csv.writer(file)
        # If the file is being created, write the header
        if not file_exists:
            writer.writerow(["Number", "Result", "Iteration"])
        # Write the data
        writer.writerow([number, result, iteration])


def load_from_database() -> list:
    """Reads the database file and returns a list of tuples with the data."""
    # TODO: Rewrite this to use a generator, to work with large files
    data = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader)
        # Read the data
        for row in reader:
            data.append((int(row[0]), int(row[1]), int(row[2])))
    return data
