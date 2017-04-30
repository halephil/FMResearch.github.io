---
layout: page
title: Over & Under Populated Counties 
subtitle: Discover counties that have too many farmers markets!
---

<img src="../SQL_data/Maps/HeatMap.png" style="width:100%;" alt="Heat Map"/>

Welcome to Farmers Markets populations research, for New York State. Above you will notice a heat map of all the farmers markets
that are located all accross the state. The more red the map is the more markets are located within that area. In total, there are 761 markets and 62 counties in the state of New York. The goal of this research page it to determine the best location to relocate you farmers markets if the current city you are in is overpopulated.

**Top 10 Counties with Most and Least Number of Markets**

| County      | # of Markets |   | County   | # of Markets |
|:-----------:|:------------:|---|:--------:|:------------:|
| Monroe      | 85           |   | Seneca   | 1            |
| Kings       | 46           |   | Hamilton | 2            |
| New York    | 44           |   | Richmond | 3            |
| Albany      | 31           |   | Wyoming  | 3            |
| Erie        | 31           |   | Fulton   | 3            |
| Westchester | 27           |   | Schuyler | 3            |
| Bronx       | 26           |   | Chemung  | 4            |
| Suffolk     | 24           |   | Greene   | 4            |
| Queens      | 23           |   | Lewis    | 4            |
| Rensselaer  | 21           |   | Yates    | 4            |

Above is table that demonstrates the counties with the most amount of markets(left 2 columns) and least amount of markets(right 2 columns). To see this more clearly, below is a map with red markers labeling counties with the most amount of markets and bluew markers labeling counties with the least amount of markets. 

<img src="../SQL_data/Maps/TopTens.png" style="width:100%;" alt="Top Tens">

# Underpopulated Counties

A county is to be considered underpopulated if the ratio of persons per market is high and square miles per market is also high. The table below demonstrates the top 10 underpopulated counties ordered by highest number of people per market.

**Underpopulated Counties**

|    County   | # of Markets | Population | People per Market | Sqr Miles per Market |
|:-----------:|:------------:|:----------:|:-----------------:|----------------------|
|   Richmond  |       2      |   468,730  |      234,365      | 51                   |
|    Queens   |      23      |  2,230,722 |       96,987      | 7.7                  |
|    Nassau   |      17      |  1,339,532 |       78,796      | 26.6                 |
|   Suffolk   |      24      |  1,493,350 |       62,222      | 98.9                 |
|    Kings    |      46      |  2,504,700 |       54,450      | 2.1                  |
|    Bronx    |      26      |  1,385,108 |       53,273      | 2.2                  |
|   Onondage  |       9      |   467,026  |       51,891      | 89.5                 |
|   New York  |      44      |  1,585,873 |       36,042      | 0.8                  |
|    Seneca   |       1      |   35,251   |       35,251      | 390                  |
| Westchester |      27      |   949,113  |       35,152      | 18.5                 |

## Richmond County
Located on the top of the list is Richmond County. With nearly half a million people and only two farmers markets, it would seem to be the ideal relocation spot. Reasons are inclear to why markets are not branching to Staten Island, but your hotspot is Southern New York. Althought the sqr miles per market is not as impressive as others, the people per market makes up for that asspect.
## Suffolk County
Base off both requires Suffolk County would be second best location to relocate. It has the second best sqr miles per market and fourth best people per markets. The cost of living is this county is reasonably high, so if possible, I would highly consider locating your market in Suffolk
## Seneca County
Moving more inland, making this a highly notable location, Senca County. Although ranked 9th in people per market column, it dominates in sqr miles per market catagory. Which allows farms to relocate to spots in Seneca County that tend to not have many local markets. A little ways away from the heart of New York, however the location could use a couple more markets.

# Overpopulated Counties

A county is to be considered overpopulated if the ratio of persons per market is low and square miles per market is also low. The table below demonstrates the top 10 overpopulated counties ordered by highest number of people per market.

| County    | # of Markets | Population | People per Market | Sqr Miles per Market |
|:---------:|:------------:|:----------:|:-----------------:|:--------------------:|
| Hamilton  | 2            | 4836       | 2418              | 904                  |
| Essex     | 8            | 39370      | 4921.3            | 239.5                |
| Franklin  | 9            | 51599      | 5733.3            | 188.4                |
| Delaware  | 8            | 47980      | 5997.5            | 183.4                |
| Schuyler  | 3            | 18343      | 6114.3            | 114                  |
| Orleans   | 7            | 42883      | 6126.1            | 116.7                |
| Yates     | 4            | 25348      | 6337              | 94                   |
| Schoharie | 5            | 32749      | 6549.8            | 125.2                |
| Lewis     | 4            | 27087      | 6771.8            | 322.5                |
| Herkimer  | 9            | 64519      | 7168.8            | 162                  |

## Essex County
Though the table is ranked in order of 'People per Market', 'Sqr Miles per Market' plays a vary significant role. Thus making Essex positioned at number 1. Hamilton County, being located in a much more rural area, may not only need 2 farmers markets, and leaving the county with only 1 may not be the greatest of idea. Therfor if you are a market in Essex, there may be better opprotunity else where.

## Franklin County
Coming in a close second is Franklin County. Although the 'People per Market' is slightly larger,the 'Sqr Mile per Market' makes up for the different. This county has one more market than Essex County, with much less sqaure milage. 

## Yates County
Placed 7th on the list, Yates County, with only 4 markets is a county worth mentioning for one lucky market. With this county being very small, I only recommend one market with he least success to relocate. The 'People per Market' has only a 400 person difference from 7th to 4th nut alomst a 100 square milage difference. 
