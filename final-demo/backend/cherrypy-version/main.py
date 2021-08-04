import MySQLdb
from MySQLdb.cursors import DictCursor
import cherrypy
import cherrypy_cors

############################## CONFIGURATION
cherrypy_cors.install()
#Connects to database server
admin_user = "me" or "cs411ppdb_admin"
db_name = "cs411ppdb_experimental" + "_local"

connection = MySQLdb.connect(
    cursorclass=DictCursor,
    user=admin_user,
    passwd="passAdmin1",
    db=db_name
)
###################################################
# Useful generic functions

def json_to_generic_query(base_query, **kwargs):
    base_query += " WHERE 1=1 "
    params = []
    conditions = []
    condition_base = " AND {} = %s "
    for key in kwargs:
        params.append(key)
        conditions.append(condition_base.format(key))
    return (base_query + "".join(condition_base), tuple(params))


############################### COURSES
@cherrypy.expose
class Courses():
    @cherrypy.tools.json_out()
    def GET(self, dept, num):
        return {'this': 'isacourse'}
    
    @cherrypy.tools.json_out()
    def POST(self):
        pass

    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    
    @cherrypy.tools.json_out()
    def PUT(self):
        pass


@cherrypy.expose
class Professors():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass

@cherrypy.expose
class Section():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass


@cherrypy.expose
class Interest():
    @cherrypy.tools.json_out()
    def GET(self):
        pass
    @cherrypy.tools.json_out()
    def POST(self):
        pass
    @cherrypy.tools.json_out()
    def DELETE(self):
        pass
    @cherrypy.tools.json_out()
    def PUT(self):
        pass

@cherrypy.expose
class NiceProfessors():
    @cherrypy.tools.json_out()
    def GET(self, gpa=3.5, count=3, limit=50):
        query = """
        SELECT p.FirstName, p.LastName
        FROM Professor p JOIN TeachingCourse tc ON tc.ProfessorLastName=p.LastName AND tc.ProfessorFirstName=p.FirstName
        JOIN Section s ON tc.Crn=s.Crn JOIN Course c ON s.CourseNumber=c.Number AND s.CourseDepartment=c.Department
        WHERE c.averageGPA > %s
        GROUP BY p.FirstName, p.LastName
        HAVING COUNT(c.averageGPA) >= %s
        ORDER BY p.LastName, p.FirstName
        LIMIT %s
        """
        cur = connection.cursor()
        cur.execute(query, (float(gpa), int(count), int(limit),))
        results = cur.fetchall()
        return results


conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'cors.expose.on': True
    }
}

cherrypy.quickstart(Test(), '/', conf)
