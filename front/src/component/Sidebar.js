import './Bar.css'
import MonthlyChartjs from './MonthlyChartjs'

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
                    <MonthlyTopList></MonthlyTopList>
                    </div>
                    <div>
                    <YearlyTopList></YearlyTopList>
                    </div>
                </div>
            </div>
        </div>
    
    )
}