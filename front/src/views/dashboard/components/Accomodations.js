import { serverDomain } from "src/domain/ServerDomain";
import React, { useState, useEffect } from 'react';
import { TableContainer, Paper,  Typography, Box, Table, TableBody, TableCell,
    TableHead, TableRow, Modal, Grid, Card, CardMedia } from '@mui/material';
import DashboardCard from '../../../components/shared/DashboardCard';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';
import { useRegCode } from "src/context/RegCodeContext";
ChartJS.register(ArcElement, Tooltip, Legend);

const Accomodations = () => {
    const [accom, setAccom] = useState ({});    // 숙소 정보
    const [accomList, setAccomList] = useState([]);
    const [accomCode, setAccomCode] = useState('');
    const [open, setOpen] = React.useState(false);      // 모달창
    const [pieChart, setPieChart] = useState({ datasets : [] });    // 파이차트 데이터
    const [imgPath, setImgPath] = useState('');
    const modal = {             // modal style
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 1000,
        height: 900,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 5,
    };
    const {regCode} = useRegCode();

    useEffect(()=>  {  
        if(regCode) {
            fetch(`${serverDomain}/accom/reg/${regCode}`)   // JSON-Server 에게 지역별 숙소 리스트 요청
                .then( res => { return res.json() } ) 
                .then( data => {
                    console.log(`fetch after ${data}` );
                    setAccomList(data);
            });
        }
    }, [regCode]);

    useEffect(()=>  {  
        if(accomCode) {
            fetch(`${serverDomain}/accom/${accomCode}`)   // JSON-Server 에게 숙소 상세 정보 데이터 요청
                .then( res => { return res.json() } ) 
                .then( data => {
                    console.log(`fetch after ${data}` );
                    setAccom(data);

                    const reviewStat = {
                        labels : ['긍정', '부정'],
                        datasets : [ {
                            type: 'doughnut',
                            data : [data.accomRevPos, data.accomRevNeg],
                            backgroundColor: 
                            [
                                'rgb(255, 99, 132)',
                                'rgb(54, 162, 235)'
                            ]
                        }]

                    }
                    setPieChart(reviewStat);

                    // 이미지 경로
                    const path = require(`../../../assets/images/word-cloud/${accomCode}_worldcloud.png`);
                    setImgPath(path);
                    console.log("imgPath : " + path);

                });
        }
    }, [accomCode]);
    


    const handleOpen = (available, accomCode) => {
        // setAccomCode(accomCode);
        console.log("handleOpen : " + available + " accomCode " + accomCode);
        setOpen(available);
        setAccomCode(accomCode);
    } 
    const handleClose = () => setOpen(false);

    

    return (
        <Box>
            {/* ------------------ modal 창 -------------------------- */}
            <Modal open={open} onClose={handleClose} aria-labelledby="modal-modal-title" aria-describedby="modal-modal-description">
                <Box sx={modal}>
                    <Typography id="modal-modal-title" variant="h3" component="h2" mb={2}>
                        {accom.accomName}
                    </Typography>
                    <Grid container spacing={3}>
                        <Grid item xs={12} lg={12}>
                            <Card>
                                <CardMedia component="img" height="380" alt="해당 관광지 이미지를 제공하지 않습니다." src={accom.imgPath} sx={{objectFit : "cover"}}></CardMedia>
                                {/* <img src={accom.imgPath} /> */}
                            </Card>
                        </Grid>
                        <Grid item xs={12} lg={6}>
                            <Box sx={{height: "300px"}}>
                                <Pie type="doughnut" data={pieChart}/>
                            </Box>
                        </Grid>
                        <Grid item xs={12} lg={6}>
                        <Card>
                                <CardMedia component="img" height="400" src={imgPath} sx={{objectFit : "cover"}} alt="해당 관광지 이미지를 제공하지 않습니다."></CardMedia>
                            </Card>
                        </Grid>
                    </Grid>
                </Box>
            </Modal>
            {/* ------------------ modal 창 -------------------------- */}

            <DashboardCard>
                <Box>
                    <Typography variant="h1" mb={2} align="center">숙박</Typography>
                    <Box>
                        <Typography variant="subtitle1" mt={3} mb={2} textAlign="right">출처 : 아고다</Typography>
                        <TableContainer component={Paper} >
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        <TableCell sx={{fontSize: 17}}>이름</TableCell>
                                        <TableCell sx={{fontSize: 17}} align="right">평점</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    { accomList && ( accomList.map((accom) => (
                                        <TableRow key={accom.accomCode} 
                                            onClick={() => handleOpen(true, accom.accomCode)}  
                                            sx={{ 
                                                '&:hover': {
                                                    backgroundColor: 'rgba(0, 0, 0, 0.04)' ,
                                                    cursor : 'pointer'
                                                }
                                            }}
                                        >
                                            <TableCell sx={{fontSize: 17}}>{accom.accomName}</TableCell>
                                            <TableCell align="right" sx={{fontSize: 17}}>
                                                {accom.accomScore}
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

export default Accomodations;