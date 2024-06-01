---
title: Recursion
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期六, 六月 1日 2024, 2:08:36 下午
---

## An alternative to iteration
1. Definition:
   Recursive functions are those functions that call themselves, which can be an alternative to iteration.
2. Idea:
   Discover the similar structure to solve a problem, and find the correlation between current item with previous items
3. Theory:
    The principles of recursion can be compared with mathematical induction. They both trace the principle of deducing the current item based on previous items and caring the base cases. A recusive function must be well-defined with no ambiguity.
4. Principles of writing recursive functions：
   start from simple cases -> find the recursive relationship(do a definite decrease) -> determine the stopping condition or the bases cases ->translate into code -> apply reason to test and examine whether we have lost some cases
   check stopping conditions -> handle one node -> handle child node
5. Is recursion slow?
   If our code has spent thousands of time computing redundant cases, it will definitely diminish the performance. Sometimes we can optimize our code by storing the value in memory location to avoid redundant computation(memorication) or thinking our code from another perspective.
## Other resursion techniques
### Tail Recursion:
1. Definition of a tail call:
   A function call is a tail call if the caller returns immediately after the called function returns, without further computation.
   Eg. If function f calls function g, then the call to function g is a tail call if the only thing f does after g returns is immediately return g's return value
2. Tail recursion:
   A recursive function is tail-recursive if and only if the recursive call is a tail call. That is after recursion, the function immediately returns the return value of that recursive function.
3. Advantage:
   The compiler can identify tail recursion and reuse the stackframe created during recursion. Because the as soon as the recursive function executes, it will return, which means the values created during call will never be used again. So the compiler can overwrite on those memory locations
4. Equivalence of tail recursion and iteration:
   **Any tail recursion code is equivalent to iteration mode**, and we can switch between these two modes. This is especially useful when programming in functional language, where you can't modify a value once you create it. As such, there are no loops.

### Mutual Recursion:
1. Concept:
   Two or more functions call each other.
2. Usage:
   When we are writing a function, we find that we can abstract a series of complicated tasks in recursive function and then we create and call that functions.
   ***Notice: The combination of mutual recursion functions should gradually return to the bases, or it will slide into infinite loops.***

