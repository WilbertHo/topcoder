PROBLEM STATEMENT
The Tree Temple consists of n rooms, numbered from 0 to n-1. There are n-1 doors in the temple, each connecting a pair of rooms. It is possible to walk from any room to any other room via one or more doors. (In other words, the topology of the temple is a tree - hence the name.)

You are given the description of the temple in three tuple (integer)s: door1, door2 and lock. Each of these tuple (integer)s has n-1 elements. For each valid i, there is a door that connects the rooms door1[i] and door2[i]. The door is locked if lock[i]=1 and unlocked if lock[i]=0.

Room n-1 is the lair of Kitayuta, the evil king. There is exactly one door that leads to this room.

There can be some keys in the temple. There is no key in room n-1. Each of the other rooms either contains no key, or it contains exactly one key. (Thus, there are exactly 2^(n-1) ways how the keys can be distributed in the temple.) The number of keys may be different from the number of locked doors.

Each key can be used to open any locked door (from either side). Once you unlock a door, it remains unlocked forever. However, once a key is used to open a door it remains stuck in the keyhole. Therefore, each key can only be used once.

Knil the hero has just arrived to the temple and entered room 0 from the outside. His destination is room n-1. Inside the temple Knil will perform a sequence of actions. In each action he either collects a key from his current room, moves through an unlocked door, or uses one of the keys he has to unlock a locked door. (Note that he cannot unlock a locked door if he currently has no keys.)

However, there is a problem: Knil does not know the layout of the temple and the initial placement of keys. It might be the case that room n-1 cannot be reached at all. It might also be the case that there is a way to reach room n-1 but Knil won't reach it because he will waste some precious key on a door he doesn't need to open. But sometimes he might get lucky: the keys may be distributed in such a way that regardless of how he uses them to open the doors it will always be possible to reach room n-1. We will call such a distribution of keys lucky. In other words, a distribution of keys is called lucky if after any sequence of valid actions there is still a sequence of additional actions that will bring Knil to the room n-1.

You are given the description of the temple in the format specified above. Return the number of lucky distributions of keys.

DEFINITION
Class:LegendOfAdlez
Method:safePatterns
Parameters:tuple (integer), tuple (integer), tuple (integer)
Returns:long integer
Method signature:def safePatterns(self, door1, door2, lock):


CONSTRAINTS
-n will be between 2 and 50, inclusive.
-door1, door2 and lock will each contain n-1 elements.
-Each element of door1 and door2 will be between 0 and n-1, inclusive.
-Each element of lock will be either 0 or 1.
-The input will represent a tree.
-There exists exactly one room directly connected to room n-1 by a door.


EXAMPLES

0)
{0}
{1}
{1}

Returns: 1

Here, the temple consists of two rooms, and the door that connects them is initially locked. Room 0 either contains a key or does not contain a key. If it contains a key, Knil can always reach room 1 by unlocking the only door. Otherwise, he cannot reach the destination.

1)
{0}
{1}
{0}

Returns: 2

Again the temple consists of two rooms, but this time the door is not locked. He can always reach the room 1 regardless of whether room 0 contains a key or not.

2)
{0, 0}
{1, 2}
{1, 1}

Returns: 1

Now the temple consists of three rooms, and each door that connects room 0 and another room is initially locked. There are 2^2 = 4 patterns of the placement of keys. In two of them, room 0 does not contain a key and reaching room 2 is impossible. If room 0 contains a key and room 1 does not, he can reach room 2 only when he uses the key at room 0 to open the door that leads to room 2. If he uses the key to open the other door, he will end up in the situation where he cannot reach room 2, since room 1 does not contain a key and the spent key will be lost forever. However, if both room 0 and room 1 contain a key, it is always possible to reach the destination. Thus, the only lucky distribution of keys is the one where both room 0 and room 1 contains a key.

3)
{0, 0, 0, 1, 2, 4, 5, 7, 8}
{1, 4, 7, 2, 3, 5, 6, 8, 9}
{1, 1, 1, 0, 1, 1, 1, 1, 0}

Returns: 8



4)
{12, 11, 1, 14, 37, 14, 8, 45, 28, 34, 21, 43, 23, 45, 29, 41, 49, 12, 18, 10, 3, 37, 30, 18, 13,
 47, 40, 42, 6, 45, 45, 17, 35, 23, 27, 1, 40, 30, 44, 5, 22, 5, 48, 19, 35, 25, 19, 39, 26}
{22, 37, 47, 40, 20, 29, 22, 0, 8, 48, 46, 15, 31, 31, 7, 23, 36, 7, 8, 32, 6, 21, 32, 33, 2,
 24, 16, 36, 34, 37, 4, 48, 38, 39, 42, 36, 4, 29, 45, 20, 9, 2, 36, 32, 14, 45, 43, 48, 46}
{1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0,
 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0}

Returns: 562949953421312



5)
{12, 7, 0, 38, 30, 31, 18, 5, 23, 0, 38, 37, 45, 27, 23, 18, 17, 38, 31, 15, 26, 23, 33, 31, 9,
 2, 13, 23, 42, 36, 39, 18, 14, 6, 43, 29, 27, 34, 18, 12, 19, 10, 41, 10, 3, 13, 38, 18, 19}
{4, 40, 20, 24, 10, 32, 12, 24, 46, 46, 22, 23, 12, 23, 42, 25, 3, 40, 46, 13, 13, 9, 44, 47, 21,
 34, 35, 16, 1, 40, 43, 27, 48, 0, 19, 4, 11, 38, 19, 49, 28, 12, 37, 8, 46, 19, 18, 44, 48}
{1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1,
 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0}

Returns: 256708595124224


