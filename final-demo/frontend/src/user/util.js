
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
    makeMockRow('CS','225', 'CS','210',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','241',  '1', 'PREREQ'),
    makeMockRow('CS','225', 'CS','374',  '1', 'PREREQ'),
    makeMockRow('CS','225', 'CS','410',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','411',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','412',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','418',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','420',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','427',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','440',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','445',  '1', 'PREREQ'),
    makeMockRow('CS','225', 'CS','446',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','465',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','466',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','467',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'CS','477',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'IE','523',  '0', 'PREREQ'),
    makeMockRow('CS','225', 'IE','531',  '1', 'PREREQ'),
    makeMockRow('CS','225', 'ECE','549',  '0', 'PREREQ'),
    makeMockRow('CS','125', 'CS','225',  '0', 'PREREQ'),
    makeMockRow('ECE','220', 'CS','225',  '0', 'PREREQ'),
    makeMockRow('CS','173', 'CS','225',  '1', 'PREREQ'),
    makeMockRow('MATH','213', 'CS','225',  '1', 'PREREQ'),
    makeMockRow('MATH','347', 'CS','225',  '1', 'PREREQ'),
    makeMockRow('MATH','412', 'CS','225',  '1', 'PREREQ'),
    makeMockRow('MATH','413', 'CS','225',  '1', 'PREREQ'),
]

const mockReturnDataReverseCS225 = [
     makeMockRow('CS', '225', 'CS', '210','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '241','1', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '242','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '374','1', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '410','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '411','0', 'PREREQ'),
     makeMockRow('CS', '241', 'ECE', '411','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '412','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '414','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '418','0', 'PREREQ'),
     makeMockRow('CS', '418', 'CS', '419','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '420','0', 'PREREQ'),
     makeMockRow('CS', '374', 'CS', '421','1', 'PREREQ'),
     makeMockRow('CS', '421', 'CS', '422','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '423','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '424','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '425','0', 'PREREQ'),
     makeMockRow('ECE', '411', 'ECE', '425','0', 'PREREQ'),
     makeMockRow('CS', '421', 'CS', '426','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '427','0', 'PREREQ'),
     makeMockRow('CS', '427', 'CS', '428','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '431','0', 'PREREQ'),
     makeMockRow('CS', '241', 'ECE', '434','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '438','0', 'PREREQ'),
     makeMockRow('CS', '241', 'ECE', '439','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '440','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '445','1', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '446','0', 'PREREQ'),
     makeMockRow('CS', '374', 'CS', '447','0', 'PREREQ'),
     makeMockRow('CS', '461', 'CS', '460','0', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '461','0', 'PREREQ'),
     makeMockRow('CS', '461', 'CS', '463','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '465','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '466','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '467','0', 'PREREQ'),
     makeMockRow('CS', '225', 'CS', '477','0', 'PREREQ'),
     makeMockRow('CS', '374', 'CS', '477','1', 'PREREQ'),
     makeMockRow('CS', '241', 'CS', '484','0', 'PREREQ'),
     makeMockRow('CS', '420', 'ECE', '508','0', 'PREREQ'),
     makeMockRow('CS', '410', 'CS', '510','0', 'PREREQ'),
     makeMockRow('CS', '412', 'CS', '510','0', 'PREREQ'),
     makeMockRow('CS', '446', 'CS', '510','0', 'PREREQ'),
     makeMockRow('CS', '411', 'CS', '511','0', 'PREREQ'),
     makeMockRow('ECE', '411', 'ECE', '511','0', 'PREREQ'),
     makeMockRow('CS', '412', 'CS', '512','0', 'PREREQ'),
     makeMockRow('CS', '418', 'CS', '519','0', 'PREREQ'),
     makeMockRow('CS', '423', 'CS', '523','0', 'PREREQ'),
     makeMockRow('CS', '425', 'CS', '523','2', 'PREREQ'),
     makeMockRow('CS', '225', 'IE', '523','0', 'PREREQ'),
     makeMockRow('CS', '423', 'CS', '525','0', 'PREREQ'),
     makeMockRow('CS', '425', 'CS', '525','0', 'PREREQ'),
     makeMockRow('CS', '438', 'CS', '525','0', 'PREREQ'),
     makeMockRow('CS', '428', 'CS', '527','0', 'PREREQ'),
     makeMockRow('ECE', '425', 'ECE', '527','0', 'PREREQ'),
     makeMockRow('CS', '427', 'CS', '528','0', 'PREREQ'),
     makeMockRow('CS', '225', 'IE', '531','1', 'PREREQ'),
     makeMockRow('CS', '446', 'IE', '534','0', 'PREREQ'),
     makeMockRow('CS', '438', 'CS', '538','0', 'PREREQ'),
     makeMockRow('CS', '446', 'CS', '546','1', 'PREREQ'),
     makeMockRow('CS', '440', 'CS', '548','0', 'PREREQ'),
     makeMockRow('CS', '446', 'CS', '548','0', 'PREREQ'),
     makeMockRow('CS', '225', 'ECE', '549','0', 'PREREQ'),
     makeMockRow('CS', '461', 'CS', '563','0', 'PREREQ'),
     makeMockRow('CS', '463', 'CS', '563','0', 'PREREQ'),
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
    return `${dept}_${num}`
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
        // console.log("A row is", item)
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
    // console.log("The prereq map is", prereq_map)
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
                    id: `e${prereq}${targetOfPrereqs}`,
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


// console.log("Linear")
// console.log(getGraph(mockLinearPrereqsAES211))
// console.log("Context CS 225")
// console.log(getGraph(mockReturnDataContextCS225))
// console.log("Prereqs ECE 210")
// console.log(getGraph(mockReturnDataPrereqsECE210))
// console.log("Prereqs CS 225")
// console.log(getGraph(mockReturnDataPrereqsCS225))
// console.log("Mixed")
// console.log(getGraph(mockReturnDataPrereqsFake100))
export {
    getGraph,
    mockLinearPrereqsAES211,
    mockReturnDataPrereqsCS225,
    mockReturnDataContextCS225,
    mockReturnDataPrereqsFake100,
    mockReturnDataContextECE210,
    mockReturnDataReverseCS225
}