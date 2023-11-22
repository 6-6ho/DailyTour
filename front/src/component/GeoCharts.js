import React from "react";
import { ResponsiveChoropleth } from "@nivo/geo";
import { scaleQuantize } from "d3-scale";
import countries from "../data/world_countries.json";
import data from "../data/test_data";

function MyResponsiveChoropleth() {
  const getColor = scaleQuantize().domain([1]).range(["#ededed", "orange"]);
  return (
    <div style={{ width: "100%", height: "100%" }}>
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
  );
}

export default MyResponsiveChoropleth;



// import React from "react";
// import { ResponsiveChoroplethCanvas } from '@nivo/geo';

// export default function GeoCharts() {
//     return (
//     <ResponsiveChoroplethCanvas
//         data={[
//             {
//             "id": "KOR",
//             "value": 317040
//             },
//             {
//                 "id": "AFG",
//                 "value": 346142
//               },
//               {
//                 "id": "AGO",
//                 "value": 10752
//               },
//               {
//                 "id": "ALB",
//                 "value": 627091
//               },
//               {
//                 "id": "ARE",
//                 "value": 22997
//               },
//               {
//                 "id": "ARG",
//                 "value": 583122
//               },
//               {
//                 "id": "ARM",
//                 "value": 406602
//               },
//               {
//                 "id": "ATA",
//                 "value": 716766
//               },
//               {
//                 "id": "ATF",
//                 "value": 70931
//               },
//               {
//                 "id": "AUT",
//                 "value": 734851
//               },
//               {
//                 "id": "AZE",
//                 "value": 396537
//               },
//               {
//                 "id": "BDI",
//                 "value": 646676
//               },
//               {
//                 "id": "BEL",
//                 "value": 449978
//               },
//               {
//                 "id": "BEN",
//                 "value": 118607
//               },
//               {
//                 "id": "BFA",
//                 "value": 312132
//               },
//               {
//                 "id": "BGD",
//                 "value": 833730
//               },
//               {
//                 "id": "BGR",
//                 "value": 675657
//               },
//               {
//                 "id": "BHS",
//                 "value": 723219
//               },
//               {
//                 "id": "BIH",
//                 "value": 219019
//               },
//               {
//                 "id": "BLR",
//                 "value": 461748
//               },
//               {
//                 "id": "BLZ",
//                 "value": 926572
//               },
//               {
//                 "id": "BOL",
//                 "value": 929292
//               }
//         ]}
//         features="/* please have a look at the description for usage */"
//         margin={{ top: 0, right: 0, bottom: 0, left: 0 }}
//         colors="nivo"
//         domain={[ 0, 1000000 ]}
//         unknownColor="#666666"
//         label="properties.name"
//         valueFormat=".2s"
//         projectionTranslation={[ 0.5, 0.5 ]}
//         projectionRotation={[ 0, 0, 0 ]}
//         enableGraticule={true}
//         graticuleLineColor="#dddddd"
//         borderWidth={0.5}
//         borderColor="#152538"
//         defs={[
//             {
//                 id: 'dots',
//                 type: 'patternDots',
//                 background: 'inherit',
//                 color: '#38bcb2',
//                 size: 4,
//                 padding: 1,
//                 stagger: true
//             },
//             {
//                 id: 'lines',
//                 type: 'patternLines',
//                 background: 'inherit',
//                 color: '#eed312',
//                 rotation: -45,
//                 lineWidth: 6,
//                 spacing: 10
//             },
//             {
//                 id: 'gradient',
//                 type: 'linearGradient',
//                 colors: [
//                     {
//                         offset: 0,
//                         color: '#000'
//                     },
//                     {
//                         offset: 100,
//                         color: 'inherit'
//                     }
//                 ]
//             }
//         ]}
//         fill={[
//             {
//                 match: {
//                     id: 'CAN'
//                 },
//                 id: 'dots'
//             },
//             {
//                 match: {
//                     id: 'CHN'
//                 },
//                 id: 'lines'
//             },
//             {
//                 match: {
//                     id: 'ATA'
//                 },
//                 id: 'gradient'
//             }
//         ]}
//         legends={[
//             {
//                 anchor: 'bottom-left',
//                 direction: 'column',
//                 justify: true,
//                 translateX: 20,
//                 translateY: -100,
//                 itemsSpacing: 0,
//                 itemWidth: 94,
//                 itemHeight: 18,
//                 itemDirection: 'left-to-right',
//                 itemTextColor: '#444444',
//                 itemOpacity: 0.85,
//                 symbolSize: 18,
//                 effects: [
//                     {
//                         on: 'hover',
//                         style: {
//                             itemTextColor: '#000000',
//                             itemOpacity: 1
//                         }
//                     }
//                 ]
//             }
//         ]}
//     />
//     )
// }

