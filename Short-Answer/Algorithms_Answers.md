#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I think this one will be O(nlogn) because the program will not run o(n) because the while condition is multiplying the result of N inside the condition and inside the block of the loop.


b) I think the worst case for this one would be O(n^2) because we have a nested loop which loops in turn creates two loops in turn increasing the runtime complexity becase for each of the items in the first loop, it will loop over each item again.


c) This will run O(n) in time complexity because the function is called recursively based on the int passed in -1 which means it will call the function as many times as the (bunnies) param until the param is 0

## Exercise II

n story building (will be passed as paramater which shows how tall building is)

egg gets broken if it is thrown off floor f or higher

egg doesnt break if it is lower than f

find floor f by dropping eggs

for this I would use a divide and concor search type algorithm

the logic is as follows:

define function to take stories as param n
initialize variable (found floor) as false
initialize variable remaining floors as range of 0 to n - 1
initialize while loop while found floor is false
    drop egg from floor index of remaining floors length divided by 2
    if egg breaks then set remaining floors to remaining_floors[remaining_floors length divided by 2:]
    else set found floor to remaining floors divided by 2

return value of found floor

The time complexity of this would be O(nlogn) because it would only loop less than the amount of floors until it finds the right floor.

I'm not sure if this is exactly what the question is wanting, if the question wants the exact floor of which the eggs will break if dropped any higher, I would solve it like this:

set i to 0
set f to none
loop through 0 to n
    drop egg from floor
    if egg doesnt break
    set i to n + 1
    else( egg breaks )
    set i to n
    set f to n (or n - 1 if f is not inclusive)
return f

this could worst case be O(n) because if f === n it will loop through many times until it finds f, but it will only break 1 egg in the process where as the other method could break a lot more eggs

the above is my exact thought process nothing taken away.