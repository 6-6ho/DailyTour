import './Bar.css'
import SideChart from './SideChart'

export default function Sidebar() {
    return(
        <div className='side-bar-wrap'>
            <div className='side-bar'>
                <div className='logo-wrap'>
                    <div className='logo-box-wrap'>
                        <img src='img/airplane_icon.png'></img>
                        <span className='logo-font'>Daily Tour</span>
                    </div>
                    <span className='logo-font'>
                        Daily Tour
                    </span>
                </div>
                <SideChart></SideChart>
            </div>
        </div>
    
    )
}