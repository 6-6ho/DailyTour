package com.daily.tour.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
// @RequiredArgsConstructor
public class Country {
    private String cntCode; // 국가코드
    private String cntName; // 국가명
    private String regCode; // 지역코드
    private String regName; // 지역명
}
