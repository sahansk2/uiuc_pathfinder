DELIMITER //
CREATE PROCEDURE find_reverse_depends(
	IN targetDept VARCHAR(4),
    IN targetNum INTEGER
)
BEGIN
	CREATE TEMPORARY TABLE RetEdgeListParents(
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
    CREATE TEMPORARY TABLE VisitedParents(
		courseDept VARCHAR(4),
        courseNum INTEGER
    );
    
    CREATE TEMPORARY TABLE ParentToVisit(
		courseDept VARCHAR(4),
        courseNum INTEGER
    );
    
    INSERT INTO ParentToVisit VALUE (targetDept, targetNum);
    FindRevDepLoop: LOOP
    INSERT IGNORE INTO RetEdgeListParents(
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
				JOIN ParentToVisit tv
				ON
						pre.CourseNumber=tv.courseNum
                    AND pre.CourseDepartment=tv.courseDept;  -- Get all entries where course appears as dependency
	INSERT IGNORE VisitedParents SELECT * FROM ParentToVisit;
    DELETE FROM ParentToVisit;
    INSERT IGNORE INTO ParentToVisit
		SELECT DISTINCT reqCourseDept, reqCourseNum FROM RetEdgeListParents WHERE
        (reqCourseDept, reqCourseNum) NOT IN (SELECT * FROM VisitedParents);
	IF (SELECT COUNT(*) FROM ParentToVisit)=0 THEN
		LEAVE FindRevDepLoop;
	END IF;
	END LOOP FindRevDepLoop;
    
	SELECT * FROM RetEdgeListParents;
    DROP TEMPORARY TABLE VisitedParents;
    DROP TEMPORARY TABLE ParentToVisit;
    DROP TEMPORARY TABLE RetEdgeListParents;
END//
DELIMITER ; 
DROP TEMPORARY TABLE VisitedParents;
DROP TEMPORARY TABLE ParentToVisit;
DROP TEMPORARY TABLE RetEdgeListParents;

CALL find_reverse_depends('ECE', 110);