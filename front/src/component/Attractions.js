import './Dashboard.css'
import './Grid.css'
import React, { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";
import { localDomain } from './common';

export default function Attractions(props) {         // 관광지 리스트
    const regCode = props.regCode;
    const [attrList, setAttrList] = useState([]);

    useEffect( ()=>  {  
        fetch(`${localDomain}/attr/reg/${regCode}`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                setAttrList(data);
                console.log(attrList);
             } 
        ); 
    }, [attrList]);

    return (
        <div className="col-5 p-10">
            <div className="rank-box-wrap">
                <div className="rank-box">
                    <div className="rank-title">
                        <h1 className="text-center">관광지</h1>
                    </div>
                    <div className="rank-list">
                        <table className="table-style">
                            <tr>
                                <th className="title-column">
                                    이름
                                </th>
                                <th className="score-column">
                                    평점
                                </th>
                            </tr>
                            
                                { attrList && (
                                    attrList.map((attr) => (
                                        <tr>
                                            <td key={attr.attrCode}> {attr.attrName} </td>
                                            
                                            <td> 
                                                <div className="score-bar-wrap">
                                                    <div className="score-bar-box">
                                                        <div className="score-bar" style={ {"width": "60%"}} > </div>
                                                    </div>
                                                    {attr.attrScore} 
                                                </div>
                                            </td>
                                        </tr>
                                    ))
                                )
                                }
                          
                        </table>
                    </div>
                </div>
            </div>
        </div>
);

}