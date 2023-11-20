package com.daily.tour.controller;

import com.daily.tour.dto.CountryEmi;
import com.daily.tour.mapper.CountryStatMapper;
//import lombok.extern.slf4j.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import static org.assertj.core.api.Assertions.assertThat;
import java.util.ArrayList;
import java.util.List;

@SpringBootTest // 테스트용 애플리케이션 컨텍스트 생성
@AutoConfigureMockMvc   // MockMvc 생성 및 자동 구성
//@Slf4j
public class CountryStatControllerTest {
//    @Autowired
//    private WebApplicationContext context;
//
//    @Autowired
//    private MockMvc mockMvc;
//
//    @Autowired
//    private CountryStatMapper countryStatMapper;
//
//    @BeforeEach
//    public void mockMvcSetUp() {
//        this.mockMvc = MockMvcBuilders.webAppContextSetup(context).build();
//    }
//
//    @Test
//    public void getThisYearMonthlyList() {
//        final String url = "http://localhost:8080/country/month";
//





//        mockMvc.perform(get("country/month"))
//                .andExpect(status().isOk())
//                .andExpect((jsonPath()))
//    }


}
