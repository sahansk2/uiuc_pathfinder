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

def json_to_generic_query(base_query, param_to_col_and_values):
    params = []
    conditions = []
    condition_base = " AND {} = %s "
    for key in param_to_col_and_values:
        params.append(key)
        conditions.append(condition_base.format(key))
    return (base_query + "".join(condition_base), tuple(params))

def query_and_get_result(query, params):
    cur = connection.cursor()
    cur.execute(query, tuple(params))
    results = cur.fetchall()
    return results

def mutate_and_get_count(query, params):
    cur = connection.cursor()
    cur.execute(query, tuple(params))
    insert_count = cur.rowcount
    connection.commit()
    return { 'affectedRows': insert_count }

############################### COURSES
@cherrypy.expose
class Courses():
    @cherrypy.tools.json_out()
    def GET(self, dept=None, number=None, title=None, gpa=None):
        query = """
        SELECT *
        FROM Course c
        WHERE 1=1
        """
        params = []
        conditions_base = " AND c.{} = %s "
        if dept is not None:
            params.append(dept)
            query += conditions_base.format("Department")
        if number is not None:
            params.append(number)
            query += conditions_base.format("Number")
        if gpa is not None:
            params.append(gpa)
            query += conditions_base.format("averageGPA")
        if title is not None:
            params.append("%{}%".format(title.lower()))
            query += " AND LOWER(c.title) LIKE %s"
        return query_and_get_result(query, params)
    
    # Confirmed to work, ZZQ 100/101
    @cherrypy.tools.json_out()
    def POST(self, dept=None, number=None, title=None, gpa=None, **kwargs):
        if not dept or not number:
            return { "affectedRows": 0 }
        else:
            query = """
            INSERT IGNORE INTO Course(Department, Number, Title, averageGPA)
            VALUES (%s, %s, %s, %s)
            """
            return mutate_and_get_count(query, [dept, number, title, gpa])

    @cherrypy.tools.json_out()
    def DELETE(self, dept=None, number=None, **kwargs):
        if not dept or not number:
            print("Bad delete on Courses, not doing anything.")
            return { "affectedRows": 0 }
        else:
            print("Attempting to delete course", dept, number)
            query = """
            DELETE FROM Course c
            WHERE c.Department=%s AND c.Number=%s
            """
            return mutate_and_get_count(query, [dept, number])
    
    @cherrypy.tools.json_out()
    def PUT(self, dept=None, number=None, gpa=None, title=None):
        if not dept or not number:
            print("Bad update on courses, not doing anything.")
            return { "affectedRows": 0 }
        else:
            query = """
            UPDATE Course
            SET {}
            WHERE Department=%s AND Number=%s"""
            set_template = "{} = %s"
            fieldNamesToUpdate = []
            valuesToSet = []
            if gpa:
                fieldNamesToUpdate.append(set_template.format('averageGPA'))
                valuesToSet.append(gpa)
            if title:
                fieldNamesToUpdate.append(set_template.format('Title'))
                valuesToSet.append(title)
            query = query.format(",".join(fieldNamesToUpdate))

            valuesToSet.extend([dept, number])
            print(query)
            return mutate_and_get_count(query, tuple(valuesToSet))

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

cherrypy.quickstart(Courses(), '/', conf)
