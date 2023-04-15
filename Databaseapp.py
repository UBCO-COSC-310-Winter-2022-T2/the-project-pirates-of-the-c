import mysql.connector as mysql
def main():
    db = mysql.connect(
    #host is always maybe changing due to non-static ip addressing
        user = 'root',
        password = 'examplepass', 
        database='mydatabase', 
        host = '172.29.0.2', 
        port = 8080
    )

    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS SensorLog(sensorID INT PRIMARY KEY, maxTEMP DOUBLE, minTEMP DOUBLE, avgTEMP DOUBLE, tempVARIANCE DOUBLE)")

    cursor.execute("INSERT INTO SensorLog VALUES (1, 25.0, 12.0, 17.0, 2.3)")
    cursor.execute("INSERT INTO SensorLog VALUES (2, 23.0, 15.0, 19.0, 1.1)")
    cursor.execute("INSERT INTO SensorLog VALUES (3, 21.2, 17.0, 19.5, 0.7)")

    cursor.execute("SELECT * FROM test")
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
    
# CREATE TABLE IF NOT EXISTS SensorLog(sensorID INT PRIMARY KEY, maxTEMP DOUBLE, minTEMP DOUBLE, avgTEMP DOUBLE, tempVARIANCE DOUBLE);
# INSERT INTO SensorLog VALUES (1, 25.0, 12.0, 17.0, 2.3);
# INSERT INTO SensorLog VALUES (2, 23.0, 15.0, 19.0, 1.1);
# INSERT INTO SensorLog VALUES (3, 21.2, 17.0, 19.5, 0.7);