import React from 'react';
import { Modal, Button } from 'react-bootstrap';
import ModalPieChart from './ModalPieChart';

// Modal.Title 수정하고 positiveReviews, negativeReviews 받아와야 함
// 이미지는 일단 해외여행 워드클라우드 이미지로 했음
const ModalComponent = ({ show, handleClose, positiveReviews, negativeReviews }) => {
  return (
    <Modal show={show} onHide={handleClose} size="xl">
      <Modal.Header closeButton>
        <Modal.Title>국회의사당</Modal.Title> 
      </Modal.Header>
      <Modal.Body>
        <div className="row">
          <div className="col-md-6">
            <ModalPieChart positiveReviews={positiveReviews} negativeReviews={negativeReviews} />
          </div>
          <div className="col-md-6">
            <img src='img/wordcloud.png'></img>
          </div>
        </div>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          닫기
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default ModalComponent;
