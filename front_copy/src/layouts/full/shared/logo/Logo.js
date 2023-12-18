import { Link } from 'react-router-dom';
// import { ReactComponent as LogoDark } from 'src/assets/images/logos/dark-logo.svg';
import TourLogoImg from 'src/assets/images/logos/tour-logo2.png'
// import Airplane from 'src/assets/images/logos/airplane_icon.png'
import { styled } from '@mui/material';

const LinkStyled = styled(Link)(() => ({
  height: '70px',
  width: '180px',
  overflow: 'hidden',
  display: 'block',
}));

const Logo = () => {
  return (
    <LinkStyled to="/">
      {/* <span>
        <img src={Airplane} />
        <span>DailyTour</span>
      </span> */}
      <img src={TourLogoImg} ></img>  
      {/* <LogoDark height={70} /> */}
    </LinkStyled>
  )
};

export default Logo;
