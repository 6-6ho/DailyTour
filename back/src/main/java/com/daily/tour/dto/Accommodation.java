package com.daily.tour.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Accommodation {    // 숙소
    private String regCode; // 지역코드
    private String accomCode;   // 숙소 코드
    private String accomName; // 숙소명
    private double accomScore;  // 숙소 평점
    private double accomRevPos;   // 긍정리뷰개수
    private double accomRevNeg;   // 부정리뷰개수
    private String imgPath; // 사진 경로
    
}
