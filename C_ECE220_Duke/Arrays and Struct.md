---
title: Arrays and Struct
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
---

## Array

### Motivation

1. Deal with multiple variables with similar properties and structures, it can help us eliminate the tedious work
2. Definition: An array is a sequence of items of the same type

### Array Declaration and Initialization

`int myArray[4]`  
`int myArray = {1,2,3,4}`

1. Declaration:  
   The array declaration should include the data type of the array and the size of the array.
2. Property:  
   **Notice: the name of the array is a pointer which points to the first element of the array. And it is not a lvalue which means we can't change where it points.**
3. Initialization:  
   Include the initial values in the curly braces  
   Notice:
   - If you input fewer initial values, the complier will automatically fill with 0s; And if you input more initial values, the complier will just give you a warning instead of crashing down.
   - When you initialize each value, you can omit the size in brackets
4. Extensions: Apply similar syntax to initialize structs

### Accessing an Array

1. Index the Array  
   `MyArray [4]` can simply access the fifth element of the array, and it can be used as either a lvalue or a rvalue.  
   Notice: **Array index is zero-based and Access out of range is an error that the complier will not detect.**
2. Pointer Arithmetic
   - Reason: The arrays are stored in a continuous locations in memory, which make the pointer arithmetic reasonable.
   - Example:

     ```c
     int sumArray(int * array, int n){
     int answer = 0;
     int * ptr = array;
     for(int i = 0; i<n; i++){
     answer += *ptr;
     ptr++;
     }
     }
     ```

3. Passing Arrays as Parameters:
   - Pass the name of the array(**It serves a pointer to the first element**)  
     `int myFunction{int * myArray, int size};`  
     Since there is no way for C to know the exact size of the array without explicitly passing it, it is advisable to pass the size of the array  
     We can either index it like an array or do pointer arithmetic 
   - Pass an array as parameter using brackets  
     `int myFunction{int myArray[], int size};`  
     You can pass any expression which ecaluates to a pointer to a sequence of elements  
     You can also apply {} to indicate the size.

### Array Caveats

1. Dangling Pointer(悬空指针)：
   - Reason: Be careful when using a pointer as a return value of the function. Because if the storage space you have created is in the local variables locations(**in the stack frame**), they will be tear down after function call. In this case, the pointer will point at something that no longer exist, which is called **Dangling Pointer**.
   - Result: Undefined behaviour.
2. Array Size:
   
   

## Struct

### Data structure

1. concept:
   1. A logical grouping of several piece of data
   2. Some operations that manipualte those data
2. Ways to build datastructre:
   - Arrays
   - Struct
   - ...
3. Principles to develop a structure:
   1. specify the fields contained in the struct
   2. specify the file-scope variables
   3. specify some operations to the structure that can be implemented by functions

### Struct

1. Definition:  
   Struct can define a structure type, it does not create instances of the struct. We apply the same way to declare variables in struct as in other places.  
   Example

   ```c
   typedef struct book_t {
	   char author[50];
	   char title[10];
	   int32_t edition;
	   }book;
	``` 

2. Memory order:  
   The fields are stored in memory the same way declared in the definition.
3. sizeof operator:  
   `sizeof (structA)` evaluates to the number of bytes occupied by the variable structA  
   **Pitfall: avoid calculating the size by hand**  
   Most ISAs impose alignment requirements that load and store of N bytes use addresses that are multiples of N. And the complier will align ***fields to their size and structures to the maximum alignment needed by any field.***
4. typedef prototype:  
   `typedef <base type> <list of types>;`  
   Note that: the structure definition need not appear before these definitions.  
   And a structure definiiton can be used as a base type.
5. Field access:  
   Apply field operator  
   `.` is the field access operator that can help to access the fields defined in the structure.  
   Without typedef, every time you want to declare a struct variable you have to code like `struct book_t bookA`  
   Apply `—>` operator to access fields after dereferencing  
   `—>` can dereference and access a field. `(*s).top` = `s->top`
6. **Pass as a parameter**:  
   Pass the pointer to the structure as a parameter instead of the whole copy, which will take up much more space.  
   Which way to push a parameter worths thinking.

### Enumeration

1. Concept:  
   Enumeration is a list of things with some common features numbered consecutively.
2. Rule:  
   In C, enumeration start with 0 but can be overridden.  
   Example: `enum {FALSE, TRUE}` FALSE has value 0 and TRUE has value1  
   And the values are numbered and re-numbered automatically.
3. Usage:  
   Impart a list of integer with significant names to make it more convenient and readable.
