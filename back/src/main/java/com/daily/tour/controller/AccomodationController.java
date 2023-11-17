package com.daily.tour.controller;

import com.daily.tour.dto.Accommodation;
import com.daily.tour.service.AccomodationService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class AccomodationController {   // 숙박시설 관련 컨트롤러

    private static AccomodationService accomodationService;


    public AccomodationController(AccomodationService accomodationService) {
        this.accomodationService = accomodationService;
    }
    @GetMapping("/accom/{regCode}")
    public ResponseEntity<List<Accommodation>> getAccomList(@PathVariable String regCode) { // 지역별 숙소 리스트
        return ResponseEntity.ok().body(accomodationService.getAccomListByRegCode(regCode));
    }

    @GetMapping("/accom/{accomCode}")
    public ResponseEntity<Accommodation> getAccomDetail(@PathVariable String accomCode) {   // 숙소 디테일
        return ResponseEntity.ok().body(accomodationService.getAccomDetailByAccomCode(accomCode));
    }
}

