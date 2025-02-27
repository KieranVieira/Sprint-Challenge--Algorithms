# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 #O(1)
    while (a < n * n * n): #O(n)
      a = a + n * n #O(1)
```


```py
b)  sum = 0 #O(1) 
    for i in range(n):#O(n)
      j = 1#O(1)
      while j < n: #O(n)
        j *= 2 #O(1)
        sum += 1 #O(1)
```

```py
c)  def bunnyEars(bunnies): 
      if bunnies == 0: #O(1)
        return 0 #O(1)

      return 2 + bunnyEars(bunnies-1) #O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
