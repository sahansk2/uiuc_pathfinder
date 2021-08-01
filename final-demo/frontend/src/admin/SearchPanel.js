import * as React from 'react'

import {     
    TABLES,
    CRUDMODE,
    tableToSearchParamsMap,
    tableToEndpointMap
} from './configAdminDashboard';

import { tableToViewMap } from './configDataView'
import { mockCourses } from './mockResponses'
import { getEmptyParams, getNullName } from './util'
import './dashboard.css'

const SearchInputPanel = ({ setSearchResults, setSelectedItem, crudMode, table }) => {
    let knownParams = tableToSearchParamsMap[table]
    let endpoint = tableToEndpointMap[table]

    const [searchParams, setSearchParams] = React.useState(getEmptyParams(knownParams));
    
    React.useEffect(() => {
        return () => {
            console.log("Table has changed, clearing previous params...")
            setSearchParams({});
            setSearchResults({});
        }
    }, [table])

    function handleOnSubmit(e) {
        e.preventDefault();
        let requestUrl = new URL(endpoint);
        for (const param in searchParams) {
            if (searchParams[param]) {
                requestUrl.searchParams.append(param, searchParams[param]);
            }
        }
        console.log("The requestURL is", requestUrl);
        // Pretend there was a fetch
        setSearchResults(mockCourses);
        console.log("Fetched results", new Date());
    }

    const handleOnChange = (e) => {
        let newSearchParams = {...searchParams};
        if (e.target.type === "checkbox") {
            newSearchParams[e.target.name] = e.target.checked;
            // hacky way to get the original null name by chopping off the "Null" suffix
            newSearchParams[e.target.name.substring(0, e.target.name.length - 4)] = "";
        } else {
            newSearchParams[e.target.name] = e.target.value;
        }
        console.log("Setting", e.target.name, "to", newSearchParams[e.target.name])
        setSearchParams(newSearchParams)
    };
    
    if (crudMode === CRUDMODE.create) {
        return (
            <p>Search disabled when creating items</p>
        )
    } else {
        let searchArea = 
            knownParams.map((searchParam, idx, _arr) => {
                let currInput = null;
                if (searchParam.nullable === true) {
                    currInput = 
                    <input 
                            type={searchParam.type}
                            value={searchParams[searchParam.name]}
                            name={searchParam.name}
                            onChange={handleOnChange}
                            disabled={searchParams[getNullName(searchParam.name)]}/>
                } else {
                    currInput = 
                    <input 
                            type={searchParam.type}
                            value={searchParams[searchParam.name]}
                            name={searchParam.name}
                            onChange={handleOnChange}/>
                }
                return <React.Fragment>
                    <label key={idx}>{searchParam.pretty}<br/>
                        {currInput}
                    </label>
                    { searchParam.nullable && 
                        <React.Fragment>
                            <input 
                                key={idx} 
                                type="checkbox" 
                                value={searchParams[getNullName(searchParam.name)]} 
                                name={getNullName(searchParam.name)} 
                                onChange={handleOnChange}/>Empty?
                        </React.Fragment> }
                    <br/>
                    </React.Fragment>
        })

        
        return <form id={`${TABLES.COURSES}Form`} onSubmit={handleOnSubmit}>
            {searchArea}
            <button type="submit">Search!</button>
        </form>
    }
}


function ResultItem({ currTable, data }) {
    const view = tableToViewMap[currTable]
    let presentableFields = new Array(data.length).fill({});
    for (let attr in data) {
        presentableFields[view[attr].pos] = {
            name: view[attr].pretty,
            value: view[attr].limit ? data[attr].substring(0, view[attr].limit) + "..." : data[attr]
        }
    }
    return <div className="search-result" >
        {presentableFields.map((field, idx, _) => {
            return <div key={idx} onClick={() => {}}>
                {field.name}: {field.value}
            </div>
        })}
    </div>
}


const SearchResultsPanel = ({ currTable, setSelectedItem, searchResults }) => {
    return <div class="search-result-panel">
        {searchResults.data.map((item, idx, _) => 
            <ResultItem currTable={TABLES.COURSES} data={item} id={idx}/>
        )}
    </div>
}

const SearchPanel = ({ currTable, crudMode, selectedItem, setSelectedItem }) => {
    const [searchResults, setSearchResults] = React.useState([]);
    
    return (
        <React.Fragment>
            <SearchInputPanel
                table={currTable}
                crudMode={CRUDMODE.search}
                setSearchResults={setSearchResults}/>
            <SearchResultsPanel
                table={currTable}
                setSelectedItem={setSelectedItem}
                searchResults={mockCourses}/>
        </React.Fragment>
    )
}

export {
    SearchPanel,
    SearchInputPanel
}