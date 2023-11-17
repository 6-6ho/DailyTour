package com.daily.tour.mapper;

import com.daily.tour.dto.CountryEmi;
import com.daily.tour.mapper.CountryStatMapper;
import lombok.extern.slf4j.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import static org.assertj.core.api.Assertions.assertThat;
import java.util.ArrayList;
import java.util.List;

@SpringBootTest // 테스트용 애플리케이션 컨텍스트 생성
@AutoConfigureMockMvc   // MockMvc 생성 및 자동 구성
@Slf4j
public class CountryMapperTest {
    @Autowired
    private CountryStatMapper countryStatMapper;

    @Test
    public void getEmiThisYearMonthlyList() {       // 2023년 월별 데이터 리스트 출력
        List<CountryEmi> list = new ArrayList<>();
        list = countryStatMapper.findEmiThisYear();
        assertThat(list).isNotNull();
        log.info("list = {}", list);
    }



}
