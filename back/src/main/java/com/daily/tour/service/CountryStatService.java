package com.daily.tour.service;

import com.daily.tour.dto.CountryEmi;
import com.daily.tour.mapper.CountryStatMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CountryStatService {

    private final CountryStatMapper countryStatMapper;

    public CountryStatService(CountryStatMapper countryStatMapper) {
        this.countryStatMapper = countryStatMapper;
    }

    public List<CountryEmi> getEmiThisYearMonthlyList() {   //  2023년 월별 국가 출국자 상위 5개 리스트
        return countryStatMapper.findEmiThisYear();
    }

    public List<CountryEmi> getEmiYearList(int year) {      // 연도별 국가 출국자 상위 5개 리스트
        return countryStatMapper.findEmiByYear(year);
    }

    public List<CountryEmi> getEmiMonthList(int month) {    // 월별 출국자 상위 5개 리스트
        return countryStatMapper.findEmiByMonth(month);
    }

    public List<String> getMonthList() { return countryStatMapper.findMonth(); }

    public List<String> getYearList() {return countryStatMapper.findYear(); }
}
