import { useEffect, useState } from "react";
import { TableContainer, Paper, Typography, Table, TableBody, TableCell, TableHead, TableRow, Box } from '@mui/material';
import { serverDomain } from "src/domain/ServerDomain";

const CountryExchnageScoreRank = () => {
    const [exScoreList, setExScoreList] = useState([]);

    useEffect(() => {
        fetch(`${serverDomain}/country/ex-score/rank`)
        .then(res => res.json())
        .then(data => {
                setExScoreList(data);
                console.log("ex-score/rank fetch after data : ", data); // 객체를 직접 로깅합니다.
            })
        .catch(error => console.error('Error fetching exchange score rank:', error)); // 에러 핸들링 추가
    }, []); // 의존성 배열을 빈 배열로 변경

    return (
        <Box>
            <TableContainer component={Paper}>
                <Table aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{ fontSize: 17 }}>국가</TableCell>
                            <TableCell align="right" sx={{ fontSize: 17 }}>검색량 점수</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        { exScoreList && (exScoreList.map((item) => (
                            <TableRow key={item.cntCode}>
                                <TableCell sx={{ fontSize: 17 }}>{item.cntName}</TableCell>
                                <TableCell sx={{ fontSize: 17 }} align="right">
                                    {item.exScore}
                                </TableCell>
                            </TableRow> )))
                        }
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
}

export default CountryExchnageScoreRank;
