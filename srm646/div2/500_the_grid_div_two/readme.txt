PROBLEM STATEMENT
John is standing at the origin of an infinite two-dimensional grid.
He is going to move along this grid.
During each second he can either stay where he is or he can move by one unit in one of the four cardinal directions (north, south, east, or west).
Some of the grid points are blocked.
John is not allowed to move to a blocked grid point.


You are given the coordinates of the blocked grid points as tuple (integer)s x and y.
For each valid i, the grid point that is x[i] units east and y[i] units north of the origin is blocked.
You are also given an integer k.
Compute and return the maximal possible x-coordinate of a point John can reach in k seconds.


DEFINITION
Class:TheGridDivTwo
Method:find
Parameters:tuple (integer), tuple (integer), integer
Returns:integer
Method signature:def find(self, x, y, k):


CONSTRAINTS
-x will contain between 0 and 47 elements, inclusive.
-x and y will contain the same number of elements.
-Each element of x will be between -1,000 and 1,000, inclusive.
-Each element of y will be between -1,000 and 1,000, inclusive.
-All pairs (x[i], y[i]) will be distinct.
-Each pair (x[i], y[i]) will be different from (0, 0).
-k will be between 1 and 1,000, inclusive.


EXAMPLES

0)
{1,1,1,1}
{-2,-1,0,1}
4

Returns: 2

The optimal strategy is to move two times north to (0, 2) and then two times east to (2,2).


1)
{-1, 0, 0, 1}
{0, -1, 1, 0}
9

Returns: 0

John can not make any moves.

2)
{}
{}
1000

Returns: 1000



3)
{1,0,0,-1,-1,-2,-2,-3,-3,-4,-4}
{0,-1,1,-2,2,-3,3,-4,4,-5,5}
47

Returns: 31


