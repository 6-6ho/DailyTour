package com.daily.tour.mapper;

import com.daily.tour.dto.Attraction;
import com.daily.tour.dto.CountryInfo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CountryInfoMapper {

    @Select("SELECT distinct ct.cnt_name as cntName, cit.search_vol as searchVol " +
            "FROM country_info_tb cit JOIN country_tb ct On cit.cnt_code = ct.cnt_code " +
            "ORDER BY cit.search_vol DESC LIMIT 5")
    List<CountryInfo> findSearchVolRank();  // 상위 검색량 순위 5개 국가


    @Select("SELECT  ex_rate as exRate, currency " +
            "FROM country_info_tb " +
            "WHERE cnt_code = #{cntCode}")
    CountryInfo findPresentExRate(String cntCode); // 국가 현재 환율

    @Select("SELECT ex_avg as exAvg, currency " +
            "FROM country_info_tb " +
            "WHERE cnt_code = #{cntCode}")
    CountryInfo findAverageExRate(String cntCode); // 국가 평균 환율

    @Select("SELECT distinct rat.reg_code as regCode, ct.reg_name as regName, ct.cnt_name as cntName " +
            "FROM REG_ATTR_TB rat JOIN COUNTRY_TB ct ON rat.reg_code = ct.reg_code " +
            "JOIN ATTR_INFO_TB ait ON rat.attr_code = ait.attr_code " +
            "WHERE ct.cnt_code=#{cntCode}")
    List<Attraction> findRegListByCntCode(String cntCode);    // 지역 리스트

}
