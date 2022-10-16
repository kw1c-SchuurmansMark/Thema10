import pymssql
import time
from gpiozero import LightSensor


conn = pymssql.connect(host='markschuurmansserver.database.windows.net', port=1433, database='Thema10', user='markschuurmans@markschuurmansserver', password='P@ssword')
cursor = conn.cursor()

ldr = LightSensor(18)
sensorDevice = 'LightSensor'

while True:    
    sensorValue = ldr.value
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f"INSERT INTO Oefening21 VALUES ('{sensorDevice}', '{sensorValue}', '{date}')")
    conn.commit()
    print('Waardes opgeslagen in de database!')
    
    time.sleep(30)
    
conn.close()