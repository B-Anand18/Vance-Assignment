import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import mysql.connector
from mysql.connector import Error

def scrape_yahoo_finance(quote, from_date, to_date):
    from_timestamp = int(datetime.strptime(from_date, "%Y-%m-%d").timestamp())
    to_timestamp = int(datetime.strptime(to_date, "%Y-%m-%d").timestamp())
    
    url = f"https://finance.yahoo.com/quote/{quote}/history/?period1={from_timestamp}&period2={to_timestamp}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finding the table in HTML
    table = soup.find('table', class_='yf-ewueuo')
    
    if table:
        # Extracting data from table
        data = []
        rows = table.find_all('tr')[1:]  
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 6:
                date = cols[0].text
                adj_close = cols[5].text
                data.append([date, adj_close])
        
        # Dataframe
        df = pd.DataFrame(data, columns=['Date', 'Adj Close'])
        return df
    else:
        print("Table not found. The website structure might have changed.")
        return None

def store_in_mysql(df, host, user, password, database, table, currency):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Currency VARCHAR(10),
                Date DATE,
                Adj_Close FLOAT
            )
            """
            cursor.execute(create_table_query)
            
            # Inserting data
            for _, row in df.iterrows():
                insert_query = f"""
                INSERT INTO {table} (Currency, Date, Adj_Close)
                VALUES (%s, %s, %s)
                """
                # Converting date string to MySQL date format
                date_obj = datetime.strptime(row['Date'], '%b %d, %Y')
                mysql_date = date_obj.strftime('%Y-%m-%d')
                
                values = (
                    currency,
                    mysql_date, 
                    row['Adj Close']
                )
                cursor.execute(insert_query, values)
            
            connection.commit()
            print("Data inserted successfully")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

cur1 = input('Exchange rates currency from: ')
cur2 = input('Exchange rates currency to: ')
quote = cur1 + cur2 + "=X"
currency = cur1 + cur2
from_date = input('Enter the start date (YYYY-MM-DD): ')
to_date = input('Enter the end date (YYYY-MM-DD): ')

df = scrape_yahoo_finance(quote, from_date, to_date)

if df is not None:
    print("Data scraped successfully. First few rows:")
    print(df.head())

    # MySQL connection
    host = 'localhost'
    user = 'root'
    password = 'your-password'
    database = 'vance'
    table = 'exchange_rates'

    store_in_mysql(df, host, user, password, database, table, currency)
else:
    print("Failed to retrieve data.")