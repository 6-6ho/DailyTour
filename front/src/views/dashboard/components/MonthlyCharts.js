import React, { useState, useEffect } from 'react';
import DashboardCard from '../../../components/shared/DashboardCard';
// import Chart from 'react-apexcharts';
import {Line} from 'react-chartjs-2';
import { serverDomain } from 'src/domain/ServerDomain';
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
// import GeoCharts from './GeoCharts';


Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );


const MonthlyCharts = () => {

    const [countryStatData, setCountryStatData] = useState({
        datasets : []
      });
      
      useEffect (() => {
          fetch(`${serverDomain}/country/month`)
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
    
      }, []);
    
        const options = {
            maintainAspectRatio: true,
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
              
            }
        };

    return (

       
      <DashboardCard title="2023년 국가별 월별 출국자 수" >

                <Line 
                    options={options}
                    data={countryStatData}
                    type="line"
                    height="130px"
                ></Line>
            
      </DashboardCard>
        
    );
};

export default MonthlyCharts;
