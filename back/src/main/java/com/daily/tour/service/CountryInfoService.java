package com.daily.tour.service;

import com.daily.tour.dto.Attraction;
import com.daily.tour.dto.Country;
import com.daily.tour.dto.CountryInfo;
import com.daily.tour.mapper.CountryInfoMapper;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;
import java.util.Map;

@Service
public class CountryInfoService {

    private final CountryInfoMapper countryInfoMapper;

    public CountryInfoService(CountryInfoMapper countryInfoMapper) {
        this.countryInfoMapper = countryInfoMapper;
    }

    public List<Attraction> getRegList(String cntCode) {    // 지역리스트
        return countryInfoMapper.findRegListByCntCode(cntCode);
    }

    public List<CountryInfo> getSearchVolRank() {   // 검색량 상위 Top 5 국가
        return countryInfoMapper.findSearchVolRank();
    }

    public CountryInfo getPresentExRate(String cntCode) {      // 현재 환율
        return countryInfoMapper.findPresentExRate(cntCode);
    }

    public CountryInfo getAverageExRate(String cntCode) {  // 평균 환율
        return countryInfoMapper.findAverageExRate(cntCode);
    }

    public List<Country> getCountryList() {
        return countryInfoMapper.findCountryList();
    }
}
