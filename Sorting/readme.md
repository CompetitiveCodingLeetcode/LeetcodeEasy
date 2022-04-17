
### For custom sorting
The following link contains the possible ways to do customized sorting using sorted() method: https://medium.com/analytics-vidhya/sorted-function-using-key-parameter-in-python-7aa9b8cebfb6

### Stable Sorting

- means if two elements are equal then the order in which the elements occur in original array is the same in sorted array too.

### in place sorting

- means no auxillary space is required for sorting.

## BUBBLE SORT

- insertion has better performance than bubble sort
- Advantage: It can detect whether the list is already sorted or not.
- Worst case time complexity: O(n^2)
- Average case time complexity: O(n^2)
- Best case time complexity: O(n)
- Worst case space complexity: O(1)
- The adjacent elements are compared and after each pass the smaller element starts coming up slowly like a bubble

## SELECTION SORT

- works well for sorting small files
- It is suitable for sorting large files with small keys because sorting is done based on keys  
- Advantage: In place sorting.
- Worst case time complexity: O(n^2)
- Average case time complexity: O(n^2)
- Best case time complexity: O(n^2)
- Worst case space complexity: O(1)
- Select the least element in the remaining array and swap with current element.

## INSERTION SORT

- suitable for small data
- in k iterations k+1 elements are sorted
- in place sorting
- Stable sorting technique  
- in case of partially pre sorted list the complexity becomes O(n+d) where d is the number of inversions (Adaptive)
- Online : can sort list as it receives
- Worst case time complexity: O(n^2)
- Average case time complexity: O(n^2)
- Best case time complexity: O(n^2)
- Worst case space complexity: O(n^2) total, O(1) in auxilary

## MERGE SORT

- merge sort is used for sorting linnked list in O(nlogn) time.
- merge sort helps in solving inversion count principle
- time complexity: O(nlogn)
- space complexity: O(n)

## QUICK SORT

- Partitioning: first, we pick an element and put it at the right position such that all elements to the left of the element are lesser and all
elements to the right are greater than it.
- hence, first is find partition element from start to end. say, the correct pos is p.
- second, recursive call to sort array from 0 to p-1 and from p+1 to end of array.
- steps are as follows:
1. find idex of pivot element by partitioning. let partition() method return p
2. sort arr from s to p-1 recursively
3. sort arr from p+1 to e recursively
4. Partitioning logic:
   1. select a pivot element (say arr[s])
   2. put the pivot element at its correct location:
      1. to find correct location we kow all elements to left of pivot should be less and to the right of pivot should be greater. Hence, count the umber of elements lesser than pivot.
      2. correct pos of pivot = s+count
   3. now put lesser elements towards left and greater elements towards right by two-pointer approach and swap
5. base case for recursion = if s>= e return