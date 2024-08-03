package com.anand.web_scrap_spring.controller;

import com.anand.web_scrap_spring.entity.ExchangeRate;
import com.anand.web_scrap_spring.service.ExchangeRateService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ForexController {

    private final ExchangeRateService exchangeRateService;

    public ForexController(ExchangeRateService exchangeRateService) {
        this.exchangeRateService = exchangeRateService;
    }

    @GetMapping("/api/forex-data")
    public List<ExchangeRate> getForexData(@RequestParam String from, @RequestParam String to, @RequestParam String period) {

        return exchangeRateService.getExchangeRate(from, to, period);
    }
}
