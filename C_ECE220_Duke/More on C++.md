---
title: More on C++
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期一, 六月 3日 2024, 10:57:06 晚上
categories: C_ECE220_Duke
---

## The difference between C and C++

### Compile in C but not in C++

![](https://s2.loli.net/2024/06/01/1QDXPHmSCuOvZpg.png)

## References and Pointers

[[Overloading and References#Reference]]

## Dynamic allocation

[[Overloading and References#Dynamic Allocation in C++]]

## Basic I/O in C++

### Basic Library in C++

1. **iostream**: iostream stands for standard input-output stream. This header file contains definitions of objects like cin, cout, cerr, etc.
2. **iomanip**: iomanip stands for input-output manipulators. The methods declared in these files are used for manipulating streams. This file contains definitions of setw, setprecision, etc.
3. **fstream**: This header file mainly describes the file stream. This header file is used to handle the data being read from a file as input or data being written into the file as output.
4. **bits/stdc++**: This header file includes every standard library. In programming contests, using this file is a good idea, when you want to reduce the time wasted in doing chores; especially when your rank is time sensitive. 

 We can apply `using namespace std` to simplify the process of using standard library function in the std namespace.

### Operators

1. Insertion operator `<<`  
   The data needed to be displayed on the screen is inserted in cout using `<<`.
2. Extraction operator `>>`  
   The extraction operator extracts data form the object cin to the place you have specified.  
Be aware the difference between redirection and insertion:  
[[Interacting with user and systems]]

> [!tip] Difference between `std::endl` and `\n`  
> `std::endl`:
>
> >It inserts a new line and **flushes the stream immediately**, which is used to achieve in-time interactions and avoid conflicts. But flush the stream is expensive, it is not suitable for many outputs to print.
>
> `\n`
>
> >It will simply print a new line by just inserting a new line, which may be pushed into buffer instead of printing immediately.

### Basic I/O stream

#### `cin`: standard input from keyboard -> `stdin` in C

1. using `>>` to take multiple inputs:  
   `cin >> name >> age;`  
   input can be:  
   `ABC`  
   `13`
2. apply member function in the string buffer  
   `cin.getline(char *buffer, int N)` Notice it will just read n-1 character and add a terminator at the end

#### `cout`: standard output to the display -> `stdout` in C

1. Using `<<` to insert data to cout  
   Notice we can insert multiple data to cout  
   `cout << "Name: << name << endl;` 
2. Implement member function  
   `cout.write(char* str, int n);`

#### `cerr`: standard error output to display(unbuffered) -> `stderr` in C

## Statement

### Jump statements in C++

1. continue:  
   It is used to execute the next iteration of the same loop while skipping the remaining part of the current condition.
2. break:  
   It is used to terminate the whole loop if the condition is met.
3. return:  
   It takes the control out of the function itself, used to terminate the entire function after execution of the function after some condition.
4. go to:  
   It is used to jump directly to that part of the program to which is being called. Every goto statement is associated with a label.  
   `goto label_name;`

### Range-based for loop

```c++
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int main()
{
    // Iterating over whole array
    vector<int> v = { 0, 1, 2, 3, 4, 5 };
    for (auto i : v)
        cout << i << ' ';
    cout << '\n';
    
    // the initializer may be a braced-init-list
    for (int n : { 0, 1, 2, 3, 4, 5 })
        cout << n << ' ';
    cout << '\n';
    
    // Iterating over array
    int a[] = { 0, 1, 2, 3, 4, 5 };
    for (int n : a)
        cout << n << ' ';
    cout << '\n';

    // Just running a loop for every array
    // element
    for (int n : a)
        cout << "In loop" << ' ';
    cout << '\n';

    // Printing string characters
    string str = "Geeks";
    for (char c : str)
        cout << c << ' ';
    cout << '\n';

    // Printing keys and values of a map
    map<int, int> MAP({ { 1, 1 }, { 2, 2 }, { 3, 3 } });
    for (auto i : MAP)
        cout << '{' << i.first << ", " << i.second << "}\n";
}

```

### Exception handling in C++

#### Exception Type

1. **Synchronous:** Exceptions that happen when something goes wrong because of a mistake in the input data or when the program is not equipped to handle the current type of data it’s working with, such as dividing a number by zero.
2. **Asynchronous**: Exceptions that are beyond the program’s control, such as disc failure, keyboard interrupts, etc.

#### C++ try and catch

1. try in C++  
The try keyword represents a block of code that may throw an exception placed inside the try block. It’s followed by one or more catch blocks. **If an exception occurs, try block throws that exception.**

2. catch in C++  
The catch statement represents a block of code that is executed when a particular exception is thrown from the try block. **The code to handle the exception is written inside the catch block.**

3. throw in C++  
An exception in C++ can be thrown using the throw keyword. When a program encounters a throw statement, then it immediately **terminates the current function and starts finding a matching catch block to handle the thrown exception.**

## Call by values and Call by references

> [!Important] Difference between call by value and call by reference  
> Call by value
>
> >When calling a function, we pass the values of variables to it. In this method, the changes made to the dumpy variables in the called functions **have no effects on the values of actual variables.**
>
> Call by Reference
>
> >When calling a function, we pass the address of variables to the function. In this method, the function could **alter the values of the variables**. It can be achieved with either pointer or references in C++
