from app import connection
from flask import jsonify

#POST Functions (CREATE)

# """How does %s work, is this fine"""
# """When they add a course should they specify interest as well?"""
def add_course(dept, num, title, avggpa = 0):     
    #SQL query addding course to Course relation       
    query = """
        INSERT INTO Course VALUES (%s, %s, %s, %s)
        """
    return


#GET Functions (Read)

#pre_req queries:
def get_prereq_chain():
    #Already written need to transfer ==> advanced query
    procedure = """
    CREATE PROCEDURE find_prereqs_cascade(
    IN targetDept VARCHAR(4),
    IN targetNum INTEGER
    )
    -- Do we need to add another begin?
    find_prereq_main:BEGIN
        DECLARE new_preCourseNum INTEGER;
        DECLARE new_preCourseDept VARCHAR(4);
        DECLARE new_reqCourseNum INTEGER;
        DECLARE new_reqCourseDept VARCHAR(4);
        DECLARE new_reqId INTEGER;
        DECLARE new_reqType ENUM('COREQ', 'PREREQ');
        
        DECLARE done BOOLEAN DEFAULT FALSE;
        
        DECLARE cur CURSOR FOR ( 
            SELECT
                pre.CourseNumber, 
                pre.CourseDepartment, 
                pre.RequiringCourseNumber, 
                pre.RequiringCourseDepartment,
                pre.RequirementGroupId,
                req.ReqType
            FROM
                (PrereqCourses pre
                JOIN RequirementGroup req ON (pre.RequirementGroupId=req.Id AND pre.RequiringCourseNumber=req.RequiringCourseNumber AND pre.RequiringCourseDepartment=req.RequiringCourseDepartment) -- Get entire requirement table
                JOIN ToVisit tv
                ON (req.RequiringCourseNumber=tv.courseNum AND req.RequiringCourseDepartment=tv.courseDept))
                
            -- ADD GROUP BY PRIMARY KEYS #NEEDS TO BE

            );
                
                
        DECLARE CONTINUE HANDLER FOR NOT Found SET done = TRUE;

        CREATE TEMPORARY TABLE RetEdgeList(
            reqCourseNum INTEGER,
            reqCourseDept VARCHAR(4),
            reqId INTEGER,
            preCourseNum INTEGER,
            preCourseDept VARCHAR(4),
            reqType ENUM('COREQ', 'PREREQ'),
            PRIMARY KEY (
                reqCourseNum, 
                reqCourseDept,
                preCourseNum,
                preCourseDept
            )
        );
        CREATE TEMPORARY TABLE Visited(
            courseDept VARCHAR(4),
            courseNum INTEGER,
            PRIMARY KEY (
                courseNum,
                courseDept
            )
        );
        CREATE TEMPORARY TABLE ToVisit(
            courseDept VARCHAR(4),
            courseNum INTEGER,
            PRIMARY KEY (
                courseNum,
                courseDept
            )
        );
        INSERT INTO ToVisit VALUES (targetDept, targetNum);
        FindPrereqLoop: LOOP
        IF (SELECT COUNT(*) FROM ToVisit)=0 THEN
            LEAVE FindPrereqLoop;
        END IF;

            OPEN cur;
                loop1: LOOP
                    FETCH cur INTO new_preCourseNum, new_preCourseDept, new_reqCourseNum, new_reqCourseDept, new_reqId, new_reqType;
                    IF done THEN LEAVE loop1;
                    END IF;
                    INSERT IGNORE INTO RetEdgeList(
                            preCourseNum,
                            preCourseDept,
                            reqCourseNum,
                            reqCourseDept,
                            reqId,
                            reqType) VALUES (new_preCourseNum, new_preCourseDept, new_reqCourseNum, new_reqCourseDept, new_reqId, new_reqType);
                        
                END LOOP loop1;
                
            CLOSE cur;
            
        INSERT IGNORE INTO Visited
            SELECT * FROM ToVisit;
        DELETE FROM ToVisit;
        INSERT INTO ToVisit
            SELECT DISTINCT preCourseDept, preCourseNum
            FROM RetEdgeList -- JOIN PONTLESS RELATION
            WHERE (preCourseDept, preCourseNum) NOT IN (
                SELECT * FROM Visited
            );
        IF (SELECT COUNT(*) FROM ToVisit)=0 THEN
            LEAVE FindPrereqLoop;
        END IF;
        END LOOP FindPrereqLoop;
        SELECT * FROM RetEdgeList;
        
        DROP TEMPORARY TABLE RetEdgeList;
        DROP TEMPORARY TABLE Visited;
        DROP TEMPORARY TABLE ToVisit;
    END//
    """

    return

def get_prereq_single_level():
    #Already written to transfer
    procedure = """
    CREATE PROCEDURE find_prereqs_single(
	IN targetDept VARCHAR(4),
    IN targetNumber INTEGER
    )
    BEGIN
	    SELECT
			pre.CourseNumber, 
            pre.CourseDepartment, 
            pre.RequiringCourseNumber, 
            pre.RequiringCourseDepartment, 
            pre.RequirementGroupId, 
            req.ReqType
		FROM
			PrereqCourses pre 
			JOIN RequirementGroup req 
            ON 
				pre.RequirementGroupId=req.Id 
                AND pre.RequiringCourseNumber=req.RequiringCourseNumber
                AND pre.RequiringCourseDepartment=req.RequiringCourseDepartment
		WHERE 
			targetDept=pre.RequiringCourseDepartment 
            AND targetNumber=pre.RequiringCourseNumber;
    END//
    """


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
    return jsonify(results)


# """Should it return the course title or Department + Number"""
def get_courses_of_interest(interest):
    #SQL query getting all the classes given the interest
    query = """
         SELECT c.CourseDepartment, c.CourseNumber
         From CourseInterest c JOIN Interest i ON(i.Id = c.InterestId)
         WHERE i.Name = %s
        """
    return

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

#inputs
#fn = professors First Name 
#ln = Professors Last Name
def get_professor(fn, ln, gpa):
    #SQL queries to search professors :

    #QUERIES WITH ONE VARIABLE GIVEN

    if gpa != None and fn == None and ln == None:
        #SQL query to get professors with AT LEAST gpa
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA = %s
                """
        return

    elif gpa == None and fn != None and ln == None:
        #SQL query to get professors with the given first name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE t.ProfessorFirstName = %s
                """
        return

    elif gpa == None and fn == None and ln != None:
        #SQL query to get professors with the given last name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE t.ProfessorLastName = %s
                """

        return

    #two variables given
    elif gpa == None and fn != None and ln != None:
        #SQL query to get professors with the given first & last name
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE t.ProfessorFirstName = %s AND t.ProfessorLastName = %s
                """
        return

    elif gpa != None and fn == None and ln != None:
        #SQL query to get professors with the given last name and AT LEAST the given GPA
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA = %s AND t.ProfessorLastName = %s
                """
        return

    elif gpa != None and fn != None and ln == None:
        #SQL query to get professors with the given first name and AT LEAST the given GPA
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA >= %s AND t.ProfessorFirstName = %s
                """
        return

    #all three given
    else:
        #sql query to get professors given first name, last name, AT LEAST the given gpa
        query = """
                SELECT t.ProfessorFirstName, t.ProfessorLastName
                FROM (TeachingCourse t JOIN Section s USING(Crn)) JOIN Course c ON((s.CourseNumber = c.Number)AND (s.CourseDepartment = c.Department))
                WHERE c.averageGPA >= %s AND t.ProfessorLastName = %s AND t.ProfessorFirstName = %s
                """
    return
    
def get_restrictions(crn, number, dept, credit_hours, start_time, end_time, days):
    #these will be sql queries to display restrictions for a given course
    #need to figure out frontend logic first dont do yet

    params = []

    query = """
            SELECT * 
            FROM Restrictions
            WHERE 1=1
            """

    return


def interest_searching():
    #sahan said this is done 
    return



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
        return

    elif title != None and gpa == None:
        #sql query just updating the title
        query = """
                UPDATE Course
                SET Title = %s
                WHERE Department = %s AND Number = %s
                """
        return

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
        return



#DELETE Functions (Delete)
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


#need to add trigger 
def trigger():
    return
