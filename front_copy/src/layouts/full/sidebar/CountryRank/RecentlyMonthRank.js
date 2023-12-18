import React, { useState, useEffect } from 'react';
import {Link} from "react-router-dom"
import { serverDomain } from 'src/domain/ServerDomain';
import { CardContent, Card,Typography,  List, ListItem, ListItemButton, ListItemText } from '@mui/material';


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
        <Card sx={{ margin: 2, maxWidth: 270}}>
           <CardContent>
           <Typography gutterBottom variant="h4" component="div"> 월별 랭킹</Typography>
            <List>
            {
                (monthList && (monthList.map((month) =>
                    <ListItem>
                         <ListItemButton component="a" href={"/country/" + month.cntCode }>
                            <ListItemText primary={month.cntName} primaryTypographyProps={{fontSize: 18}}/>
                        </ListItemButton>
                    </ListItem>
                )))
            }
            </List>
            
            </CardContent>
        </Card>
    );
}
export default RecentlyMonthRank;