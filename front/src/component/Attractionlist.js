import './Dashboard.css'
import './Grid.css'
import React, { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";

export default Attractionlist(props) {   
    
    const [attrList, setAttrList] = useState([]);

    useEffect( ()=>  {  
        fetch(`${localDomain}/attr/reg/regCode`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                const optionList = [];

                for(let i=0; i<data.length; i++) {
                    optionList.push(<option value={data[i]}>{data[i]}년</option>)
                }

                setYearList(optionList);
                console.log(yearList);
                // console.log(month);
             } 
        ); 
    }, []);

    return (

    )

}