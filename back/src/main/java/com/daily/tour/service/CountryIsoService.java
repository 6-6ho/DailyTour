package com.daily.tour.service;

import com.daily.tour.dto.CountryIso;
import com.daily.tour.mapper.CountryIsoMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CountryIsoService {

    private final CountryIsoMapper countryIsoMapper;


    public CountryIsoService(CountryIsoMapper countryIsoMapper) {
        this.countryIsoMapper = countryIsoMapper;
    }

    public List<CountryIso> getCountryIsoCodeList(List<String> cntCodeList) {
        countryIsoMapper.findCountryIsoCode(cntCodeList);
    }
}
