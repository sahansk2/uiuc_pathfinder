import * as React from 'react'
import { fakeFetch } from '../mockutils'
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
            setSearchResults(null);
            setSelectedItem(null);
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
        fakeFetch(requestUrl, mockCourses)
            .then(data => {
                setSearchResults(data);
                console.log("Fetched results", new Date());
            })
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
    

    let searchArea = 
        knownParams.map((param, idx, _arr) => {
            let currInput = null;
            if (param.nullable === true) {
                currInput = 
                <input 
                        type={param.type}
                        value={searchParams[param.name]}
                        name={param.name}
                        onChange={handleOnChange}
                        disabled={searchParams[getNullName(param.name)]}/>
            } else {
                currInput = 
                <input 
                        type={param.type}
                        value={searchParams[param.name]}
                        name={param.name}
                        onChange={handleOnChange}/>
            }
            return <React.Fragment>
                <label key={idx}>{param.pretty}<br/>
                    {currInput}
                </label>
                {/* { param.nullable && 
                    <React.Fragment>
                        <input 
                            key={idx} 
                            type="checkbox" 
                            value={searchParams[getNullName(param.name)]} 
                            name={getNullName(param.name)} 
                            onChange={handleOnChange}/>Search for missing?
                    </React.Fragment> } */}
                <br/>
                </React.Fragment>
    })

        
    return <form id={`${TABLES.COURSES}Form`} onSubmit={handleOnSubmit}>
        {searchArea}
        <button type="submit">Search!</button>
    </form>
}


function ResultItem({ currTable, data, setSelectedItem }) {
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
            return <div key={idx} onClick={() => {
                console.log("Selected item will be updated to", data)
                setSelectedItem(data)
            }}>
                {field.name}: {field.value}
            </div>
        })}
    </div>
}


const SearchResultsPanel = ({ currTable, setSelectedItem, searchResults }) => {
    return <div className="search-result-panel">
        {searchResults?.data.map((item, idx, _) => 
            <ResultItem currTable={TABLES.COURSES} data={item} id={idx} setSelectedItem={setSelectedItem}/>
        )}
    </div>
}

const SearchPanel = ({ currTable, crudMode, selectedItem, setSelectedItem }) => {
    const [searchResults, setSearchResults] = React.useState(null);

    return (
        <React.Fragment>
            <SearchInputPanel
                table={currTable}
                crudMode={crudMode}
                setSearchResults={setSearchResults}
                setSelectedItem={setSelectedItem}/>
            <SearchResultsPanel
                table={currTable}
                setSelectedItem={setSelectedItem}
                searchResults={searchResults}/>
        </React.Fragment>
    )

}

export {
    SearchPanel,
    SearchInputPanel
}