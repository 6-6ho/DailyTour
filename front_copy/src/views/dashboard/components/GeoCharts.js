import React from "react";
import { ResponsiveChoropleth } from "@nivo/geo";
import { scaleQuantize } from "d3-scale";
import countries from "../data/world_countries.json";
import data from "../data/test_data";
import DashboardCard from "src/components/shared/DashboardCard";


const GeoCharts = () => {
    const getColor = scaleQuantize().domain([1]).range(["#ededed", "orange"]);
    return(
        <DashboardCard>
     <div style={{ width: "100%", height: "233px" }}>
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
    </div>
    </DashboardCard>

  );

}

export default GeoCharts;