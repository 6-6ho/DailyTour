import React, { useState, useEffect } from 'react';
import {Link} from "react-router-dom"
import { serverDomain } from 'src/domain/ServerDomain';
import DashboardCard from '../../../components/shared/DashboardCard';
import {List, ListItem, ListItemButton, ListItemText, ListItemIcon, Typography, Divider } from '@mui/material';
const RecentlyMonthRank = () => {
    const [monthList, setMonthList] = useState([]); // 월별 rank

    
    useEffect( ()=>  {  
        fetch(`${serverDomain}/country/month/8`)  // JSON-Server 에게 students data 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
               console.log(data);
               setMonthList(data);
             } 
        ); 
    }, []);

    
    return (
        <DashboardCard title="월별 랭킹">
            <Typography variant="caption" textAlign="right">출처 : 한국관광 데이터랩(한국관광공사)</Typography>
            <List >
            {
                (monthList && (monthList.map((month, index) =>
                <ListItem sx={{paddingLeft: "2px", paddingRight: "2px"}}>
                    <ListItemButton sx={{paddingLeft: 0}} component="a" href={"/country/" + month.cntCode }>
                        <ListItemIcon primaryTypographyProps={{fontSize: 18}}>{index+1} 위 </ListItemIcon>
                        <ListItemText primary={month.cntName} primaryTypographyProps={{fontSize: 18}}/>
                    </ListItemButton>
                </ListItem>     
                )))
            }
  
            </List>
        </DashboardCard>
    );
}
export default RecentlyMonthRank;