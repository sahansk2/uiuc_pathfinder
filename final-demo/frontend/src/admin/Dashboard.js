import * as React from 'react';
import './dashboard.css'
import {     
    TABLES
} from './configAdminDashboard';

import { SearchPanel } from './SearchPanel'

const TableSelector = ({ setMode }) => {
    return (
        <div className="table-modifier">
            <button type="button" onClick={() => setMode(TABLES.COURSES)}>Courses</button>
            <button type="button" onClick={() => setMode(TABLES.SECTIONS)}>Sections</button>
            <button type="button" onClick={() => setMode(TABLES.INTERESTS)}>Interests</button>
            <button type="button" onClick={() => setMode(TABLES.PROFESSORS)}>Professors</button>
        </div>
    )
}


const Dashboard = () => {
    const [currTable, setTable] = React.useState(TABLES.COURSES);
    const [selectedItem, setSelectedItem] = React.useState({});
    const setTableAPI = (state) => {
        console.log("New table state!", state)
        setTable(state)
    }
    return (
        <div>
            <TableSelector setMode={setTableAPI}/>
            <div className="dashboard-main">
                <SearchPanel 
                    currTable={currTable} 
                    setSelectedItem={setSelectedItem}
                    selectedItem={selectedItem}/>
            </div>
        </div>
    );
}

export {
    Dashboard
}