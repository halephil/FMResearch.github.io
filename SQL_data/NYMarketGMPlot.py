import gmplot
import mysql.connector
from mysql.connector import Error
from pythonToMySQL_Markets import dbController



class drawMap(object):
        
    def createMaps(self):
        longQuery = ('SELECT counties.Longitude, counties.Latitude \
                      FROM v_nummarkets, markets\
                     WHERE counties.county = v_nummarkets.county')

        self.dbConnector.crs.execute(longQuery)
        lonList = []
        latList = []
        count = 0
        for lon, lat in self.dbConnector.crs:
            if count < 10:
                lonList.append(float(lon.replace(u'\N{MINUS SIGN}', '-')))
                latList.append(float(lat.replace(u'\N{MINUS SIGN}', '-')))
                print("Long: {}\nLat: {}\n".format(lonList[count]),latList[count])
                count = count + 1

        #print(lonList[1])
        
        #NOTE: The lat and long are reverse on the database
        # MUST CHANGE, I think

        #Heat Map
        #self.gmap.heatmap(latList,lonList)
        #self.gmap.draw("heatMap.html")

        #Plot 1
        #self.gmap.scatter(latList, lonList,'cornflowerblue', edge_width=10)
        #self.gmap.draw("scatterMap.html")

        #Plot 2 NOT Using
        #self.gmap.scatter(latList,lonList,'l',market=False)
        #self.gmap.draw('scatter2Map.html')

    

    def draw(self):
        #self.createMaps()
        self.tenCounties()

    def tenCounties(self):
        
        ToplatList = [43.144705,40.645223,40.712578,42.644320,42.786137, 42.804823,40.935479,40.863843,40.864398, 40.7466, 42.6273]
        ToplonList = [-77.663899,-73.946029,-74.002863,-73.882116,-78.706256,-78.764635,-73.781986, -73.864282, -72.871777, -73.9384, -73.7089]

        BotlatList = [42.761142,42.8198,40.595644,42.8307, 43.3608,42.370896, 42.0581,42.3542, 44.3166,42.660860]
        BotlonList = [-76.835319,-75.5443,-74.139906,-78.0923, -76.3536, -76.874087,-76.6143, -75.7469, -73.5821,  -77.076977]
        
        self.gmap.scatter(ToplatList, ToplonList,'red', edge_width=10)
        self.gmap.scatter(BotlatList, BotlonList, 'blue', edge_width=10)
        
        self.gmap.draw('topTenMap.html')

    
        

    dbConnector = dbController()
    dbConnector.connect()
    gmap = gmplot.GoogleMapPlotter(42.70149, -74.03254, 8)

if __name__ == '__main__':
    draw = drawMap()
    draw.draw()
