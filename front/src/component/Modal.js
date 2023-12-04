import React from 'react';
import './Modal.css'; // 모달 스타일을 위한 CSS 파일

const Modal = ({ handleClose, show, children }) => {
  const showHideClassName = show ? 'modal display-block' : 'modal display-none';

  return (
    <div className={showHideClassName}>
      <div className='modal-main'>
        {children}
        <button type='button' className='close-button' onClick={handleClose}>
          ×
        </button>
      </div>
    </div>
  );
};

export default Modal;
