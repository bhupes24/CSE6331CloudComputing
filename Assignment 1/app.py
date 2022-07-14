import csv
import urllib
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from models.people import db, PeopleModel

# params = urllib.parse.quote_plus(r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:trial6331dbserver.database.windows.net,1433;Database=triall6331db;Uid=trial6331admin;Pwd=Admin6331;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
# engine_azure = create_engine(conn_str,echo=True)
#
# print('connection is ok')
# print(engine_azure.table_names())

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'triall6331db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/loadPeopleDataFromFile' , methods = ['GET','POST'])
def loadpeopledata():
    isSuccess=False
    if request.method == 'POST':
        print(os.path.join(basedir, 'people.csv'))
        with open(os.path.join(basedir, 'people.csv'), newline='') as f:
            reader = csv.reader(f, delimiter=',')
            cont=True
            people_list = []
            for row in reader:
                if cont:
                    cont=False
                    continue
                people = PeopleModel( name=row[0], state=row[1], salary=row[2], grade=row[3], room=row[4], telnum=row[5], picture=row[6], keywords=row[7])
                people_list.append(people)
                print(people_list)
            try:
                db.session.bulk_save_objects(people_list)
                db.session.commit()
                isSuccess = True
            except:
                isSuccess = False

            if isSuccess:
                return "Records Created Successfully"
            else:
                return "Record Crestion Failes, Please try again"

@app.route('/listpeople', methods=['GET'])
def listpeople():
    peopleList = PeopleModel.query.all()
    print(peopleList)
    return render_template("ListPeople.html", peopleList=peopleList)


@app.route('/')
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'pictures/m.jpg')
    return render_template("Hello.html", user_image=full_filename)



if __name__ == '__main__':
    app.run(debug=True)
