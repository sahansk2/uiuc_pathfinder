const TABLES = {
    COURSES: "courses",
    SECTIONS: "sections",
    INTERESTS: "interests",
    PROFESSORS: "professors"
}

const CRUDMODE = {
    search: "search",
    create: "create",
    update: "update"
}

let defaultSearchParams = {
    nullable: false,
    type: "text"
}

let courseSearchParams = [
    {
        pretty: "Department Code",
        name: "dept",
        ...defaultSearchParams
    },
    {
        ...defaultSearchParams,
        pretty: "Number",
        type: "number",
        name: "number",
    },
    {
        pretty: "Title",
        name: "title",
        ...defaultSearchParams
    },
    {
        pretty: "Average GPA",
        name: "gpa",
        type: "number",
        nullable: true
    }
]

let professorSearchParams = [
    {
        ...defaultSearchParams,
        pretty: "Last Name",
        name: "lastName"
    },
    {
        ...defaultSearchParams,
        pretty: "First Initial",
        name: "firstName"
    },
    {
        ...defaultSearchParams,
        pretty: "Average Rating",
        name: "rating",
        type: "number",
        nullable: true
    }
]

let sectionSearchParams = [
    {
        ...defaultSearchParams,
        pretty: "CRN",
        name: "crn"
    },
    {
        ...defaultSearchParams,
        pretty: "Course Number",
        name: "number"
    },
    {
        ...defaultSearchParams,
        pretty: "Course Department",
        name: "dept"
    },
    {
        ...defaultSearchParams,
        pretty: "Credit Hours",
        name: "credits",
        type: "number",
        nullable: true
    },
    {
        ...defaultSearchParams,
        pretty: "Start Time",
        name: "timeStart",
        nullable: true
    },
    {
        ...defaultSearchParams,
        pretty: "End Time",
        name: "timeEnd",
        nullable: true
    },
    {
        ...defaultSearchParams,
        pretty: "Days",
        name: "days",
        nullable: true
    }
]

let interestSearchParams = [
    {
        ...defaultSearchParams,
        pretty: "Interest Name",
        name: "name"
    }
]

const tableToSearchParamsMap = {
    [TABLES.COURSES]: courseSearchParams,
    [TABLES.PROFESSORS]: professorSearchParams,
    [TABLES.SECTIONS]: sectionSearchParams,
    [TABLES.INTERESTS]: interestSearchParams
}

const tableToEndpointMap = {
    [TABLES.COURSES]: "https://www.blah.com/courses",
    [TABLES.PROFESSORS]: "https://www.blah.com/professors",
    [TABLES.SECTIONS]: "https://www.blah.com/sections",
    [TABLES.INTERESTS]: "https://www.blah.com/interests"
}

export {
    TABLES,
    CRUDMODE,
    tableToSearchParamsMap,
    tableToEndpointMap
}