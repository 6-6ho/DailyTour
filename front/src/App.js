// import './App.css';

// import Navbar from './component/Navbar'
// import Sidebar from './component/Sidebar'
import Dashboard from './component/Dashboard';
import Tourboard from './component/Tourboard'
import {BrowserRouter,Route,Routes} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path="/" element={<Dashboard/>}></Route>
          <Route path="/country/:regCode" element={<Tourboard/>}></Route>
        </Routes>
        {/* <div className="col-2">
          <Sidebar></Sidebar>
        </div>
        <div className="col-8 right-wrap">
          <Navbar></Navbar>
          <Dashboard></Dashboard>
        </div> */}
      </div>
    </BrowserRouter>
  );
}

export default App;
