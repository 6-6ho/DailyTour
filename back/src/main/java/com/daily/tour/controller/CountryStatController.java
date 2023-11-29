package com.daily.tour.controller;


import com.daily.tour.dto.Country;
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

    @Autowired
    private final CountryService countryService;

    public CountryStatController(CountryService countryService) {
        this.countryService = countryService;
    }

    @GetMapping("/country/month") // 2023년 월별 통계 리스트 (2023년 전체)
    public ResponseEntity<List<CountryEmi>> getThisYearMonthlyStat() {
        return ResponseEntity.ok().body(countryService.getEmiThisYearMonthlyList());
    }

    @GetMapping("/country/year/{year}")  // 연도별 통계
    public ResponseEntity<List<CountryEmi>> getYearStat(@PathVariable int year) {
        return ResponseEntity.ok().body(countryService.getEmiYearList(year));
    }
    @GetMapping("/country/month/{month}")   // 월별 통계
    ResponseEntity<List<CountryEmi>> getMonthStat(@PathVariable int month) {
        return ResponseEntity.ok().body(countryService.getEmiMonthList(month));
    }

    @GetMapping("/country/month/list")
    ResponseEntity<List<String>> getMonthList() {   // 월 리스트
        return  ResponseEntity.ok().body(countryService.getMonthList());
    }
    
    @GetMapping("/country/year/list")
    ResponseEntity<List<String>> getYearList() {    // 연도 리스트
        return  ResponseEntity.ok().body(countryService.getYearList());
    }

    @GetMapping("/country/{cntCode}")
    ResponseEntity<List<Country>> getRegList(String cntCode) {    // 국가 지역 리스트
        return ResponseEntity.ok().body(countryService.getRegList(cntCode));
    }
}
