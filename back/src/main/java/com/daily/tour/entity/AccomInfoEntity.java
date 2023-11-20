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
public class Accommodation {    // 숙소


//    private String regCode; // 지역코드
    @Id
    private String accomCode;   // 숙소 코드
//    private String accomName; // 숙소명
    private double accomScore;  // 숙소 평점
    private double accomSentiPos;   // 긍정리뷰개수
    private double accomSentiNeg;   // 부정리뷰개수
    
}
