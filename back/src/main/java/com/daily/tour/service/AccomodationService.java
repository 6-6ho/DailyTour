package com.daily.tour.service;

import com.daily.tour.dto.Accommodation;
import com.daily.tour.mapper.AccomodationMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AccomodationService {
    private final AccomodationMapper accomodationMapper;

    public AccomodationService(AccomodationMapper accomodationMapper) {
        this.accomodationMapper = accomodationMapper;
    }

    public List<Accommodation> getRegListByCntCode(String cntCode) {
        return accomodationMapper.findRegListByCntCode(cntCode);
    }

    public List<Accommodation> getAccomListByRegCode(String regCode) {  // 지역별 슥소 리스트 상위 5개
        return accomodationMapper.findAccomListByRegCode(regCode);
    }

    public Accommodation getAccomDetailByAccomCode(String accomCode) {  // 숙소 디테일 정보 
        return accomodationMapper.findAccomDetailByAccomCode(accomCode);
    }

}
