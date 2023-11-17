package com.daily.tour.mapper;

import com.daily.tour.dto.CountryEmi;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
@Mapper
public interface CountryStatMapper {

    @Select("SELECT cet.cnt_code as cntCode, ct.cnt_name as cntName, cet.year as year, cet.month as month, cet.emi as emi " +
            "FROM Country_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
            "WHERE cet.year=2023 ORDER BY cet.emi DESC LIMIT 5")
    List<CountryEmi> findEmiThisYear();  // 국가별 올해 월별 출국자 수

    @Select("SELECT cet.cnt_code as cntCode, ct.cnt_name as cntName, cet.year as year, cet.month as month, cet.emi as emi " +
            "FROM Country_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
            "WHERE cet.year = #{year} ORDER BY cet.year DESC LIMIT 5")
    List<CountryEmi> findEmiByYear(int year); //  연도별 출국자 수

    @Select("SELECT ct.cnt_name as cntName, cet.emi as emi" +
            "FROM Country_Emi_tb cet JOIN Country_tb ct ON cet.cnt_code = ct.cnt_code " +
            "WHERE cet.month=#{month} AND cet.year=2023 ORDER BY cet.emi DESC LIMIT 5")
    List<CountryEmi> findEmiByMonth(int month); // 월별 출국자 많은 국가 5개

}
