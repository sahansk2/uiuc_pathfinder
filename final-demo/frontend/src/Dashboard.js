import * as React from 'react';
import './dashboard.css'

const TABLES = {
    COURSES: "courses",
    SECTIONS: "sections",
    INTERESTS: "interests",
    PROFESSORS: "professors"
}
const TableSelector = ({ setMode }) => {
    return (
        <div className="table-modifier">
            <button type="button" className="btn btn-primary" onClick={() => setMode(TABLES.COURSES)}>Courses</button>
            <button type="button" className="btn btn-primary" onClick={() => setMode(TABLES.SECTIONS)}>Sections</button>
            <button type="button" className="btn btn-primary" onClick={() => setMode(TABLES.INTERESTS)}>Interests</button>
            <button type="button" className="btn btn-primary" onClick={() => setMode(TABLES.PROFESSORS)}>Professors</button>
        </div>
    )
}

const SearchPanel = ({ searchFields, endpoint }) => {
    return (
        <form>
            {searchFields.map((field, index, _arr) => {
                return (<div key={index} className="form-floating mb-3">
                        <input name={field.name} id={`${field.name}Search`} type="text" className="form-control" onChange={() => console.log('hi')}/>
                        <label for={`${field.name}Search`}>{field.pretty}</label>
                </div>
                )
            })}
            <button type="submit" className="btn btn-success">Go</button>
        </form>
    )
}

const Dashboard = () => {
    let searchableFields = [
        {
            pretty: "Department",
            name: "dept"
        },
        {
            pretty: "Number",
            name: "number"
        }
    ]
    const [currTable, setTable] = React.useState(TABLES.COURSES);
    const setTableAPI = (state) => {
        console.log("New table state!", state)
        setTable(state)
    }
    return (
        <div>
            <TableSelector setMode={setTableAPI}/>
            <div className="dashboard-main">
                <SearchPanel searchFields={searchableFields}/>
            </div>
        </div>
    );
}

export {
    Dashboard
}