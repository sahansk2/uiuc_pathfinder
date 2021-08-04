import * as React from 'react';

import { getGraph,  mockReturnDataPrereqsCS225 as mockData, mockReturnDataContextCS225 as mockData2, mockReturnDataReverseCS225 as reverseMock} from './util'

import { GraphDisplay } from './GraphDisplay'

import { graphFetch, fakeFetch } from '../mockutils'
import { endpointBase } from '../config';

function UserGraphConfig({ setGraphData }) {
    const [option, setOption] = React.useState("prereqs");
    const [num, setNum] = React.useState("");
    const [dept, setDept] = React.useState("");

    const handleOnSubmit = (e) => {
        e.preventDefault();
        console.log("Fetching data from endpoint at", new Date());
        let fetchUrl = null;
        if (option === "prereqs") {
            fetchUrl = new URL(endpointBase + '/prereqs');
        } else if (option === "reverse") {
            fetchUrl = new URL(endpointBase + '/reverse')
        } else {
            fetchUrl = new URL(endpointBase + '/context')
        }

        // fetchUrl.searchParams.set("searchmode", option)
        fetchUrl.searchParams.set("number", num)
        fetchUrl.searchParams.set("dept", dept)
        console.log(fetchUrl)
        if (option === "prereqs") {
            console.log("Prereq fetch")
            fetch(fetchUrl)
                .then((data) => data.json())
                .then(data => {
                    const renamedGraphData = data.map(val => {
                        return {courseDepartment: val.preCourseDept,
                            courseNumber: val.preCourseNum,
                            requiringCourseDepartment: val.reqCourseDept,
                            requiringCourseNumber: val.reqCourseNum,
                            groupId: val.reqId,
                            type: val.reqType,}
                        })
                        console.log("Successfully fetched data at", new Date());
                        console.log(renamedGraphData)
                    setGraphData(getGraph(renamedGraphData))
                });
        } else if (option === "reverse") {
            console.log("Reverse fetch")
            fetch(fetchUrl)
                .then((data) => data.json())
                .then(data => {
                    const renamedGraphData = data.map(val => {
                        return {courseDepartment: val.preCourseDept,
                            courseNumber: val.preCourseNum,
                            requiringCourseDepartment: val.reqCourseDept,
                            requiringCourseNumber: val.reqCourseNum,
                            groupId: val.reqId,
                            type: val.reqType,}
                        })
                    console.log("Successfully fetched data at", new Date());
                    console.log(renamedGraphData)
                    setGraphData(getGraph(renamedGraphData))
                });
        } else {
            console.log("A real fetch")
            fetch(fetchUrl)
                .then((data) => data.json())
                .then(data => {
                    const renamedGraphData = data.map(val => {
                        return {courseDepartment: val.CourseDepartment,
                        courseNumber: val.CourseNumber,
                        requiringCourseDepartment: val.RequiringCourseDepartment,
                        requiringCourseNumber: val.RequiringCourseNumber,
                        groupId: val.RequirementGroupId,
                        type: val.ReqType,}
                        })
                    console.log("Successfully fetched data at", new Date());
                    console.log(renamedGraphData)
                    setGraphData(getGraph(renamedGraphData))
                });
        }
    }

    return <form onSubmit={handleOnSubmit}>
        <input 
            type="radio" 
            name="searchmode" 
            onChange={(e) => setOption(e.target.value)}
            value="prereqs"
            checked={option === "prereqs"}/>Prereqs<br/>
        <input 
            type="radio"
            name="searchmode"
            onChange={e => setOption(e.target.value)}
            value="reverse"
            checked={option === "reverse"}/>Dependents<br/>
        <input 
            type="radio"
            name="searchmode"
            onChange={e => setOption(e.target.value)}
            value="context"
            checked={option === "context"}/>Course Context<br/>
        <input 
            type="text"
            name="dept"
            onChange={e => setDept(e.target.value)}
            value={dept}
            required={true}/> Course Department <br/>
        <input
            type="number"
            name="num"
            onChange={e => setNum(e.target.value)}
            value={num}
            required={true}/> Course Number <br/>
        <button type="submit">Search!</button>
    </form>
}

function CourseInformationPanel({selectedCourse}) {
    if (selectedCourse) {

        return <div>
        <h2>{selectedCourse.course.title}</h2>
        <h3>{selectedCourse.course.num} {selectedCourse.course.dept}</h3>
        {selectedCourse.course.avgGpa && <h4>Average GPA: {selectedCourse.course.avgGpa}</h4>}
        <h3>Restrictions:</h3>
        <ul>
            {selectedCourse.restrictions.map(r => <li>{r}</li>)}
        </ul>
        <h3>Professors</h3>
        <ul>
        {selectedCourse.professors.map(p => <li>{p.firstname} {p.lastname}</li>)}
            </ul>
    </div>
    } else {
        return <div>Click on an element to getstarted!</div>
    }
}

function NiceProfessorResult({ prof }) {
    return <div className="nice-professor-result">
        <p>First Name: {prof.FirstName}</p>
        <p>Last Name: {prof.LastName}</p>
    </div>

}

function NiceProfessorPanel({ }) {
const [niceProfessors, setNiceProfessors] = React.useState([])
    const handleOnSubmit = (e) => {
        e.preventDefault()
        fetch(new URL(endpointBase + "/nice"), { method: "GET" })
            .then(data => data.json())
            .then(data => setNiceProfessors(data))
    }
    
    return <React.Fragment>
                <button onClick={() => setNiceProfessors([])}>Clear</button>
                <form onSubmit={handleOnSubmit}>
        <button type="submit">Find professors who teach easy courses often!</button> 
        <div className="nice-professor-container">
            {niceProfessors.map(prof => <NiceProfessorResult prof={prof}/>)}
        </div>
    </form>
    </React.Fragment>
    
}

function UserDashboard(props) { 
    const [graphData, setGraphData] = React.useState(null);
    const [selectedCourse, setSelectedCourse] = React.useState(null);
    return <div>
        <UserGraphConfig setGraphData={setGraphData}/>
        <GraphDisplay setSelectedCourse={setSelectedCourse} data={graphData}/>
        <CourseInformationPanel selectedCourse={selectedCourse}/>
        <hr/>
        <NiceProfessorPanel/>
    </div>
}

export {
    UserDashboard
}
