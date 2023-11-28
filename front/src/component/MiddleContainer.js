import './Dashboard.css';


export default function MiddleContainer() {
    return (
        <div className="middle-container-box-wrap">

            <div className="col-4 h-10">
                <div className='year-chart-box p-1'>
                    <div className="select-box-container">
                        <select>
                        </select>
                    </div>
                    <div className="">

                    </div>
                </div>
            </div>

            <div className="col-6 h-10 pl-1">
                <div className="word-cloud-box">

                </div>
            </div>
        </div>
    )
}