USE cs411ppdb_experimental;

DELIMITER //

CREATE PROCEDURE find_prereqs_cascade(
    IN targetDept VARCHAR(4),
    IN targetNum INTEGER
)
find_prereq_main:BEGIN
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

    INSERT IGNORE INTO RetEdgeList(
			preCourseNum,
			preCourseDept,
			reqCourseNum,
			reqCourseDept,
            reqId,
			reqType)
		SELECT
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
				JOIN ToVisit tv
                ON
						req.RequiringCourseNumber=tv.courseNum
                    AND req.RequiringCourseDepartment=tv.courseDept; -- Join with that which needs to be visited
	INSERT IGNORE INTO Visited
		SELECT * FROM ToVisit;
	DELETE FROM ToVisit;
    INSERT INTO ToVisit
		SELECT DISTINCT preCourseDept, preCourseNum
        FROM RetEdgeList
        WHERE (preCourseDept, preCourseNum) NOT IN (
			SELECT * FROM Visited
		);
	IF (SELECT COUNT(*) FROM ToVisit)=0 THEN
		LEAVE FindPrereqLoop;
	END IF;
    END LOOP;
	SELECT * FROM RetEdgeList;
    
    DROP TEMPORARY TABLE RetEdgeList;
    DROP TEMPORARY TABLE Visited;
    DROP TEMPORARY TABLE ToVisit;
END//

DELIMITER ;

DROP PROCEDURE `find_prereqs_cascade`;

DROP TEMPORARY TABLE RetEdgeList;
DROP TEMPORARY TABLE Visited;
DROP TEMPORARY TABLE ToVisit;
CALL find_prereqs_cascade('CS', 225);

CALL find_prereqs_cascade('ECE', 210);
SELECT * FROM RetEdgeList;
CALL find_prereqs_single('CS', 225);
-- Procedure to find all immediate prereqs
DELIMITER //
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
DELIMITER ;

SHOW PROCESSLIST;
DROP PROCEDURE find_prereqs_cascade;

SELECT * FROM ToVisit;
CALL find_prereqs_cascade('CS', 374);


