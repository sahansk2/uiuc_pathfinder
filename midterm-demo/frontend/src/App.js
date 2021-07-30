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
  if (typeof result == 'undefined') {
    return <div class="row">
      <div class="card">
      <p><mark class="primary tag">Enter a query to start searching!</mark></p>
        </div>
      </div>
  }
  if (result.length == 0) {
    return <div class="card">
    <p><mark class="secondary tag">No results!</mark></p>
      </div>
  }
  return (
    <div class="row">
      {
        result.map(r => 
          <div class="card">
            {Object.entries(r).map(
              ([k, v]) => 
                <p>
                  <mark class="tag">{k}</mark>
                  <mark class="tag tertiary">{v}</mark>
                </p>)} 
          </div>)
      }
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
    data.forEach((v, k) => {
      if (v.length) {
        params[k] = v 
      }
    })
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
    <button onClick={() => setResponse(undefined)}>Clear</button>
    <BasicResult result={response}/>
    
    </div>
  );
}

function App() {
  return (
    <div>
      <DemoItem 
        title="Advanced Query 1: Course Context - Find A Course's Prerequisites and where it is a Prerequisite" 
        fields={['dept', 'num', 'limit']} 
        endpoint="http://localhost:8080/coursecontext"/>
      <DemoItem
        title="Advanced Query 2: Nice Professors - Professors who teach at least X courses where the average GPA for each is at least Y"
        fields={['gpa', 'count', 'limit']}
        endpoint="http://localhost:8080/highgpaprofs"/>
      <DemoItem
        title="CREATE Demo: Courses"
        fields={['dept', 'num', 'title', 'avgGpa']}
        endpoint="http://localhost:8080/makecourse"
        />
      <DemoItem
        title="Keyword search on course titles"
        fields={['keyword', 'limit']}
        endpoint="http://localhost:8080/courses"/>
      <DemoItem
        title="UPDATE Demo: Professor Rating"
        fields={['firstname', 'lastname', 'rating']}
        endpoint="http://localhost:8080/profrating"
      />
      <DemoItem
        title="Search Professors by Last Name"
        fields={['lastname']}
        endpoint="http://localhost:8080/findprof"
      />
      <DemoItem
        title="DELETE Demo: Restrictions"
        fields={['crn', 'detail']}
        endpoint="http://localhost:8080/delrestriction"/>
      <DemoItem
        title="Search Restrictions by Detail"
        fields={['detail']}
        endpoint="http://localhost:8080/findrestrict"
      />
    </div>
  );
}

export default App;
