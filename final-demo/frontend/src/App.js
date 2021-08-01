import './index.css';
import {Dashboard} from './admin/Dashboard'

function AdminPage() {
  return (
    <div className="container">
      <h1>Admin Dashboard</h1>
      <Dashboard/>
    </div>
  );
}

function App() {
  return <AdminPage/>
}

export default App;
