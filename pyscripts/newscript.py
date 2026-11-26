from pathlib import Path
import csv
CSV_FILE = Path("C:/Users/ohana/Downloads/data.csv")

def csv_reader():
    devices = {}

    with open (CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            device_name = row["Device Name"]
            devices[device_name] = {
                "ip_address" : row["IP Address"],
                "username" : row["Username"],
                "password" : row["Password"]
            }

