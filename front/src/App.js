import './App.css';
import './component/Grid.css'
import Navbar from './component/Navbar'
import Sidebar from './component/Sidebar'
import Dashboard from './component/Dashboard';

function App() {
  return (
    <div className="App">
      <div className="col-2">
        <Sidebar></Sidebar>
      </div>
      <div className="col-8 right-wrap">
        <Navbar></Navbar>
        <Dashboard></Dashboard>
      </div>
    </div>
  );
}

export default App;
