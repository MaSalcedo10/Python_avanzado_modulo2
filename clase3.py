# MANEJO DE ARCHIVOS CSV #

import csv
from pathlib import Path

FILE_PATH = Path("users.csv")

def read_csv():
    try:
        with open(FILE_PATH, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row.get("first_name") + " : " + row.get("email"))
    except FileNotFoundError:
        print("EL ARCHIVO users.csv NO EXISTE. PRIMERO DEBES CREARLO.")
        
def write_csv():
    try:
        with open(FILE_PATH, 'a') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["first_name", "last_name", "email"]
            )
            #first_name,last_name,email
            writer.writerows([
            {
                "first_name": "Miguel",
                "last_name": "García",
                "email": "miguel@example.com"
            },
            {
                "first_name": "Ana",
                "last_name": "López",
                "email": "ana@example.com"
            }])
    except Exception as e:
        print("OCURRIÓ UN ERROR AL ESCRIBIR EN EL ARCHIVO: ", e)         
            

if __name__ == "__main__":
    write_csv()
    read_csv()