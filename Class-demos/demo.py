import psycopg2
#establish connection
conn = psycopg2.connect(dbname="example")

cur= conn.cursor()

#create a table
cur.execute("""CREATE TABLE table1(
            id INTEGER PRIMARY KEY,
            completed BOOLEAN NOT NULL DEFAULT False );
            
             """)
#insert records
cur.execute("""
INSERT INTO table1(id,completed)
            VALUES(1, TRUE);
            


""")
# commit the transaction
conn.commit()
#close the cursor andconnection
cur.close()
conn.close()
