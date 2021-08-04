import './index.css';
import * as React from 'react';
import { Dashboard } from './admin/Dashboard'
import {
  HashRouter as Router,
  Link,
  Route,
  Switch
} from 'react-router-dom';
import { UserDashboard } from './user/UserDashboard'

function UserPage() {
  return (
    <div className="container">
      <h1>User Dashboard</h1>
      <UserDashboard/>
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
        <Link to='/admin' className="navLink">Admin</Link>
        <Link to='/main' className="navLink">User</Link>
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
