from app import db #from oour ther python programm called app we are importing db object

db.create_all() #using db object to craete the table in postgreSQL DB

#this program will throw warning we can ignore

#We are instantiating Data class from here as this will send app as the value for the __name__ variable instead of main 
