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

    @Select("SELECT distinct cet.cnt_code as cntCode, ct.cnt_name as cntName, cet.month as month, cet.emi as emi " +
            "FROM Country_Month_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
            "JOIN (select cnt_code " +
            "FROM Country_month_emi_tb " +
            "GROUP BY cnt_code " +
            "ORDER BY sum(emi) DESC " +
            "limit 5)as top_country on cet.cnt_code = top_country.cnt_code")
    List<CountryEmi> findEmiThisYear();  // 국가별 올해 월별 출국자 수

    @Select("SELECT distinct cet.cnt_code as cntCode, ct.cnt_name as cntName, cet.year as year, cet.emi as emi " +
            "FROM Country_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
            "WHERE cet.year = #{year} ORDER BY emi DESC LIMIT 5")
    List<CountryEmi> findEmiByYear(@Param("year") int year); //  연도별 출국자 수

    @Select("SELECT distinct ct.cnt_code as cntCode, cet.emi as emi, cet.month as month, ct.cnt_name as cntName  " +
            "FROM Country_Month_Emi_tb cet join Country_tb ct on cet.cnt_code = ct.cnt_code " +
            "WHERE cet.month = #{month} " +
            "ORDER BY emi desc " +
            "LIMIT 5")
    List<CountryEmi> findEmiByMonth(@Param("month") int month); // 월별 출국자 많은 국가 5개

    @Select("SELECT DISTINCT month FROM Country_Month_Emi_tb")
    List<String> findMonth();
    @Select("SELECT DISTINCT year FROM Country_Emi_tb")
    List<String> findYear();

}
