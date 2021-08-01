import { CRUDMODE } from './configAdminDashboard'

const ModeSelector = ({ setCrudMode }) => {
    function handleOnChange(e) {
        console.log("Updating mode to", e.target.value)
        setCrudMode(e.target.value);
    }
    return <div onChange={handleOnChange}>
        <input type="radio" value={CRUDMODE.create} name="crudMode"/>Create
        <input type="radio" value={CRUDMODE.update} name="crudMode"/>Update
        <input type="radio" value={CRUDMODE.delete} name="crudMode"/>Delete
    </div>
}
const EditorPanel = ({ setCrudMode }) => {
    return <div>
        <ModeSelector setCrudMode={setCrudMode}/>
    </div>
}


export {
    EditorPanel
}