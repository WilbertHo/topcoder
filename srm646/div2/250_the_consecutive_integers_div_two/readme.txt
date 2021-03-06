PROBLEM STATEMENT
John and Brus have a set of integers.
You are given its elements in a tuple (integer) numbers.
They can change the integers in numbers by performing some operations.
In each operation John will pick a number and Brus will either increase or decrease it by 1.


You are also given an integer k which is either 1 or 2.
John and Brus want to have at least k integers with consecutive values in their set.
Compute and return the smallest number of operations they have to perform.


DEFINITION
Class:TheConsecutiveIntegersDivTwo
Method:find
Parameters:tuple (integer), integer
Returns:integer
Method signature:def find(self, numbers, k):


CONSTRAINTS
-numbers will contain between 2 and 47 elements, inclusive.
-Each element of numbers will be between -10,000,000 and 10,000,000, inclusive.
-All elements of numbers will be distinct.
-k will be between 1 and 2, inclusive.


EXAMPLES

0)
{4, 47, 7}
2

Returns: 2

There are three optimal strategies:

Increase 4 two times to obtain {6,47,7}.
Decrease 7 two times to obtain {4,47,5}.
Increase 4 and decrease 7 to obtain {5,47,6}.

Note that the consecutive values can appear anywhere in the set, their position in numbers does not matter.

1)
{1, 100}
1

Returns: 0

No operation is needed.

2)
{-96, -53, 82, -24, 6, -75}
2

Returns: 20



3)
{64, -31, -56}
2

Returns: 24


