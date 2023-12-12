package com.daily.tour.mapper;

import com.daily.tour.dto.Attraction;
import com.daily.tour.dto.Country;
import com.daily.tour.dto.CountryInfo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CountryInfoMapper {

    @Select("SELECT distinct ct.CNT_NAME as cntName, cit.SEARCH_VOL as searchVol " +
            "FROM country_info_tb cit JOIN country_tb ct On cit.CNT_CODE = ct.CNT_CODE " +
            "ORDER BY cit.SEARCH_VOL DESC LIMIT 5")
    List<CountryInfo> findSearchVolRank();  // 상위 검색량 순위 5개 국가

    @Select("SELECT EX_RATE as exRate, CURRENCY " +
            "FROM country_info_tb " +
            "WHERE CNT_CODE = #{cntCode}")
    CountryInfo findPresentExRate(String cntCode); // 국가 현재 환율

    @Select("SELECT EX_AVG as exAvg, CURRENCY " +
            "FROM country_info_tb " +
            "WHERE CNT_CODE = #{cntCode}")
    CountryInfo findAverageExRate(String cntCode); // 국가 평균 환율

    @Select("SELECT distinct rat.REG_CODE as regCode, ct.REG_NAME as regName, ct.CNT_NAME as cntName " +
            "FROM reg_attr_tb rat JOIN country_tb ct ON rat.REG_CODE = ct.REG_CODE " +
            "JOIN attr_info_tb ait ON rat.ATTR_CODE = ait.ATTR_CODE " +
            "WHERE ct.CNT_CODE=#{cntCode}")
    List<Attraction> findRegListByCntCode(String cntCode);    // 지역 리스트

    @Select("SELECT distinct CNT_CODE as cntCode, CNT_NAME as cntName " +
            "FROM country_tb ")
    List<Country> findCountryList();        // 국가 리스트


}
