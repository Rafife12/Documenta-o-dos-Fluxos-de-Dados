# pip install pymssql

import pymssql

conn = pymssql.connect(
    server="rds-report.co5wnte5cgso.sa-east-1.rds.amazonaws.com",
    user=f"{user}", password=f"{password}",
    database="{database}", as_dict=True
)

cursor = conn.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables")
for row in cursor.fetchall():
    print(row["table_name"])
