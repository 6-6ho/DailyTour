package com.daily.tour.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CountryInfo {
    private String cntName; // 국가 이름
    private String cntCode; // 국가 코드
    private String currency; // 통화
    private double exRate;    // 환율
    private double exAvg;  // 평균 환율
    private double searchScore;   // 검색량 점수
    private double exScore;
    private double dtScore;
}
