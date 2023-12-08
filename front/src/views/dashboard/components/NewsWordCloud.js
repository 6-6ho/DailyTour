import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import WordCloudImg from '../data/news_wordcloud2.png'

const NewsWordCloud = () => {
    return (
        <DashboardCard title="해외여행 주요 키워드">
            <img src={WordCloudImg} sx={{disply: "block"}}></img>
        </DashboardCard>
    )
}

export default NewsWordCloud;