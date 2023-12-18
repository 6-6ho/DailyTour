package com.daily.tour.controller;


import com.daily.tour.dto.CountryEmi;
import com.daily.tour.service.CountryStatService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class CountryStatController {

//    @Autowired
    private final CountryStatService countryStatService;

    public CountryStatController(CountryStatService countryStatService) {
        this.countryStatService = countryStatService;
    }

    @GetMapping("/country/month") // 2023년 월별 통계 리스트 (2023년 전체)
    public ResponseEntity<List<CountryEmi>> getThisYearMonthlyStat() {
        return ResponseEntity.ok().body(countryStatService.getEmiThisYearMonthlyList());
    }

    @GetMapping("/country/year/{year}")  // 연도별 통계
    public ResponseEntity<List<CountryEmi>> getYearStat(@PathVariable int year) {
        return ResponseEntity.ok().body(countryStatService.getEmiYearList(year));
    }
    @GetMapping("/country/month/{month}")   // 월별 통계
    ResponseEntity<List<CountryEmi>> getMonthStat(@PathVariable int month) {
        return ResponseEntity.ok().body(countryStatService.getEmiMonthList(month));
    }

    @GetMapping("/country/month/list")
    ResponseEntity<List<String>> getMonthList() {   // 월 리스트
        return  ResponseEntity.ok().body(countryStatService.getMonthList());
    }
    
    @GetMapping("/country/year/list")
    ResponseEntity<List<String>> getYearList() {    // 연도 리스트
        return  ResponseEntity.ok().body(countryStatService.getYearList());
    }


}
