import { useEffect } from "react";
import { serverDomain } from "src/domain/ServerDomain";


const DailyTourScoreRank = () => {
    const [scoreList, setScoreList] = useEffect([]);

    useEffect(() => {
        fetch(`${serverDomain}/country/dt-score/rank`)
    })


}

export default  DailyTourScoreRank;