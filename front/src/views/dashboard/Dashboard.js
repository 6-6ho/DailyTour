import React from 'react';
import { Grid, Box, Stack, Typography } from '@mui/material';
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
import DashboardCard from 'src/components/shared/DashboardCard';
import { useCntCodeList } from 'src/context/CntCodeListContext';
import DailyTourScoreRank from './components/DailyTourScoreRank';

const Dashboard = () => {
   return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        
        <Grid container rowSpacing={2} columnSpacing={1}>
          <Grid item xs={12} lg={12}>
            <DashboardCard title="2023년 국가별 월별 출국자 수">
              <Stack direction="row">  
                <Grid item xs={7} lg={7}>
                  <GeoCharts />
                </Grid>
                <Grid item xs={5} lg={5}>
                  <MonthlyCharts />
                </Grid>
              </Stack>
              <Typography variant="subtitle1" mt={2} textAlign="right">출처 : 한국관광 데이터랩(한국관광공사)</Typography>
              <Typography variant="subtitle1" textAlign="right">국민 해외관광객 주요 목적지별 통계</Typography>
            </DashboardCard>
          </Grid>

          
      {/* 오른쪽 섹션: SelectYearChart */}
      <Grid item xs={12} lg={7}>
        <SelectYearChart />
      </Grid>

          <Grid item xs={12} lg={5}>
            <Grid container spacing={2} sx={{height : "100%"}}>
          {/* 위쪽: RecentlyMonthRank와 RecentlyYearRank */}
          <Grid item xs={6}>
            <RecentlyMonthRank />
          </Grid>
          <Grid item xs={6}>
            <RecentlyYearRank />
          </Grid>
          {/* 아래쪽: TravelHashtag */}
          <Grid item xs={12}>
            <TravelHashtag />
          </Grid>
        </Grid>
        </Grid>


          {/* <Stack spacing={{ xs: 1, sm: 2 }}  direction="row" useFlexGap flexWrap="wrap">
              <Grid item xs={12} lg={3}>
                <RecentlyMonthRank />
              </Grid>
              <Grid item xs={12} lg={3}>
                <RecentlyYearRank/>
              </Grid>
              <Grid item xs={12} lg={6}>
              <TravelHashtag />
              </Grid>
          </Stack>

          <Grid item xs={12} lg={6}>
              <SelectYearChart />
            </Grid> */}
          
          <Grid item xs={12} lg={4}>
            <NewsWordCloud />
          </Grid>
          <Grid item xs={12} lg={4}>
            <SearchRankCountry />
          </Grid>
          <Grid item xs={12} lg={4}>
            <DailyTourScoreRank />
          </Grid>
          {/* <Grid item xs={12} lg={4}>
            <TravelHashtag />
          </Grid> */}
        </Grid>
      </Box>
    </PageContainer>
  );
};

export default Dashboard;
