package com.daily.tour.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AttrController {  // 관광지 관련 컨트롤러

    @GetMapping("/attr")
    public void attrList() {

    }
}
