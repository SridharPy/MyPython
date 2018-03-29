from flask import Flask, render_template, request

from flask.ext.sqlalchemy import SQLAlchemy #flask.ext.sqlalchemy is used to state thata SQLAlchemy libraray is installed in flask directory in same parent  directory

#virtual--> lib-->flask--> ext--> __int__.py the SQLAlchecmy is here

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres@localhost/PythonDB" #Providing the db connection string for our web "app" : postgresql://uid:pwd@servername/db_name
db=SQLAlchemy(app) #Creating SQLAlchemy object for our web app named "app"

class Data(db.Model):
    #we are accessing Model class from SQLAlchemy object named "db". Our class Data is inherting from Model class
    __tablename__="User_Data" #Here we provide the table name which will be created in postgresql db
    id=db.Column(db.Integer,primary_key=True) #Providing columns name, data type and constraint for table data
    email_id=db.Column(db.String(120),unique=True) #email_id column will be fo String with a limit of 120 characters and unique value
    height_cm=db.Column(db.Integer)

    def __init__(self,email_id,height_cm): #Initialize the instance variable
        self.email_id=email_id
        self.height_cm=height_cm
    #We will not instatiate this class Data from here as it will run as main so we will run this script from python console then we run from app import db
    #the we run db.create_all() to create the table in the postgresql
    #or run the script craetedb.py




@app.route("/") #This is the decorator for home page
def index():
    return render_template("index.html") #this page will be diplayed in home page

@app.route("/success", methods=["POST"]) #For HTML POST in index.html page's form the below page will be shown, default is get if not specified
def success():
    if request.method=='POST':
        email=request.form["email_val"] #Here email_val is grabbed from index.html(whatever value is entered in page) and stored in email variable
        height=request.form["height_val"]
        print(request.form) #prints email and height in the console from html form.
        print(email,height) #Printing variable values

        if db.session.query(Data).filter(Data.email_id==email).count()==0: #Here we are checking if email already exists in the DB if no execute below code
            data=Data(email,height)#Craeteing object or intantiating Data class and grabbing email and height values from the frontend web app
            db.session.add(data) #adding the email and height captured by data object of Data lass and adding  it to the dB tabel
            db.session.commit()#Commiting the values added
            return render_template("success.html")#this page will be renderd when submit is pressed; described in index.htm form
        return render_template("index.html", text="This email id already exists")

if __name__=="__main__":
    app.debug=True
    app.run(port=5001) #if port not specified then port 5000 is used
