import './Dashboard.css'
import './Grid.css'
import React, { useState, useEffect } from 'react';
import { localDomain } from './common';

export default function Accomodations(props) {  // 숙박
    const regCode = props.regCode;
    const [accomList, setAccomList] = useState([]);

    console.log(regCode);

    useEffect( ()=>  {  
        fetch(`${localDomain}/accom/reg/${regCode}`)   // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                console.log(data);
                setAccomList(data);
            } 
        ); 
    }, [accomList]);

    return (
        <div className="col-5 p-10">
            <div className="rank-box-wrap">
                <div className="rank-box">
                    <div className="rank-title">
                        <h1>숙박</h1>
                    </div>
                    <div className="rank-list">
                        <table className="table-style">
                            <tr>
                                <th>
                                    이름
                                </th>
                                <th>
                                    평점
                                </th>
                            </tr>
                            
                                { accomList && (
                                    accomList.map((accom) => (
                                        <tr>
                                            <td key={accom.accomCode}> {accom.accomName} </td>
                                            <td> {accom.accomScore} </td>
                                        </tr>
                                    ))
                                )
                                }
                          
                        </table>
                    </div>
                </div>
            </div>
        </div>
                        
        
    )
}