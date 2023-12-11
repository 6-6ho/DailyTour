import React from 'react';
import { Grid, Box } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';
// components
import MonthlyCharts from './components/MonthlyCharts';
import GeoCharts from './components/GeoCharts';
import SelectYearChart from './components/SelectYearChart';
import NewsWordCloud from './components/NewsWordCloud';
import SearchRankCountry from './components/SearchRankCountry';
// import RecentlyMonthRank from 'src/layouts/full/sidebar/CountryRank/RecentlyMonthRank';
// import RecentlyYearRank from 'src/layouts/full/sidebar/CountryRank/RecentlyYearRank';

const Dashboard = () => {
  return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        <Grid container rowSpacing={3}>
              <Grid item xs={12} lg={7}>
                <GeoCharts />
              </Grid>
              <Grid item xs={12} lg={5}>
                <MonthlyCharts />
              </Grid>
     
              <Grid item xs={12} lg={6}>
                <SelectYearChart />
              </Grid>
              <Grid item xs={12} lg={6}>
                <NewsWordCloud />
              </Grid>
          <Grid item xs={12} lg={4}>
            <SearchRankCountry />
          </Grid>
          <Grid item xs={12} lg={8}>
          
          </Grid>
          <Grid item xs={12}>
          </Grid>
          
        </Grid>
      </Box>
    </PageContainer>
  );
};

export default Dashboard;
