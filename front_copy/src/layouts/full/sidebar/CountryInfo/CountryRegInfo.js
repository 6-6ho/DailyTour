import { useParams } from "react-router-dom";
import React, { useState, useEffect, useContext } from 'react';
import { serverDomain } from "src/domain/ServerDomain";
import { List, ListItem, ListItemText,ListItemButton, Divider, Box, Select, MenuItem, Card } from '@mui/material';
import { useRegCode } from "src/context/RegCodeContext";

const CountryRegInfo = () => {
    const params = useParams();
    const cntCode = params.cntCode;
    const [regList, setRegList] = useState([]); // 지역리스트 
    const [cntName, setCntName] = useState('');
    const {setRegCode} = useRegCode();
 
    console.log(cntCode);

    useEffect( ()=>  {  
        fetch(`${serverDomain}/country/reg/${cntCode}`)   // JSON-Server에 국가의 지역 리스트 요청
	        .then( res => { return res.json() } ) 
	        .then( data => {
                setRegList(data);
                if(data.length > 0) {
                    setCntName(data[0].cntName);
                    setRegCode(data[0].regCode);
                    console.log(`cntName : ${data[0].cntName}`);
                    console.log(`default value regCode : ${data[0].regCode}`);
                }
                
            } 
        ); 
    }, [cntCode, setRegCode]);

    const changeSelect = (code) => () => {
        setRegCode(code);
    }

    return (
        <Box>
        {cntName && (
            <Box>
                <h1>{cntName}</h1> 
                <Divider></Divider>
                <List>
                    {
                        (regList && (regList.map((item) => 
                            <ListItem key={item.regCode}>
                                <ListItemButton onClick={changeSelect(item.regCode)} >
                                    <ListItemText primary={item.regName} primaryTypographyProps={{fontSize: 18}} />
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

export default CountryRegInfo;