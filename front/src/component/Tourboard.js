import './Dashboard.css'
import './Grid.css'
import Navbar from './Navbar';
import { useParams } from "react-router-dom";
import React, { useState, useEffect } from 'react';
import { localDomain } from './common';

export default function Tourboard() {
    const params = useParams();
    const cntCode = params.cntCode;
    const [regList, setRegList] = useState([]); // 지역리스트 
    console.log(cntCode);

    useEffect( ()=>  {  
        fetch(`${localDomain}/attr/${cntCode}`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
              
               setRegList(data);
               console.log(regList);
             } 
        ); 
    }, []);




    return (
        <div className="dashboard-wrap">
            <div className="col-2">
                <div className='side-bar-wrap'>
                    <div className='side-bar'>
                        <div className='logo-wrap'>
                            <div className='logo-box-wrap'>
                                <img src='img/airplane_icon.png'></img>
                                <span className='logo-font'>Daily Tour</span>
                            </div>
                        </div>
                        <div className="country-title">
                            <h3></h3>
                        </div>

                    </div>
                </div>
            </div>
            <div className="col-8 right-wrap">
                <Navbar></Navbar>
                <div class='dashboard-div'>
                    <div class='exchange-rate-box-wrap'>
                        <div class='exchange-rate-box'>
                        
                        </div>
                    </div>
                    
                    <div class="rank-div">
                        <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">

                                </div>
                            </div>
                        </div>
                        
                        <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}