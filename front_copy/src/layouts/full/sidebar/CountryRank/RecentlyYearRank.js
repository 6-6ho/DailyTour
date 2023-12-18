import React, { useState, useEffect } from 'react';

import {Link} from "react-router-dom"
import { serverDomain } from 'src/domain/ServerDomain';
import {Card, CardContent, Typography,  List, ListItem, ListItemButton, ListItemText } from '@mui/material';


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
        <Card  sx={{ margin: 2, maxWidth: 270 }}>
            <CardContent>
            <Typography gutterBottom variant="h4" component="div"> 연도별 랭킹</Typography>
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
            </CardContent>
        </Card>
    )
}   

export default RecentlyYearRank;