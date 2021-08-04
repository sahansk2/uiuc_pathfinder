import { TABLES } from './configAdminDashboard'

const courseView = {
    Department: {
        pretty: "Course",
        pos: 0
    },
    Number: {
        pretty: "Department",
        pos: 1
    },
    Title: {
        pretty: "Title",
        pos: 2,
        limit: 10
    },
    averageGPA: {
        pretty: "Average GPA",
        nullable: true,
        pos: 3
    }
}

const sectionView = {
    Crn: {
        pretty: "CRN",
        pos: 0
    },
    CourseNumber: {
        pretty: "Course Number",
        pos: 2
    },
    CourseDepartment: {
        pretty: "Course Department",
        pos: 1
    },
    creditHours: {
        pretty: "Credit Hours",
        pos: 3
    },
    startTime: {
        pretty: "Starting Time",
        pos: 4
    },
    endTime: {
        pretty: "Ending Time",
        pos: 5
    },
    days: {
        pretty: "Days",
        pos: 6
    }
}

const professorView = {
    FirstName: {
        pretty: "First Name",
        pos: 0
    },
    LastName: {
        prettY: "Last Name",
        pos: 1
    },
    Rating: {
        pretty: "RMP Rating",
        pos: 2
    }
}


const interestView = {
    Name: {
        pretty: "Interest Name",
        pos: 0
    },
    Id: {
        pretty: "ID (read only)",
        pos: 1
    }
}

const tableToViewMap = {
    [TABLES.COURSES]: courseView,
    [TABLES.SECTIONS]: sectionView,
    [TABLES.PROFESSORS]: professorView,
    [TABLES.INTERESTS]: interestView
}

export {
    tableToViewMap
}