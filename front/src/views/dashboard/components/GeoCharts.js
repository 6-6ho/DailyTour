import React, { useState, useEffect }from "react";
import { ResponsiveChoropleth } from "@nivo/geo";
import {Box} from '@mui/material';
import { scaleQuantize } from "d3-scale";
import countries from "../data/world_countries.json";
import { useCntCodeList } from "src/context/CntCodeListContext";
import { serverDomain } from "src/domain/ServerDomain";

const GeoCharts = () => {
    const getColor = scaleQuantize().domain([1]).range(["#ededed", "orange"]);
    const {cntCodeList} = useCntCodeList();
    const [geoCodeList, setGeoCodeList] = useState([
      { "id" : null,
        "value" : null  
      }
    ]);
    

    useEffect(() => {

      if (cntCodeList.length > 0) {
      
        console.log("GeoCharts cntCodeList : " + cntCodeList);
        const queryParams = cntCodeList.map(code => `cntCodeList=${encodeURIComponent(code)}`).join('&');
        // const param = { "cntCodeList" : cntCodeList }

        console.log(queryParams);


        fetch(`${serverDomain}/country/iso?${queryParams}`)
        .then(res => {return res.json()})
        .then(data => { 
            console.log("geo code data: " + data );
            
            const geoData = data.map(item => {
              return { 
                  "id": item.isoCode, 
                  "value": item.totalEmi 
              };
            });

              setGeoCodeList(geoData);
          });

        }
      }, [cntCodeList]);

    return(
      // <DashboardCard title="2023년 국가별 월별 출국자 수 국가">
     <Box style={{ width: "100%", height: "400px" }}>
      <ResponsiveChoropleth
        data={geoCodeList && (geoCodeList)}

        features={countries.features}
        margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
        colors={getColor}
        domain={[0, 1]}
        unknownColor="#ededed"
        valueFormat=".2s"
        projectionType="equirectangular"
        projectionScale={140}
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