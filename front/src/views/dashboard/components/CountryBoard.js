import React, { useEffect, useState } from 'react';
import { Grid, Box, Card, CardMedia, Stack } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';
import Attractions from './Attractions';
import Accomodations from './Accomodations';
import { useRegCode } from "src/context/RegCodeContext";
import PresentExchangeRate from './PresentExchangeRate';
import AverageExchangeRate from './AverageExchangeRate';
import CountryExchnageScore from './CountryExchangeScore';
import CountryExchnageScoreRank from './CountryExchangeScoreRank';
import { useSelectCntCode } from 'src/context/SelectCntCodeContext';
import DashboardCard from 'src/components/shared/DashboardCard';

const CountryBoard = () => {
    const {regCode} = useRegCode();
    const {selectCntCode} = useSelectCntCode();
    const [imgPath, setImgPath] = useState('');

    console.log("CountryBoard selectCntCode : " + selectCntCode);


    // 국가 코드 바뀔 떄마다 사진 이름이 바뀜. 
    useEffect(() => {
        if(selectCntCode) {
            const path = require(`../../../assets/images/picture/${selectCntCode}.jpg`);
            setImgPath(path);
            console.log("imgPath : " + path);
        }
    }, [selectCntCode]);
    

    return (
        <PageContainer title="Dashboard" description="this is Dashboard">
            <Box>
                <Grid container spacing={2}>
                    <Grid item xs={12} lg={12}>
                        <Card>
                            <CardMedia component="img" height="400" src={imgPath}></CardMedia>
                        </Card>
                    </Grid>

                    <Grid item xs={12} lg={3}>
                        <PresentExchangeRate />
                    </Grid>
                    <Grid item xs={12} lg={3}>
                        <AverageExchangeRate />
                    </Grid>
                    <Grid item xs={12} lg={6}>
                        <DashboardCard title="" >
                        <Stack direction="row">  
                            <Grid item xs={7} lg={7}>
                                <CountryExchnageScore />
                            </Grid>
                            <Grid item xs={5} lg={5}>
                                <CountryExchnageScoreRank />
                            </Grid>
                            
                        </Stack>
                        </DashboardCard>
                    </Grid>

                    <Grid item xs={12} lg={6}>
                        <Attractions regCode={regCode}/>
                    </Grid>
                    <Grid item xs={12} lg={6}>
                        <Accomodations regCode={regCode}/>
                    </Grid>
                </Grid>

            </Box>
        </PageContainer>
    );
}

export default CountryBoard;