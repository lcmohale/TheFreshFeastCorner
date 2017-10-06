import os
from cs50 import SQL
from flask import Flask, render_template, url_for, request, request, redirect


app = Flask(__name__) #tell the App the name
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
db = SQL('sqlite:///database.db') #locate the database

@app.route('/')
def index():
    #HERE WE WOULD DO ALOT OF GETTING FROM DATABASE, before we render
    Specials = db.execute('SELECT * FROM Specials ORDER BY id DESC')
    special = []
    for i in range(6):
        special.append(Specials[i])
		
    Qoutes = db.execute('SELECT * FROM Qoutes ORDER BY id DESC')
    MenuData = db.execute('SELECT * FROM MenuData')
	
    qoutes = []
    for i in range(4):
        qoutes.append(Qoutes[i])

    return render_template('index.html',Specials = special, Qoutes = qoutes)

@app.route('/input/', methods=['GET','POST'])	
def input():
    if request.method == 'GET':
        return render_template('input.html')
    else:
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special1)", special1 = request.form['Special1'])
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special2)", special2 = request.form['Special2'])
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special3)", special3 = request.form['Special3'])
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special4)", special4 = request.form['Special4'])
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special5)", special5 = request.form['Special5'])
        db.execute("INSERT INTO Specials ('SpecialName') VALUES (:special6)", special6 = request.form['Special6'])
		
		#Quotes
        db.execute("INSERT INTO Qoutes ('QouteText') VALUES (:qoute1)", qoute1 = request.form['qoute1'])
        db.execute("INSERT INTO Qoutes ('QouteText') VALUES (:qoute2)", qoute2 = request.form['qoute2'])
        db.execute("INSERT INTO Qoutes ('QouteText') VALUES (:qoute3)", qoute3 = request.form['qoute3'])
        db.execute("INSERT INTO Qoutes ('QouteText') VALUES (:qoute4)", qoute4 = request.form['qoute4'])
       
        return redirect(url_for('index'))

@app.route('/menuUpload/', methods = ['POST'])
def menuUpload():
    target = os.path.join(APP_ROOT,'static/images/')
    f1 = request.files['img1']
    f2 = request.files['img2']
    f3 = request.files['img3']
    f4 = request.files['img4']
    f5 = request.files['img5']
    f1.save(target + 'res_img_1.jpg')
    f2.save(target + 'res_img_2.jpg')
    f3.save(target + 'res_img_3.jpg')
    f4.save(target + 'res_img_4.jpg')
    f5.save(target + 'res_img_5.jpg')
	
	#db.execute("INSERT INTO MenuData ('foodName','imgRef','Price') VALUES (:foodName,:imgRef,:Price)", foodName = request.form['foodName1'],imgRef = request.form['imgRef'],Price = request.form['price1'])
	
	
	
	
    return redirect(url_for('index'))
	
if __name__ == '__main__':
    app.run(debug = True);
