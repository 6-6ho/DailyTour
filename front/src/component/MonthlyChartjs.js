import './Dashboard.css';
import './Grid.css';
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
    // const [country, setCountry] = useState([]);
    const [countryStatData, setCountryStatData] = useState({
      datasets : []
    });
    
    useEffect (() => {
        fetch(`${localDomain}/country/month`)
        .then(res => {return res.json()})
        .then(data => {
            // setCountry(data);
            console.log(data);

            const dataArray = data.reduce((acc, { cntName, month, emi }) => {
              if (!acc[cntName]) {
                acc[cntName] = { cntName, month: [], emi: [] };
              }
              acc[cntName].month.push(month);
              acc[cntName].emi.push(emi);
              return acc;
            }, {});
        
            const countryData = Object.values(dataArray);
            
            const countryStat = {
              labels: countryData[0].month,
              datasets: [
                {
                  label: countryData[0].cntName,
                  data: countryData[0].emi,
                  borderColor: 'rgb(255, 99, 132)',
                  backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
                {
                  label: countryData[1].cntName,
                  data: countryData[1].emi,
                  borderColor: 'rgb(100, 162, 100)',
                  backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
                {
                  label: countryData[2].cntName,
                  data: countryData[2].emi,
                  borderColor: 'rgb(90, 200, 235)',
                  backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
                {
                  label: countryData[3].cntName,
                  data: countryData[3].emi,
                  borderColor: 'rgb(150, 162, 235)',
                  backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
                {
                  label: countryData[4].cntName,
                  data: countryData[4].emi,
                  borderColor: 'rgb(150, 85, 125)',
                  backgroundColor: 'rgba(255, 99, 132, 0.5)',
                },
              ]
            };

            setCountryStatData(countryStat);

            console.log(countryStat);
    });

    });

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
                    <Line type="line" data={countryStatData} options={options} className='monthly-line-charts'/>
                    </diV>
                </div>
               
            </div>
        </div>
    )
}