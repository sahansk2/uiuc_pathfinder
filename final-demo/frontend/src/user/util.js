const mockReturnDataContextECE210 = [

makeMockRow('ECE', '210', 'ECE', '307',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '310',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '311',  '0', 'COREQ'),
makeMockRow('ECE', '210', 'ECE', '329',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '330',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '333',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '340',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '342',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '343',  '0', 'COREQ'),
makeMockRow('ECE', '210', 'ECE', '403',  '1', 'PREREQ'),
makeMockRow( 'ECE', '210','BIOE', '414',  '0', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '461',  '1', 'PREREQ'),
makeMockRow('ECE', '210', 'ECE', '486',  '0', 'PREREQ'),
makeMockRow('ECE', '110', 'ECE', '210',  '1', 'PREREQ'),
makeMockRow('PHYS', '212','ECE', '210',   '0', 'PREREQ'),

]
const mockReturnDataContextCS225 = [
    makeMockRow('CS', '225', 'CS', '210', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '241', '1', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '374', '1', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '410', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '411', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '412', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '418', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '420', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '427', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '440', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '445', '1', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '446', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '465', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '466', '0', 'PREREQ'),
    makeMockRow('CS', '225', 'CS', '467', '0', 'PREREQ'),
]

const mockReturnDataPrereqsCS225 = [
    makeMockRow('CS', '125',  'CS', '173',  '0',  'PREREQ'),
    makeMockRow('ECE', '220',  'CS', '173',  '0',  'PREREQ'),
    makeMockRow('MATH', '220',  'CS', '173',  '1',  'PREREQ'),
    makeMockRow('MATH', '221',  'CS', '173',  '1',  'PREREQ'),
    makeMockRow('ECE', '120',  'ECE', '220',  '0',  'PREREQ'),
    makeMockRow('CS', '125',  'CS', '225',  '0',  'PREREQ'),
    makeMockRow('CS', '173',  'CS', '225',  '1',  'PREREQ'),
    makeMockRow('MATH', '213',  'CS', '225',  '1',  'PREREQ'),
    makeMockRow('ECE', '220',  'CS', '225',  '0',  'PREREQ'),
    makeMockRow('MATH', '347',  'CS', '225',  '1',  'PREREQ'),
    makeMockRow('MATH', '412',  'CS', '225',  '1',  'PREREQ'),
    makeMockRow('MATH', '413',  'CS', '225',  '1',  'PREREQ'),
    makeMockRow('MATH', '220',  'MATH', '231',  '0',  'PREREQ'),
    makeMockRow('MATH', '221',  'MATH', '231',  '0',  'PREREQ'),
    makeMockRow('MATH', '231',  'MATH', '347',  '0',  'PREREQ'),
]

const mockReturnDataPrereqsECE210 = [
    makeMockRow('ECE',  '110', 'ECE', '210',  '0',   'PREREQ'),
    makeMockRow('PHYS',  '212', 'ECE', '210',  '1',   'PREREQ'),
    makeMockRow('PHYS',  '101', 'PHYS', '211',  '0',   'COREQ'),
    makeMockRow('PHYS',  '211', 'PHYS', '212',  '0',   'PREREQ'),
]


const mockReturnDataPrereqsFake100 = [
    makeMockRow('AES', '210', 'AES', '310', '0', 'PREREQ'),
    makeMockRow('ZEQ', '101', 'AES', '310', '1', 'PREREQ'),
    makeMockRow('ZEQ', '102', 'AES', '310', '1', 'PREREQ'),
    makeMockRow('ZEQ', '103', 'AES', '310', '1', 'PREREQ'),
]


const mockLinearPrereqsAES211 = [
    makeMockRow('ZZZ', '200', 'ZZZ', '300', '0', 'PREREQ'),
    makeMockRow('ZZZ', '100', 'ZZZ', '200', '0', 'PREREQ'),
    makeMockRow('ZZZ', '010', 'ZZZ', '100', '0', 'PREREQ'),
]

function makeMockRow(predept, prenum, reqdept, reqnum, group, type) {
    return {
        courseDepartment: predept,
        courseNumber: prenum,
        requiringCourseDepartment: reqdept,
        requiringCourseNumber: reqnum,
        groupId: group,
        type: type
    }
}

function getCourseKey(dept, num) {
    return `${dept}${num}`
}

function getCourseKeyWithGroup(dept, num, group) {
    return `${dept}${num}${group}`
}

function getORnode(requiring, group) {
    return `OR_${requiring}_${group}`
}
function getGraph(data) {
    let keyMap = {}
    let prereq_map = {}
    for (let item of data) {
        console.log(item)
        const preCourseKey = getCourseKey(item.courseDepartment, item.courseNumber)
        const reqCourseKey = getCourseKey(item.requiringCourseDepartment, item.requiringCourseNumber)
        if (!prereq_map.hasOwnProperty(preCourseKey)) {
            prereq_map[preCourseKey] = {}
        }
        if (!prereq_map.hasOwnProperty(reqCourseKey)) {
            prereq_map[reqCourseKey] = {}
        }
        if (!prereq_map[reqCourseKey].hasOwnProperty(item.groupId)) {
            prereq_map[reqCourseKey][item.groupId] = []
        }
        
        prereq_map[reqCourseKey][item.groupId].push(preCourseKey)
        
        keyMap[preCourseKey] = {
            dept: item.courseDepartment,
            number: item.courseNumber
        }
        keyMap[reqCourseKey] = {
            dept: item.requiringCourseDepartment,
            number: item.requiringCourseNumber
        }
    }
    let nodes = []
    let edges = []
    // Creates course nodes
    console.log(prereq_map)
    for (const courseId of Object.keys(prereq_map)) {
        nodes.push({
            id: courseId,
            label: `${keyMap[courseId].dept} ${keyMap[courseId].number}`
        })
    }
    // Second pass
    for (const courseId of Object.keys(prereq_map)) {
        // If we have multiple groups
        for (const groupId of Object.keys(prereq_map[courseId])) {
            // If we have a group with multiple courses in it, we need to make an OR node and point everything to the OR node
            let targetOfPrereqs = null
            if (prereq_map[courseId][groupId].length > 1) {
                // We link to the OR node
                targetOfPrereqs = getORnode(courseId, groupId)
                // create an OR node
                nodes.push({
                    id: targetOfPrereqs,
                    label: "OR"
                })

                edges.push({
                    source: targetOfPrereqs,
                    target: courseId
                })
            } else {
                targetOfPrereqs = courseId
            }
            for (const prereq of prereq_map[courseId][groupId]) {
                edges.push({
                    id: `e${edges.length}`,
                    source: prereq,
                    target: targetOfPrereqs
                })
            }
        }
    }
    return {
        nodes: nodes,
        edges: edges
    }
}


console.log("Linear")
console.log(getGraph(mockLinearPrereqsAES211))
console.log("Context CS 225")
console.log(getGraph(mockReturnDataContextCS225))
console.log("Prereqs ECE 210")
console.log(getGraph(mockReturnDataPrereqsECE210))
console.log("Prereqs CS 225")
console.log(getGraph(mockReturnDataPrereqsCS225))
console.log("Mixed")
console.log(getGraph(mockReturnDataPrereqsFake100))
export {
    getGraph,
    mockLinearPrereqsAES211,
    mockReturnDataPrereqsCS225,
    mockReturnDataContextCS225,
    mockReturnDataPrereqsFake100,
    mockReturnDataContextECE210
}