import './Dashboard.css';
import './Grid.css';
import React, { useState } from 'react';
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
import GeoCharts from './GeoCharts';


Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

// 월별 해외여행 차트 
export default function MonthlyChartjs() { 
  const [country, setCountry] = useState([]);

  useEffect (() => {
      url = `${localDomain}/country/month`;

      fetch(url)
      .then(res => {return res.json()})
      .then(data => {setCountry(data)}
      );

  }, [])


    const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
    const data = {
        labels: labels,
        datasets: [
          {
            label: '일본',
            data: [1300, 1500, 2100, 3000, 4000, 5000, 6000, 7000],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
          {
            label: '중국',
            data: [500, 900, 1100, 1000, 1000, 900, 1100, 1000 ],
            borderColor: 'rgb(100, 162, 100)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
          {
            label: '미국',
            data:[1000, 1100, 1200, 2000, 2500, 4000, 3500, 3800 ],
            borderColor: 'rgb(90, 200, 235)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
          {
            label: '베트남',
            data: [1500, 1300, 1800, 2500, 3000, 3500, 3000, 4000 ],
            borderColor: 'rgb(150, 162, 235)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
        ]
      };

    const options = {
        maintainAspectRatio: false,
        charts: {
          type: 'line',
          
        },
        stroke: {
          curve: 'smooth',
        },
        plugins: {
          legend: {
            position: 'top',
          },
          
          title: {
            display: true,
            text: '2023 월별 국가별 출국자 수'
          }
          
        }
    };


    return(
        <div className="monthly-chart-box-wrap">
            
            <div className="monthly-chart-box">
                
                {/* 지도 차트 */}
                <div className='monthly-chart-left'>    
                    <GeoCharts></GeoCharts>
                    
                </div>
                    
                {/* 월별 국가 출국자 수 차트 */}
                <div className='monthly-chart-right'>
                    <diV className='monthly-line-charts-container'>
                    <Line type="line" data={data} options={options} className='monthly-line-charts'/>
                    </diV>
                </div>
               
            </div>
        </div>
    )
}