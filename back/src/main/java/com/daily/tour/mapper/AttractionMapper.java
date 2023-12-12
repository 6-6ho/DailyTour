package com.daily.tour.mapper;

import com.daily.tour.dto.Attraction;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface AttractionMapper {

//    @Select("SELECT " +
//            "FROM Reg_Attr_tb rat JOIN Country_tb ct ON rat.reg_code = ct.reg_code " +
//            "JOIN Attr_Info_tb ait ON rat.attr_code = ait.attr_code" +
//            "WHERE rat.reg_code = {regCode}")
    @Select("SELECT distinct ct.CNT_CODE as cntCode, rat.REG_CODE as regCode, rat.ATTR_CODE as attrCode, " +
            "rat.ATTR_NAME as attrName, ait.ATTR_SCORE as attrScore " +
            "FROM reg_attr_tb rat JOIN country_tb ct ON rat.REG_CODE = ct.REG_CODE " +
            "JOIN attr_info_tb ait ON rat.ATTR_CODE = ait.ATTR_CODE " +
            "WHERE rat.REG_CODE = #{regCode} " +
            "ORDER BY ait.ATTR_SCORE DESC LIMIT 5")
    List<Attraction> findAttrListByRegCode(@Param("regCode") String regCode); // 관광지 상위 5개 리스트

    @Select("SELECT rat.ATTR_CODE as attrCode, rat.ATTR_NAME as attrName, ait.ATTR_SCORE as attrScore, " +
            "ait.ATTR_REV_POS as attrRevPos, ait.ATTR_REV_NEG as attrRevNeg " +
            "FROM reg_attr_tb rat JOIN attr_info_tb ait ON rat.ATTR_CODE = ait.ATTR_CODE " +
            "WHERE rat.ATTR_CODE = #{attrCode}")
    Attraction findAttrDetailByAttrCode(@Param("attrCode") String attrCode); // 관광지 디테일 정보*/


}
