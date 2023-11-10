import './Dashboard.css'
import './Grid.css'
import React from 'react'
import ApexCharts from 'react-apexcharts';
import GeoCharts from './GeoCharts';
// 월별 해외여행 차트 
export default function MonthlyChart() { 



    return(
        <div className="monthly-chart-box-wrap">
            
            <div className="monthly-chart-box">
                <div className='monthly-chart-left'>    
                    <GeoCharts></GeoCharts>
                    
                </div>
                    
                <div className='monthly-chart-right'>
                    <diV className='monthly-line-charts-container'>
                        <ApexCharts 
                                series={ [
                                    { name: "일본",
                                data: [1300, 1500, 2100, 3000, 4000, 5000, 6000, 7000],
                                },
                                { name: "중국",
                                data: [1000, 900, 1100, 1000, 1000, 900, 1100, 1000 ],
                                },
                                { name: "미국",
                                data:  [1000, 1100, 1200, 2000, 2500, 4000, 3500, 3800 ],
                                },
                                { name: "베트남",
                                data:  [1500, 1300, 1800, 2500, 3000, 3500, 3000, 4000 ],
                                }         

                                    ]} 
                                options={
                                    {  
                                    chart : {
                                        responsive: false,
                                        type: 'line', 
                                        zoom: {
                                            enabled: false
                                        }                 
                                    }, 
                                    stroke : {
                                        curve: 'smooth'
                                    }
                                    
                                }}>

                            </ApexCharts>
                        </diV>
                    </div>
                {/* </div> */}
            </div>
        </div>
    )
}