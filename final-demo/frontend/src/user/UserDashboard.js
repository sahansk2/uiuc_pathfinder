import * as React from 'react';

import { getGraph,  mockReturnDataPrereqsCS225 as mockData, mockReturnDataContextCS225 as mockData2 } from './util'

import { GraphDisplay } from './GraphDisplay'

import { graphFetch } from '../mockutils'

function UserGraphConfig({ setGraphData }) {
    const [option, setOption] = React.useState("prereqs");
    const [num, setNum] = React.useState("");
    const [dept, setDept] = React.useState("");

    const handleOnSubmit = (e) => {
        e.preventDefault();
        console.log("Fetching data from endpoint at", new Date());
        const fetchUrl = new URL('https://localhost.com/endpoint')
        fetchUrl.searchParams.set("searchmode", option)
        fetchUrl.searchParams.set("num", num)
        fetchUrl.searchParams.set("dept", dept)
        if (option === "prereqs") {
            graphFetch(fetchUrl, mockData)
                .then((data) => {
                    console.log("Successfully fetched data at", new Date());
                    console.log(data)
                    setGraphData(data)
                });       
        } else {
            graphFetch(fetchUrl, mockData2)
                .then((data) => {
                    console.log("Successfully fetched data at", new Date());
                    console.log(data)
                    setGraphData(data)
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
            name="num"
            onChange={e => setNum(e.target.value)}
            value={num}
            required={true}/> Course Number <br/>
        <input 
            type="text"
            name="dept"
            onChange={e => setDept(e.target.value)}
            value={dept}
            required={true}/> Course Department <br/>
        <button type="submit">Search!</button>
    </form>
}

function CourseInformationPanel({  }) {

}
function UserDashboard(props) { 
    const [graphData, setGraphData] = React.useState(null);
    return <div>
        <UserGraphConfig setGraphData={setGraphData}/>
        <GraphDisplay data={graphData}/>
    </div>
}

export {
    UserDashboard
}
