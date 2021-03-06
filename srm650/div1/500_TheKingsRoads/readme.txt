PROBLEM STATEMENT

You live in the Kingdom of Byteland.
The kingdom has a very interesting history.
It has already existed for h years.
During the first year of its existence the inhabitants built the first city.
During each of the next h-1 years the following procces occurred:
For each city built in the previous year, two additional cities were built and the older city was connected to each the two new cities by a bidirecional road.
Now, after h full years, the kingdom contains exactly (2^h)-1 cities and (2^h)-2 roads.




Recently the King did two changes to the kingdom.
First, he numbered the cities from 1 to (2^h)-1 in an arbitrary way.
Then, he added exactly three new roads to the kingdom.
(After the addition there may be multiple roads connecting the same pair of cities.
Also, some of the new roads may connect some city to itself.)




You are given the integer h and two tuple (integer)s a and b with (2^h)+1 elements each.
For each valid i, there is a road between the cities a[i] and b[i].




Return "Correct" if it is possible that the given list of roads is the current road network in the Kingdom of Byteland.
Otherwise, return "Incorrect".


DEFINITION
Class:TheKingsRoadsDiv1
Method:getAnswer
Parameters:integer, tuple (integer), tuple (integer)
Returns:string
Method signature:def getAnswer(self, h, a, b):


CONSTRAINTS
-h will be between 2 and 10, inclusive.
-a and b will contain exactly (2^h)+1 elements each.
-Each element of a and b will be between 1 and (2^h)-1, inclusive.


EXAMPLES

0)
3
{1, 3, 2, 2, 3, 7, 1, 5, 4}
{6, 5, 4, 7, 4, 3, 3, 1, 7}

Returns: "Correct"

One possibility is that city 3 was built during the first year, cities 1 and 4 during the second year, and the other four cities during the third year.
Then the King added the roads 3-5, 2-7, and 7-3.

1)
2
{1, 2, 1, 3, 3}
{2, 1, 2, 3, 3}

Returns: "Incorrect"



2)
3
{1, 3, 2, 2, 6, 6, 4, 4, 7}
{2, 1, 4, 5, 4, 4, 7, 7, 6}

Returns: "Incorrect"



3)
2
{1, 2, 2, 1, 1}
{1, 2, 2, 1, 2}

Returns: "Incorrect"



4)
5
{6, 15, 29, 28, 7, 13, 13, 23, 28, 13, 30, 27, 14, 4, 14, 19, 27, 20, 20, 19, 10, 15, 7, 7, 19, 29, 4, 24, 10, 23, 30, 6, 24}
{9, 22, 30, 20, 26, 25, 8, 7, 24, 21, 27, 31, 4, 28, 29, 6, 16, 1, 17, 10, 3, 12, 30, 18, 14, 23, 19, 21, 5, 13, 15, 2, 11}

Returns: "Correct"



5)
2
{1,1,1,2,1}
{2,3,1,2,2}

Returns: "Correct"


