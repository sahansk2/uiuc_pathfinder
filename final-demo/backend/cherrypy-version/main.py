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
        conditions_end = " LIMIT 60"
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

        query += conditions_end
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
    def GET(self, firstName=None, lastName=None, rating=None):
        query = """
        SELECT *
        FROM Professor
        WHERE 1=1
        """
        params = []
        conditions_base = " AND {} = %s "
        conditions_end = " LIMIT 60"
        if firstName is not None:
            params.append(firstName)
            query += conditions_base.format("FirstName")
        if lastName is not None:
            params.append(lastName)
            query += conditions_base.format("LastName")
        if rating is not None:
            params.append(rating)
            query += conditions_base.format("Rating")

        query += conditions_end
        return query_and_get_result(query, params)

    @cherrypy.tools.json_out()
    def POST(self, firstName=None, lastName=None, rating=None):
        if not firstName or not lastName:
            return { "affectedRows": 0 }
        else:
            query = """
            INSERT IGNORE INTO Professor(FirstName, LastName, Rating)
            VALUES (%s, %s, %s)
            """
            return mutate_and_get_count(query, [firstName, lastName, rating])

    @cherrypy.tools.json_out()
    def DELETE(self, firstName=None, lastName=None, **kwargs):
        if not firstName or not lastName:
            print("Bad delete for professor, not doing anything")
            return { "affectedRows": 0 }
        else:
            query = """
            DELETE FROM Professor
            WHERE FirstName = %s AND LastName = %s
            """
            return mutate_and_get_count(query, [firstName, lastName])

    @cherrypy.tools.json_out()
    def PUT(self, firstName=None, lastName=None, rating=None, **kwargs):
        if not firstName or not lastName:
            print("Bad update on professor, not doing anything")
            return { "affectedRows": 0 }
        else:
            query = """
            UPDATE Professor
            SET {}
            WHERE FirstName=%s AND LastName=%s"""
            set_template = "{} = %s"
            fieldNamesToUpdate = []
            valuesToSet = []
            if rating:
                fieldNamesToUpdate.append(set_template.format('Rating'))
                valuesToSet.append(rating)
            query = query.format(",".join(fieldNamesToUpdate))
            valuesToSet.extend([firstName, lastName])
            print(query)
            return mutate_and_get_count(query, tuple(valuesToSet))

@cherrypy.expose
class Section():
    @cherrypy.tools.json_out()
    def GET(self, crn=None, number=None, dept=None, credits=None, timeStart=None, timeEnd=None, days=None):
        query = """
        SELECT *
        FROM Section
        WHERE 1=1
        """
        params = []
        conditions_base = " AND {} = %s "
        conditions_end = " LIMIT 60"
        if crn is not None:
            params.append(crn)
            query += conditions_base.format("Crn")
        if number is not None:
            params.append(number)
            query += conditions_base.format("CourseNumber")
        if dept is not None:
            params.append(dept)
            query += conditions_base.format("CourseDepartment")
        if credits is not None:
            params.append(credits)
            query += conditions_base.format("creditHours")
        if timeStart is not None:
            params.append(timeStart)
            query += conditions_base.format("startTime")
        if timeEnd is not None:
            params.append(timeEnd)
            query += conditions_base.format("endTime")
        if days is not None:
            params.append(days)
            query += conditions_base.format("days")
        
        query += conditions_end
        print(query)
        return query_and_get_result(query, params)

    @cherrypy.tools.json_out()
    def POST(self, crn=None, number=None, dept=None, credits=None, timeStart=None, timeEnd=None, days=None):
        if not crn:
            return { "affectedRows": 0 }
        else:
            query = """
            INSERT IGNORE INTO Section
            (`Crn`,
            `CourseNumber`,
            `CourseDepartment`,
            `creditHours`,
            `startTime`,
            `endTime`,
            `days`)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s);
            """
            return mutate_and_get_count(query, [
                crn, number, dept, credits, timeStart, timeEnd, days
            ])

    @cherrypy.tools.json_out()
    def DELETE(self, crn=None, **kwargs):
        if not crn:
            print("No CRN found, will not delete")
            return { 'affectedRows': 0 }
        else:
            query = """
            DELETE FROM Section
            WHERE Crn=%s
            """
            return mutate_and_get_count(query, [crn])

    @cherrypy.tools.json_out()
    def PUT(self, crn=None, number=None, dept=None, credits=None, timeStart=None, timeEnd=None, days=None):
        if not crn:
            print("Bad update on section, not doing anything")
            return { "affectedRows": 0 }
        else:
            query = """
            UPDATE Section
            SET {}
            WHERE Crn=%s"""
            set_template = "{} = %s"
            fieldNamesToUpdate = []
            valuesToSet = []
            if number:
                fieldNamesToUpdate.append(set_template.format('CourseNumber'))
                valuesToSet.append(number)
            if dept:
                fieldNamesToUpdate.append(set_template.format("CourseDepartment"))
                valuesToSet.append(dept)
            if credits:
                fieldNamesToUpdate.append(set_template.format("creditHours"))
                valuesToSet.append(credits)
            if timeStart:
                fieldNamesToUpdate.append(set_template.format('startTime'))
                valuesToSet.append(timeStart)
            if timeEnd:
                fieldNamesToUpdate.append(set_template.format('endTime'))
                valuesToSet.append(timeEnd)
            if days:
                fieldNamesToUpdate.append(set_template.format('days'))
                valuesToSet.append(days)
            query = query.format(",".join(fieldNamesToUpdate))
            valuesToSet.extend([crn])
            print(query)
            return mutate_and_get_count(query, tuple(valuesToSet))


@cherrypy.expose
class Interest():
    @cherrypy.tools.json_out()
    def GET(self, keyword):
        query = """
        SELECT Name
        FROM Interest
        WHERE LOWER(Name) like %s
        LIMIT 60
        """

        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(keyword.lower()),))
        results = cur.fetchall()
        return results  
        
    @cherrypy.tools.json_out()
    def POST(self, name, id):
        query = """
            INSERT INTO Interest ('Name','Id')
            VALUES (%s, %s)
            """
        cur = connection.cursor()
        cur.execute(query, (str(name), int(id)))
        insert_count = cur.rowcount 
        connection.commit()

        return [{ 'insertedRows': insert_count }]

    @cherrypy.tools.json_out()
    def DELETE(self, name, id):
        query = """
        DELETE FROM Interest
        Where LOWER(Name) LIKE %s AND Id = %s
        """
        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(name.lower()), int(id)))
        delete_count = cur.rowcount
        connection.commit()
        return [{ 'deletedRows': delete_count }]

    @cherrypy.tools.json_out()
    def PUT(self, name):
        pass
        

@cherrypy.expose
class NiceProfessors():
    @cherrypy.tools.json_out()
    def GET(self, gpa=3.5, count=3, limit=60):
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

@cherrypy.expose
class CourseInfo():
    @cherrypy.tools.json_out()
    def GET(self, dept, num):
        query = """
        SELECT c.Title, c.Department, c.Number, c.averageGPA, p.FirstName, p.LastName, p.Rating, r.Detail
        FROM ((((
        Course c JOIN Section s 
        ON (c.Number = s.CourseNumber AND c.Department = s.CourseDepartment))
        JOIN TeachingCourse tc
        ON (tc.Crn = s.Crn))
        JOIN Professor p
        ON (p.FirstName = tc.ProfessorFirstName AND p.LastName = tc.ProfessorLastName))
        JOIN Restriction r
        ON (r.Crn = s.Crn))
        WHERE c.Number = %s AND c.Department LIKE %s 
        LIMIT 60    
        """

        cur = connection.cursor()
        cur.execute(query, (int(num), "%{}%".format(dept.lower(), int(limit))))
        results = cur.fetchall()

        #python processing heres
        return results


    @cherrypy.expose
    class CourseContext():
        @cherrypy.tools.json_out()
        def GET(self, dept, num):
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
            """
            cur = connection.cursor()
            cur.execute(query, (num, dept, num, dept, int(limit)))
            results = cur.fetchall()
            return results

conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'cors.expose.on': True
    }
}

cherrypy.tree.mount(Courses(), '/course', conf)
cherrypy.tree.mount(Professors(), '/professor', conf)
cherrypy.tree.mount(Section(), '/section', conf)
cherrypy.tree.mount(NiceProfessors(), '/nice', conf)
cherrypy.quickstart()
