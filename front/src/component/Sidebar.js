import './Bar.css'
import MonthlyChartjs from './MonthlyChartjs'
import MonthlyTopList from './MonthlyTopList'
import YearlyTopList from './YearlyTopList'

export default function Sidebar() {
    return(
        <div className='side-bar-wrap'>
            <div className='side-bar'>
                <div className='logo-wrap'>
                    <div className='logo-box-wrap'>
                        <img src='img/airplane_icon.png'></img>
                    </div>
                    <span className='logo-font'>
                        Daily Tour
                    </span>
                    <div>
                    <MonthlyTopList/>
                    </div>
                    <div>
                    <YearlyTopList/>
                    </div>
                </div>
            </div>
        </div>
    
    )
}