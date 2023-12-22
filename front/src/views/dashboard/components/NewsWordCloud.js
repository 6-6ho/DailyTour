import { useTheme } from '@mui/material/styles';
import { Typography, Card, CardMedia } from '@mui/material';
import DashboardCard from '../../../components/shared/DashboardCard';
import WordCloudImg from  '../../../assets/images/word-cloud/news-wordcloud.png'
// import WordCloudPath from '../../../assets/images/word-cloud/news-wordcloud.png'

const NewsWordCloud = () => {
    return (
        <DashboardCard title="해외여행 주요 키워드" >
            <Card>
                <CardMedia component="img" height={280} src={WordCloudImg} sx={{objectFit : 'contain'}}></CardMedia>
            </Card>
            <Typography variant="subtitle1" mt={2} textAlign="right">출처 : (주)여행신문</Typography>
            <Typography variant="subtitle1" textAlign="right">기간 : 2023.07.27~2023.11.14</Typography>
        </DashboardCard>
    )
}

export default NewsWordCloud;