import cherrypy
import MySQLdb
from MySQLdb.cursors import DictCursor

admin_user = "cs411ppdb_admin"
db_name = "cs411ppdb_experimental"

connection = MySQLdb.connect(
    cursorclass=DictCursor,
    user=admin_user,
    passwd="passAdmin1",
    db=db_name
)

class BackendApp():
    @cherrypy.expose
    def index(self):
        return "Midterm server is running"
    
    @cherrypy.expose
    def section(self):
        return "This endpoint deletes sections"
    
    @cherrypy.expose
    @cherrypy.tools.json_out() # Automatically respond with json
    def courses(self, keyword, limit=10):
        query = """
        SELECT * FROM Course c
        WHERE LOWER(c.Title) LIKE %s
        ORDER BY c.Title
        LIMIT %s
        """
        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(keyword.lower()), int(limit)))
        results = cur.fetchall()
        return results
    

cherrypy.quickstart(BackendApp())