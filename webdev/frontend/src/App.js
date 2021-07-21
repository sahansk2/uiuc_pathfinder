import logo from './logo.svg';
import React from 'react';
import axios from 'axios';

function EditableTextBox(props) {
  const ref = React.useRef();
  const name = props.name;
  return (
    <input type="text" ref={ref} name={name}/>
  )
}

function BasicResult(props) {
  const result = props.result;
  return (
    <div>
      <p>
        {JSON.stringify(result)}
      </p>
    </div>
  )
}

function DemoItem(props) {
  const title = props.title;
  const fields = props.fields;
  const endpoint = props.endpoint;
  const [response, setResponse] = React.useState();
  console.log(fields)
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const data = new FormData(e.target);

    let params = {}
    data.forEach((v, k) => params[k] = v)
    axios.get(endpoint, {params: params})
      .then(resp => {
        setResponse(resp["data"])
      })
      .catch(err => setResponse({"Error": "Unable to fetch response!"}))
  }

  const simpleFormFields = fields.map((f) =>
    <div key={f}>
    <label>
      {f}:
      <EditableTextBox name={f}/>
    </label>
    </div>
  )

  return (
    <div>
    <form onSubmit={handleSubmit}>
      <h1>{props.title}</h1>
      {simpleFormFields}
      <input type="submit" value="Submit"/>
    </form>
    <button onClick={() => setResponse({})}>Clear</button>
    <BasicResult result={response}/>
    
    </div>
  );
}

function App() {
  return (
    <div>
      <DemoItem 
        title="Advanced Query 1: Course Context" 
        fields={['dept', 'num']} 
        endpoint="http://localhost:8080/coursecontext"/>
      <DemoItem
        title="Advanced Query 2: Professors teaching at least N courses with at least K gpa"
        fields={['gpa', 'count', 'limit']}
        endpoint="http://localhost:8080/highgpaprofs"/>
      <DemoItem
        title="CREATE Demo: Courses"
        fields={['dept', 'num', 'title', 'avgGpa']}
        endpoint="http://localhost:8080/makecourse"
        />
      <DemoItem
        title="UPDATE Demo: Professor Rating"
        fields={['firstname', 'lastname', 'rating']}
        endpoint="http://localhost:8080/profrating"
      />
      <DemoItem
        title="DELETE Demo: Restrictions"
        fields={['crn', 'detail']}
        endpoint="http://localhost:8080/delrestriction"/>
      <DemoItem
        title="Keyword search on course titles"
        fields={['keyword', 'limit']}
        endpoint="http://localhost:8080/courses"/>
    </div>
  );
}

export default App;
