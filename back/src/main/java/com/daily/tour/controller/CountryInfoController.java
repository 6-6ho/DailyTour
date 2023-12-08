package com.daily.tour.controller;

import com.daily.tour.dto.Attraction;
import com.daily.tour.dto.CountryInfo;
import com.daily.tour.service.CountryInfoService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
@Slf4j
public class CountryInfoController {

    private final CountryInfoService countryInfoService;


    public CountryInfoController(CountryInfoService countryInfoService) {
        this.countryInfoService = countryInfoService;
    }

    @GetMapping("/country/reg/{cntCode}")
    public ResponseEntity<List<Attraction>> getRegList(@PathVariable String cntCode) {  // 국가별 지역리스트
        log.info("{}", countryInfoService.getRegList(cntCode));
        return ResponseEntity.ok().body(countryInfoService.getRegList(cntCode));
    }

    @GetMapping("/search-rank")
    public ResponseEntity<List<CountryInfo>> getSearchVolRank() {   // 국가 검색량 상위 Top 5 리스트
        return ResponseEntity.ok().body(countryInfoService.getSearchVolRank());
    }

    @GetMapping("/present-rate/{cntCode}")
    public ResponseEntity<CountryInfo> getPresentExRate(@PathVariable String cntCode) {   // 국가 현재 환율
        return ResponseEntity.ok().body(countryInfoService.getPresentExRate(cntCode));
    }

    @GetMapping("/avg-rate/{cntCode}")
    public ResponseEntity<CountryInfo> getAverageExRate(@PathVariable String cntCode) {  // 국가 평균 환율
        return ResponseEntity.ok().body(countryInfoService.getAverageExRate(cntCode));
    }


}
