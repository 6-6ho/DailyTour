import { Grid, Stack, Chip, Typography } from "@mui/material";
import DashboardCard from "src/components/shared/DashboardCard";


const TravelHashtag = () => {

    return (
        <DashboardCard title="해외여행 체크리스트">
           <Stack spacing={{ xs: 1, sm: 2 }} direction="row" useFlexGap flexWrap="wrap">
            <Chip label="#카드" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
            <Chip label="#보험" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
            <Chip label="#코로나" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
            <Chip label="#로밍" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
            <Chip label="#유심" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
            <Chip label="#비행기" color="primary" size="large" sx={{ height: '35px', fontSize: '18px', '& .MuiChip-label': { display: 'block', whiteSpace: 'normal',} ,}}> </Chip>
           </Stack>
           <Typography variant="subtitle1" textAlign="right" mt={2}>출처 : 구글 트렌드 분석</Typography>
        </DashboardCard>
    )

}

export default TravelHashtag;