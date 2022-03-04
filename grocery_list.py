import sqlite3

groceries = [
	"Pudding",
    "Maultaschen",
    "Tomaten (passiert)",
    "Tomate (stückig)",
    "Chilli con Carne (fertig)",
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
# create a connection to the grocery_list.db
# create an cursor object to interact with database 
connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

# Create a table in grocery_list.db with 
# 1. column id index and
# 2. column groceries
# loop will add every item in grocery list into db table
cursor.execute("CREATE TABLE groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
	cursor.execute("INSERT INTO groceries (name) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()