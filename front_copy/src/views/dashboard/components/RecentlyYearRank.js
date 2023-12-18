import React, { useState, useEffect } from 'react';

import {Link} from "react-router-dom"
import { serverDomain } from 'src/domain/ServerDomain';
import DashboardCard from '../../../components/shared/DashboardCard';
import {List, ListItem, ListItemButton, ListItemText } from '@mui/material';


const RecentlyYearRank = () => {
    const [yearList, setYearList] = useState([]);   // 연도별 rank
    
    useEffect( ()=>  {  
        fetch(`${serverDomain}/country/year/2023`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
               console.log(data);
               setYearList(data);
             } 
        ); 
    }, []);

    return (
        <DashboardCard title="연도별 랭킹">
            <List>
                {
                    (yearList && (yearList.map((year) => 
                        <ListItem>
                             <ListItemButton component="a" href={"/country/" + year.cntCode }>
                            <ListItemText primary={year.cntName} primaryTypographyProps={{fontSize: 18}} />
                        </ListItemButton>
                        </ListItem>
                    )))
                }
            </List>
        </DashboardCard>
    )
}   

export default RecentlyYearRank;