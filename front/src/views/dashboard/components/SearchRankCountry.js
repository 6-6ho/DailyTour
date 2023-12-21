import React, {useState, useEffect} from 'react';
import DashboardCard from 'src/components/shared/DashboardCard';
import { serverDomain } from 'src/domain/ServerDomain';
import { TableContainer,
    Paper,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    Box} from '@mui/material';


const SearchRankCountry = () => {
    const [searchRank, setSearchRank] = useState([]);

    useEffect(() => {
        fetch(`${serverDomain}/search-rank`)
        .then(res => {return res.json()})
        .then(data => {
                setSearchRank(data);
                console.log("search-rank fetch after data : " + data)
            }
        )
    }, []);

    return (
        <DashboardCard title="국가 검색량 TOP5">
            {/* <Typography variant="h1" mb={2} align="center">국가 검색량 TOP5</Typography> */}
            <Box>
                <TableContainer component={Paper}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell sx={{fontSize: 17}}>국가</TableCell>
                                <TableCell align="right" sx={{fontSize: 17}}>검색량</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            { searchRank && ( searchRank.map((item) => (
                                <TableRow key={item.cntName}>
                                    <TableCell sx={{fontSize: 17}}>{item.cntName}</TableCell>
                                    <TableCell sx={{fontSize: 17}} align="right" >
                                        {item.searchVol}
                                    </TableCell>
                                </TableRow>
                                )))
                            }
                        </TableBody>
                    </Table>
                </TableContainer>
                <Typography variant="subtitle1" mt={2} textAlign="right">출처 : 문화 빅데이터 플랫폼(한국문화정보원)</Typography>
            </Box>
        </DashboardCard>
    )

}

export default SearchRankCountry;