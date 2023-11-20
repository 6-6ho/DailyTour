package com.daily.tour;


import com.daily.tour.controller.CountryStatController;
import com.daily.tour.mapper.CountryStatMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;


@WebMvcTest(controllers = CountryStatController.class)
public class CountryTest {

    @Autowired
    private MockMvc mvc;

//    @Autowired
//    private CountryStatMapper countryMapper;







}
