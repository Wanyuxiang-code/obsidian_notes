---
title: Access Control & Constructors,Destructors
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期六, 六月 1日 2024, 2:08:35 下午
---

## Access Control
### Difference between access control and scope
> [!Important] Difference
> Scope:
> >Scope means visibility, which considers the ability whether the complier can recognize a variable/structure/function.
> 
> Access Control
> >Access control is the ability that whether a code can access(modify) a variable/structure/...

#### C: Access Rights == Scope
C entangles information hiding with file management, offering a few choices for scope: file/global/compound statement.
And **scope implies access control in C**, as long as the complier can recognize the code(can track them in its stack frame), the code can modify the data by name.
Dilemma: If we want to implement module design, which means share information among several files, we sometimes have to jam all modules into a single file(In this case, the code can recognize the variables)

#### C++: Access Rights != Scope
Considering the incapability of module design and extensibility in C, C++ decouples access control from scope.
> [!Important] Access rights in C++
> Access rights in C++ are granted by a **class** and are specified in the class's definition.
> Scope is only visibility in C++ and does not grant access rights.
 
### Access control in C++
#### Basics  Understanding
> [!Note] Ability & Inability of Access control in C++
> Ability
> >A class can allow another class to access specific fields of any instance or to call specific functions.
> 
> Inability
> >Access rights to specific instances are not controllable, which means we can't control the concrete access rights to a specified instance of a certain class
> 
> 即C++中的访问权限均在类的维度上操作，我们可以声明对类中具体的子项的访问权限，但不能更改一个孤立的类的项的访问权限

In C++ code, since access rights can be managed explicitly, all class definitions are globally visible -> Better extensibility when implementing module design

#### Scope resolution operator
In C++, the scope resolution operator is used for specify which scope and namespace to access.
Usage:
[Scope resolution operator in C++](https://www.geeksforgeeks.org/scope-resolution-operator-in-c/)
#### Levels of access rights
- **private**
  Access is allow only within the class's functions: member and class function, code in the class definition, **friend classes/functions.**
  **Even the derived class's functions can't modify the class.** 
  This is the default class access right.
- **protected**
  protected extends access to **code within any derived class's functions.**
- **public**
  public allows any code to use the fields and functions, which should generally only be used for interface functions.
  
> [!Info] Friends
> Classes can have friends, which are functions or classes that are granted access to its private and protected member. This is done by friend keyword.
>**Notice**:
>Friend functions are in the global namespace, not in the class, so access control has no relevance. Its return type is often the whole instance.
>1. Friend function could be either global function or other class member function
>>- `friend return_type func_name (arguments)` for global function
>>- `friend return_type class_name::funcname (arguments)` for a member function of another function
>
>
>2. Declare a friend class `friend class friendname`
>3. Friendship is not mutual, and friendship is not inherited.

^72a29f

```c++
class MyClass {
private:
    int privateVar;
//We can also declare a friend by friend keyword
friend class F;
public:
    friend void accessPrivate( MyClass& obj );
    //MyClass& means reference, similar to pointer
};

void accessPrivate( MyClass& obj ) {
    // Allowed to access obj's privateVar
    obj.privateVar = 10;
}
```

## Constructors & Destructors
Constructor and destructors are both member functions with **implicit this pointer**.
### Constructors
Constructors are used for initializing a class member, which are often declared as public access right.
> [!Note] Called time
> - Automatic variables(called at point of declaration)
> - Static variables(called before main)
> - Dynamic variables(at point of allocation)
>**Notice**
>> Constructors are **always** called for initialization, 任意的class instance declare 过程一定会调用construtor,注意与赋值时可能会重载的赋值运算符区分！！
>> 



Common Features of Constructors:
- name: **the name of the class**
- return type: none(**even not void**)
- **a class can have more than one constructor, overloading is allowed(we can define multiple versions)**. In this case, we can have **default constructor with empty body, parameterized constructor and copy constructor together**.(==注意default constructor相互冲突的情况==)
- 注意default constructor with no arguments, parameterized constructor and copy constructor**均为constructor, 用于初始化(也仅有初始化的时候调用）**，它们需要的参数不同，copy constructor利用已有instance的reference.
- access rights一般为public
#### Two Default Constructors
Two public constructors are created by default
##### Constructors with no arguments
The constructor with no arguments created **only if no constructors declared in class definition used for initializing array elements**. ==Array of a class' instances are not allowed if no constructor with no arguments exists==
operation
  It initializes each field based on its type,对一般的变量填bits,对instance调用相应的constructor
  - Fields that are not instances are left as bits(concrete fields left as bits)
  - Fields that are instances are initialized using the constructors with no arguments for their class, which must exist and be accessible(Initialize an abstract struct)
##### Copy Constructor
**It takes one argument: a reference* to another instance of the same class,注意copy constructor经常接受const reference型的参数防止更改**
```c++
#include <iostream>
using namespace std;
class Sample {
	int id;
public:
	Sample(int x) { id = x; }
	Sample(const Sample &t){
		id = t.id;
	}
	void display() { cout << "ID=" << id; }
};
int main()
{
	Sample obj1(10);
	obj1.display();
	cout << endl;
	//Emplicit copy constructor calling
	Sample obj2(obj1); // or obj2=obj1;
	obj2.display();
	return 0;
}
```

#### Initializer
> [!Important] Concept
> A brief specification for initialization, consisting of a **base class or field name and an arbitrary expression in parentheses**
> For base classes and instances, lists of expression are passed to constructors.
##### Order of initializer
Order of initializer does not affect code, but should match the order of execution
1. Base class:
   in order of derivation list, if a class does not appear in the list, constructor with no arguments is called
2. Fields
   in order listed in class definition. if a field that is an instance does not appear in the list, constructor with no arguments is called.
Because Initializers are executed before constructor's code, thus when we implement the constructor's code, all base classes have been initialized and all fields have been initialized.
**Use initializers, Not code to initialize Instances to avoid re-initialization**
```c++
class MyClass {
public:
    MyClass(int val) : value(val) {} // Using an initializer list
private:
    int value;
};
MyClass obj(42); // 'value' is initialized with 42 using the initializer list
```
The initializer list and the constructor declaration are separated by `:`.
**A constructor can't be inherited**
### Destructors
> [!Important] Concept
> A destructor is a special member function of a class that is called to clean up an object when it is no longer needed. 
> Its purpose is to release resources that the object may have acquired during its lifetime, such as memory, file handles, network connections, etc. 
> The destructor is defined with the `~` prefix followed by the class name and does not have a return type or parameters.

> [!Note] Called time
> - Automatic variables: at the end of scope
> - **Static variables: after main**
> - **Dynamic variables: at the point of deallocation**
> Not called cases:
> >When the program abnormally terminates or dynamically allocated instances that are not deallocated

1. Common Features of Destructors:
- name: **the name of the class**
- return type: none(**even not void**)
- take no arguments
- it should be declared in public access right, exactly one destructor should be defined
- **A user-defined constructor is needed when we have dynamically allocated memory or pointer in class**, we have to define it to avoid memory leak.
2. Operation order
==The order of implemening destructor is the reverse order of constructor.==

3. Tips 
> [!Warning] define destructor and make it virtual
>  In a hierarchy of classes, derived classes may allocate resources that need to be released explicitly. **A virtual destructor ensures that the destructor chain is properly executed, starting from the most derived class up to the base class. This allows each class to clean up its own resources.**
>  **In sum it can keep consistency when encountering unmatched but need to be accurate types**
>  ==Don't call destructor for fields that are instances, such calls are made automatically, but we must call destructor for dynamically allocated variables==

4. Example code:
```c++
class MyClass {
public:
    ~MyClass() {
        // Clean-up code here
    }
};
```

## this pointer
### Motivation
How objects look at functions and data members of a class
1. Each object gets its **own copy of the data member**.
2. All-access the same function definition as present in the code segment.
The complier supplies an **implicit pointer** along with the names of the function as **this**. “this""pointer指向当前non-static member function调用的obejct
> [!tip] Availability
>-  "this" pointer is **passed as a hidden argument to all nonstatic member function calls** and is available as a **local variable** within the body of all **nonstatic functions.**
> - It is non available in static member functions as static member functions can be **called without any object.**
> - ==注意在LC3的stack frame中可以作为non static member function的隐藏变量！！==

### Application
- When local variable's name is same as member's name
- To return reference to the calling object
```c++
#include<iostream> 
using namespace std; 
class Test 
{ 
private: 
int x; 
int y; 
public: 
Test(int x = 0, int y = 0) { this->x = x; this->y = y; } 
Test &setX(int a) { x = a; return *this; } 
Test &setY(int b) { y = b; return *this; } 
void print() { cout << "x = " << x << " y = " << y << endl; } 
}; 
int main() 
{ 
Test obj1(5, 5); 
// Chained function calls. All calls modify the same object 
// as the same object is returned by reference 
obj1.setX(10).setY(20); 
obj1.print(); 
return 0; 
} 
```

## Virtual Function
### Concept
> [!Important] Virtual function
>A virtual function (also known as virtual methods) is a member function that is declared within a base class and is re-defined (overridden) by a derived class.
>>When you refer to a **derived class object using a pointer or a reference to the base class, you can call a virtual function for that object and execute the derived class’s version of the method**.

### Usage 
In sum: **Allow for polymorphism for a class cluster**
- Virtual functions ensure that the correct function is called for an object, regardless of the type of reference (or pointer) used for the function call.
- Functions are declared with a **virtual** keyword in a base class.
### Rules
1. Virtual functions **cannot be static**.
2. A virtual function can be a friend function of another class.
3. Virtual functions should **be accessed using a pointer or reference of base class type to achieve runtime polymorphism.**
4. **The prototype of virtual functions should be the same** in the base as well as the derived class.
5. They are always **defined in the base class and overridden in a derived class**. It is not mandatory for the derived class to override (or re-define the virtual function), in that case, the base class version of the function is used.
6. A class may have a [virtual destructor](https://www.geeksforgeeks.org/virtual-destructor/) but it cannot have a virtual constructor.
### Example
```c++
#include <iostream>
using namespace std;
class base {
public:
	virtual void print() { cout << "print base class\n"; }
	void show() { cout << "show base class\n"; }
};
class derived : public base {
public:
	void print() { cout << "print derived class\n"; }
	void show() { cout << "show derived class\n"; }
};
int main()
{
	base* bptr;
	derived d;
	bptr = &d;
	// Virtual function, binded at runtime
	bptr->print();
	// Non-virtual function, binded at compile time
	bptr->show();
	return 0;
}

```


