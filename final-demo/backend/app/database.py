from app import connection
from flask import jsonify

#this is where we need to make all the sql queries

# Example from Flask Lecture Video:

# def fetch_todo() -> dict:
#     """Reads all tasks listed in the todo table

#     Returns:
#         A list of dictionaries
#     """

#     conn = db.connect()
#     query_results = conn.execute("Select * from tasks;").fetchall()
#     conn.close()
#     todo_list = []
#     for result in query_results:
#         item = {
#             "id": result[0],
#             "task": result[1],
#             "status": result[2]
#         }
#         todo_list.append(item)

#     return todo_list

#pre_req queries:
def get_prereq_chain():
    #Already written need to transfer
    return

def get_prereq_single_level():
    #Already written to transfer
    return

#professor queries
def get_professor_rating(lastname):
    query = """
    SELECT *
    FROM Professor p
    WHERE p.LastName = %s
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
    WHERE p.LastName = %s
    """
    cur = connection.cursor()
    cur.execute(query, ("%{}%".format(lastname),))
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
    cur.execute(query, (float(gpa), int(count), int(limit),))
    results = cur.fetchall()
    return results


# """Should it return the course title or Department + Number"""
def get_courses_of_interest(interest):
    #SQL query getting all the classes given the interest
    query = """
         SELECT c.CourseDepartment, c.CourseNumber
         From CourseInterest c JOIN Interest i ON(i.Id = c.InterestId)
         WHERE i.Name = %s

        """
    return

#adding and deleting 
# 
# """How does %s work, is this fine"""
# """When they add a course should they specify interest as well?"""
def add_course(dept, num, title, avggpa = 0):     
    #SQL query addding course to Course relation       
    query = """
        INSERT INTO Course VALUES (%s, %s, %s, %s)

        """
    return

def delete_course(dept, num):
    #SQL query deleting course
    query = """
        DELETE FROM Course
        WHERE Number = %s AND Department = %s

        DELETE FROM CourseInterest
        WHERE CourseNumber = %s AND CourseDepartment = %s
        """
    return

def delete_restriction(crn, detail):
    query = """DELETE FROM Restriction rst
        WHERE rst.Crn = %s AND rst.Detail = %s
        """
    return

def update_course(dept, number, title, gpa):
    #SQL query to update course. Note dept and number will be used in WHERE clause, the title and gpa are what is getting changed
    if title == None and gpa != None:
        #sql query just updating the gpa
        query = """
                UPDATE Course
                SET averageGPA = %s
                WHERE Department = %s AND Number = %s
                """
        return

    if title != None and gpa == None:
        #sql query just updating the title
        query = """
                UPDATE Course
                SET Title = %s
                WHERE Department = %s AND Number = %s
                """
        return

    if title != None and gpa != None:
        #sql query just updating the gpa, and title
        query = """
                UPDATE Course
                SET averageGPA = %s
                WHERE Department = %s AND Number = %s

                UPDATE Course
                SET Title = %s
                WHERE Department = %s AND Number = %s
                """
        return


    return

#course searching

#"""Should it return the course title or Department + Number"""
def course_search(dept, num, gpa):                    
    #only one variable is given 
    if gpa != None and dept == None and num == None:
        #SQL query to get courses with the given gpa
        query = """
                SELECT Department, Number
                FROM Course
                WHERE averageGPA = %s
                """
        return

    elif gpa == None and dept != None and num == None:
        #SQL query to get courses with the given dept
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Department = %s
                """
        return

    elif gpa == None and dept == None and num != None:
        #SQL query to get courses with the given num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s
                """
        return

    #two variables given
    elif gpa == None and dept != None and num != None:
        #SQL query to get courses with the given dept and num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND Department = %s
                """
        return

    elif gpa != None and dept == None and num != None:
        #SQL query to get courses with the given gpa and num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND averageGPA = %s
                """
        return

    elif gpa != None and dept != None and num == None:
        #SQL query to get courses with the given dept and gpa
        query = """
                SELECT Department, Number
                FROM Course
                WHERE averageGPA = %s AND Department = %s
                """
        return

    #all three given
    else:
        #sql query to get courses given gpa, dept, & num
        query = """
                SELECT Department, Number
                FROM Course
                WHERE Number = %s AND Department = %s AND averageGPA = %s
                """
        return

