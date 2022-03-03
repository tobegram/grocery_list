import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "0000"

@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["shopping_items"] = get_db()
    return render_template("index.html", all_items=session["all_items"], 
                                shopping_items=session["shopping_items"])

@app.route("/add_items", methods=["POST"])
def add_items():
    session["shopping_items"].append(request.form["my_selection"])
    return render_template("index.html", all_items=session["all_items"], 
                                shopping_items=session["shopping_items"]) 
    
@app.route("/remove_items", methods=["POST", "GET"])
def remove_items():
    checked_boxes = request.form.getlist("my_input")
    
    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True
    
    return render_template("index.html", all_items=session["all_items"], 
                                shopping_items=session["shopping_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute("select * from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[1]) for val in all_data]
        
        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]
        
    return all_data, shopping_list

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
if __name__ == '__main__':
    app.run(debug=True)
