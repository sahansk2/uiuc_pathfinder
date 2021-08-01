import './index.css';
import * as React from 'react';
import { Dashboard } from './admin/Dashboard'
import {
  BrowserRouter as Router,
  Link,
  Route,
  Switch
} from 'react-router-dom';

function UserPage() {
  return (
    <div>
      <p>
        Insert the user code here.
      </p>
    </div>
  )
}

function AdminPage() {
  return (
    <div className="container">
      <h1>Admin Dashboard</h1>
      <Dashboard/>
    </div>
  );
}

function App() {
  return (
    <React.Fragment>
      <Router>
        <Link to='/admin'>Admin</Link>
        <Link to='/main'>User</Link>
        <Switch>
          <Route path="/admin">
            <AdminPage/>
          </Route>
          <Route path="/main">
            <UserPage/>  
          </Route>
      </Switch>
      </Router>
    </React.Fragment>
  )
}

export default App;
