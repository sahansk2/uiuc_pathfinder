USE cs411ppdb_experimental;

CREATE TABLE Interest(
	Name VARCHAR(255) UNIQUE NOT NULL,
    Id INTEGER AUTO_INCREMENT,
    PRIMARY KEY (Id)
);

CREATE TABLE Course(
	Title VARCHAR(255) NOT NULL,
    Number INTEGER,
    Department VARCHAR(4),
    averageGPA REAL,
    PRIMARY KEY (Number, Department)
);

CREATE TABLE CourseInterest(
	InterestId INTEGER NOT NULL,
    CourseNumber INTEGER,
    CourseDepartment VARCHAR(4),
    PRIMARY KEY (InterestId, CourseNumber, CourseDepartment),
    FOREIGN KEY (InterestId)
		REFERENCES Interest(Id),
	FOREIGN KEY (CourseNumber, CourseDepartment)
 		REFERENCES Course(Number, Department)
);

CREATE TABLE Professor(
	FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Rating REAL,
    PRIMARY KEY (FirstName, LastName)
);


CREATE TABLE Section(
	Crn INTEGER,
    CourseNumber INTEGER NOT NULL,
    CourseDepartment VARCHAR(4) NOT NULL,
    creditHours INTEGER,
    startTime VARCHAR(8),
    endTime VARCHAR(8),
    days VARCHAR(5),
    PRIMARY KEY (Crn),
    FOREIGN KEY (CourseNumber, CourseDepartment)
		REFERENCES Course(Number, Department)
);

CREATE TABLE TeachingCourse(
	ProfessorLastName VARCHAR(100),
    ProfessorFirstName VARCHAR(100),
    Crn Integer,
    PRIMARY KEY (ProfessorLastName, ProfessorFirstName, Crn),
    FOREIGN KEY (Crn)
		REFERENCES Section(Crn),
	FOREIGN KEY (ProfessorFirstName, ProfessorLastName)
		REFERENCES Professor(FirstName, LastName)
);

CREATE TABLE Restriction(
	Crn INTEGER,
    Detail VARCHAR(255),
    PRIMARY KEY (Crn, Detail),
    FOREIGN KEY (Crn) REFERENCES Section(Crn)
);

CREATE TABLE RequirementGroup(
	RequiringCourseNumber INTEGER,
    RequiringCourseDepartment VARCHAR(4),
    Id INTEGER,
    ReqType ENUM('COREQ', 'PREREQ'),
    PRIMARY KEY (RequiringCourseNumber, RequiringCourseDepartment, Id),
    FOREIGN KEY (RequiringCourseNumber, RequiringCourseDepartment)
		REFERENCES Course(Number, Department)
);

CREATE TABLE PrereqCourses(
	CourseNumber INTEGER,
    CourseDepartment VARCHAR(4),
	RequiringCourseNumber INTEGER,
    RequiringCourseDepartment VARCHAR(4),
    RequirementGroupId INTEGER,
    PRIMARY KEY (CourseNumber, CourseDepartment, RequiringCourseNumber, RequiringCourseDepartment, RequirementGroupId),
	FOREIGN KEY (RequiringCourseNumber, RequiringCourseDepartment, RequirementGroupId) 
		REFERENCES RequirementGroup(RequiringCourseNumber, RequiringCourseDepartment, Id),
    FOREIGN KEY (CourseNumber, CourseDepartment)
		REFERENCES Course(Number, Department)
);
