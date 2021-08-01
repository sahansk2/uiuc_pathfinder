#initializes the flask app 
from flask import Flask
import MySQLdb
from MySQLdb.cursors import DictCursor

#defines the app
app = Flask(__name__)


#Connects to database server
admin_user = "cs411ppdb_admin"
db_name = "cs411ppdb_experimental"

connection = MySQLdb.connect(
    cursorclass=DictCursor,
    user=admin_user,
    passwd="passAdmin1",
    db=db_name
)



