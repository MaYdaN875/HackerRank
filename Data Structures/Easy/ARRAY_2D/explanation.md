# Arrays 2D

Note: Don't overthink

## Case:
Given a 6x6 2D array 'arr'. An hourglass is a subset of values with indices falling in the following pattern:

There are 16 hourglasses in a 6x6 array. The "hourglass sum" is the sum of the values in an hourglass. Calculate the "hourglass sum" for every hourglass in 'arr'. Then print the maximum hourglass sum.

## Example:
arr = 

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

## The 16 hourglass sum are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

the highest hourglass is 28 from the hourglass beginning at row 1 column 2

### Function parameters

int arr[6][6]: a 2D array of integers

### Returns

int: the maximum hourglass sum

### Another example: 

#### Sample input

arr = 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

#### Sample output

19
