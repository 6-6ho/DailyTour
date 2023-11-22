import './YearlyTopList.css'; // 이 CSS 파일에서 스타일을 정의합니다.

const YearlyTopList = () => {
  const data = [
    { id: 1, name: '일본' },
    { id: 2, name: '베트남' },
    { id: 3, name: '미국' },
    { id: 4, name: '태국' },
    { id: 5, name: '싱가포르' }
  ];

  return (
    <div className="list-container">
      <div className="list-title">
        <span>연도별</span>
      </div>
      <div className="list-header">
        <span>#</span>
        <span>Name</span>
      </div>
      <ul className="list-items">
        {data.map((item) => (
          <li key={item.id} className="list-item">
            <span>{item.id}</span>
            <span>{item.name}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default YearlyTopList;
