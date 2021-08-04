import { endpointBase } from '../config'

const endpointBaseAdmin = endpointBase + '/admin'

const TABLES = {
    COURSES: "courses",
    SECTIONS: "sections",
    INTERESTS: "interests",
    PROFESSORS: "professors"
}

const CRUDMODE = {
    search: "GET",
    create: "POST",
    update: "PUT",
    delete: "DELETE"
}

const defaultSearchParams = {
    nullable: false,
    type: "text"
}

const courseFields = {
    dept: {
        pretty: "Department Code",
        name: "dept",
        ...defaultSearchParams
    },
    number: {
        ...defaultSearchParams,
        pretty: "Number",
        type: "number",
        name: "number",
    },
    title: {
        pretty: "Title",
        name: "title",
        ...defaultSearchParams
    },
    gpa: {
        pretty: "Average GPA",
        name: "gpa",
        type: "number",
        nullable: true
    }
}

const courseSearchParams = [
    courseFields.dept,
    courseFields.number,
    courseFields.title,
    courseFields.gpa
]

const courseCreateParams = [
    courseFields.dept,
    courseFields.number,
    courseFields.title,
    courseFields.gpa
]

const courseUpdateParams = [
    courseFields.dept,
    courseFields.number,
    courseFields.title,
    courseFields.gpa
]

const courseDeleteParams = [
    courseFields.dept,
    courseFields.number
]

const professorFields = {
    lastName: {
        ...defaultSearchParams,
        pretty: "Last Name",
        name: "lastName"
    },
    firstName: {
        ...defaultSearchParams,
        pretty: "First Initial",
        name: "firstName"
    },
    rating: {
        ...defaultSearchParams,
        pretty: "Average Rating",
        name: "rating",
        type: "number",
        nullable: true
    }
}

const professorSearchParams = [
    professorFields.lastName,
    professorFields.firstName,
    professorFields.rating
]

const professorCreateParams = [
    professorFields.lastName,
    professorFields.firstName,
    professorFields.rating
]

const professorUpdateParams = [
    professorFields.lastName,
    professorFields.firstName,
    professorFields.rating
]

const professorDeleteParams = [
    professorFields.lastName,
    professorFields.firstName
]

const sectionFields = {
    crn: {
        ...defaultSearchParams,
        pretty: "CRN",
        name: "crn"
    },
    number: {
        ...defaultSearchParams,
        pretty: "Course Number",
        name: "number"
    },
    dept: {
        ...defaultSearchParams,
        pretty: "Course Department",
        name: "dept"
    },
    credits: {
        ...defaultSearchParams,
        pretty: "Credit Hours",
        name: "credits",
        type: "number",
        nullable: true
    },
    timeStart: {
        ...defaultSearchParams,
        pretty: "Start Time",
        name: "timeStart",
        nullable: true
    },
    timeEnd: {
        ...defaultSearchParams,
        pretty: "End Time",
        name: "timeEnd",
        nullable: true
    },
    days: {
        ...defaultSearchParams,
        pretty: "Days",
        name: "days",
        nullable: true
    }
}

const sectionSearchParams = [
    sectionFields.crn,
    sectionFields.number,
    sectionFields.dept,
    sectionFields.credits,
    sectionFields.timeStart,
    sectionFields.timeEnd,
    sectionFields.days
]

const sectionCreateParams = [
    sectionFields.crn,
    sectionFields.number,
    sectionFields.dept,
    sectionFields.credits,
    sectionFields.timeStart,
    sectionFields.timeEnd,
    sectionFields.days
]

const sectionUpdateParams = [
    sectionFields.crn,
    sectionFields.number,
    sectionFields.dept,
    sectionFields.credits,
    sectionFields.timeStart,
    sectionFields.timeEnd,
    sectionFields.days
]

const sectionDeleteParams = [
    sectionFields.crn
]

const interestFields = {
    name: {
        ...defaultSearchParams,
        pretty: "Interest Name",
        name: "name"
    }
}

const interestSearchParams = [
    interestFields["name"],
]

const interestDeleteParams = [
    interestFields["name"],
]

const interestUpdateParams = [
    interestFields["name"],
]

const interestCreateParams = [
    interestFields["name"],
]

const tableToSearchParamsMap = {
    [TABLES.COURSES]: courseSearchParams,
    [TABLES.PROFESSORS]: professorSearchParams,
    [TABLES.SECTIONS]: sectionSearchParams,
    [TABLES.INTERESTS]: interestSearchParams
}

const tableToDeleteParamsMap = {
    [TABLES.COURSES]: courseDeleteParams,
    [TABLES.PROFESSORS]: professorDeleteParams,
    [TABLES.SECTIONS]: sectionDeleteParams,
    [TABLES.INTERESTS]: interestDeleteParams
}

const tableToUpdateParamsMap = {
    [TABLES.COURSES]: courseUpdateParams,
    [TABLES.PROFESSORS]: professorUpdateParams,
    [TABLES.SECTIONS]: sectionUpdateParams,
    [TABLES.INTERESTS]: interestUpdateParams
}

const tableToCreateParamsMap = {
    [TABLES.COURSES]: courseCreateParams,
    [TABLES.PROFESSORS]: professorCreateParams,
    [TABLES.SECTIONS]: sectionCreateParams,
    [TABLES.INTERESTS]: interestCreateParams
}

const crudModeToMap = {
    [CRUDMODE.create]: tableToCreateParamsMap,
    [CRUDMODE.update]: tableToUpdateParamsMap,
    [CRUDMODE.delete]: tableToSearchParamsMap
}
const tableToEndpointMap = {
    [TABLES.COURSES]: endpointBaseAdmin + "/courses",
    [TABLES.PROFESSORS]: endpointBaseAdmin + "/professors",
    [TABLES.SECTIONS]: endpointBaseAdmin + "/sections",
    [TABLES.INTERESTS]: endpointBaseAdmin + "/interests"
}

export {
    TABLES,
    CRUDMODE,
    tableToSearchParamsMap,
    tableToCreateParamsMap,
    tableToUpdateParamsMap,
    tableToDeleteParamsMap,
    crudModeToMap,
    tableToEndpointMap
}
