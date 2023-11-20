package com.daily.tour.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CountryInfo {
    private String cntCode; // 국가 코드
    private long search_vol;   // 검색량
    private double exRateBuy;    // 환율살 때
    private double exRateSell;  // 환율팔 때
}