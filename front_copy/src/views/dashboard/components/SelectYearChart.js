import { Select, MenuItem, Box } from '@mui/material';
import React, { useState, useEffect } from 'react';
import DashboardCard from '../../../components/shared/DashboardCard';
import { Bar} from 'react-chartjs-2';
import { serverDomain } from 'src/domain/ServerDomain';
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

const SelectYearChart = () => {
  const [yearList, setYearList] = useState([]);
  const [selected, setSelected] = useState("2023");
  const [countryStatData, setCountryStatData] = useState({
      datasets : []
  });


  useEffect( ()=>  {  
      fetch(`${serverDomain}/country/year/list`)  // JSON-Server 에게 year List 요청
        .then( res => { return res.json() } ) 
        .then( data => {


              setYearList(data);
              console.log(yearList);
              // console.log(month);
           } 
      ); 
  }, []);

  const changeSelect = (e) => {
      let year = e.target.value;
      setSelected(year);
  }

  useEffect( ()=>  {      
      fetch(`${serverDomain}/country/year/` + selected)  // JSON-Server 에게 선택된 year의 정보 요청
        .then( res => { return res.json() } ) 
        .then( data => {  
              console.log(data);

              const countryStat = {
                  
              labels: data.map((country) => country.cntName),
              datasets: [{
                      type:'bar',
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
  }, selected);

  
  const options = {
      maintainAspectRatio: true,
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
    
        
      }
  };
    
    
    return (
      <DashboardCard title={selected + "년 국가별 출국자 수" } >
        <Box>
          <Select  labelId="month-dd" id="month-dd" value={ selected }   size="small"
              onChange={changeSelect}>
              {
                yearList && ( yearList.map((year) => (
                  <MenuItem value={year}>{year}년</MenuItem>
                )))
              }
          </Select>
          <Bar type='bar' data={countryStatData} options={options} height="200px" className='monthly-line-charts'/>
        </Box>
      </DashboardCard>

    )
}

export default SelectYearChart;