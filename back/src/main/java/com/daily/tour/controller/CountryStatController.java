package com.daily.tour.controller;


import com.daily.tour.dto.CountryEmi;
import com.daily.tour.service.CountryService;
import org.apache.coyote.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.sql.Array;
import java.util.ArrayList;
import java.util.List;

@RestController
public class CountryStatController {

//    @Autowired
    private final CountryService countryService;

    public CountryStatController(CountryService countryService) {
        this.countryService = countryService;
    }

    @GetMapping("/country/month") // 2023년 월별 통계 리스트 (2023년 전체)
    public ResponseEntity<List<CountryEmi>> getThisYearMonthlyStat() {
//        List<CountryEmi> countryList = new ArrayList<>();
//        countryList = countryService.getEmiThisYearMonthlyList();
        return ResponseEntity.ok().body(countryService.getEmiThisYearMonthlyList());
    }


    @GetMapping("/country/year/{year}")  // 연도별 통계
    public ResponseEntity<List<CountryEmi>> getYearStat(@PathVariable int year) {
//        List<CountryEmi> countryList = new ArrayList<>();
//        countryList = countryService.getEmiYearList(year);

        return ResponseEntity.ok().body(countryService.getEmiYearList(year));
    }


    @GetMapping("/country/month/{month}")   // 월별 통계
    ResponseEntity<List<CountryEmi>> getMonthStat(@PathVariable int month) {
//        List<CountryEmi> countryList = new ArrayList<>();
//        countryList = countryService.getEmiMonthList(month);
        return ResponseEntity.ok().body(countryService.getEmiMonthList(month));
    }
}
