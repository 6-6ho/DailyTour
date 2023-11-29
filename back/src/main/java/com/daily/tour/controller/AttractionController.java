package com.daily.tour.controller;

import com.daily.tour.dto.Attraction;
import com.daily.tour.service.AttractionService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController

@Slf4j
public class AttractionController {  // 관광지 관련 컨트롤러

    private final AttractionService attractionService;

    public AttractionController(AttractionService attractionService) {
        this.attractionService = attractionService;
    }

    @GetMapping("/attr/{cntCode}")
    public ResponseEntity<List<Attraction>> getRegList(@PathVariable String cntCode) {
        log.info("{}", attractionService.getRegList(cntCode));
        return ResponseEntity.ok().body(attractionService.getRegList(cntCode));
    }

    @GetMapping("/attr/reg/{regCode}")
    public ResponseEntity<List<Attraction>> getAttrList(@PathVariable String regCode) {    // 관광지 상위 5개 리스트
       return ResponseEntity.ok().body(attractionService.getAttrList(regCode));
    }

    @GetMapping("/attr/detail/{attrCode}")
    public ResponseEntity<Attraction> getAttrDetail(@PathVariable String attrCode) {   // 관광지 디테일 정보
        return ResponseEntity.ok().body(attractionService.getAttrDetail(attrCode));
    }


}
