
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

## 
