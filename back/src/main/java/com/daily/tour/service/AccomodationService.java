package com.daily.tour.service;

import com.daily.tour.dto.Accommodation;
import com.daily.tour.mapper.AccomodationMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AccomodationService {
    private static AccomodationMapper accomodationMapper;

    public List<Accommodation> getAccomListByRegCode(String regCode) {  // 지역별 슥소 리스트 상위 5개
        return accomodationMapper.findByAccomListByRegCode(regCode);
    }

    public Accommodation getAccomDetailByAccomCode(String accomCode) {  // 숙소 디테일 정보 
        return accomodationMapper.findByAccomDetailByAccomCode(accomCode);
    }

}
