import React from 'react';
import notionIcon from '../';
import githubIcon from './path/to/githubIcon.png';

const DocumentComponent = () => {
  const notionUrl = '여기에 노션 주소를 입력하세요'; // 실제 노션 주소를 입력해주세요
  const githubUrl = 'https://github.com/6-6ho/DailyTour'; // 깃헙 주소

  return (
    <div>
      <a href={notionUrl} target="_blank" rel="noopener noreferrer">
        <img src={notionIcon} alt="노션 아이콘" />
        노션 주소
      </a>
      <a href={githubUrl} target="_blank" rel="noopener noreferrer">
        <img src={githubIcon} alt="깃헙 아이콘" />
        깃헙 주소
      </a>
    </div>
  );
};

export default DocumentComponent;
