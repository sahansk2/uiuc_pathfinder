import * as React from 'react';
import './dashboard.css'
import {     
    TABLES,
    CRUDMODE
} from './configAdminDashboard';

import { SearchPanel } from './SearchPanel'
import { EditorPanel } from './EditorPanel'

const TableSelector = ({ currTable, setTable }) => {
    const menu = [
        {
            id: TABLES.COURSES,
            pretty: "Courses"
        },
        {
            id: TABLES.SECTIONS,
            pretty: "Sections"
        },
        {
            id: TABLES.INTERESTS,
            pretty: "Interests"
        },
        {
            id: TABLES.PROFESSORS,
            pretty: "Professors"
        }
    ]
    return (
        <div className="table-modifier">
            {menu.map((item, idx, _) => {
                const className = currTable === item.id ? "selected-table" : "";
                return (
                    <button className={className} onClick={() => setTable(item.id)}>{item.pretty}</button>
                )
            })}
        </div>
    )
}

const Dashboard = () => {
    const [currTable, setTable] = React.useState(TABLES.COURSES);
    const [selectedItem, setSelectedItem] = React.useState(null);
    const [crudMode, setCrudMode] = React.useState(CRUDMODE.update);
    const setTableAPI = (state) => {
        console.log("New table state!", state)
        setTable(state)
    }
    return (
        <div>
            <TableSelector currTable={currTable} setTable={setTableAPI}/>
            <div className="dashboard-main">
                <SearchPanel 
                    crudMode={crudMode}
                    currTable={currTable} 
                    setSelectedItem={setSelectedItem}
                    selectedItem={selectedItem}/>
                <EditorPanel setCrudMode={setCrudMode}/>
            </div>
        </div>
    );
}

export {
    Dashboard
}