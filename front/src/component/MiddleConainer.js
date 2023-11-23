import './Dashboard.css';
import React, { useState, useEffect } from 'react';
import {Line} from 'react-chartjs-2';
import { localDomain } from './common';
import {
    Chart,
    LineController,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  } from "chart.js";
Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );


export default function MiddleContainer() {
    const [month, setMonth] = useState([]);

    useEffect( ()=>  {  
        fetch(`${localDomain}/month/list`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => { setMonth( data ); console.log(month); } 
        ); 
    }, []);

    return (
        <div className="middle-container-box-wrap">

            <div className="col-4 h-10">
                <div className='year-chart-box p-1'>
                    <div className="select-box-container">
                        <select>
                            <option></option>
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