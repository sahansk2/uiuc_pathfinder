-- Select professors who teach more than 3 courses with an average GPA higher than 3.5
-- They're probably cool people if they're always involved in classes with high GPA, after all
SELECT p.FirstName, p.LastName
	FROM Professor p JOIN TeachingCourse tc ON tc.ProfessorLastName=p.LastName AND tc.ProfessorFirstName=p.FirstName
    JOIN Section s ON tc.Crn=s.Crn JOIN Course c ON s.CourseNumber=c.Number AND s.CourseDepartment=c.Department
    WHERE c.averageGPA > 3.5
    GROUP BY p.FirstName, p.LastName
    HAVING COUNT(c.averageGPA) > 3
    LIMIT 15;