import pandas as pd
import sqlite3

def load_csv_to_db(csv_file, db_file):
    # Loading data from a CSV file
    data = pd.read_csv(csv_file)
    
    # Connection to a SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Loading data into a SQLite table
    data.to_sql('data_table', conn, if_exists='replace', index=False)
    
    # Closing the connection
    conn.close()

def query_db(db_file, query):
    # Connection with sqlite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Executing Query
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Closed Connection
    conn.close()
    return results

if __name__ == "__main__":
    load_csv_to_db('data.csv', 'data.db')
    
    sum_result = query_db('data.db', 'SELECT SUM(column_name) FROM data_table')
    print("Sum:", sum_result)
    
    avg_result = query_db('data.db', 'SELECT AVG(column_name) FROM data_table')
    print("Average:", avg_result)