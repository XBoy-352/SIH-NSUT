import mysql.connector as sql
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

mydb = sql.connect(host = "localhost", database = "aadhaar", user = "root", password = "vanssh1234aalok?")
db = mydb.cursor()

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/output', methods = ['POST', 'GET'])
def output():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        aadhaar = request.form['aadhaar']
        db.execute(''' INSERT INTO authentication VALUES(%s,%s)''',(roll_no,aadhaar))
        mydb.commit()
        db.close()
        return redirect(url_for("output"))
    else:
        return render_template('output.html')

if __name__ == '__main__':
    app.run(debug = True)
mydb.close()
