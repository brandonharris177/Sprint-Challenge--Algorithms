#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this code is O(n) meaning it runs once for each input and the size of the input and the amount of time for the fuction to run are related at a set non growing number. In this case the funciton runs equal to the number of inputs (i.e. 5 inputs, it runs 5 times). Although this is not always the case i.e O(2n), O(1/2n) ect. in this case it only runs one more time for each additional input. because a grows by n * n and you must do that n times to get n * n *n which is the value where the while loop stops running. 


b) The runtime complexity of this code is O(n). While it is tempting to put this codes runtime complexity as O(n^2) the first for loop does not actually do anything to the inputs and instead just creates a variable while the real work is done in the while loop making it so sum is actually only counted once for each input value and thus they have a 1:1 growth ratio. 


c) The runtime complexity of this code is O(n). In recursion the function is called within itself. For this function the original number is inputed and then calles the funciton again decremented by 1 and so on until it reaches 0 at which point 0 is returned. That means that is is invoked an equal number of times to the input put into the function giving it a 1:1 growth rate. 


## Exercise II


