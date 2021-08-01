import { TABLES } from './configAdminDashboard'

const courseView = {
    dept: {
        pretty: "Course",
        pos: 0
    },
    num: {
        pretty: "Department",
        pos: 1
    },
    title: {
        pretty: "Title",
        pos: 2,
        limit: 10
    },
    gpa: {
        pretty: "Average GPA",
        nullable: true,
        pos: 3
    }
}

const tableToViewMap = {
    [TABLES.COURSES]: courseView
}

export {
    tableToViewMap
}