package com.daily.tour.controller;


import com.daily.tour.dto.CountryIso;
import com.daily.tour.service.CountryIsoService;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Param;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@Slf4j
public class CountryIsoController {

    private final CountryIsoService countryIsoService;


    public CountryIsoController(CountryIsoService countryIsoService) {
        this.countryIsoService = countryIsoService;
    }

    @GetMapping("/country/iso")
    public List<CountryIso> getCountryIsoCode(@RequestParam List<String> cntCodeList) {
        log.info("getCountryIsoCode : {cntCodeList}", cntCodeList);
        return countryIsoService.getCountryIsoCodeList(cntCodeList);
    }
}
