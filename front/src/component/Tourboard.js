import './Dashboard.css'
import './Grid.css'
import Navbar from './Navbar';
import { useParams } from "react-router-dom";
import React, { useState, useEffect } from 'react';
import { localDomain } from './common';
import Exchange from './Exchange';
import Accomodations from './Accomodations';
import Attractions from './Attractions';

export default function Tourboard() {
    const params = useParams();
    const cntCode = params.cntCode;
    const [regList, setRegList] = useState([]); // 지역리스트 
    const [cntName, setCntName] = useState('');
    const [selected, setSelected] = useState("");
    console.log(cntCode);



    useEffect( ()=>  {  
        fetch(`${localDomain}/attr/${cntCode}`)   // JSON-Server에 국가의 지역 리스트 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
               setRegList(data);
               console.log(regList);

               if(data.length > 0 ) {
                setCntName(data[0].cntName);
                setSelected(data[0].regCode);
               }
                
            } 
        ); 
    }, [cntCode]);

    useEffect(() => {
        console.log(regList);
    }, [regList]);

    const changeSelect = (e) => {
        let regCode = e.target.value;
        setSelected(regCode);
        console.log(selected);
    }


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
                        {cntName && (
                                <div>
                                    <h1>{cntName}</h1>
                                    <select onChange={changeSelect} value={selected}>
                                        {regList.map(item => (
                                            <option key={item.regCode} value={item.regCode}>{item.regName}</option>
                                        ))}
                                    </select>
                                </div>
                            )}
                        </div>

                    </div>
                </div>
            </div>
            <div className="col-8 right-wrap">
                <Navbar></Navbar>
                <div class='dashboard-div'>
                    <Exchange></Exchange>
                
                        {
                            selected && (
                                <div class="rank-div">
                                    <Attractions regCode = {selected} ></Attractions>
                                    <Accomodations regCode = {selected} ></Accomodations>
                                </div>
                            )
                        }
                       
                        {/* <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">

                                </div>
                            </div>
                        </div> */}

                      
                        
                        {/* <div class="col-5 p-10">
                            <div class="rank-box-wrap">
                                <div class="rank-box">
                                    
                                </div>
                            </div>
                        </div> */}
                    
                </div>
            </div>
        </div>
    )
}