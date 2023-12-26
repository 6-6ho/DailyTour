import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { Typography, Box, CardContent, Stack } from "@mui/material";
import { serverDomain } from "src/domain/ServerDomain";

const CountryExchnageScore = () => {
    const [countryInfo, setCountryInfo] = useState(0);
    const params = useParams();
    const cntCode = params.cntCode;

    useEffect(()=> {
        if(cntCode) {
            fetch(`${serverDomain}/country/ex-score/${cntCode}`)
            .then(res => {return res.json()})
            .then(data => {
                setCountryInfo(data);
                    console.log("ex-score fetch after data : " + data)
                }
            )
        }
        
    }, [])

    return (
        <Box>
            <CardContent>
                <Stack spacing={3} justifyContent="center" alignItems="center">
                    <Typography variant="h3" mt={3}> 환율 점수 </Typography>
                    {/* <PaidIcon sx={{ fontSize: 40}} > </PaidIcon> */}
                    <Stack direction="row" spacing={2}>
                        <Typography variant="h2" mt={2}>{countryInfo.exScore} / 5.00 </Typography>
                    </Stack>
                </Stack>
            </CardContent>
            <Typography variant="subtitle1" mt={3} textAlign="center"> 출처 : 하나은행</Typography>
            <Typography variant="subtitle1" textAlign="center"> 기간 : 2023.01.01~2023.11.30</Typography>
        </Box>
    )

}

export default CountryExchnageScore;