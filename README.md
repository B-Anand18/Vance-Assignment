# Vance Assignment
This repository contains two distinct projects: one for web scraping using
Python and the other a web scraping API project using Spring Boot.
Below you\'ll find a brief overview of each project, including their
setup and usage.

## Projects 1. Web Scraping using Python 
This project is designed to scrape historical exchange rate data from Yahoo Finance and store it in local MySQL database.
The script allows you to fetch exchange rates between two currencies
over a specified date range and stores the data in a MySQL database.

It takes input from user which include currency and dates and stores the data. 


### Setup
1. Ensure you have Python and the required libraries installed. You can
   install the necessary packages using pip.

2. Update the mysql connect variable

3. Execute the Python script and provide the required inputs



## Project 2. Web Scraping API Project using Spring Boot 
This project provides an API to fetch exchange rate data. It uses Spring Boot to expose an
endpoint that allows you to request exchange rate data between two
currencies over a specified period.

### Working/Logic
Once the api is triggered with correct request params - from, to, 
and period, for example - INR, USD, 10M
So first it will calculate end date which is today - 10 months (10M)
Once i get start date(today) and end date, i will search in repo for data which come under this date 
and has same currency and return it.

### Setup
Update the application.properties file with the following configuration:

properties Copy code spring.application.name=web-scrap-spring


spring.datasource.url=jdbc:mysql://localhost:3306/vance


spring.datasource.username=root spring.datasource.password=your_password


spring.jpa.hibernate.ddl-auto=update 


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

