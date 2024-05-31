---
---

## Pointers
### Basic Concepts:
1. Concept:
   Pointers are way of refering to the memory location of a variable.(A varibale type)
   - Geometry understanding: Arrow ->(Points to somewhere)
   - Hardware implementation: Pointer memory location stores the location of the variable it points
2. Basic Operations:
   1. Declaring a Pointer:
      In brief: * + the specific data type
      Reason: The "pointer" by itself is a not a type, instead it is a type constructor
      Example: `char * my_char`
   2. Assigning a Pointer:
      Assign a pointer by specifying the address you want it to point at
      ***Applying & operator***
      Example: `*ptr = &my_char`
   3. Dereferencing a Pointer:
      Read the value that the pointer points by dereferencing operator
      ***Dereferecing operator $*$***
3. Basic operators:
   1. $*$:Derefercing operator
      It can read the value that a ***pointer*** points 
   2. &:Address operator
      It can represent the ***address*** a variable stores
   3. They are inverse operators
4. Lvalues and Rvalues:
   - Lvalues:
     The values can be put at the left side of an assigning expression, technically referring to ***Modifiable Memory Location***
     It usually includes ***variables, pointer***
     **Notice: An complex expression can't be lvalues since it does not have a specific address that can be modified. And &variable can be lvalues**
   - Rvalues:
     The values can be put at the right side of an assigning expression
     All lvalues can be rvalues, and rvalues must have specific values

### Review of Memory
1. Structure:
   0x00000000: **NULL**
   Code
   Static data: Store the global variables that are accessible through the file
   Heap: Dynamically allocated memory
   ...
   Stack: Function call and local Variables
2. Call Convention for LC3-C
   - Push parameters(right to left)
   - Call the function:
     - Leave space for local variables
     - Store previous stack frame
     - Store return address
     - Code
     - Set return value
     - Restore R7
     - Load previous stack frame
     - move R6 to return value
   - Read the return value
   - Pop off the return value
3. NULL:
   - Location: 0x000000000
   - Content: Nothing, it does not point to anything
   - Significance:
     - Examine the error by checking whether the retrun value is NULL
     - Representing ending
     - Initialize pointer
     - Security: **Segmentation Fault: An error indicates that we attempted to access memory in an invalid way**
   - Type: **void**
     A void pointer can point to any type of data
     But because we don't know a void* actually points at, **it can neither be deferenced nor achieved pointer arithmetic**
   - **Pitfall**:
     NUL is a ASCII character
     NULL is a pointer to nothing
     "null" is an English word
     0 is a number

### Special Pointers
1. Useful operator:
   - **.** : member access operator, it can help access the obejct inside a struct
   - $*$: dereference operator
2. Order difference of pointer to struct:
   `*a.p`: Due to the priority, it equals to `*(a.p)`, it first evaluates a.p and then dereference that arrow
   **Notice: it will often result in error because iff a.p is a pointer, it can be dereferrenced. And it's not the right way to call a object inside a sturct**
   `(*a).p`: it first deference a and then evaluates p in a, it can be simplied as `a->b`
3. Pointers to Pointers
   1. Add the levels by adding the number of $*$
   2. Example: `int**` : pointer to an integer pointer
4. Const:
   1. Definition: The variable that we tell the complier that we can't change
   2. Notation: `const int x = 3;`
   3. Application in Pointers(Both the data and the pointer can be constant):
      1. declare a constant data
         `const int *p = &x;`, in this case we can't directly revise the value the pointer points by pointers, but we can change where p points.
         `*p = 4;`is illegal
         `p = &y;`is legal
      2. declare a constant pointer:
         `int * const p = &x;`, in this case we can modify the value address &x stores but we can't revise where p points.
         `*p = 4;`is legal
         `p = &y;`is illegal 
         We can also combine the two: `const int * const p = &x;`
      3. Typical misunderstanding: 
         ```c
         int x = 4;
         const int *p = &x;
         x = 4;
		  ```
		  This operation is legal, because the two declaration of pointer and variable does not conflict with each other and we don't try to use pointer p to modify where it points.
		  And the next is an illegal example:
		  ```c
		  const int x = 4;
		  int * q = &x;
		  *q = 5;
		  ```
		  In this case the two declaration conflicts with each other and the complier will print errors.

### Aliasing and Arithmetic
1. Aliasing:
   1. Definition:
      When two or more pointer point to one address, we say they alias with each other.
   2. Danger:
      Abuse of pointers may result in many conflicts including wrongly matching the data type of pointer and variables.

2. Pointer Arithmetic:
   1. Meaning: we could do addition for a pointer,which will result in it points to the next data in memory. **But this is confusing and we don't know where it points iff we derefernce the new pointer, the complier will produce errors.**
   2. Arithmetic: When adding N to a pointer to any type T, the complier will generate the instructions whcih add N$*$ (the number of bytes for values of type T) to the numeric value of the pointer.
      **Notice: the offset of pointer arithmetic depends on the specific type of the pointer and addressibility of memory. And x86 is byte-addressable***
      For multidimensional data, notice that the pointer arithmetic depends on size:
      `array[3][5]`:
      `array[0]+1` will refer to `array[0][1]`
      `array+1` will refer to `array[1][0]` 
      Tip: For multidimensional arrays, we just need to multiply the size of lower dimension for larger index or simply use multiple square brackets

