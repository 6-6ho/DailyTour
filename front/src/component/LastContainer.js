import './Dashboard.css'
import './Grid.css'
import Navbar from './Navbar';
import Sidebar from './Sidebar';


export default function LastContainer() {
    return(
        <div className="App">
            <div className="col-2">
                <Sidebar></Sidebar>
            </div>
            <div className="col-8 right-wrap">
                <Navbar></Navbar>
                
            </div>
        </div>
    )    
}