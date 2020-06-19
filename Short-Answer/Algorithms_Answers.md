#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this code is O(n) meaning it runs once for each input and the size of the input and the amount of time for the fuction to run are related at a set non growing number. In this case the funciton runs equal to the number of inputs (i.e. 5 inputs, it runs 5 times). Although this is not always the case i.e O(2n), O(1/2n) ect. in this case it only runs one more time for each additional input. because a grows by n * n and you must do that n times to get n * n *n which is the value where the while loop stops running. 


b) The runtime complexity of this code is O(n). While it is tempting to put this codes runtime complexity as O(n^2) the first for loop does not actually do anything to the inputs and instead just creates a variable while the real work is done in the while loop making it so sum is actually only counted once for each input value and thus they have a 1:1 growth ratio. 


c) The runtime complexity of this code is O(n). In recursion the function is called within itself. For this function the original number is inputed and then calles the funciton again decremented by 1 and so on until it reaches 0 at which point 0 is returned. That means that is is invoked an equal number of times to the input put into the function giving it a 1:1 growth rate. 


## Exercise II
A binary search seems ideal for this type of issue as the number of cracked eggs is minimized since finding something by increment in the worst case senario requires guesses equal to the number of floors while using a biary search only takes a logrithmic amount of time and is thus much quicker. Since we do not know what floor the eggs break on we will need an exertnal function that I will call brerak(f) that takes the floor into account, if the egg is broken it reaturns true else it returns false

def break(mid):
    if egg(mid) == "broken"
        return True
    if egg(mid) != "broken"
        return False

def egg_break(floors):
    lowest_floor = 0
    highest_floor = len(floors)-1
    mid = highest_floor - lowest_floor//2
    while break(mid) == True or break(mid+1) == False:
        if break(mid) == True and break(mid+1) == True
            highest_floor = mid
            mid = highest_floor - lowest_floor//2
        elif break(mid) == False and break(mid+1) == False
            lowest_floor = mid
            mid = highest_floor - lowest_floor//2
    return(mid)

runime complexity is O(log n) as explained above

