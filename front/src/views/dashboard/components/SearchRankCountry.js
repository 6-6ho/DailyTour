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
                                <TableCell>국가</TableCell>
                                <TableCell align="right">검색량</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            { searchRank && ( searchRank.map((item) => (
                                <TableRow key={item.cntName}>
                                    <TableCell>{item.cntName}</TableCell>
                                    <TableCell align="right">
                                        {item.searchVol}
                                    </TableCell>
                                </TableRow>
                                )))
                            }
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        </DashboardCard>
    )

}

export default SearchRankCountry;