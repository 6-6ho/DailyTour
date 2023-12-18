import React from 'react';
import { Grid, Box } from '@mui/material';
import PageContainer from 'src/components/container/PageContainer';
// components
import MonthlyCharts from './components/MonthlyCharts';
import GeoCharts from './components/GeoCharts';
import SelectYearChart from './components/SelectYearChart';
import NewsWordCloud from './components/NewsWordCloud';
import SearchRankCountry from './components/SearchRankCountry';
import RecentlyMonthRank from './components/RecentlyMonthRank';
import RecentlyYearRank from './components/RecentlyYearRank';
import TravelHashtag from './components/TravelHashtag';
// import RecentlyMonthRank from 'src/layouts/full/sidebar/CountryRank/RecentlyMonthRank';
// import RecentlyYearRank from 'src/layouts/full/sidebar/CountryRank/RecentlyYearRank';

const Dashboard = () => {
  return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        <Grid container rowSpacing={2} columnSpacing={1}>
              <Grid item xs={12} lg={7}>
                <GeoCharts />
              </Grid>
              <Grid item xs={12} lg={5}>
                <MonthlyCharts />
              </Grid>
              <Grid item xs={12} lg={3}>
                <RecentlyMonthRank />
              </Grid>
              <Grid item xs={12} lg={3}>
                <RecentlyYearRank/>
              </Grid>
              <Grid item xs={12} lg={6}>
                <SelectYearChart />
              </Grid>
              <Grid item xs={12} lg={4}>
                <NewsWordCloud />
              </Grid>
              <Grid item xs={12} lg={4}>
                <SearchRankCountry />
              </Grid>
              <Grid item xs={12} lg={4}>
               <TravelHashtag />
              </Grid>
         </Grid>
      </Box>
    </PageContainer>
  );
};

export default Dashboard;
