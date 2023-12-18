package com.daily.tour.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CountryIso {
    private String cntCode; // 국가 코드
    private String isoCode; // 국제 표준 국가 코드
    private long totalEmi;   // 출국자 수 합계
}
