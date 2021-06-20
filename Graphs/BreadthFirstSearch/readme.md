### list of questions

- Given the Process ids in array and the parent of these Process ids in separate array, and the process id we need to kill. Find the List of the process which would get killed on killing the given process.

Example:

pid{1,2,3,4,5,6,7,8,9} 
parentpid{2,0,2,3,3,3,3,4,5} 
Killing Process: 3
Output :{4,5,6,7,8,9} 

Create a Directed Graph between the parent and Child process and perform BFS (Breadth First search)

- 