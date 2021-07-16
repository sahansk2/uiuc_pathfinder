-- Get context of a course in its tree (where does it lie?)
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
				WHERE pre.CourseNumber=225
                AND pre.CourseDepartment='CS') AS unlockables
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
				WHERE req.RequiringCourseNumber=225
                AND req.RequiringCourseDepartment='CS')
		LIMIT 15;

