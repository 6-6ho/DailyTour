import React, { useState, useEffect } from 'react';

import {Link} from "react-router-dom"
import { serverDomain } from 'src/domain/ServerDomain';
import DashboardCard from '../../../components/shared/DashboardCard';
import {List, ListItem, ListItemButton, ListItemIcon, ListItemText, Typography, Stack } from '@mui/material';
import { Padding } from '@mui/icons-material';


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
            <Stack direction="column"  mb={1}>
                <Typography variant="caption" textAlign="right">출처 : 한국관광 데이터랩(한국관광공사)</Typography>
                <Typography variant="caption" textAlign="right">2023년 기준</Typography>
            </Stack>
            <List>
                {
                    (yearList && (yearList.map((year, index) => 
                        <ListItem sx={{paddingLeft: "2px", paddingRight: "2px"}}>
                             <ListItemButton sx={{paddingLeft: 0}} component="a" href={"/country/" + year.cntCode }>
                                <ListItemIcon  primaryTypographyProps={{fontSize: 18}}>{index+1} 위 </ListItemIcon>
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