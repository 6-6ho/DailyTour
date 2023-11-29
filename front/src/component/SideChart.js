import React, { useState, useEffect } from 'react';
import {Line, Bar} from 'react-chartjs-2';
import {Link} from "react-router-dom"
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
    const [monthList, setMonthList] = useState([]); // 월별 rank
    const [yearList, setYearList] = useState([]);   // 연도별 rank
    
    useEffect( ()=>  {  
        fetch(`${localDomain}/country/month/8`)
	        .then( res => { return res.json() } ) 
	        .then( data => {
               console.log(data);
               setMonthList(data);
             } 
        ); 
    }, []);

    useEffect( ()=>  {  
        fetch(`${localDomain}/country/year/2023`)
	        .then( res => { return res.json() } ) 
	        .then( data => {
               console.log(data);
               setYearList(data);
             } 
        ); 
    }, []);


    return (
        <div className="side-chart-box-container">
            <div className="side-chart-box">
                <ol className="side-ol-style">
                    {
                        monthList.map( (month) => (
                            <li className key={month.cntCode}> <Link to={"/country/" + month.cntCode }> {month.cntName} </Link> </li>
                        ))
                    }
                    
                </ol>
            </div>
            <div className="side-chart-box">
            <ol className="side-ol-style">
                    {
                        yearList.map( (year) => (
                            <li className key={year.cntCode}> <Link to={"/country/" + year.cntCode }> {year.cntName} </Link> </li>
                        ))
                    }
                    
                </ol>
            </div>
        </div>
    )
}