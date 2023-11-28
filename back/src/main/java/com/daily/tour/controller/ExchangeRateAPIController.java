package com.daily.tour.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ExchangeRateAPIController {        // 환율 API

    @GetMapping("/exchange")
    public void getExchangeRate() {
        String authKey = "QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e";
//        String searchDate = "";
        String dataType = "AP01";
        String url= "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey="
                + authKey + "&data=" + dataType;



    }


}
