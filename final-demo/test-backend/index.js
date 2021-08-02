const express = require('express')
const app = express()
const port = 4000
const adminrouter = express.Router()

function makeMap(rows, values) {
    return values.map((val) => {
        row = {}
        for (let v = 0; v < val.length; v++) {
            if (val[v] !== null) {
                row[rows[v]] = val[v]
            }
        }
        return row
    })
}


adminrouter.get('/courses', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.json([
        {
            dept: "CS",
            num: "225",
            title: "Data Structures",
            gpa: 3.4
        },
        {
            dept: "ECE",
            num: "374",
            title: "Algorithms"
        },
        {
            dept: "CS",
            num: "173",
            title: "Discrete Math for CS",
            gpa: 3.2
        }
    ])
})

adminrouter.post('/courses', (req, res) => {
    console.log("Got ", req.query, new Date());
    res.send({ affectedRows: 5 })
})

adminrouter.delete('/courses', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({ affectedRows: 3 })
})

adminrouter.get('/professors', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send(makeMap(
        ['FirstName', 'LastName', 'Rating'],
        [
            ['C', 'Larrison', null],
            ['C', 'Murphy', 3],
            ['D', 'Riechers', null],
            ['X', 'Chen', 4.5],
            ['D', 'King', null],
            ['J', 'Gulley', null],
            ['R', 'May', null],
            ['I', 'Minefee', 2.2],
            ['Z', 'Revell', null],
            ['J', 'Fisher', 5.0],
            ['A', 'Belmont', null],
            ['J', 'Guest', null],
            ['M', 'Pool', null],
            ['A', 'Aguayo', null],
            ['W', 'Davey', null]
        ]
    ))
})

adminrouter.post('/professors', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({ affectedRows: 1 })
})
adminrouter.delete('/professors', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({ affectedRows: 8 })
})

adminrouter.get('/interests', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send(
        makeMap(['interest', 'id'], [
            ['ARTIFICIAL INTELLIGENCE, ROBOTICS, AND CYBERNETICS', '7'],
            ['BIG DATA ANALYTICS AND SYSTEMS', '17'],
            ['BIOENGINEERING, ACOUSTICS, AND MAGNETIC RESONANCE ENGINEERING', '1'],
            ['CIRCUITS', '5'],
            ['COMMUNICATION SYSTEMS', '8'],
            ['CONTROL SYSTEMS', '2'],
            ['CYBERPHYSICAL SYSTEMS', '13'],
            ['ELECTROMAGNETICS', '3'],
            ['FOUNDATIONS AND THEORY', '9'],
            ['HARDWARE SYSTEMS', '15'],
            ['MICROELECTRONICS/PHOTONICS', '6'],
            ['NANOTECHNOLOGY', '10'],
            ['NETWORKING, MOBILE, AND DISTRIBUTED COMPUTING', '16'],
            ['POWER AND ENERGY SYSTEMS', '4'],
            ['REMOTE SENSING AND SPACE SCIENCE', '11'],
            ['SIGNAL PROCESSING', '12'],
            ['TRUST, RELIABILITY, AND SECURITY', '14'],
        ])
    )
})

adminrouter.post('/interests', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({'affectedRows': 7})
})

adminrouter.delete('/interests', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({'affectedRows': 8})
})

adminrouter.get('/sections', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send(makeMap(
        ['Crn', 'CourseNumber', 'CourseDepartment', 'creditHours', 'startTime', 'endTime', 'days'], [,
        ['12238', '399', 'ANTH', '3', '01:00 PM', '02:50 PM', 'MWF'],
        ['22237', '199', 'ME', '1', '', '', ''],
        ['22243', '199', 'ME', '1', '04:00 PM', '05:50 PM', 'M'],
        ['22421', '199', 'ME', '3', '', '', ''],
        ['23777', '499', 'MUS', '2', '01:00 PM', '01:50 PM', 'MW'],
        ['23791', '499', 'MUS', '1', '', '', ''],
        ['23793', '499', 'MUS', '4', '11:00 AM', '11:50 AM', 'TR'],
        ['23799', '499', 'MUS', '2', '09:00 AM', '09:50 AM', 'MW'],
        ['23831', '499', 'MUS', '1', '12:30 PM', '01:50 PM', 'M'],
        ['23861', '499', 'MUS', '1', '12:30 PM', '01:50 PM', 'W'],
        ['23877', '499', 'MUS', '2', '11:00 AM', '11:50 AM', 'TR'],
        ['24158', '199', 'MUS', '2', '', '', ''],
        ['26997', '199', 'SOCW', '1', '', '', ''],
        ['28337', '199', 'UP', '3', '03:30 PM', '04:50 PM', 'F'],
        ['28358', '199', 'UP', '3', '04:00 PM', '05:20 PM', 'TR'],
        ]
    )
)})

adminrouter.post('/sections', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({'affectedRows': 18})
})

adminrouter.delete('/sections', (req, res) => {
    console.log("Got ", req.query, new Date())
    res.send({'affectedRows': 13})
})

app.use('/admin', adminrouter)

app.listen(port, () => {
    console.log("Listening on port", port)
})
