PROBLEM STATEMENT

A teacher is trying to arrange a group of students into a line.
The teacher knows that whenever she places two students with the same age next to each other, they will talk and disturb everyone.
She wants to avoid that.



You are given a tuple (integer) x.
Each element of x is the age of one of the students.



Determine whether it is possible for the teacher to arrange the students in a line so that there are no disturbances.
If it can be done, return "possible" (quotes for clarity).
If there will always be some pair of adjacent students with the same age, return "impossible".
Note that the return value is case-sensitive.


DEFINITION
Class:PeacefulLine
Method:makeLine
Parameters:tuple (integer)
Returns:string
Method signature:def makeLine(self, x):


CONSTRAINTS
-x will have between 1 and 25 elements, inclusive.
-Each element of x will be between 1 and 25, inclusive. 


EXAMPLES

0)
{1,2,3,4}

Returns: "possible"

In this case, no two students have the same age so any order works.

1)
{1,1,1,2}

Returns: "impossible"

Regardless of which order we choose, two of the 1s will always be adjacent.

2)
{1,1,2,2,3,3,4,4}

Returns: "possible"

One example of a peaceful line is {1,2,3,4,1,2,3,4}

3)
{3,3,3,3,13,13,13,13}

Returns: "possible"



4)
{3,7,7,7,3,7,7,7,3}

Returns: "impossible"



5)
{25,12,3,25,25,12,12,12,12,3,25}

Returns: "possible"



6)
{3,3,3,3,13,13,13,13,3}

Returns: "possible"


