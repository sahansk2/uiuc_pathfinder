from app import connection
from flask import jsonify

#POST Functions (CREATE)

# """How does %s work, is this fine"""
# """When they add a course should they specify interest as well?"""
def add_course(dept, num, title, avggpa = None):     
    #SQL query addding course to Course relation       
    query = """
            INSERT INTO Course ('Department', 'Number', 'Title', 'averageGPA')
            VALUES (%s, %s, %s, %s)
            """

    cur = connection.cursor()
    cur.execute(query, (str(dept), int(num), str(title), float(avggpa)))
    insert_count = cur.rowcount
    connection.commit()

    return [{ 'insertedRows': insert_count }]

def add_professor(fn, ln, rating):
    query = """
            INSERT INTO Professor ('FirstName', 'LastName', 'Rating')
            VALUES (%s, %s, %s)
            """
    cur = connection.cursor()
    cur.execute(query, (str(fn), str(ln), int(rating)))
    insert_count = cur.rowcount 
    connection.commit()

    return [{ 'insertedRows': insert_count }]

def add_section(crn, number, dept, hours, stime, etime , days):
    query = """
            INSERT INTO Section ('Crn', 'CourseNumber', 'CourseDepartment', 'creditHours', 'startTime', 'endTime', 'days')
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
    cur = connection.cursor()
    cur.execute(query, (int(crn), int(number), str(dept), int(hours), str(stime), str(etime) , str(days)))
    insert_count = cur.rowcount 
    connection.commit()

    return [{ 'insertedRows': insert_count }]

def add_interests(name, id):
    query = """
            INSERT INTO Section ('Name','Id')
            VALUES (%s, %s)
            """
    cur = connection.cursor()
    cur.execute(query, (str(name), int(id)))
    insert_count = cur.rowcount 
    connection.commit()

    return [{ 'insertedRows': insert_count }]

###################################################################################
#GET Functions (Read)
###################################################################################

def course_search(dept, num, gpa):                    
    #only one variable is given 
    if gpa != None and dept == None and num == None:
        #SQL query to get courses with the given gpa
        query = """
                SELECT Department, Number
                FROM Course
                WHERE averageGPA = %s
                """

        cur = connection.cursor()
        cur.execute(query, (float(gpa),))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa == None and dept != None and num == None:
        #SQL query to get courses with the given dept
        query = """
                SELECT Department, Number
                FROM Course
                WHERE LOWER(Department) LIKE %s
                """
        
        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(dept.lower(),)))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa == None and dept == None and num != None:
        #SQL query to get courses with the given num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s
                """

        cur = connection.cursor()
        cur.execute(query, (int(num),))
        results = cur.fetchall()

        return jsonify(results)

    #two variables given
    elif gpa == None and dept != None and num != None:
        #SQL query to get courses with the given dept and num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND LOWER(Department) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, (int(num), "%{}%".format(dept.lower(),)))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa != None and dept == None and num != None:
        #SQL query to get courses with the given gpa and num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND averageGPA = %s
                """
        cur = connection.cursor()
        cur.execute(query, (int(num), float(gpa)))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa != None and dept != None and num == None:
        #SQL query to get courses with the given dept and gpa
        query = """
                SELECT Department, Number
                FROM Course
                WHERE averageGPA = %s AND LOWER(Department) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa), "%{}%".format(dept.lower(),)))
        results = cur.fetchall()

        return jsonify(results)

    #all three given
    else:
        #sql query to get courses given gpa, dept, & num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND LOWER(Department) LIKE %s AND averageGPA = %s
                """

        cur = connection.cursor()
        cur.execute(query, (int(num), "%{}%".format(dept.lower(),), int(dept)))
        results = cur.fetchall()

        return jsonify(results)

#inputs
#fn = professors First Name 
#ln = Professors Last Name
def get_professor(fn, ln, gpa = 0):
    #SQL queries to search professors :

    #QUERIES WITH ONE VARIABLE GIVEN

    if gpa != None and fn == None and ln == None:
        #SQL query to get professors with AT LEAST gpa
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA >= %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa),))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa == None and fn != None and ln == None:
        #SQL query to get professors with the given first name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE LOWER(t.ProfessorFirstName) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(fn.lower()),))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa == None and fn == None and ln != None:
        #SQL query to get professors with the given last name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE LOWER(t.ProfessorLastName) LIKE %s
                """

        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(ln.lower()),))
        results = cur.fetchall()

        return jsonify(results)

    #two variables given
    elif gpa == None and fn != None and ln != None:
        #SQL query to get professors with the given first & last name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE LOWER(t.ProfessorFirstName) LIKE %s AND LOWER(t.ProfessorLastName) LIKE %s
                """
        
        cur = connection.cursor()
        cur.execute(query, ("%{}%".format(fn.lower()),"%{}%".format(ln.lower())))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa != None and fn == None and ln != None:
        #SQL query to get professors with the given last name and AT LEAST the given GPA
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA = %s AND LOWER(t.ProfessorLastName) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa),"%{}%".format(ln.lower())))
        results = cur.fetchall()

        return jsonify(results)

    elif gpa != None and fn != None and ln == None:
        #SQL query to get professors with the given first name and AT LEAST the given GPA
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA >= %s AND LOWER(t.ProfessorFirstName) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa),"%{}%".format(fn.lower())))
        results = cur.fetchall()

        return jsonify(results)

    #all three given
    else:
        #sql query to get professors given first name, last name, AT LEAST the given gpa
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA >= %s AND LOWER(t.ProfessorLastName) LIKE %s AND LOWER(t.ProfessorFirstName) LIKE %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa), "%{}%".format(ln.lower()),"%{}%".format(fn.lower())))
        results = cur.fetchall()

        return jsonify(results)



def get_section(crn, num, dept, hours, start, end, days):
    #these will be sql queries to display restrictions for a given course
    #need to figure out frontend logic first dont do yet

    params = []
    # Where 1=1 is just to simplify the logic here
    query = "SELECT FROM Section WHERE 1=1 "
    # To allow for easier dynamic making
    condition_base = "AND {} = %s \n"
    conditions = []
    if crn is not None:
        params.append(crn)
        conditions.append(condition_base.format("Crn"))
    if num is not None:
        params.append(num)
        conditions.append(condition_base.format("CourseNumber"))
    if dept is not None:
        params.append(dept)
        conditions.append(condition_base.format("CourseDepartment"))
    if hours is not None:
        params.append(hours)
        conditions.append(condition_base.format("creditHours"))
    if start is not None:
        params.append(start)
        conditions.append(condition_base.format("startTime"))
    if end is not None:
        params.append(end)
        conditions.append(condition_base.format("endTime"))
    if days is not None:
        params.append(days)
        conditions.append(condition_base.format("days"))

    query += " ".join(conditions)

    cur = connection.cursor()
    cur.execute(query, tuple(params))
    results = cur.fetchall()

    return jsonify(results)


def get_interest(keyword):
    query = """
    SELECT Name
    FROM Interest
    WHERE LOWER(Name) like %s
    """

    cur = connection.cursor()
    cur.execute(query, ("%{}%".format(keyword.lower()),))
    results = cur.fetchall()
    return results

#professor queries
def get_professor_rating(lastname):
    query = """
    SELECT *
    FROM Professor p
    WHERE LOWER(p.LastName) LIKE %s
    ORDER BY p.LastName, p.FirstName
    """
    cur = connection.cursor()
    cur.execute(query, ("%{}%".format(lastname),))
    results = cur.fetchall()

    return jsonify(results)

def get_professor_classes(lastname):
    query = """ 
    SELECT c.Title, c.Department, C.Number
    FROM (Professor p 
    JOIN TeachingCourse tc 
    ON (p.FirstName = tc.ProfessorFirstName AND p.LastName = tc.ProfessorLastName))
    JOIN Sections s 
    ON (s.Crn = tc.CRN)
    JOIN Course c 
    ON (c.Department = s.CourseDepartment AND c.Number = s.CourseNumber)
    WHERE LOWER(p.LastName) LIKE %s
    """
    cur = connection.cursor()
    cur.execute(query, ("%{}%".format(lastname.lower()),))
    results = cur.fetchall()

    return jsonify(results)

def get_highgpaprofs(gpa=3.5, count=3, limit=50):
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
    cur.execute(query, (float(gpa), int(count), int(limit)))
    results = cur.fetchall()
    return jsonify(results)


# """Should it return the course title or Department + Number"""
def get_courses_of_interest(interest):
    #SQL query getting all the classes given the interest
    query = """
         SELECT c.CourseDepartment, c.CourseNumber
         From CourseInterest c JOIN Interest i ON(i.Id = c.InterestId)
         WHERE LOWER(i.Name) LIKE %s
        """
    cur = connection.cursor()
    cur.execute(query, ("%{}%".format(interest.lower()),))
    results = cur.fetchall()

    return jsonify(results)


#DO 
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


#PUT/PATCH Functions (Update)
def update_course(dept, number, title, gpa):
    #SQL query to update course. Note dept and number will be used in WHERE clause, the title and gpa are what is getting changed
    if title == None and gpa != None:
        #sql query just updating the gpa
        query = """
                UPDATE Course
                SET averageGPA = %s
                WHERE Department = %s AND Number = %s
                """
        
        cur = connection.cursor()
        cur.execute(query, (float(gpa), str(dept), int(number)))
        impact_count = cur.rowcount
        connection.commit()
        return [{ 'updatedRows': impact_count }]

    elif title != None and gpa == None:
        #sql query just updating the title
        query = """
                UPDATE Course
                SET Title = %s
                WHERE Department = %s AND Number = %s
                """
        cur = connection.cursor()
        cur.execute(query, (str(title), str(dept), int(number)))
        impact_count = cur.rowcount
        connection.commit()
        return [{ 'updatedRows': impact_count }]

    elif title != None and gpa != None:
        #sql query just updating the gpa, and title
        query = """
                UPDATE Course
                SET averageGPA = %s
                WHERE Department = %s AND Number = %s
                UPDATE Course
                SET Title = %s
                WHERE Department = %s AND Number = %s
                """
        cur = connection.cursor()
        cur.execute(query, (float(gpa), str(dept), int(number), str(title), str(dept), int(number)))
        impact_count = cur.rowcount
        connection.commit()
        return [{ 'updatedRows': impact_count }]



#DELETE Functions (Delete)
def delete_course(dept, num):
    #SQL query deleting course
    query = """
        DELETE FROM Course
        WHERE Number = %s AND LOWER(Department) LIKE %s;
        """
        #ADD CONSTRAINT IN mySQL workbench
    
    cur = connection.cursor()
    cur.execute(query, (int(num), "%{}%".format(dept.lower())))
    delete_count = cur.rowcount
    connection.commit()
    return [{ 'deletedRows': delete_count }]

def delete_restriction(crn, detail):
    query = """DELETE FROM Restriction rst
        WHERE rst.Crn = %s AND LOWER(rst.Detail) LIKE %s
        """

    cur = connection.cursor()
    cur.execute(query, (int(crn), "%{}%".format(detail.lower())))
    delete_count = cur.rowcount
    connection.commit()
    return [{ 'deletedRows': delete_count }]


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

def get_course_info(dept, num):
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
    """

    cur = connection.cursor()
    cur.execute(query, (int(num), "%{}%".format(dept.lower())))
    results = cur.fetchall()
    return results

def get_prereq_chain(targetdept, targetnum):
#Already written need to transfer ==> advanced query
#Notes

    cur = connection.cursor()
    data = cur.callproc('find_prereqs_cascade',(targetdept, targetnum))[0]

    return data