---
title: Dynamic Allocation in C
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
date created: 星期一, 五月 27日 2024, 11:46:53 中午
---

## Motivation

1. Since the stack frame will be tear down after a function call, we can apply **dynamic allocation** to allocate memory to store some data created during a function call. Or sometimes we need to dynamic reszing our data memory location to fit the need need.
2. ==Storage location: heap==
3. The standard C library including dynamic allocation functions:  
   `#include <stdlib.h>`
4. Basic operations:
   - allocating memory: with **malloc** function or **realloc** to reallocate memory
   - freeing memory: with **free** function

## Rules:

1. Don't read or write memory locations before or after a block
2. Call free exactly on each block
3. Don't call free on any other pointer, including pointers into a block
4. Don't access a block after freeing it

## Common functions

### Malloc

1. Usage: allocate memory
2. prototype:  
   `void * malloc(size_t size);`
   1. `size_t size`: the argument specify how many bytes to allocate( can employ `sizeof` function to specify the memory storage)
   2. **return value**: **a void pointer to the memory location you want to allocate**, you can simply assign any other pointer type to void pointer. Or malloc will return NULL for failure.(==Notice to implement type conversion==)  
      **Notice: Apply sizeof function of your target yavriable to keep consistency and robust property of your code**
3. Application:  
   We can combine memory allocation with struct to create more complicated data structures and store them in heap.
4. Shallow copy and Deep copy:
   1. Shallow copy:  
      Shallow copy just copy a pointer to the same location. The two objects share the same memory location, which means once we have changed or freed the corresponding memory locations both two objects will change.  
      Example:  
      `polygon_t * p2 = p1;`or

      ```c
      polygon_t * p2 = malloc(sizeof(*p2));
      *p2 = *p;
        ```

   2. Deep copy:  
      Deep copy will duplicate the whole objects in different memory locations, which means we can freely change the previous memory location.  
      ![](https://s2.loli.net/2024/06/01/ZSCkERU74wrj95M.png)
  5. Notice: we can't assume the allocated memory locations are all filled with 0s, if we want a zeroed chunk of memory, use `calloc`

### Calloc

1. prototype:  
   `void * calloc (size_t num_elts, size_t elt_size);`  
   The number of bytes needed is the product of those two arguments.  
   It will also a pointer to the allocated chunk of memory or NULL for failure.
2. Usage:  
   Set the allocated memory all to zero.

### Free

1. Usage: free the memory location allocated by the user.(The data will remain on the heap until the user explicitly free the according memory locations)
2. prototype:  
   `void free(void *ptr);`  
   `void *ptr`: starting address of the memory that needs to be freed, which should match with the return value malloc.
3. Effects:  
   The memory freed will be deallocated, and any previous pointer to those locations will be dangling pointers, which can't be dereferenced. If the argument is not a starting address of a block, it will result in error.
4. **Notice:**  
   **Free only frees the specified memory, if it contains pointer to other locations in the heap, we should free them first, or we may never be able to have access to it**
5. Memory leaks:  
   When you lose all references to a block of memory, and the memory is still allocated, you have leaked memory -> results in significant drop in performance.  
   free(NULL) will do nothing
6. Common problems:
   1. Multiple freeing:  
      Trying to free the same memory location twice is called double freeing, which will cause the program to crash.
   2. Freeing something that is not at the start of the block returned by malloc.
   3. Freeing a variable that is not on the heap.

### Realloc

1. Usage: use to request for more memory locations than previously requested malloc
2. prototype:  
   `void * realloc(void *ptr, size_t size);`  
   size_t size resizes the memory allocation starting from where ptr points.
3. **Notice:**  
   **realloc may give a new memory location for the reallocated data**
4. **Tip**:  
   `ptr = realloc (ptr, new_size)` if realloc fails, the address of old block is gone!  
   Use a temporary variable when calling realloc.

   ```c
   int32_t * temp;
   temp = ralloc (ptr, new_size);
   if (NULL != new_copy){
	   ptr = new_copy;
	   }
     ```

### Getline

1. Usage:  
   Compared to fgets which has to specify the size of input string, getline can apply dynamic allocation to read a line without specifying the maximum length.
2. prototype:  
   ![](https://s2.loli.net/2024/06/01/3DhyreFvWap6Tz8.png)
3. detail:<[getline | Coursera](https://www.coursera.org/learn/interacting-system-managing-memory/supplement/4Fwiv/getline)>

### Sbrk

1. Usage:  
   change the break of dynamic allocated memory block. Break means the address after the end of the heap.
2. Prototype:  
   `void *sbrk (intptr_t increment);`  
   `intptr_t increment`: type: an integer large enough to hold a pointer, and specify the increment of break  
   return value: the address of the previous break 

## Application

### Flatten and unflatten Datastructure

1. Motivation:  
   Pointers are memory addresses, and don't mean anything on other computers in later execution. So if we want to save a data structure to a file, we need to flatten the data structure by removing all pointers and packing data into a contiguous array of bytes.
2. Example: Flatten a tree based on recursion

### Best-Fit Logarithmic Allocator

$$Sum = N*\sum_{i=1}{\frac{1}{2^i}}$$