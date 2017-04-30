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

A county is to be considered underpopulated if the ratio of persons per market is high and square miles per market is also high. The table below demonstrates the top 10 underpopulated counties ordered by highest number of people per market. Noteable mention, 8 out of 10 of these counties are located in the near or next to the city of New York, making these relocation spots inside of the city.

**Underpopulated Counties**

|    County   | # of Markets | Population | People per Market | Sqr Miles per Market |
|:-----------:|:------------:|:----------:|:-----------------:|----------------------|
|  [Richmond] |       2      |   468,730  |      234,365      | 51                   |
|   [Queens]  |      23      |  2,230,722 |       96,987      | 7.7                  |
|   [Nassau]  |      17      |  1,339,532 |       78,796      | 26.6                 |
|  [Suffolk]  |      24      |  1,493,350 |       62,222      | 98.9                 |
|   [Kings]   |      46      |  2,504,700 |       54,450      | 2.1                  |
|   [Bronx]   |      26      |  1,385,108 |       53,273      | 2.2                  |
|  [Onondage] |       9      |   467,026  |       51,891      | 89.5                 |
|  [New York] |      44      |  1,585,873 |       36,042      | 0.8                  |
|   [Seneca]  |       1      |   35,251   |       35,251      | 390                  |
|[Westchester]|      27      |   949,113  |       35,152      | 18.5                 |

[Richmond]: https://www.google.com/maps/place/Staten+Island,+NY/@41.283467,-74.027548,8.4z/data=!4m5!3m4!1s0x89c245ef79f4d4e7:0x50271f8534babc78!8m2!3d40.5795317!4d-74.1502007
[Queens]: https://www.google.com/maps/place/Queens,+NY/@41.3933054,-74.3881935,8.16z/data=!4m5!3m4!1s0x89c24369470a592b:0x4109d18b6c5c7b05!8m2!3d40.7282239!4d-73.7948516
[Nassau]: https://www.google.com/maps/place/Nassau+County,+NY/@41.3444867,-74.2426644,8z/data=!4m5!3m4!1s0x89c2b19dcb5e0ca1:0x1b248a99d3069e6a!8m2!3d40.6546145!4d-73.5594128
[Suffolk]: https://www.google.com/maps/place/Suffolk+County,+NY/@41.8171784,-75.9207583,7.34z/data=!4m5!3m4!1s0x89e0ae80c89bf9d7:0x95c40c490d1d5f53!8m2!3d40.9848784!4d-72.6151169
[Kings]: https://www.google.com/maps/place/Brooklyn,+NY/@41.2680459,-74.479275,8.3z/data=!4m5!3m4!1s0x89c24416947c2109:0x82765c7404007886!8m2!3d40.6781784!4d-73.9441579
[Bronx]: https://www.google.com/maps/place/Bronx+County,+NY/@41.086677,-74.4074573,9.18z/data=!4m5!3m4!1s0x89c2e08bea1f4105:0xc9a6488c48b356c2!8m2!3d40.8370495!4d-73.8654295
[Onondage]: https://www.google.com/maps/place/Onondaga+County,+NY/@42.90109,-76.8355984,7.26z/data=!4m5!3m4!1s0x89d9f4fe45a3ff35:0xb24aa2acf278b259!8m2!3d43.026819!4d-76.1783739
[New York]: https://www.google.com/maps/place/New+York+County,+NY/@41.0652269,-74.1067182,9.03z/data=!4m5!3m4!1s0x89c2ed64fc3b013b:0xd813d2023b2ead16!8m2!3d40.7830603!4d-73.9712488
[Seneca]: https://www.google.com/maps/place/Seneca+County,+NY/@42.7982513,-76.7517118,7.81z/data=!4m5!3m4!1s0x89d0bfcbf409766f:0xcd3d73bd901df123!8m2!3d42.7651891!4d-76.8720961
[Westchester]: https://www.google.com/maps/place/Westchester+County,+NY/@41.7182918,-74.1540104,7.53z/data=!4m5!3m4!1s0x89c2c96a9d6b59af:0x370ed86222bddb89!8m2!3d41.1220194!4d-73.7948516

## Richmond County
Located on the top of the list is Richmond County. With nearly half a million people and only two farmers markets, it would seem to be the ideal relocation spot. Reasons are inclear to why markets are not branching to Staten Island, but your hotspot is Southern New York. Althought the sqr miles per market is not as impressive as others, the people per market makes up for that asspect.
## Suffolk County
Base off both requires Suffolk County would be second best location to relocate. It has the second best sqr miles per market and fourth best people per markets. The cost of living is this county is reasonably high, so if possible, I would highly consider locating your market in Suffolk
## Seneca County
Moving more inland, making this a highly notable location, Senca County. Although ranked 9th in people per market column, it dominates in sqr miles per market catagory. Which allows farms to relocate to spots in Seneca County that tend to not have many local markets. A little ways away from the heart of New York, however the location could use a couple more markets.

# Overpopulated Counties

A county is to be considered overpopulated if the ratio of persons per market is low and square miles per market is also low. The table below demonstrates the top 10 overpopulated counties ordered by highest number of people per market. Noteable mention, the majority of these counties are located in rural areas, which would most likely mean that these markets would relocat into a city.

| County    | # of Markets | Population | People per Market | Sqr Miles per Market |
|:---------:|:------------:|:----------:|:-----------------:|:--------------------:|
|[Hamilton] | 2            | 4836       | 2418              | 904                  |
| [Essex]   | 8            | 39370      | 4921.3            | 239.5                |
|[Franklin] | 9            | 51599      | 5733.3            | 188.4                |
|[Delaware] | 8            | 47980      | 5997.5            | 183.4                |
|[Schuyler] | 3            | 18343      | 6114.3            | 114                  |
|[Orleans]  | 7            | 42883      | 6126.1            | 116.7                |
|[Yates]    | 4            | 25348      | 6337              | 94                   |
|[Schoharie]| 5            | 32749      | 6549.8            | 125.2                |
|[Lewis]    | 4            | 27087      | 6771.8            | 322.5                |
|[Herkimer] | 9            | 64519      | 7168.8            | 162                  |

[Hamilton]: https://www.google.com/maps/place/Hamilton+County,+NY/@43.0152304,-75.6520657,7.3z/data=!4m5!3m4!1s0x89df17cb6a970eab:0x2d236705dcc7c72f!8m2!3d43.4764406!4d-74.4056612
[Essex]: https://www.google.com/maps/place/Essex+County,+NY/@43.2160659,-75.541765,7.54z/data=!4m5!3m4!1s0x4ccb1bc35229d23d:0xc18b42628062b901!8m2!3d44.0107408!4d-73.9507728
[Franklin]: https://www.google.com/maps/place/Franklin+County,+NY/@43.2170037,-75.6189279,7.3z/data=!4m5!3m4!1s0x4ccb9fcb580c5add:0xe9db12a83af25dc!8m2!3d44.5926135!4d-74.3387798
[Delaware]: https://www.google.com/maps/place/Delaware+County,+NY/@42.6883681,-75.8229518,7.81z/data=!4m5!3m4!1s0x89d091e7bf3fa51d:0x34ca4327527d2f24!8m2!3d42.2452081!4d-74.8741045
[Schuyler]: https://www.google.com/maps/place/Schuyler+County,+NY/@43.0451611,-76.1927426,7.7z/data=!4m5!3m4!1s0x89d0f48aae81dd3d:0x725a69d482a9961a!8m2!3d42.3796425!4d-76.8720961
[Orleans]: https://www.google.com/maps/place/Orleans+County,+NY/@43.055253,-75.5561791,7.38z/data=!4m5!3m4!1s0x89d41105a0f5cb23:0xc14fea72db78047a!8m2!3d43.4088624!4d-78.2020387
[Yates]: https://www.google.com/maps/place/Yates+County,+NY/@42.7865978,-76.3035679,7.58z/data=!4m5!3m4!1s0x89d0e330cc172577:0x454614735e61d96d!8m2!3d42.6430846!4d-77.1485163
[Schoharie]: https://www.google.com/maps/place/Schoharie+County,+NY/@42.2766827,-75.8642091,7.49z/data=!4m5!3m4!1s0x89dc25aa468f12fd:0xeef5bee83b61bcab!8m2!3d42.6550335!4d-74.4994517
[Lewis]: https://www.google.com/maps/place/Lewis+County,+NY/@42.7211827,-76.18459,7.29z/data=!4m5!3m4!1s0x89d89653cc41534f:0x9741799e3c907a52!8m2!3d43.840112!4d-75.4344727
[Herkimer]: https://www.google.com/maps/place/Herkimer+County,+NY/@42.91111,-75.4780511,7.04z/data=!4m5!3m4!1s0x89dec0fb88b3e3c9:0x36203db10f9ca406!8m2!3d43.1630587!4d-74.8741045


## Essex County
Though the table is ranked in order of 'People per Market', 'Sqr Miles per Market' plays a vary significant role. Thus making Essex positioned at number 1. Hamilton County, being located in a much more rural area, may not only need 2 farmers markets, and leaving the county with only 1 may not be the greatest of idea. Therfor if you are a market in Essex, there may be better opprotunity else where.

## Franklin County
Coming in a close second is Franklin County. Although the 'People per Market' is slightly larger,the 'Sqr Mile per Market' makes up for the different. This county has one more market than Essex County, with much less sqaure milage. 

## Yates County
Placed 7th on the list, Yates County, with only 4 markets is a county worth mentioning for one lucky market. With this county being very small, I only recommend one market with he least success to relocate. The 'People per Market' has only a 400 person difference from 7th to 4th nut alomst a 100 square milage difference. 

# Conclusion

The goal here is not to even out the ratio throughout the state of New York. Instead, we seek to help markets that may not be doing as well as others. Therefor with the top 10 tables shown above, if marked as 'underpopulated' you may be seeing new markets coming to your area. If marked as 'overpopulated' maybe seek other counties who could use a little more variety.
