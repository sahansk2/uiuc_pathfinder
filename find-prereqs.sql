USE cs411ppdb_experimental;

DELIMITER //
CREATE PROCEDURE find_prereqs_cascade(
    IN targetDept VARCHAR(4),
    IN targetNum INTEGER
)
find_prereq_main:BEGIN
	-- Variables to hold results of cursors.
	DECLARE iterReqDept, iterPreDept VARCHAR(4);
    DECLARE iterReqNum, iterReqId, iterPreNum INTEGER;
    DECLARE iterReqType ENUM('COREQ', 'PREREQ');
    DECLARE iterDone BOOLEAN DEFAULT FALSE;
    -- Cursor for immediate prereqs for parent
	DECLARE parentPreReqCur CURSOR FOR (
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
            AND targetNum=pre.RequiringCourseNumber);    
	-- Definition of temporary tables
    -- RetEdgeList: contains table to be returned, is an edge list
    -- Visited: Necessary tables for BFS operation
    -- ToVisit: Necessary tables for BFS operation
	DECLARE CONTINUE HANDLER FOR NOT FOUND set iterDone=TRUE;
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
    -- BEGIN ALGORITHM HERE
    OPEN parentPreReqCur;
    -- Step 1: Insert all children into table
    scrapeParent: REPEAT
        FETCH FROM parentPreReqCur INTO iterPreNum, iterPreDept, iterReqNum, iterReqDept, iterReqId, iterReqType;
		INSERT IGNORE INTO RetEdgeList(reqCourseNum, reqCourseDept, preCourseNum, preCourseDept, reqId, reqType)
			VALUE (iterReqNum, iterReqDept, iterPreNum, iterPreDept, iterReqId, iterReqType);
    UNTIL iterDone END REPEAT;
    SET iterDone = FALSE;
    CLOSE parentPreReqCur;
    -- Mark parent as visited
	INSERT INTO Visited VALUES (targetDept, targetNum);
    
    whileHasUnvisitedPrereqs: LOOP
    BEGIN
		-- Iteration: Insert all unvisited prerequisites into ToVisit
		DECLARE childCur CURSOR FOR (
			SELECT DISTINCT preCourseDept, preCourseNum
            FROM RetEdgeList
            WHERE (preCourseDept, preCourseNum) NOT IN (
				SELECT * FROM Visited
            )
        );
        OPEN childCur;
        childLoop: REPEAT
			FETCH FROM childCur INTO iterPreDept, iterPreNum;
            INSERT IGNORE INTO ToVisit(courseDept, courseNum) VALUE (iterPreDept, iterPreNum);
        UNTIL iterDone=True END REPEAT;
        SET iterDone = FALSE;
        CLOSE childCur;
        -- End Iteration
        -- If there are no more courses to visit, leave the loop; we're done.
        IF (SELECT COUNT(*) FROM ToVisit)=0
        THEN
			LEAVE whileHasUnvisitedPrereqs;
        END IF;
    END;
    BEGIN
		DECLARE willVisitCourseDept VARCHAR(4);
        DECLARE willVisitCourseNum INTEGER;
		DECLARE willVisitCur CURSOR FOR (
			SELECT * FROM ToVisit
        );
        OPEN willVisitCur;
        -- Iterate over course that needs to be visited.
        visitCourses: REPEAT
        BEGIN -- willVisit
			FETCH willVisitCur INTO willVisitCourseDept, willVisitCourseNum;
            -- Iterate over prerequisite group for each course that needs to be visited
            BEGIN -- willVisitPrereqs (updates RetEdgeList, Visited)
				DECLARE willVisitPrereqIterDone BOOLEAN DEFAULT FALSE;
				DECLARE willVisitPrereqsCur CURSOR FOR (
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
						willVisitCourseDept=pre.RequiringCourseDepartment 
						AND willVisitCourseNum=pre.RequiringCourseNumber
				);
                DECLARE CONTINUE HANDLER FOR NOT FOUND SET willVisitPrereqIterDone=TRUE;
                -- Iteration: Insert each prereq into the final table
                OPEN willVisitPrereqsCur;
                REPEAT 
					FETCH FROM willVisitPrereqsCur INTO iterPreNum, iterPreDept, iterReqNum, iterReqDept, iterReqId, iterReqType;
					INSERT IGNORE INTO RetEdgeList(reqCourseNum, reqCourseDept, preCourseNum, preCourseDept, reqId, reqType)
						VALUE (iterReqNum, iterReqDept, iterPreNum, iterPreDept, iterReqId, iterReqType);
				UNTIL willVisitPrereqIterDone=TRUE END REPEAT;
                CLOSE willVisitPrereqsCur;
                SET willVisitPrereqIterDone=FALSE;
                -- End iteration
                INSERT IGNORE INTO Visited(courseDept, courseNum) VALUE (willVisitCourseDept, willVisitCourseNum);
            END; -- willVisitPrereqs
        END;-- willVisits
        UNTIL iterDone END REPEAT;
        SET iterDone = FALSE;
DELETE FROM ToVisit;
	LEAVE find_prereq_main;
    END;
    END LOOP whileHasUnvisitedPrereqs;
    -- END ALGORITHM HERE
SELECT 
    *
FROM
    RetEdgeList;
    -- Do cleanup
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


SELECT DISTINCT preCourseDept, preCourseNum
            FROM RetEdgeList
            WHERE (preCourseDept, preCourseNum) NOT IN (
				SELECT * FROM Visited
            );
SELECT * FROM ToVisit;