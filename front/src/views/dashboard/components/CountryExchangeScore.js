import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { Typography, Box, CardContent, Stack } from "@mui/material";


const CountryExchnageScore = () => {
    const [exScore, setExScore] = useState();
    const params = useParams();
    const cntCode = params.cntCode;

    useEffect(()=> {
        fetch(`${serverDomain}/country/ex-score`)
        .then(res => {return res.json()})
        .then(data => {
                setExScore(data);
                console.log("ex-score fetch after data : " + data)
            }
        )
    }, [exScore])

    return (
        <Box>
            <CardContent>
                <Stack spacing={3} justifyContent="center" alignItems="center">
                    <Typography variant="h3" > 환율 점수 </Typography>
                    <PaidIcon sx={{ fontSize: 40}} > </PaidIcon>
                    <Stack direction="row" spacing={2}>
                        <Typography variant="h2">{ exChange.exAvg} </Typography>
                        <Typography variant="h2">{exChange.currency}</Typography>
                    </Stack>
                </Stack>
            </CardContent>
            <Typography variant="subtitle1" mt={2} textAlign="right"> 출처 : 하나은행</Typography>
            <Typography variant="subtitle1" textAlign="right"> 기간 : 2023.01.01~2023.11.30</Typography>
        </Box>
    )

}

export default CountryExchnageScore;