package com.daily.tour.mapper;


import com.daily.tour.dto.CountryIso;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CountryIsoMapper {

    @Select({"<script> SELECT distinct CNT_CODE as cntCode, ISO_CODE as isoCode " +
            "FROM country_iso_tb " +
            "WHERE CNT_CODE IN <foreach item='item' collection='cntCodeList' open='(' separator=',' close=')'>" +
            "#{item}" +
            "</script>"})
    List<CountryIso> findCountryIsoCode(List<String> cntCodeList);  // 국제 표준으로 변환
}
