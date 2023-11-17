package com.daily.tour.controller;


import com.daily.tour.dto.CountryEmiDTO;
import com.daily.tour.service.CountryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class CountryController {

    @Autowired
    CountryService countryService;
    @GetMapping("/country/month")
    public List<CountryEmiDTO> getMonthlyStat() {        // 올해 월별 통계 리스트
        List<CountryEmiDTO> countryList = new ArrayList<>();

        countryList = countryService.getEMIThisYearMonthlyList();
        return countryList;
    }


//    @GetMapping("/country/{year}")
//    public List<>




}
