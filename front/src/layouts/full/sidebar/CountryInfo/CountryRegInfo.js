import { useParams } from "react-router-dom";
import React, { useState, useEffect, useContext } from 'react';
import { serverDomain } from "src/domain/ServerDomain";
import {  FormControl, InputLabel, Box, Select, MenuItem } from '@mui/material';
import { useRegCode } from "src/context/RegCodeContext";

const CountryRegInfo = () => {
    const params = useParams();
    const cntCode = params.cntCode;
    const [regList, setRegList] = useState([]); // 지역리스트 
    const [cntName, setCntName] = useState('');
    const {regCode, setRegCode} = useRegCode();
 
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
                    console.log(`regCode : ${data[0].regCode}`);
                }
                
            } 
        ); 
    }, [cntCode, setRegCode]);

    // const changeSelect = (code) => () => {
    //     setRegCode(code);
    // }

    const changeSelect = (event) => {
        console.log("chanageSelect :  " + event.target.value);
        setRegCode(event.target.value);
    }

    return (
        <Box>
        {cntName && (
             <Box >
                {/* <h1>{cntName}</h1> 
                <Divider></Divider> */}
                {/* <List>
                    {
                        (regList && (regList.map((item) => 
                            <ListItem key={item.regCode}>
                                <ListItemButton onClick={changeSelect(item.regCode)} >
                                    <ListItemText primary={item.regName} primaryTypographyProps={{fontSize: 18}} />
                                </ListItemButton>
                            </ListItem>
                        )))
                    }
                </List> */} 

                {   regList && (
                     <FormControl required sx={{ m: 1, minWidth: 120 }}>
                        <InputLabel id="demo-select-small-label">지역</InputLabel>
                        <Select   labelId="demo-select-small-label" id="demo-select-small" onChange={changeSelect} value={regCode} label="지역" sx={{fontSize: '17px'}}>
                            {regList.map(item => (
                                <MenuItem key={item.regCode} value={item.regCode}>{item.regName}</MenuItem>
                                ))
                            }
                        </Select>
                    </FormControl>
                 )}
                    
                


                        {/* <Select labelId="month-dd" id="month-dd" size="small" onChange={changeSelect}>
                        {   regList && (regList.map(item => (
                            <MenuItem key={item.regCode} value={item.regCode}>{item.regName}</MenuItem>
                            )))
                        }
                    
                    </Select> */}
                    
                
                
{/* 
                <FormControl >
                    <Select  labelId="demo-simple-select-label"
    id="demo-simple-select" value={ setRegCode } onChange={changeSelect} sx={{ m: 1, minWidth: 120}} size="small" >
                        {regList && (regList.map(item => (
                            <MenuItem key={item.regCode} value={item.regCode}>{item.regName}</MenuItem>
                        )))
                    }
                    </Select> 
                </FormControl> */}


            </Box>
            )}
        </Box>

    )
}

export default CountryRegInfo;