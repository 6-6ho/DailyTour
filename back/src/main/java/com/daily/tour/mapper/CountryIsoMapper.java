package com.daily.tour.mapper;


import com.daily.tour.dto.CountryIso;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CountryIsoMapper {

    @Select({"<script> SELECT cit.ISO_CODE as isoCode, SUM(cit.ISO_CODE) as totalEmi " +
            "FROM country_iso_tb cit join country_month_emi_tb cmt on cit.CNT_CODE = cmt.CNT_CODE " +
            "WHERE cit.CNT_CODE IN <foreach item='item' collection='cntCodeList' open='(' separator=',' close=')'>" +
            "#{item} </foreach>"  +
            "</script>"})
    List<CountryIso> findCountryIsoCode(List<String> cntCodeList);  // 국제 표준으로 변환 후 월별 출국자 수 총 합계
}
