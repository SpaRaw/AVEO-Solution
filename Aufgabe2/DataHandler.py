import sqlite3
import json
from typing import Literal, Tuple
import zipfile

class DataHandler():
    def __init__(self):
        with zipfile.ZipFile("Data/first_names.zip", 'r') as zip_ref:
            zip_ref.extractall("/Data")

    def loadDataIntoDataBase(self) -> None:
        connection = sqlite3.connect("first_names.db")
        cursor = connection.cursor()

        with open("Data/first_names.json", encoding="utf8") as file:
            data = json.load(file)
            for name, stats in data.items():
                isFemale = stats["gender"].__contains__("F")
                isMale = stats["gender"].__contains__("M")

                if isMale and isFemale:
                    if stats["gender"]["F"] < stats["gender"]["M"]:
                        cursor.execute(f"INSERT INTO Names VALUES ('{name}', 'M', '{stats['gender']['M']}')")
                    elif stats["gender"]["F"] > stats["gender"]["M"]:
                        cursor.execute(f"INSERT INTO Names VALUES ('{name}', 'F', '{stats['gender']['F']}')")
                    else:
                        cursor.execute(f"INSERT INTO Names VALUES ('{name}', 'O', '0.00')")
                else:
                    if isMale:
                        cursor.execute(f"INSERT INTO Names VALUES ('{name}', 'M', '{stats['gender']['M']}')")

                    if isFemale:
                        cursor.execute(f"INSERT INTO Names VALUES ('{name}', 'F', '{stats['gender']['F']}')")
                connection.commit()
            connection.close()

    def getNameInformation(self, name: Literal) -> Tuple:
        connection = sqlite3.connect("first_names.db")
        cursor = connection.cursor()
        result = cursor.execute(f"Select * From Names where name='{name}'").fetchone()
        if result is None:
            return (name, "unknown", "0.5")
        return result
