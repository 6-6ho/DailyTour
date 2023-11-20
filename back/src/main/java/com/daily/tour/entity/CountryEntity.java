package com.daily.tour.entity;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Entity
@Table(name="COUNTRY_TB")
@NoArgsConstructor
@AllArgsConstructor
// @RequiredArgsConstructor
public class Country {
    @Id
    @Column(name="cnt_code")
    private String cntCode; // 국가코드
    @Id
    @Column(name="reg_code")
    private String regCode; // 지역코드
    @Column(name="cnt_name")
    private String cntName; // 국가명
    @Column(name="reg_name")
    private String regName; // 지역명
}
