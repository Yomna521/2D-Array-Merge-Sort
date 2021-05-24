# 2D-Array-Merge-Sort

Implementation of merge sort for a two-dimensional array. In case of odd dimension, the first division contains more number of elements than the second one. The complete execution of merge sort arranges the elements in increasing order either moving row-wise or column-wise.<br>
For example, let there be a 4×44×4 two dimensional array. The complete process to be implemented is illustrated in Fig. 1. Similarly, Fig. 2 demonstrates the scenario for a 3×33×3 two dimensional array. One has to keep on dividing till a single element is remaining. During merging, first the row elements get sorted in increasing order followed by sorting of elements lying in the same column.
### Fig.1
![1](https://user-images.githubusercontent.com/59218287/119340273-9c645400-bc92-11eb-9567-6b0e9e836cb6.jpg)
### Fig.2
![2](https://user-images.githubusercontent.com/59218287/119340285-9ec6ae00-bc92-11eb-8c45-e582c89d8cdf.jpg)
## Input:
•	Line 1 contains two space separated integers MM and NN, i.e. the size of two dimensional array.
•	Line 2 contains M∗NM∗N unique integers separated by space. These are the contents of a two dimensional array in row-major order.
## Output:
•	Line 1 is space separated M∗NM∗N integers sequence. These are the final contents of a two dimensional array in row-major order.
## Constraints
•	All range in between 1 and 1000.
## Sample Input 1:
4 4
18 4 16 8 23 13 20 11 28 24 26 25 1 30 15 19
## Sample Output 1:
1 8 16 18 4 13 19 23 11 15 20 28 24 25 26 30

## Sample Input 2:
3 3
18 9 11 1 4 15 13 23 20
## Sample Output 2:
1 4 11 9 15 18 13 20 23
