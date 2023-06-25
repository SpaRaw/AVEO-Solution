import csv
import sqlite3
from typing import Dict

class DataHandler:

    def getCoordinates(self, ip: int) -> Dict:
        connection = sqlite3.connect("Data/ip.db")
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM ip WHERE network = '{ip}'").fetchone()
        connection.commit()
        connection.close()
        if result == None:
            return ("no data on"+str(ip), "NaN", "Nan")
        return result