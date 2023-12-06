import React from 'react';
import { Pie } from 'react-chartjs-2';

const ModalPieChart = ({ positiveReviews, negativeReviews }) => {
  const data = {
    labels: ['긍정 리뷰', '부정 리뷰'],
    datasets: [
      {
        data: [positiveReviews, negativeReviews],
        backgroundColor: ['#36A2EB', '#FF6384'],
        hoverBackgroundColor: ['#36A2EB', '#FF6384']
      }
    ]
  };

  return <Pie data={data} />;
};

export default ModalPieChart;