package com.daily.tour.dto;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CountryDTO {
    private String cntCode; // 국가코드
    private String cntName; // 국가명
    private String regCode; // 지역코드
    private String regName; // 지역명
}
