import React from 'react';
import { Grid, Box } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';
import Attractions from './Attractions';
import Accomodations from './Accomodations';
import { useRegCode } from "src/context/RegCodeContext";
import PresentExchangeRate from './PresentExchangeRate';
import AverageExchangeRate from './AverageExchangeRate';

const CountryBoard = () => {
    const {regCode} = useRegCode();
    
    return (
        <PageContainer title="Dashboard" description="this is Dashboard">
            <Box>
                <Grid container spacing={2}>
                    <Grid item xs={12} lg={3}>
                        <PresentExchangeRate />
                    </Grid>
                    <Grid item xs={12} lg={3}>
                        <AverageExchangeRate />
                    </Grid>
                    <Grid item xs={12} lg={6}>
                        <AverageExchangeRate />
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