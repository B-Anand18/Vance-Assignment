Vance Assignment Welcome to the Vance Assignment repository! This
repository contains two distinct projects: one for web scraping using
Python and the other for a web scraping API project using Spring Boot.
Below you\'ll find a brief overview of each project, including their
setup and usage.

Projects 1. Web Scraping using Python This project is designed to scrape
exchange rate data from Yahoo Finance and store it in a MySQL database.
The script allows you to fetch exchange rates between two currencies
over a specified date range and stores the data in a MySQL database.

Features Scrapes exchange rate data from Yahoo Finance. Stores data in a
MySQL database. Customizable date range for data fetching. Setup and
Usage Install Required Packages:

Ensure you have Python and the required libraries installed. You can
install the necessary packages using pip:

bash Copy code pip install requests beautifulsoup4
mysql-connector-python Configure Database Connection:

Update the following variables in your script with the correct details:

python Copy code host = \'localhost\' user = \'root\' password =
\'your-password\' database = \'vance\' table = \'exchange_rates\' Run
the Script:

Execute the Python script and provide the required inputs:

python Copy code cur1 = input(\'Exchange rates currency from: \') cur2 =
input(\'Exchange rates currency to: \') quote = cur1 + cur2 + \"=X\"
currency = cur1 + cur2 from_date = input(\'Enter the start date
(YYYY-MM-DD): \') to_date = input(\'Enter the end date (YYYY-MM-DD): \')
The script will fetch the data and store it in the MySQL database.

2\. Web Scraping API Project using Spring Boot This project provides an
API to fetch exchange rate data. It uses Spring Boot to expose an
endpoint that allows you to request exchange rate data between two
currencies over a specified period.

Features Provides a RESTful API to fetch exchange rate data. Allows
querying data between two currencies over various periods. Setup and
Usage Configure Spring Boot Application:

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

bash Copy code curl \--location
\'http://localhost:8080/api/forex-data?from=INR&to=USD&period=1Y\' \\
\--header \'Content-Type: application/json\'
