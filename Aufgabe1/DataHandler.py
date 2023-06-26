import csv
import sqlite3
from typing import Dict
import zipfile

class DataHandler:
    def __init__(self):
        with zipfile.ZipFile("Data/ip.zip", 'r') as zip_ref:
            zip_ref.extractall("/Data")

    def getCoordinates(self, ip: int) -> Dict:
        connection = sqlite3.connect("Data/ip.db")
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM IPv4 WHERE network = '{ip}'").fetchone()
        connection.commit()
        connection.close()
        if result == None:
            return ("no data on"+str(ip), "NaN", "Nan")
        return result
