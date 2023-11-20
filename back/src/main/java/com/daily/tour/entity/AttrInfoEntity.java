package com.daily.tour.entity;

import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
public class Attraction {   // 관광지
    private String regCode; // 지역코드
    private String attrCode;    // 관광지 코드
    private String attrName;    // 관광지명
    private double attrScore;   // 관광지 평점
    private int attrScorePos;   // 관광지 긍정 리뷰 개수
    private int attrScoreNeg;   // 관광지 부정 리뷰 개수
}
