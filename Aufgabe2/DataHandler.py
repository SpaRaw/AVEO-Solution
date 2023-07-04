import sqlite3
import json
from typing import Literal, Tuple
import zipfile
import os

class DataHandler():
    def __init__(self):
        archive = zipfile.ZipFile("Data/h.zip")
        archive.extractall("Data/")


    def getNameInformation(self, name: Literal) -> Tuple:
        connection = sqlite3.connect("Data/h/Names.db")
        cursor = connection.cursor()
        result = cursor.execute(f"Select * From protagonist where Name='{name}'").fetchone()
        if result is None:
            return (name, "unknown", "0.5")
        return result
