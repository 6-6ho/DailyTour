package com.daily.tour.mapper;

import com.daily.tour.dto.Accommodation;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface AccomodationMapper {   // 숙소

    @Select("SELECT CNT_CODE as cntCode, CNT_NAME as cntName" +
            "FROM country_tb")
    List<Accommodation> findRegListByCntCode(@Param("cntCode") String cntCode); // 지역 리스트

    @Select("SELECT distinct ct.CNT_CODE as cntCode, rat.REG_CODE as regCode, rat.ACCOM_CODE as accomCode, " +
            "rat.ACCOM_NAME as accomName, ait.ACCOM_SCORE as  accomScore " +
            "FROM reg_accom_tb rat JOIN country_tb ct ON rat.REG_CODE = ct.REG_CODE " +
            "JOIN accom_info_tb ait ON rat.ACCOM_CODE = ait.ACCOM_CODE " +
            "WHERE rat.REG_CODE = #{regCode} " +
            "ORDER BY ait.ACCOM_SCORE DESC LIMIT 5")
    List<Accommodation> findAccomListByRegCode(@Param("regCode") String regCode);   // 지역별 숙소 리스트 평점기준 상위 5개


    @Select("SELECT rat.ACCOM_CODE as accomCode, rat.ACCOM_NAME as accomName, ait.ACCOM_SCORE as accomScore, " +
            "ait.ACCOM_REV_POS as accomRevPos, ait.ACCOM_REV_NEG as accomRevNeg, amt.img_path as imgPath " +
            "FROM reg_accom_tb rat JOIN accom_info_tb ait ON rat.ACCOM_CODE = ait.ACCOM_CODE " +
            "JOIN accom_img_tb amt ON amt.accom_code = rat.accom_code " +
            "WHERE rat.ACCOM_CODE = #{accomCode}")
    Accommodation findAccomDetailByAccomCode(@Param("accomCode") String accomCode);   // 숙소 디테일 정보
}
