import { useParams } from "react-router-dom";
import React, { useState, useEffect, useContext } from 'react';
import { serverDomain } from "src/domain/ServerDomain";
import { List, ListItem, ListItemText,ListItemButton, Divider, Box, Select, MenuItem, Card } from '@mui/material';
import { useRegCode } from "src/context/RegCodeContext";


const CountryList = () => {
    const params = useParams();
    const cntCode = params.cntCode;
    const [cntList, setCntList] = useState([]); // 국가리스트
    // const [cntName, setCntName] = useState('');
    // const {setRegCode} = useRegCode();

    useEffect( ()=>  {  
        fetch(`${serverDomain}/country-list`)   // JSON-Server에 국가 리스트 요청 
	        .then( res => { return res.json() } ) 
	        .then( data => {
                setCntList(data);
                console.log(`country list fetch : ${data}`);
                // if(data.length > 0) {
                //     setCntName(data[0].cntName);
                //     setRegCode(data[0].regCode);
                //     console.log(`cntName : ${data[0].cntName}`);
                //     console.log(`default value regCode : ${data[0].regCode}`);
                // }
                
            } 
        ); 
    }, [cntList]);

    return(
        <Box>
        {cntList && (
            <Box>
                <List>
                    {
                        (cntList && (cntList.map((item) => 
                            <ListItem key={item.cntCode}>
                                <ListItemButton component="a" href={"/country/" + item.cntCode} >
                                    <ListItemText primary={item.cntName} primaryTypographyProps={{fontSize: 18}} />
                                </ListItemButton>
                            </ListItem>
                        )))
                    }
                </List>

                {/* <Select  labelId="month-dd" id="month-dd" value={ selected }   size="small"
                    onChange={changeSelect}>
                    {regList && (regList.map(item => (
                        <MenuItem key={item.regCode} value={item.regCode}>{item.regName}</MenuItem>
                    )))
                    }
                </Select>  */}
            </Box>
            )}
        </Box>
    )

}

export default CountryList;