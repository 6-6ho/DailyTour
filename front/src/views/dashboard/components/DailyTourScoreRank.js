import { useEffect, useState } from "react";
import DashboardCard from 'src/components/shared/DashboardCard';
import { serverDomain } from "src/domain/ServerDomain";
import { TableContainer,
    Paper,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    Box} from '@mui/material';


const DailyTourScoreRank = () => {
    const [scoreList, setScoreList] = useState([]);

    useEffect(() => {
        fetch(`${serverDomain}/country/dt-score/rank`)
        .then( res => { return res.json() } ) 
        .then( data => {
            setScoreList(data);
            console.log("dt-score rank : " + data);

        });
    }, [scoreList])

    return (
        <DashboardCard title="Daily Tour 점수 순위" sx={{minHeight: '500px'}}>
        {/* <Typography variant="h1" mb={2} align="center">국가 검색량 TOP5</Typography> */}
        <Box>
            <TableContainer component={Paper}>
                <Table aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{fontSize: 17}}>국가</TableCell>
                            <TableCell align="right" sx={{fontSize: 17}}>점수</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        { scoreList && ( scoreList.map((item) => (
                            <TableRow key={item.cntCode}>
                                <TableCell sx={{fontSize: 17}}>{item.cntName}</TableCell>
                                <TableCell sx={{fontSize: 17}} align="right" >
                                    {item.dtScore}
                                </TableCell>
                            </TableRow>
                            )))
                        }
                    </TableBody>
                </Table>
            </TableContainer>
            <Typography variant="subtitle1" mt={2} textAlign="right">자체적으로 국가 별 종합 점수를 냈습니다.</Typography>
        </Box>
    </DashboardCard>
    )
}

export default  DailyTourScoreRank;