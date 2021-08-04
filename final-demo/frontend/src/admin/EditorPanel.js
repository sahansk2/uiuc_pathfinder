import * as React from 'react';
import { CRUDMODE, crudModeToMap } from './configAdminDashboard'
import { getEmptyParams, getNullName } from './util';

const ModeSelector = ({ setCrudMode }) => {
    function handleOnChange(e) {
        console.log("Updating mode to", e.target.value)
        setCrudMode(e.target.value);
    }
    return <div className="mode-selector-container" onChange={handleOnChange}>
        <div className="mode-selector-item">
            <input className="mode-selector-item" type="radio" value={CRUDMODE.create} name="crudMode" required={true}/>Create
        </div>
        <div className="mode-selector-item">
            <input className="mode-selector-item" type="radio" value={CRUDMODE.update} name="crudMode" required={true}/>Update
        </div>
        <div className="mode-selector-item">
            <input className="mode-selector-item" type="radio" value={CRUDMODE.delete} name="crudMode" required={true}/>Delete
        </div>
    </div>
}

const EditorScreen = ({ crudMode, currTable, setCrudMode }) => {
    const crudParams = crudModeToMap[crudMode][currTable];
    const [editValues, setEditValues] = React.useState(getEmptyParams(crudParams));
    console.log("Running the EditorScreen render")
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log("The value of editValues now is", editValues, "at", new Date())
        console.log("This is what we will send")
        console.log("CRUDVALUE is: ", crudMode)
        console.log("endpoint is: ", currTable)
        setEditValues(getEmptyParams(crudParams))
    }

    const handleOnChange = (e) => {
        let newSearchParams = {...editValues};
        if (e.target.type === "checkbox") {
            newSearchParams[e.target.name] = e.target.checked;
            // hacky way to get the original null name by chopping off the "Null" suffix
            newSearchParams[e.target.name.substring(0, e.target.name.length - 4)] = "";
        } else {    
            newSearchParams[e.target.name] = e.target.value;
        }
        console.log("Setting", e.target.name, "to", newSearchParams[e.target.name])
        setEditValues(newSearchParams)
    }

    return <div>
        <form onSubmit={handleSubmit}>
            <h2>Editor</h2>
            {crudParams.map((val, idx, _) => {
                return (
                    <React.Fragment>
                        {val.pretty}<br/>
                        <input
                        name={val.name}
                        type={val.type}
                        value={editValues[val.name]}
                        onChange={handleOnChange}
                    /><br/> 
                    {/* { val.nullable && 
                    <React.Fragment>
                        <input 
                            key={idx} 
                            type="checkbox" 
                            value={editValues[getNullName(val.name)]} 
                            name={getNullName(val.name)} 
                            onChange={handleOnChange}/>Set to null?<br/>
                    </React.Fragment> }*/}
                    </React.Fragment>
                )
            })}
            <ModeSelector setCrudMode={setCrudMode}/>
            <button type="submit">Submit!</button>
        </form>
    </div>
}

const EditorResult = ({ editResult }) => {
    return <div>
        { editResult && <div>
            Server responded with {JSON.stringify(editResult)}
            </div>}
    </div>
}
const EditorPanel = ({ setCrudMode, crudMode, currTable }) => {
    const [editResult, setEditResult] = React.useState(null);
    return <div>
        <EditorScreen setEditResult={setEditResult} setCrudMode={setCrudMode} currTable={currTable} crudMode={crudMode}/>
        <EditorResult editResult={editResult}/>
    </div>
}


export {
    EditorPanel
}