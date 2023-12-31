package com.daily.tour.service;

import com.daily.tour.dto.Attraction;
import com.daily.tour.mapper.AttractionMapper;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class AttractionService {
    private final AttractionMapper attractionMapper;

    public AttractionService(AttractionMapper attractionMapper) {
        this.attractionMapper = attractionMapper;
    }

    public List<Attraction> getRegList(String cntCode) {    // 지역리스트
        return attractionMapper.findRegListByCntCode(cntCode);
    }

    public List<Attraction> getAttrList(String regCode) {   // 관광지 리스트 (지역 코드로 검색하여 리스트 반환
        return attractionMapper.findAttrListByRegCode(regCode);
    }
    
    public Attraction getAttrDetail(String attrCode) {  // 관광지 디테일 정보
        return attractionMapper.findAttrDetailByAttrCode(attrCode);
    }
}
