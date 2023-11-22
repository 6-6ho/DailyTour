import './Bar.css'

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
                </div>
            </div>
        </div>
    
    )
}