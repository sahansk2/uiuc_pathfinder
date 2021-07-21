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
    @cherrypy.tools.json_out()
    def course(self, dept, num, title, rating='NULL'):
        query = """
        INSERT INTO `cs411ppdb_experimental_local`.`Course`
        (`Title`,
        `Number`,
        `Department`,
        `averageGPA`)
        VALUES
        (%s, %s, %s, %s);
        """
        cur = connection.cursor()
        cur.execute(query, (dept, num, title, rating))
        insert_count = cur.rowcount
        return { 'insertedRows': insert_count }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def profrating(self, firstname, lastname, rating):
        query = """
        UPDATE Professor
        SET
        Rating = %s
        WHERE FirstName = %s AND LastName = %s;
        """
        cur = connection.cursor()
        cur.execute(query, (rating, firstname, lastname))
        impact_count = cur.rowcount
        return { 'updatedRows': impact_count }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delrestriction(self, interest, detail):
        query = """
        DELETE FROM Restriction rst
        WHERE rst.Crn = %s AND rst.Detail = %s
        """
        cur = connection.cursor()
        cur.execute(query, (interest, detail))
        delete_count = cur.rowcount
        return { 'deletedRows': delete_count }


    @cherrypy.expose
    @cherrypy.tools.json_out() # Automatically respond with json
    def courses(self, keyword, limit=10):
        # you can hit this endpoint at /courses?keyword=whatever
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