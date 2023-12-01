import './Dashboard.css'
import './Grid.css'
import MiddleContainer from './MiddleContainer'
// import MonthlyChart from './MonthlyChart'
import MonthlyChartjs from './MonthlyChartjs'
import Navbar from './Navbar'
import Sidebar from './Sidebar'

export default function Dashboard() {
    return (
        
        <div className="dashboard-wrap">
      <div className="col-2">
        <Sidebar></Sidebar>
      </div>
      <div className="col-8 right-wrap">
        <Navbar></Navbar>
        <div className="dashboard-div">
            <MonthlyChartjs></MonthlyChartjs>
            <MiddleContainer></MiddleContainer>

        </div>
      </div>
    </div>
        
    )
}