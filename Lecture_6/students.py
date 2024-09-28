import csv 

name = input("What is your name?")
home = input("Where is your home")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": home})