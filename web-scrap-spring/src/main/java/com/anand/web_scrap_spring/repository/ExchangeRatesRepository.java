package com.anand.web_scrap_spring.repository;

import com.anand.web_scrap_spring.entity.ExchangeRate;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;

@Repository
public interface ExchangeRatesRepository extends JpaRepository<ExchangeRate, Long> {

    List<ExchangeRate> findByCurrencyAndDateBetween(String currency, LocalDate startDate, LocalDate endDate);

}
