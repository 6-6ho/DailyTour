import './Dashboard.css'
import MiddleContainer from './MiddleContainer'
// import MonthlyChart from './MonthlyChart'
import MonthlyChartjs from './MonthlyChartjs'


export default function Dashboard() {
    return (
        <div className="dashboard-div">
            <MonthlyChartjs></MonthlyChartjs>
            <MiddleContainer></MiddleContainer>
        </div>
    )
}