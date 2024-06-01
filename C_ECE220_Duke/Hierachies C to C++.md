---
title: Hierachies C to C++
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期六, 六月 1日 2024, 2:08:36 下午
---

## Hierarchies of structures
### Motivation
#### Basic concept
We want to organize and structure massive inter-relatd data ->
Apply type hierarchy which is a way to organize and structure a hierarchical tree.
> [!Note]
> Type Hierarchy
> Each node in the tree represents a class and the edges represent the inheritance relationships between these classes.
> 
> *Often Used in OOP(Object-oriented programming)*

![](https://s2.loli.net/2024/06/01/5JpyvB4ghdqPCVS.png)
#### Property and Advantage
##### Advantage
- **Code Reusability**: Common functionality can be encapsulated in a base class, and derived classes can reuse this code without rewriting it.
- **Extensibility**: New classes can be easily added to the hierarchy to extend the system's capabilities.
- **Organization**: It helps in organizing code in a logical manner, making it easier to understand and maintain.
- **Polymorphism**: It enables the use of a unified interface for objects of different classes, which can be treated as objects of the base class.
##### Property
- **Single Inheritance**: A class inherits from only one base class.
- **Multiple Inheritance**: A class can inherit from multiple base classes.
- **Hierarchical Inheritance**: A class can be a base class for one or more classes, which in turn can be base classes for other classes, creating a tree-like structure.
- **Multilevel Inheritance**: A class can inherit from a derived class, which itself is a derived class from another class.
> [!Remark]
> 即继承关系可以多样化，子类可继承多个父类的属性，父类也可作为多个子类的属性

### Implementation Details
#### Structure Example
##### Code
==Highlight the inheritance of different structure hierarchy==
```c++
// Base class
class reference_t {
public:
    char* author_list;
    char* title;
    int32_t year;
    // Constructor, other common methods
};

// Derived class for papers
class paper_t : public reference_t {
public:
    int32_t pages;
    int32_t month;
    // Constructor, paper-specific methods
};

// Derived class for articles
class article_t : public paper_t {
public:
    char* journal;
    int32_t volume;
    int32_t number;
    // Constructor, article-specific methods
};
```
##### Memory Layout
In C++, when a class is derived from another class, the base class part of the derived class comes first in memory.
>Memory Layout
+------------------+ <--- Memory address of the book object
| double_list_t* prev | 
| double_list_t* next |
+------------------+
| char* author_list |
+------------------+
| char* title      |
+------------------+
| int32_t year     |
+------------------+
| char* publisher  |
+------------------+
| char* address   |
+------------------+
| uint64_t ISBN    |
+------------------+

Derived result:
> [!Important] Pointer aliasing
> Because double_list_t is at the beginning of both reference_t and book_t objects, so a book_t* pointer can be "aliased" to a double_list_t pointer. They all point to the beginning part of an objcet.

>[!Warning] Safety of casts -> One-direction Process
> It is safe to **cast a pointer of a derived class to a pointer of a base class** because the derived class has inherited all properties of the base class.
> But the reverse process is not safe without knowing for sure the concrete derived class to manage
> 注意C++中void* pointer不能直接被编译器隐式转换，一定需要明确声明
 
#### Dynamic Type Information
> [!Motivation]
> We don't want to divide the whole data structure separately, but we indeed need to operate differently based on the concrete derived class type.
> > Solution: Apply **dynamic type information** and use switch to implement

Similar ideas to operate based on different types in [[Containers and Iterators#Method Adopt a Callback function]] and mp11, and the it can also adopt the idea of function pointer to add extensibility [[Use of Pointers#Function Pointer]].
```c
struct reference_t {
	double_list_t link;
	char* author_list;
	char* title;
	int32_t year;
	int32_t type; //Define the type of this object
	void (*print_citation) (reference_t* ref);
}
//Print our bibliography, remember to use function pointer to achieve packaging
double_list_t* elt;
for (elt = biblio.next; &biblio != elt; elt = elt->next){
	elt->print_citation (elt);
	//Function print_citation will first evaluate the type of the reference and then adopt different function 
}
void print_citation (reference_t* ref){
	//Don't forget to apply enumeration to impart values with significant names
	switch (ref->type) {
	case TYPE_PAPER: print_paper_citation ((paper_t*)ref}; break;
	//...
}
```
> [!Supplement]
> For higher level of packaging, we can create a virtual function table for a type and for a variable.
> But it is at the cost of accessing more memory.


## Data and Function Inheritance
### Motivation and Basic Concepts
People wanted to automate tasks to enforce best practices and reuce opportunities for human error. The programer specify only the type hierarchy and which functions should be changed for a subtype.
> [!Remark]
> 充分利用已有对象特性，减少重复造轮子。利用封装清晰的interface调用轮子，隐去函数具体执行过程的

> [!Important] Child Inherits all data and functions on its parent
> **Data Inheritance**
> >If a base has a field, so do all types derived from that base type
> 
> **Function Inheritance**
> >If a function operates on a base type, the function also operates on any type derived from that base type.

> [!Important] Data structure and Class
> Data structure
> >A struct with fields related with **static data, interface function, internal functions, initialization/teardown functions**
> 
> Class
> >Include **Data member(variables defined in a class), Member Functions, Constructors, Destructors, Access modifiers, Inheritance**
> >Everything related to a class must appear in class definition
> >`::` namespace operator
### Implementation
A class declaration can include:
>access control level(default == private)
>fields(instance variables)
>class variables(declared with keyword  `static`)
>member function
>class functions 
```c++
class MyClass : public ParentCLass {
	//fields-> the same as a struct, the order of declaraion is the order in memory, and fields come after fields from parent class
	int32_t x;
	double y;
	
	//Class variables prefixed with static(Class variable is the shared variable for the whole class instead of one instance). Those variables are stored in global variable area
	static int32_t classInt;
	static double classDouble;
	//Notice, the code in class declaration just declares the existence of those variables but does not create storage. Static variables must also be declared outside of the class definition. It should also be initialized outside.
	
	//Member functions have an implicit first argument, a pointer to an instance of the class. And they are used like a field
	int32_t memFunc (char x, double* y);
	//Actually its C signature is like: memFunc(MyClass* this, char x, double* y)
	
	//Class Functions are declared with static Prefix, and their signatures are exactly the same as in C. Invoke a class function by Class:: prefix
	//If class functions or member fucntions are declared outside class definition, we must use namespace operator to specify the scope. Within their range we can infer the symbols from the class.
	//Notice when declaring class function outside, don't use "static" keyword in declaration
}
```

> [!Tip] 
> 
>    Local variables and global variables
> - Local variables only exist in the block where it is declared while global variable exist throughout the whole lifetime of the program.
> - **The complier will give precedence to the local variable when the two have the same name, and if we want to access global variable, we can use `::` (socpe resolution operator) instead**
>   
>   Storage class
> - static storage class: Static variables can **preserve their value of their last use in their scope during the whole lifetime of the program**
> - extern storage class: It tells us the variables is defined elsewhere and not within the same block where it is used. It is often used to impart access rights between different files.
> - mutable storage class: Applying `mutable` keyword can allow us to change storage class of a variable.

## Class Layout in C++
### Basic Idea
1. A Class is a user-defined data type that has data members and member functions.
2. Data members are the data variables and member functions are the functions used to manipulate these variables togethe
### Access control
Access control define the different access rights for different fields of a class, for more details:
[[Access Control & Constructors,Destructors#Access Control]]
Once we have access rights to a class, we can use `.` to access the class member of an instance.
### Inheritance Relationship
[[Hierachies C to C++#Data and Function Inheritance]]
### Data Members
#### Non-static data
Non-static data are unique to every instance of a certain class, and each instance will have its own copy of non-static data members.
**Declared inside the class definition but outside any function**.
#### Static data
These are shared among all instances of a certain class, there is only one copy of static data regardless of how many instances.
**Declared outside the class definition in the source file注意在class definition 类内define时需要`static`label但在外部声明时不需要,仅需声明所属的class。**
Static data仅能在class声明外初始化。
```c++
class MyClass {
private:
    static int staticDataMember; // Shared among all instances
public:
    MyClass() {} // Constructor
};
// Static data member definition must be outside the class definition
int MyClass::staticDataMember = 0;
```
### Functions
#### Constructors and Destructors for initialization and removal
Constructor and destructor属于member function.
特别地，当我们涉及到声明并初始化或者清楚创建的实例时，编译器会调用在class中定义的constructors与destructor.
[[Access Control & Constructors,Destructors#Constructors & Destructors]]
#### Non-static member functions
Member function操作于具体某一个实例中的数据，规定了一个类中作用于实例的相关操作。
**Defined inside the class declaration as prototypes. Their implementations are provided outside the class declaration, usually in the source file**. They can **access both static and non-static data members**
> [!important] this pointer
> 注意non-static member function有隐式的指向当前特定instance的指针作为第一个
> 参数

#### Static member Function
Defined and implemented similarly to member functions but **can only access static data members and other static member functions.**

**注意static member function没有this pointer, class内声明时有`static`label，class外定义时只需标明class类**

#### Friend function
[[Access Control & Constructors,Destructors#^72a29f]]
