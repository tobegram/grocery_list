import sqlite3

groceries = [
	"Äpfel",
    "Tomaten",
    "Tomaten (passiert)"
]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
	cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()