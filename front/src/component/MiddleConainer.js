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
    return (
        <div className="middle-container-box-wrap">

            <div className="col-5 h-10">
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

            <div className="col-5 h-10 pl-1">
                <div className="word-cloud-box">

                </div>
            </div>
        </div>
    )
}