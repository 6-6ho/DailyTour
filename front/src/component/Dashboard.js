import './Dashboard.css'
import MonthlyChart from './MonthlyChart'
import YearChart from './YearChart'

export default function Dashboard() {
    return (
        <div className="dashboard-div">
            <MonthlyChart></MonthlyChart>
            <YearChart> </YearChart>
        </div>
    )
}