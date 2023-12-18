import { useEffect, useState } from "react";
import { useParams } from "react-router";
import DashboardCard from "src/components/shared/DashboardCard";
import { serverDomain } from "src/domain/ServerDomain";
import PaidIcon from '@mui/icons-material/Paid';
import { Typography, Box, CardContent, Stack } from "@mui/material";

const PresentExchangeRate = () => {
    const [exChange, setExChange] = useState(0);
    const params = useParams();
    const cntCode = params.cntCode;

    useEffect(() => {
        fetch(`${serverDomain}/present-rate/${cntCode}`)
        .then( res => {return res.json()} )
        .then(data => {
            setExChange(data);
            console.log("present-rate fetch :" + data);
        });
    }, exChange);

    return (
        <DashboardCard>
            <Box>
                <CardContent>
                    <Stack justifyContent="center" alignItems="center" spacing={3}>
                        <Typography variant="h3" > 현재 환율 </Typography>
                        <PaidIcon sx={{ fontSize: 40 }} > </PaidIcon>
                        <Stack direction="row" spacing={2} justifyContent="center" alignItems="center">
                            <Typography variant="h2">{ exChange.exRate} </Typography>
                            <Typography variant="h2">{exChange.currency}</Typography>
                        </Stack>
                    </Stack>
                </CardContent>
            </Box>
        </DashboardCard>
    )

}

export default PresentExchangeRate;