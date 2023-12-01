import './Dashboard.css';
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


export default function MiddleContainer() {     
    const [yearList, setYearList] = useState([]);
    const [selected, setSelected] = useState("");
    const [countryStatData, setCountryStatData] = useState({
        datasets : []
    });


    useEffect( ()=>  {  
        fetch(`${localDomain}/country/year/list`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                const optionList = [];

                for(let i=0; i<data.length; i++) {
                    optionList.push(<option value={data[i]}>{data[i]}년</option>)
                }

                setYearList(optionList);
                console.log(yearList);
                // console.log(month);
             } 
        ); 
    }, []);

    const changeSelect = (e) => {
        let year = e.target.value;
        setSelected(year);

        
        fetch(`${localDomain}/country/year/` + year)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {  
                console.log(data);

            
                const countryStat = {
                    
                labels: data.map((country) => country.cntName),
                datasets: [{
                        type:'bar',
                        label: data.map((country) => country.cntName),
                        data: data.map((country) => country.emi),
                        backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        ],
                        borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        ],

                    }], 
                borderWidth: 2
                
                };

                setCountryStatData(countryStat);

                console.log(countryStat); 
                } 
        ); 
    }

    
    const options = {
        maintainAspectRatio: false,
        charts: {
            type: 'bar',
          },
        scales: {
            y: {
              beginAtZero: true,
            },
        },
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: `${selected}년 국가별 출국자 수`
          }
          
        }
    };

    return (
        <div className="middle-container-box-wrap">

            <div className="col-4 h-10">
                <div className='year-chart-box p-1'>
                    <div className="select-box-container">
                        <select onChange={changeSelect} value={selected} defaultValue={1}>
                            {yearList}
                        </select>
                    </div>
                    <div className="monthly-chart-box">
                        {/* <div className='monthly-chart-right'> */}
                            <diV className='monthly-line-charts-container'>
                                <Bar type='bar' data={countryStatData} options={options} className='monthly-line-charts'/>
                            </diV>
                        {/* </div> */}
                    </div>
                </div>
            </div>

            <div className="col-3 h-10 pl-1">
                <div className="word-cloud-box">
                    
                </div>
            </div>
            <div className="col-3 h-10 pl-1">
                <div className="word-cloud-box p-1">
                    <span className="word-cloud-title text-center"> 해외여행 기사 주요 키워드 </span>
                    <div className="img-wrap">
                        <img src="img/news_wordcloud2.png"></img>
                    </div>
                </div>
            </div>
        </div>
    )
}