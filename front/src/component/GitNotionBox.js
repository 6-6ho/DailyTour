import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './GitNotionBox.css';

const GitNotionBox = () => {
  const notionUrl = 'https://www.notion.so/696dd8073e32490da7353ddf0f75e816';
  const githubUrl = 'https://github.com/6-6ho/DailyTour';

  return (
    <div className='git-notion-box'>
      <div className="d-flex flex-column align-items-start my-1">
        <a href={notionUrl} target="_blank" rel="noopener noreferrer" className="icon mb-2">
          <img src='img/notion_icon.png' className="notionIcon" alt="Notion Icon" />
        </a>
        <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="icon mt-2">
          <img src='img/github_icon.png' className="githubIcon" alt="GitHub Icon" />
        </a>
        <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/03/28/78/56/turbojet.jpg?w=500&h=-1&s=1" width="300" height="200"></img>
      </div>
    </div>
  );
};

export default GitNotionBox;
