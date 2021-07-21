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
    def highgpaprofs(self, gpa=3.5, count=3, limit=50):
        query = """
        SELECT p.FirstName, p.LastName
        FROM Professor p JOIN TeachingCourse tc ON tc.ProfessorLastName=p.LastName AND tc.ProfessorFirstName=p.FirstName
        JOIN Section s ON tc.Crn=s.Crn JOIN Course c ON s.CourseNumber=c.Number AND s.CourseDepartment=c.Department
        WHERE c.averageGPA > %s
        GROUP BY p.FirstName, p.LastName
        HAVING COUNT(c.averageGPA) >= %s
        LIMIT %s
        """
        cur = connection.cursor()
        cur.execute(query, (float(gpa), int(count), int(limit),))
        results = cur.fetchall()
        return results
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def coursecontext(self, dept, num, limit=50):
        query = """
        SELECT * FROM (SELECT
                pre.CourseNumber,
                pre.CourseDepartment,
                pre.RequiringCourseNumber,
                pre.RequiringCourseDepartment,
                pre.RequirementGroupId,
                req.ReqType
            FROM
                (PrereqCourses pre
                JOIN RequirementGroup req
                ON
                    pre.RequirementGroupId=req.Id
                    AND pre.RequiringCourseNumber=req.RequiringCourseNumber
                    AND pre.RequiringCourseDepartment=req.RequiringCourseDepartment) -- Get entire requirement table
                WHERE pre.CourseNumber=%s
                AND pre.CourseDepartment=%s) AS unlockables
        UNION
            (SELECT
                pre.CourseNumber,
                pre.CourseDepartment,
                pre.RequiringCourseNumber,
                pre.RequiringCourseDepartment,
                pre.RequirementGroupId,
                req.ReqType
            FROM
                (PrereqCourses pre
                JOIN RequirementGroup req
                ON
                    pre.RequirementGroupId=req.Id
                    AND pre.RequiringCourseNumber=req.RequiringCourseNumber
                    AND pre.RequiringCourseDepartment=req.RequiringCourseDepartment) -- Get entire requirement table
                WHERE req.RequiringCourseNumber=%s
                AND req.RequiringCourseDepartment=%s)
        LIMIT %s;
        """
        cur = connection.cursor()
        cur.execute(query, (num, dept, num, dept, int(limit)))
        results = cur.fetchall()
        return results
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def course(self, dept, num, title, rating='NULL'):
        query = """
        INSERT IGNORE INTO Course
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
        connection.commit()
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
        connection.commit()
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
        connection.commit()
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