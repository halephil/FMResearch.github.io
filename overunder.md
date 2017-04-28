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

## Underpopulated Counties

A county is to be considered underrpopulated if the ratio of markets to county populated in high. The table below demonstrates counties that anywhere from 35,00 to 234,00 per market. Almost 5x as many people as markets that many be over populated; which will be explained below.

**Underpopulated Counties**

|    County   | # of Markets | Population | People per Market |
|:-----------:|:------------:|:----------:|:-----------------:|
|   Richmond  |       2      |   468,730  |      234,365      |
|    Queens   |      23      |  2,230,722 |       96,987      |
|    Nassau   |      17      |  1,339,532 |       78,796      |
|   Suffolk   |      24      |  1,493,350 |       62,222      |
|    Kings    |      46      |  2,504,700 |       54,450      |
|    Bronx    |      26      |  1,385,108 |       53,273      |
|   Onondage  |       9      |   467,026  |       51,891      |
|   New York  |      44      |  1,585,873 |       36,042      |
|    Seneca   |       1      |   35,251   |       35,251      |
| Westchester |      27      |   949,113  |       35,152      |
