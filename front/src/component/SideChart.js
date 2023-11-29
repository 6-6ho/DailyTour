
import './Bar.css';
import React, { useState, useEffect } from 'react';
import {Line, Bar} from 'react-chartjs-2';
import { localDomain } from './common';
import {
    Chart,
    LineController,
    BarController,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    BarElement
  } from "chart.js";
Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    BarElement,
    Title,
    Tooltip,
    Legend
  );




export default function SideChart() {
    const [monthStat, setMonthStat] = useState([]);
    const [yearStat, setYearStat] = useState([]);

    useEffect( ()=>  {  
        fetch(`${localDomain}/country/month/8`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                console.log(data);

                setMonthStat(data);

                // console.log(month);
             } 
        ); 
    }, []);


    return (
        <div className="side-chart-box-container">
            <div className="side-chart-box">
                
                <div className="list-div col-10">
                    <ul className="ul-style-none">
                        {monthStat.map(item =>(
                            <li className="li-style-none"><a href={'/country/' + item.regCode}>일본</a></li>
                       
                        ))}
                        <li className="li-style-none"><a href="">일본</a></li>
                        <hr></hr>
                        <li className="li-style-none"><a href="">일본</a></li>
                        <hr></hr>
                        <li className="li-style-none"><a href="">일본</a></li>
                    </ul>
                </div>
            </div>
            <div className="side-chart-box">
                <div>
                    
                </div>
            </div>
        </div>
    )
}