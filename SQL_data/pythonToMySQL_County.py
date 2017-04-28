import csv
import mysql.connector
from mysql.connector import Error

tableName = 'ny_markets.counties'


class dbController(object):    

    databaseName = 'ny_markets'
    
    def connect(self):
        """ Connect to MySQL database """
        try:
            if self.DBconnection.is_connected():
                print('Connected to {} database'.format(self.databaseName))
                self.clearTable()
                self.loadData()

        except Error as e:
            print(e)
    ##########################################

    def printTest(self):
        query = ('SELECT county \
                    FROM counties')
        self.crs.execute(query)

        i = 1
        sep = ' '
        for line in self.crs:
            if i > 3:
                break
            i = i + 1
            string = line[0].split(sep,1)[0]
            print(string) 

    def clearTable(self):
        try:
            add_market = ("DELETE FROM {}".format(tableName))
            self.crs.execute(add_market)
            self.DBconnection.commit()
            print("Table Deleted")
        except mysql.connector.Error as err:
            print("Failed to delete table.")
            

    ##############################################
    def loadData(self):
        with open("NY_Geographics.csv", "rb") as f:
            reader = csv.reader(f)
            next(f)
            next(f)
            next(f)
            sep = ' County'
            for line in enumerate(reader):
                print(line[1][6])
                string = line[1][6].split(sep,1)[0]
                add_market = ("INSERT INTO {} VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tableName,line[1][0],line[1][1],line[1][2],line[1][3],line[1][4],line[1][5],string,line[1][7],line[1][8],line[1][9],line[1][10],line[1][11],line[1][12],line[1][13]))

                self.crs.execute(add_market)
                self.DBconnection.commit()
        
        

    ##############################################

    def createDB(self):
        dbName = raw_input('Name Database:')
        try:
            db = 'CREATE DATABASE {}'.format(dbName) 
            self.crs.execute(db)
            self.DBconnection.commit()
            self.setDB(dbName)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def setDB(self, dbStr):
        self.databaseName = dbStr
        return
        
    ##############################################
    
    DBconnection = mysql.connector.connect(host='127.0.0.1', user='root', password='password', database = databaseName)
    crs = DBconnection.cursor()

    
 
if __name__ == '__main__':
    dbClass = dbController()
    #dbClass.createDB()
    dbClass.connect()
    #dbClass.clearTable()
    #dbClass.printTest()
