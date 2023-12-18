import { serverDomain } from "src/domain/ServerDomain";
import React, { useState, useEffect } from 'react';
import { TableContainer, Paper,  Typography, Box, Table, TableBody, TableCell,
    TableHead, TableRow, Modal, Grid } from '@mui/material';
import DashboardCard from '../../../components/shared/DashboardCard';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';


const Attractions = (props) => {
    const regCode = props.regCode;
    const [attrList, setAttrList] = useState([]);
    const [attr, setAttr] = useState ({});
    const [attrCode, setAttrCode] = useState('');
    const [open, setOpen] = React.useState(false);
    const [pieChart, setPieChart] = useState({ datasets : [] });
    const modal = {             // modal style
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 1000,
        height: 800,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 5,
    };

    useEffect( ()=>  {  
        if(regCode) {
            fetch(`${serverDomain}/attr/reg/${regCode}`)  // JSON-Server 에게 지역별 관광지 리스트 요청 
                .then( res => { return res.json() } ) 
                .then( data => {
                    setAttrList(data);
                    console.log(attrList);
                } 
            ); 
        }
    }, [regCode]);

    
    useEffect(()=>  {  
        if(attrCode) {
            fetch(`${serverDomain}/attr/${attrCode}`)   // JSON-Server 에게 지역별 숙소 데이터 요청
                .then( res => { return res.json() } ) 
                .then( data => {
                    console.log(`fetch after ${data}` );
                    setAttr(data);

                    const reviewStat = {
                        labels : ['긍정', '부정'],
                        datasets : [ {
                            type: 'doughnut',
                            data : [data.attrRevPos, data.attrRevNeg],
                            backgroundColor: 
                            [
                                'rgb(255, 99, 132)',
                                'rgb(54, 162, 235)'
                            ]
                        }]

                    }
                    setPieChart(reviewStat);

            });
        }
    }, [attrCode]);

    const handleOpen = (bool, attrCode) => {
        // setAccomCode(accomCode);
        console.log("handleOpen : " + bool + " attrCode " + attrCode);
        setOpen(bool);
        setAttrCode(attrCode);
    } 
    const handleClose = () => setOpen(false);

    return (
        <Box>
            <Modal open={open} onClose={handleClose} aria-labelledby="modal-modal-title" aria-describedby="modal-modal-description">
                <Box sx={modal}>
                    <Typography id="modal-modal-title" variant="h3" component="h2">
                        {attr.attrName}
                    </Typography>
                    <Grid container spacing={3}>
                        <Grid item xs={12} lg={12}>
                            <Box sx={{height: "300px"}}>
                                <Pie type="doughnut" data={pieChart}/>
                            </Box>
                        </Grid>
                        <Grid item xs={12} lg={6}>
                            <Box sx={{height: "300px"}}>
                                <Pie type="doughnut" data={pieChart}/>
                            </Box>
                        </Grid>
                        <Grid item xs={12} lg={6}>
                            <Box sx={{height: "300px"}}>
                                <Pie type="doughnut" data={pieChart}/>
                            </Box>
                        </Grid>
                    </Grid>
                    
                </Box>
            </Modal>

            <DashboardCard >
                <Box>
                    <Typography variant="h1" mb={2} align="center">관광지</Typography>
                    <Box>
                        <TableContainer component={Paper}>
                            <Table aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell sx={{fontSize: 17}}>이름</TableCell>
                                        <TableCell sx={{fontSize: 17}}  align="right">평점</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    { attrList && ( attrList.map((attr) => (
                                        <TableRow key={attr.attrCode} 
                                            onClick={() => handleOpen(true, attr.attrCode)} 
                                            sx={{ 
                                            '&:hover': {
                                                backgroundColor: 'rgba(0, 0, 0, 0.04)' ,
                                                cursor : 'pointer'
                                            }
                                        }} >
                                            <TableCell sx={{fontSize: 17}}>{attr.attrName}</TableCell>
                                            <TableCell sx={{fontSize: 17}} align="right">
                                                {attr.attrScore}
                                            </TableCell>
                                        </TableRow>
                                        )))
                                    }
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </Box>
                </Box>
            </DashboardCard>
        </Box>
    )

}

export default Attractions;