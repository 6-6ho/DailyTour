package com.daily.tour.controller;


import com.daily.tour.dto.CountryIso;
import com.daily.tour.service.CountryIsoService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class CountryIsoController {

    private final CountryIsoService countryIsoService;


    public CountryIsoController(CountryIsoService countryIsoService) {
        this.countryIsoService = countryIsoService;
    }

    @GetMapping("/country/iso")
    public List<CountryIso> getCountryIsoCode(List<String> cntCodeList) {
        return countryIsoService.getCountryIsoCodeList(cntCodeList);
    }
}
