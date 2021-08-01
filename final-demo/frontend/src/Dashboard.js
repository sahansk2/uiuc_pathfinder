import * as React from 'react';
import './dashboard.css'
import {     
    TABLES,
    CRUDMODE,
    tableToSearchParamsMap,
    tableToEndpointMap
} from './configAdminDashboard';

function getEmptyParams(knownParams) {
    let emptySearchParams = {}
    for (let p of knownParams) {
        emptySearchParams[p.name] = "";
        if (p.nullable) {
            emptySearchParams[`${p.name}Null`] = "false";
        }
    }
    return emptySearchParams
}

const SearchInputPanel = ({ setSelectedItem, crudMode, table }) => {
    let knownParams = tableToSearchParamsMap[table]
    let endpoint = tableToEndpointMap[table]

    const [searchParams, setSearchParams] = React.useState(getEmptyParams(knownParams));
    
    React.useEffect(() => {
        console.log("Table has changed, clearing previous params...")
        return () => setSearchParams({})
    }, [table])

    if (crudMode === CRUDMODE.create) {
        return (
            <p>Search disabled when creating items</p>
        )
    } else {
            const handleOnChange = (e) => {
            let newSearchParams = {...searchParams};
            newSearchParams[e.target.name] = e.target.type === "checkbox" ? e.target.checked : e.target.value;
            console.log("Setting", e.target.name, "to", newSearchParams[e.target.name])
            setSearchParams(newSearchParams)
        };

        let searchArea = 
            knownParams.map((searchParam, idx, _arr) => {
                return <React.Fragment>
                    <label key={idx}>{searchParam.pretty}<br/>
                        <input 
                            type={searchParam.type}
                            value={searchParams[searchParam.name]}
                            name={searchParam.name}
                            onChange={handleOnChange}/><br/>
                    </label>
                    { searchParam.nullable && 
                        <React.Fragment>
                            <input 
                                key={idx} 
                                type="checkbox" 
                                value={searchParams[`${searchParam.name}Null`]} 
                                name={`${searchParam.name}Null`} 
                                onChange={handleOnChange}/>Empty?
                        </React.Fragment> }
                    <br/>
                    </React.Fragment>
        })

        function handleOnSubmit(e) {
            e.preventDefault();
            let requestUrl = new URL(endpoint);
            for (const param in searchParams) {
                if (searchParams[param]) {
                    requestUrl.searchParams.append(param, searchParams[param])
                }
            }
            console.log("The requestURL is", requestUrl);
        }
        return <form id={`${TABLES.COURSES}Form`} onSubmit={handleOnSubmit}>
            {searchArea}
            <button type="submit">Search!</button>
        </form>
    }
}

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

const SearchPanel = ({ searchFields, endpoint, currTable }) => {
    return (
          <SearchInputPanel table={currTable} crudMode={CRUDMODE.search} setSelectedItem={null}/>
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
                <SearchPanel currTable={currTable} searchFields={searchableFields}/>
            </div>
        </div>
    );
}

export {
    Dashboard
}