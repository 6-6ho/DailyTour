import React, { useState, useEffect }from "react";
import { ResponsiveChoropleth } from "@nivo/geo";
import {Box} from '@mui/material';
import { scaleQuantize } from "d3-scale";
import countries from "../data/world_countries.json";
import data from "../data/test_data";
import DashboardCard from "src/components/shared/DashboardCard";
import { useCntCodeList } from "src/context/CntCodeListContext";
import { serverDomain } from "src/domain/ServerDomain";

const GeoCharts = () => {
    const getColor = scaleQuantize().domain([1]).range(["#ededed", "orange"]);
    const {cntCodeList} = useCntCodeList();
    const [geoCodeList, setGeoCodeList] = useState([]);
    useEffect(() => {

      if (!cntCodeList.length) return;
      
      // const queryParams = cntCodeList.map(code => `cntCodeList=${code}`).join('&'); // cntCodeList를 쿼리 파라미터로 변환
      // console.log(queryParams); 
      fetch(`${serverDomain}/country/iso?cntCodeList=${cntCodeList}`)
      .then(res => {return res.json()})
      .then(data => { 
          console.log("geo code data: " + data );
          setGeoCodeList(data);
        })
      }, [cntCodeList]);

    return(
      // <DashboardCard title="2023년 국가별 월별 출국자 수 국가">
     <Box style={{ width: "100%", height: "300px" }}>
      <ResponsiveChoropleth
        data={data}

        features={countries.features}
        margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
        colors={getColor}
        domain={[0, 1]}
        unknownColor="#ededed"
        valueFormat=".2s"
        projectionScale={50}
        projectionTranslation={[0.5, 0.5]}
        projectionRotation={[0, 0, 0]}
        enableGraticule={true}
        graticuleLineColor="#ffffff"
        borderWidth={0.5}
        borderColor={{ theme: "background" }}
        tooltip={(data, color) => (
          <div
            style={{
              maintainAspectRatio: true,
              responsive: false,
              padding: 12,
              color,
              height: "100%",
              background: "#ffffff"
            }}
          >
            <span>Look, I'm custom :</span>
            <br />
            <strong>
              <span>{data.feature.properties.name}</span>
            </strong>
            <br />
            <strong>
              {data.feature.id}: {data.feature.value}
            </strong>
          </div>
        )}
      />
    </Box>
    // </DashboardCard>

  );

}

export default GeoCharts;