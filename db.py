import sqlite3
con=sqlite3.connect('Sales Company.db')
def get_all_sales():
    cur=con.cursor()
    cur.execute('select ID,amount,salesDate,region from Sales order by date(salesDate)') 
    rows=cur.fetchall()
    return rows

print(get_all_sales())