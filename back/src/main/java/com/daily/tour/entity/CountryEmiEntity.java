package com.daily.tour.entity;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
//@RequiredArgsConstructor
public class CountryEmi {
    @Id
    private String cntCode; // 국가코드
    private String cntName; // 국가명
    private long year; // 연도
    private long month;    // 월
    private long emi; // 출국자 수
}
