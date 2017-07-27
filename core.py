import time
import os
import json
from datetime import datetime


class Scanner(object):
    """
    """
    def __init__(self):
        try:
            with open("config.json") as f:
                config = json.load(f)
                self.path = config["folder"]
                self.scan_interval = config["scan_interval"]
        except Exception as i:
            print(type(i))
            print(i.args)
            print(i)
        try:
            with open("db.json") as f:
                self.db = json.load(f)
        except Exception as i:
            print(type(i))
            print(i.args)
            print(i)
        self.status = True

    def scan(self):
        files = []
        try:
            folder = os.listdir(self.path)
            for file in folder:
                if file not in self.db:
                    files.append(file)
            else:
                pass
        except Exception as i:
            print(type(i))
            print(i.args)
            print(i)

        return files


def print_file(path, file):
    file_name = path + file
    os.startfile(file_name, "print")


def log_file(files):
    current_time = str(datetime.today())
    for file in files:
        scanner.db[file] = current_time

    try:
        with open("db.json", "w") as f:
            json.dump(scanner.db, f)
    except Exception as i:
        print(type(i))
        print(i.args)
        print(i)


if __name__ == "__main__":
    print(" ---------------------------------")
    print("|            FramPrint            |")
    print(" ---------------------------------")

    scanner = Scanner()

    while True:
        files = scanner.scan()
        for file in files:
            print("PRINTING - " + file)
            print_file(scanner.path, file)
            if len(files) > 1:
                time.sleep(5)
            else:
                pass
        if len(files) > 0:
            log_file(files)
        else:
            pass

        time.sleep(scanner.scan_interval)
