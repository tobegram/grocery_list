import sqlite3

groceries = [
	"Pudding",
    "Maultaschen",
    "Tomaten (passiert)",
    "Tomate (stückig)"
    "Chilli con Carne (fertig),"
    "Milch (Hafer)",
    "Knoblauch",
    "Ghee",
    "Mehl (Dinkel Typ 610)",
    "Butter",
    "Kaffee (gemahlen)",
    "Maultaschen",
    "Schupfnudeln",
    "Apfelmark",
    "Gries (Dinkel)",
    "Geschirrspülmittel",
    "Eier",
    "Olivenöl",
    "Parmesan (am Stück)",
    "Schlagsahne",
    "Spaghetti"
    
    ""
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