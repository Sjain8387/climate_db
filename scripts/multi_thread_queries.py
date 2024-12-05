import threading
import mysql.connector

def insert_data():
    conn = mysql.connector.connect(
        host='automated-mysql-server.database.windows.net',
        user='climate_db',
        password='@Parttime2023',
        database='climate_db'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('Location3', '2024-01-03', 25.0, 10.0, 70.0)")
    conn.commit()
    cursor.close()
    conn.close()

def select_data():
    conn = mysql.connector.connect(
        host='automated-mysql-server.database.windows.net',
        user='climate_db',
        password='@Parttime2023',
        database='climate_db'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

def update_data():
    conn = mysql.connector.connect(
        host='automated-mysql-server.database.windows.net',
        user='climate_db',
        password='@Parttime2023',
        database='climate_db'
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE ClimateData SET humidity = 65.0 WHERE location = 'Location1'")
    conn.commit()
    cursor.close()
    conn.close()

threads = []
for func in [insert_data, select_data, update_data]:
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
