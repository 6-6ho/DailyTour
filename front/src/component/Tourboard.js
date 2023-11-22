import './Dashboard.css'
import './Grid.css'
import Navbar from './Navbar';
import Sidebar from './Sidebar';


export default function Tourboard() {
    return (
        <div className="App">
            <div className="col-2">
                <Sidebar></Sidebar>
            </div>
            <div className="col-8 right-wrap">
                <Navbar></Navbar>
                <div class='dashboard-div'>
                    <div class='exchange-rate-box-wrap'>
                        <div class='exchange-rate-box'>
                        </div>
                    </div>
                    
                    <div class="rank-div">
                        <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}