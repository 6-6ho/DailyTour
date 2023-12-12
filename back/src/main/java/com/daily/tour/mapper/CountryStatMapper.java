package com.daily.tour.mapper;

import com.daily.tour.dto.CountryEmi;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
@Mapper
public interface CountryStatMapper {

//    @Select("SELECT cet.cnt_code as cntCode, ct.cnt_name as cntName, cet.year as year, cet.month as month, cet.emi as emi " +
//            "FROM Country_Month_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
//            "WHERE cet.year=2023")

    @Select("SELECT distinct cet.CNT_CODE as cntCode, ct.CNT_NAME as cntName, cet.MONTH as month, cet.EMI as emi " +
            "FROM country_month_emi_tb cet JOIN country_tb ct ON cet.CNT_CODE = ct.CNT_CODE " +
            "JOIN (select CNT_CODE " +
            "FROM country_month_emi_tb " +
            "GROUP BY CNT_CODE " +
            "ORDER BY sum(EMI) DESC " +
            "limit 5)as top_country on cet.CNT_CODE = top_country.CNT_CODE")
    List<CountryEmi> findEmiThisYear();  // 국가별 올해 월별 출국자 수

    @Select("SELECT distinct cet.CNT_CODE as cntCode, ct.CNT_NAME as cntName, cet.YEAR as year, cet.EMI as emi " +
            "FROM country_emi_tb cet JOIN country_tb ct ON cet.CNT_CODE = ct.CNT_CODE " +
            "WHERE cet.YEAR = #{year} " +
            "ORDER BY EMI DESC LIMIT 5")
    List<CountryEmi> findEmiByYear(@Param("year") int year); //  연도별 출국자 수

    @Select("SELECT distinct ct.CNT_CODE as cntCode, cet.EMI as emi, cet.MONTH as month, ct.CNT_NAME as cntName  " +
            "FROM country_month_emi_tb cet join country_tb ct on cet.CNT_CODE = ct.CNT_CODE " +
            "WHERE cet.MONTH = #{month} " +
            "ORDER BY EMI desc LIMIT 5")
    List<CountryEmi> findEmiByMonth(@Param("month") int month); // 월별 출국자 많은 국가 5개

    @Select("SELECT DISTINCT MONTH FROM country_month_emi_tb")
    List<String> findMonth();
    @Select("SELECT DISTINCT YEAR FROM country_emi_tb")
    List<String> findYear();

}
