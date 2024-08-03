# Vance Assignment
This repository contains two distinct projects: one for web scraping using
Python and the other for a web scraping API project using Spring Boot.
Below you\'ll find a brief overview of each project, including their
setup and usage.

## Projects 1. Web Scraping using Python 
This project is designed to scrape exchange rate data from Yahoo Finance and store it in a MySQL database.
The script allows you to fetch exchange rates between two currencies
over a specified date range and stores the data in a MySQL database.

Ensure you have Python and the required libraries installed. You can
install the necessary packages using pip

Update the mysql connect variable

Execute the Python script and provide the required inputs:



## 2. Web Scraping API Project using Spring Boot 
This project provides an API to fetch exchange rate data. It uses Spring Boot to expose an
endpoint that allows you to request exchange rate data between two
currencies over a specified period.

Working/Logic -> Once the api is triggered with correct request params, given from, to, 
and period, for example give INR, USD, 10M
So first I will calculate endDate which is now and startDate which is now - 10 months
Once i get start date and end date, i will search in repo for data and return it 


Update the application.properties file with the following configuration:

properties Copy code spring.application.name=web-scrap-spring
spring.datasource.url=jdbc:mysql://localhost:3306/vance
spring.datasource.username=root spring.datasource.password=your_password
spring.jpa.hibernate.ddl-auto=update Run the Spring Boot Application:

Start the Spring Boot application. You can use your preferred method
(e.g., mvn spring-boot:run or running the application directly from your
IDE).

Test the API:

Use curl or any API client to test the API. Here\'s an example curl
command:
```
curl --location 'http://localhost:8080/api/forex-data?from=INR&to=USD&period=1Y' \
--header 'Content-Type: application/json'
```

