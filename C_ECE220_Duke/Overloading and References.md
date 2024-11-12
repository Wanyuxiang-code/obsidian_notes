---
title: 2024-05-27-Overloading and References
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
---

## Dynamic Allocation in C++

[[Dynamic Allocation in C]]

### Use `new` to create new instances

1. prototype of new  
   `new <classname> (args,...)`  
   new will return a pointer to a constructed class instance  
   Use () to include arguments passed to constructors, omitted if there are no arguments  
   On failure new throws an exception, which terminates the program  
   注意new一般会与constructor配合initialzie an instance and create a pointer to the instance  
2. Example:  
   `MyClass* m = new MyClass (arg1, arg2, ...);`  
   It can also used to dynamically allocate an array.  
   `MyClass*m = new MyClass[42];`

   ```c++
   int (*a)[3] = new int[n][3];
   for (i = 0; i< n; i++) for (j = 0; j < 3; j++) {a[n][j] = 0;}


```
   
> [!warning]
> The programmer should remerber whether each allocation was an instance or an array. If deallocated in the wrong type, tedious degugging!
### Use `delete` to deallocate instances
   `delete m; // delete an instance`
   `delere[] m; //delete an array`

## Overloading and References
### Basic Overloading Concepts
#### Overloaded Functions
1. concept:
   Functions can be overloaded meaning that one function name may have multiple definitions. And the complier choose the version of the function based on the number and types of arguments.
2. Notice:
   The complier selection must be **unambiguous**. For the version that the complier can't determine, it will not choose.
#### Overloading Operators
1. Concpet:
   Operators can be redefined in several ways, specific to their types of operands. It is aimed at **natural use of user-defined operands**.
   Prototype for operator function:
   `classname operator<operator symbol> (args)`  
2. Integrated with auto-conversion
   Since we want to expand some operators to the types we have defined, and we don't want to implement conversion in hand when managing different types of operators.
3. Methods:
   C++ combines implicit casts with symmetric definitions.
   > [!Info] implicit casts, explicit casts & symmetric definitions
   > **Implicit casts**:
   > >After the constructor is determined, the complier will perform implicit conversion between some numeric types, pointers and references and... This process is achived without any explicit instructions from the programmer.
   > 
   > **Explicit casts**:
   > >Explicit casts are performed by the programmer using specific cast operators.
   > >If you want to avoid implicit casts, add explicit before the constructor.
   > 
   > **Symmetric definitions**:
   > >Defining operators in such a way that they can be used in a nartural and interchangeable manner.

> [!Info] Explicit cast conversion
> Static cast:
> >`static_cast<Type>(expression)`
> 
> C-style Cast:
> >`(Type)expression` is less safe in C++ and may perform conversions that are not allowed by other C++ cast operators
> 
> Functional cast:
> >`Type(expression)` it is preferred in C++, more explicit and more clearer.

==注意C++中void pointer需明确转换类型==
And C++ will also enable friend functions to perform this process. [[Access Control & Constructors,Destructors#^72a29f]]
Example
```c++
class complex {
public:
    public:
	    double real, imag;
	    //constructor that allows implicit casts
	    complex(int r = 0, int i = 0) : real(static_cast<double>(r)), imag(static_cast<double>(i)) {}
    //Overload for complex addition
    complex operator+(complex const& obj)
    {
		complex res;
		res.real = real + obj.real;
		res.imag = imag + obj.imag;
	}
    // Overload for complex * int
    friend complex operator*(const complex& c, int i) {
        // Implement multiplication
    }
    // Symmetric overload for int * complex
    friend complex operator*(int i, const complex& c) {
        // Implement symmetric multiplication
        return operator*(c, i); // Often, the operation is commutative
    }
};
//implicit casts performed by complier
complex c;
//explicit casts
complex c(10,5);
complex c3 = c1 + c2;

```

>**Notice**:
>1. Operators often return an instance on the stack.
>- Chaining: Returning an instance allows chaining of operations, which can easily evaluate some expressions
>- Avoiding side effects: It can avoid some side effects on the original objects
>2. Operators' Arguments should be constant references.

4. Some operators can't be overloaded:
   - member access `.`
   - pointer to member function invocation `.*`
   - conditional expression `? :`
   - scope identification `::`

5. Some expressions are not equivalent in C++
   - `array[10] !=  *(array + 10)`  
   The previous calls operator`[]` , the latter calls operators `+, *`
   - assign operator != copy constructor

## Reference

### Basic Concepts

> [!Important] Concept  
> A reference is implemented identically to a pointer, but is syntactically equivalent to the base type(the type to which the pointer points)
>
> > References can't be modified, ther are single-assignment(Just as const pointer).

### Difference between pointers

> [!Note] Difference between pointer and reference
> - **Initialization**: References must be initialized when declared, whereas pointers can be initialized later or set to `nullptr`.
> - **Reassignment**: References **cannot be changed once initialized**; pointers can be reassigned to point to different objects.
> - **Indirection**: With pointers, you often use the `*` operator to dereference the pointer and access the object it points to. With references, you use the reference as if it were the object itself.
> - **Nullability**: Pointers can be null, indicating that they do not point to a valid object. References cannot be null.

Usage:

- Pointer:  
  Use pointer for modifiable arguments
- Reference:  
  Use `const` with reference arguments; References can also be adopted to functions

Notice:  
We can't have **pointers to references, references to references, array of references**.

### NRVO: named return value optimization

1. Concept:  
   Most C++ compliers transform a returned instance into an implicit instance pointer as a new first argument, returning either void or the instance pointer
2. Principles:  
   A caller allocates space for an instance then passes a pointer to the instance and the function fills the bits. This can save the work of calling copy constructors.