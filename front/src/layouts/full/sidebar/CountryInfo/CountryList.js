import { useParams } from "react-router-dom";
import React, { useState, useEffect, useContext } from 'react';
import { serverDomain } from "src/domain/ServerDomain";
import { List, ListItem, ListItemText,ListItemButton, Divider, Box, Select, MenuItem, Card } from '@mui/material';


const CountryList = () => {
    const params = useParams();
    const cntCode = params.cntCode;     // select한 국가 보기
    const [cntList, setCntList] = useState([]); // 국가리스트

    useEffect( ()=>  {  
        fetch(`${serverDomain}/country-list`)   // JSON-Server에 국가 리스트 요청 
	        .then( res => { return res.json() } ) 
	        .then( data => {
                setCntList(data);
                console.log(`country list fetch : ${data}`);
            } 
        ); 
    }, []);

    return(
        <Box>
        {cntList && (
            <Box>
                <List>
                    {
                        (cntList && (cntList.map((item, index) => 
                            <ListItem key={item.cntCode}>
                                <ListItemButton component="a" href={"/country/" + item.cntCode} selected={item.cntCode === cntCode}>
                                    <ListItemText primary={item.cntName} primaryTypographyProps={{fontSize: 18}} />
                                </ListItemButton>
                            </ListItem>
                        )))
                    }
                </List>
            </Box>
            )}
        </Box>
    )

}

export default CountryList;