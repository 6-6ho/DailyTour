package com.daily.tour.repository;

import com.daily.tour.entity.AccomInfoEntity;
import com.daily.tour.entity.RegAccomEntity;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import java.util.List;
import java.util.Optional;

@SpringBootTest
@Slf4j
public class AccomodationRepoTest {

//    @Autowired
    AccomodationRepository accomodationRepository;


    RegAccomRepository regAccomRepository;

    @Test
    public void classTest() {
        System.out.println(accomodationRepository.getClass().getName());
    }


    // @Test
//    public void selectTest() {  // 조회 테스트
//        String accomCode="AC001";
//
//        Optional<AccomInfoEntity> accomInfo = accomodationRepository.findById(accomCode);
//
//        if(accomInfo.isPresent()) {
//            log.info("accomInfo = {}",accomInfo.get());
//        }
//
//    }

    /*@Test
    public void regAccomTest() {
        String regCode = "REG001";
        String accomCode = "AC006";

        List<RegAccomEntity> accomList = regAccomRepository.findByRegCodeOrderByAccomInfo_AccomScoreDesc(regCode);
        if(!accomList.isEmpty()) {
            log.info("accomList = {}", accomList);
        }

        Optional<RegAccomEntity> accom = regAccomRepository.findByAccomCode(accomCode);
        if(accom.isPresent()) {
            log.info("accom = {}", accom);
        }

    }*/

}
