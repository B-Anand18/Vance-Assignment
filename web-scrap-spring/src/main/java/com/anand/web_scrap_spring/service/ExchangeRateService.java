package com.anand.web_scrap_spring.service;

import com.anand.web_scrap_spring.entity.ExchangeRate;
import com.anand.web_scrap_spring.repository.ExchangeRatesRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class ExchangeRateService {

    private final ExchangeRatesRepository exchangeRatesRepository;

    public ExchangeRateService(ExchangeRatesRepository exchangeRatesRepository) {
        this.exchangeRatesRepository = exchangeRatesRepository;
    }

    public List<ExchangeRate> getExchangeRate(String from, String to, String period) {
        String currency = from + to;

        LocalDate startDate = findDate(period);
        LocalDate endDate = LocalDate.now();

        return exchangeRatesRepository.findByCurrencyAndDateBetween(currency, startDate, endDate);
    }

    private LocalDate findDate(String period) {

        int n = period.length();
        char unit = period.charAt(n - 1);
        int value = Integer.parseInt(period.substring(0,n-1));

        LocalDate now = LocalDate.now();

        switch (unit) {
            case 'Y' :
                return now.minusYears(value);
            case 'M' :
                return now.minusMonths(value);
            case 'D' :
                return now.minusDays(value);
            case 'W' :
                return now.minusWeeks(value);
            default :
                throw new IllegalArgumentException("Invalid period unit: " + unit);
        }
    }
}