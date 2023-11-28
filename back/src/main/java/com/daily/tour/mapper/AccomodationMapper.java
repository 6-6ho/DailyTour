package com.daily.tour.mapper;

import com.daily.tour.dto.Accommodation;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface AccomodationMapper {   // 숙소

    @Select("SELECT cnt_code as cntCode, cnt_name as cntName" +
            "FROM Country_tb")
    List<Accommodation> findRegListByCntCode(@Param("cntCode") String cntCode); // 지역 리스트

    @Select("SELECT ct.cnt_code as cntCode, rat.reg_code as regCode, rat.accom_code as accomCode, " +
            "rat.accom_name as accomName, ait.accom_score as  accomScore " +
            "FROM REG_ACCOM_TB rat JOIN COUNTRY_TB ct ON rat.reg_code = ct.reg_code " +
            "JOIN ACCOM_INFO_TB ait ON rat.accom_code = ait.accom_code " +
            "WHERE rat.reg_code = #{regCode} " +
            "ORDER BY ait.accom_score DESC LIMIT 5")
    List<Accommodation> findAccomListByRegCode(@Param("regCode") String regCode);   // 지역별 숙소 리스트 평점기준 상위 5개


    @Select("SELECT rat.accom_code as accomCode, rat.accom_name as accomName, ait.accom_score as accomScore, " +
            "ait.accom_score_pos as accomScorePos, ait.accom_score_neg as accomScoreNeg " +
            "FROM REG_ACCOM_TB rat JOIN ACCOM_INFO_TB ait ON rat.attr_code = ait.attr_code " +
            "WHERE rat.accom_code = #{accomCode}")
    Accommodation findAccomDetailByAccomCode(@Param("accomCode") String accomCode);   // 숙소 디테일 정보
}
