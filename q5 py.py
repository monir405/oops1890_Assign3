import sqlite3
con=sqlite3.connect('Sales Company.db')
class DailySales:
     def __init__(self,ID,Amount,SalesDate,Region):
          self.ID=ID
          self.Amount=Amount
          self.SalesDate=SalesDate
          self.Region=Region

     def fromDb(self,Date,Region):
        cur=con.cursor()
        cur.execute('select ID,amount,salesDate,region from Sales where region=? and salesDate=? order by date(salesDate)',(Region,Date)) 
        rows=cur.fetchall()
        Sales=[]  
        for Row in rows:          
            Sales.append(DailySales(Row[0],Row[1],Row[2],Row[3])    )
        return Sales
     
class Regions:
    def __init__(self):
        self.regions=[]
    
    def add(self,region):
        self.regions.append(region)
        

print(DailySales('','','','').fromDb('2020-12-12','e')[0])

