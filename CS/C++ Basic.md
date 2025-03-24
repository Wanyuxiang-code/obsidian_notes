---
title: C++ Basic
date: 2025-03-11
date modified: 2025-03-13
categories: CS225
tags: [CS225]
---

#CS225 

## 基础语法

### Template 模板

#### 模板的基本概念

模板本质上是一种参数化的类型或函数。 你可以把类型或函数的一部分（通常是类型）作为参数传递给模板，编译器会根据你提供的参数生成特定的代码。

#### 模板的种类

C++ 中有两种主要的模板：

*   **函数模板 (Function Templates)**
*   **类模板 (Class Templates)**

**2.1 函数模板**

函数模板允许你创建可以处理多种数据类型的函数。

**语法:**

```c++
template <typename TypeParameter1, typename TypeParameter2, ...>
return_type function_name(parameter_list) {
  // 函数体
}
```

*   `template`: 关键字，表示这是一个模板定义。
*   `typename`: 关键字，用来声明类型参数。 也可以使用 `class` 关键字来代替 `typename`，但 `typename` 更清晰地表达了参数是类型。
*   `TypeParameter1, TypeParameter2, ...`: 类型参数列表，用逗号分隔。 这些类型参数可以在函数定义中使用。
*   `return_type`: 函数的返回类型。
*   `function_name`: 函数名。
*   `parameter_list`: 函数的参数列表。

**例子：交换两个变量的值**

```c++
template <typename T>
void swap(T& a, T& b) {
  T temp = a;
  a = b;
  b = temp;
}

int main() {
  int x = 5, y = 10;
  swap(x, y);
  std::cout << "x = " << x << ", y = " << y << std::endl; // 输出 x = 10, y = 5

  double p = 3.14, q = 2.71;
  swap(p, q);
  std::cout << "p = " << p << ", q = " << q << std::endl; // 输出 p = 2.71, q = 3.14

  return 0;
}
```

**2.2 类模板**

类模板允许你创建可以处理多种数据类型的类。  这在容器类（例如 `std::vector`，`std::list`）的实现中非常有用。

**语法:**

```c++
template <typename TypeParameter1, typename TypeParameter2, ...>
class ClassName {
  // 类定义 (成员变量、成员函数等)
};
```

*   `template`: 关键字，表示这是一个模板定义。
*   `typename`: 关键字，用来声明类型参数。 也可以使用 `class` 关键字来代替 `typename`。
*   `TypeParameter1, TypeParameter2, ...`: 类型参数列表，用逗号分隔。 这些类型参数可以在类定义中使用。
*   `ClassName`: 类名。

**例子：一个简单的动态数组类**

```c++
template <typename T>
class DynamicArray {
private:
  T* data;
  int size;
  int capacity;

public:
  DynamicArray(int initialCapacity = 10) : size(0), capacity(initialCapacity) {
    data = new T[capacity];
  }

  ~DynamicArray() {
    delete[] data;
  }

  void push_back(const T& value) {
    if (size == capacity) {
      // 扩容
      capacity *= 2;
      T* newData = new T[capacity];
      for (int i = 0; i < size; ++i) {
        newData[i] = data[i];
      }
      delete[] data;
      data = newData;
    }
    data[size++] = value;
  }

  T& operator[](int index) {
    if (index < 0 || index >= size) {
      throw std::out_of_range("Index out of bounds");
    }
    return data[index];
  }

  int getSize() const {
    return size;
  }
};

int main() {
  DynamicArray<int> intArray;
  intArray.push_back(1);
  intArray.push_back(2);
  intArray.push_back(3);

  std::cout << "Int Array Size: " << intArray.getSize() << std::endl; // 输出 Int Array Size: 3
  std::cout << "Int Array[0]: " << intArray[0] << std::endl;        // 输出 Int Array[0]: 1

  DynamicArray<double> doubleArray;
  doubleArray.push_back(3.14);
  doubleArray.push_back(2.71);

  std::cout << "Double Array Size: " << doubleArray.getSize() << std::endl; // 输出 Double Array Size: 2
  std::cout << "Double Array[1]: " << doubleArray[1] << std::endl;      // 输出 Double Array[1]: 2.71

  return 0;
}
```

在这个例子中，`DynamicArray` 是一个类模板。 `typename T` 表示 `T` 是一个类型参数，可以用来指定数组中存储的数据类型。  `DynamicArray<int>` 创建一个存储整数的动态数组，而 `DynamicArray<double>` 创建一个存储双精度浮点数的动态数组。

#### 模板参数

模板参数可以是：

*   **类型参数 (Type Parameters)**: 用 `typename` 或 `class` 声明，例如 `typename T`。
*   **非类型参数 (Non-Type Parameters)**: 可以是整数、枚举、指针或引用等。  例如 `template <int N>`，这里 `N` 就是一个非类型参数。
*   **模板参数 (Template Parameters)**：模板本身可以作为另一个模板的参数。

**3.1 非类型模板参数**

非类型模板参数允许你在编译时指定一个常量值。

**例子：固定大小的数组**

```c++
template <typename T, int N>
class FixedSizeArray {
private:
  T data[N];
public:
  T& operator[](int index) {
    if (index < 0 || index >= N) {
      throw std::out_of_range("Index out of bounds");
    }
    return data[index];
  }
};

int main() {
  FixedSizeArray<int, 5> intArray;
  intArray[0] = 10;
  std::cout << intArray[0] << std::endl; // 输出 10
  return 0;
}
```

在这个例子中，`N` 是一个非类型模板参数，它指定了数组的大小。  `FixedSizeArray<int, 5>` 创建一个可以存储 5 个整数的固定大小的数组。

**3.2 模板参数作为模板参数**

模板参数本身也可以是另一个模板，这允许你创建更复杂和灵活的数据结构。

**例子：存储一个 `std::vector` 的 `std::list`**

```c++
#include <vector>
#include <list>
#include <iostream>

template <typename T>
void printList(const std::list<T>& lst) {
    for (const auto& element : lst) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}


int main() {
    // Create a list of vectors of integers
    std::list<std::vector<int>> listOfVectors;

    // Add some vectors to the list
    listOfVectors.push_back({1, 2, 3});
    listOfVectors.push_back({4, 5, 6, 7});
    listOfVectors.push_back({8, 9});

    // Iterate through the list and print each vector
    for (const auto& vec : listOfVectors) {
        std::cout << "Vector elements: ";
        for (int element : vec) {
            std::cout << element << " ";
        }
        std::cout << std::endl;
    }

    std::list<int> myList = {10, 20, 30, 40, 50};
    printList(myList);

    return 0;
}
```

#### 模板实例化

模板本身不是真正的类或函数。 只有当你使用具体的类型参数来实例化模板时，编译器才会生成实际的代码。 模板实例化可以分为两种：

*   **隐式实例化 (Implicit Instantiation)**: 当你使用模板时，编译器会自动推断类型参数并生成代码。 例如，`max(x, y)` 会隐式地实例化 `max<int>(int a, int b)`。
*   **显式实例化 (Explicit Instantiation)**: 你可以显式地告诉编译器为一个特定的类型生成模板代码。 例如，`template int max<int>(int a, int b);` 会显式地实例化 `max<int>(int a, int b)`。

**显式实例化例子:**

```c++
template <typename T>
T min(T a, T b) {
  return (a < b) ? a : b;
}

// 显式实例化 min<double>(double a, double b)
template double min<double>(double a, double b);

int main() {
  // 你仍然可以使用隐式实例化
  std::cout << min(5, 10) << std::endl; // 输出 5 (int)

  // 使用显式实例化
  double p = 3.14, q = 2.71;
  std::cout << min<double>(p, q) << std::endl; // 输出 2.71 (double)

  return 0;
}
```

#### 模板特化 (Template Specialization)

模板特化允许你为特定的类型参数组合提供不同的模板实现。 这在你需要为某些类型提供优化或特殊处理时非常有用。

**5.1 函数模板特化**

你可以为特定的类型提供不同的函数模板实现。

**例子：为 `char*` 类型的 `max` 函数提供特殊处理**

```c++
#include <cstring> // for strcmp

template <typename T>
T max(T a, T b) {
  return (a > b) ? a : b;
}

// 函数模板特化：为 char* 类型提供特殊处理
template<>
const char* max<const char*>(const char* a, const char* b) {
  return (std::strcmp(a, b) > 0) ? a : b;
}

```

### Struct

**1. `struct`（结构体）**

*   **定义：** `struct` 是一种用户自定义的数据类型，它可以将多个不同类型的变量组合在一起，形成一个复合数据类型。`struct` 中的成员变量可以是基本数据类型（如 `int`、`float`、`char`），也可以是其他用户自定义类型（如 `class`、`struct`）。

*   **语法：**

    ```c++
    struct 结构体名 {
        成员变量类型 成员变量名1;
        成员变量类型 成员变量名2;
        // ...
    }; // 注意分号
    ```

    例如：

    ```c++
    struct Point {
        int x;
        int y;
    };
    ```

*   **使用：**

    *   **创建结构体变量：**

        ```c++
        Point p1; // 创建一个 Point 类型的变量 p1
        ```

    *   **访问结构体成员：** 使用 `.` 运算符访问结构体成员。

        ```c++
        p1.x = 10; // 设置 p1 的 x 坐标为 10
        p1.y = 20; // 设置 p1 的 y 坐标为 20
        cout << "x = " << p1.x << ", y = " << p1.y << endl; // 输出 p1 的 x 和 y 坐标
        ```

*   **初始化：**

    *   **默认初始化：** 如果没有显式初始化，结构体成员将使用默认值初始化（例如，`int` 类型默认为 0）。
    *   **列表初始化：**

        ```c++
        Point p2 = {30, 40}; // 使用列表初始化 p2
        ```

    *   **指定成员初始化（C++20）：**

        ```c++
        Point p3{.x = 50, .y = 60}; // 使用指定成员初始化 p3
        ```

**2. `struct` 与 `class` 的区别**

*   **默认访问权限（Default Access）：**
    *   `struct`：成员变量的默认访问权限是 `public`（公共的）。
    *   `class`：成员变量的默认访问权限是 `private`（私有的）。

*   **继承时的默认访问权限：**
    *   `struct`：默认是 public 继承。
    *   `class`：默认是 private 继承。

*   **其他方面：**

    * 在 C++ 中，`struct` 默认不包含 Member Function

### 类 ->面向对象

#### Copy Constructor vs Assignment Operator & Rule of Three

**1. Copy Constructor vs Assignment Operator**

|**对比项**|**拷贝构造函数**|**赋值运算符**|
|---|---|---|
|**作用**|用于创建新对象并复制|用于已有对象的赋值|
|**调用时机**|初始化对象时|赋值操作时|
|**默认实现**|逐成员拷贝|逐成员赋值|
|**是否释放旧资源**|否（对象是新创建的）|是（必须释放旧资源）|

==拷贝构造函数（Copy Constructor）==

- **定义**：  
拷贝构造函数用于**创建新对象**并将另一个对象的值复制到新对象中。

- **语法**：

```cpp
ClassName(const ClassName& other);
````

- **调用时机**：

- 通过 `ClassName obj2 = obj1;` 进行对象初始化时。
- 通过 `ClassName obj2(obj1);` 进行对象初始化时。
- 当对象按**值传递**或**按值返回**时。

**示例**：

```cpp
class Example {
public:
    int* data;
    
    // 拷贝构造函数
    Example(const Example& other) {
        data = new int(*other.data);
    }
};
```

---

==2. 赋值运算符（Assignment Operator）==

- **定义**： 赋值运算符用于**将一个已经存在的对象**的值赋给另一个**已经存在的对象**。

- **语法**：

```cpp
ClassName& operator=(const ClassName& other);
```

- **调用时机**：

- `obj1 = obj2;`（`obj1` 已经存在，给它赋值）

- **示例**：

```cpp
class Example {
public:
    int* data;
    
    // 赋值运算符
    Example& operator=(const Example& other) {
        if (this != &other) { // 防止自赋值,常见的代码流程
            delete data; // 释放旧资源！！重要
            data = new int(*other.data);
        }
        return *this;
    }
};
```

---
**2. Rule of Three（三法则）**

**三法则（Rule of Three）** 指的是如果一个类需要**显式定义**以下三者之一，则很可能需要显式定义另外两个：

1. **拷贝构造函数**
2. **赋值运算符**
3. **析构函数**

 **为什么需要三法则？**

当类涉及**动态内存分配**或其他**资源管理**（如文件句柄、互斥锁），默认的拷贝构造、赋值运算符只会**浅拷贝**，导致资源重复释放（如 `delete` 两次）或悬挂指针（dangling pointer）。

**示例：违反三法则的类**

```cpp
class BadExample {
public:
    int* data;

    BadExample(int value) { data = new int(value); }
    ~BadExample() { delete data; }  // 需要释放资源

    // 但是没有提供拷贝构造和赋值运算符，导致浅拷贝问题
};

void test() {
    BadExample obj1(10);
    BadExample obj2 = obj1;  // 这里调用默认拷贝构造，data 指针被浅拷贝！
    obj2 = obj1;  // 这里调用默认赋值运算符，data 指针被浅拷贝！
}  // obj1 和 obj2 都会调用析构函数，导致 delete 两次，程序崩溃！
```

**正确实现（遵循三法则）**

```cpp
class GoodExample {
public:
    int* data;

    // 构造函数
    GoodExample(int value) { data = new int(value); }

    // 拷贝构造函数
    GoodExample(const GoodExample& other) {
        data = new int(*other.data);
    }

    // 赋值运算符
    GoodExample& operator=(const GoodExample& other) {
        if (this != &other) {
            delete data;  // 释放旧资源
            data = new int(*other.data);
        }
        return *this;
    }

    // 析构函数
    ~GoodExample() { delete data; }
};
```

### 函数

#### 参数传递

> [!tip] Pass by Value, Pass by Reference, Pass by Pointers

**1. 概念对比**

| 特性               | 值传递 (Pass by Value) | 引用传递 (Pass by Reference) | 指针传递 (Pass by Pointer) |
| ---------------- | ------------------- | ------------------------ | ---------------------- |
| **传递内容**         | 实参的副本               | 实参的别名                    | 实参的地址                  |
| **修改实参**         | 否                   | 是                        | 是                      |
| **空值**           | 不可能                 | 不可能                      | 可能 (空指针)               |
| **开销**           | 较大 (复制对象)           | 较小 (无复制)                 | 较小 (复制地址)              |
| **安全性**          | 高 (不修改实参)           | 中                        | 低 (可能空指针)              |
| Copy Constructor | 调用，构造创建对象的副本        | 不调用，因为传递的是对象的别名          | 不调用，因为传递的是对象的地址        |

**2. 详细解释**

*   **值传递 (Pass by Value)**

    *   **传递内容:** 函数接收的是实参的一个副本，这个副本会在函数内部被当作一个新的变量使用。
    *   **修改实参:** 由于函数操作的是实参的副本，因此对形参的任何修改都不会影响到原始的实参。
    *   **空值:** 不存在空值的情况，因为传递的是一个实际的值，而不是地址或引用。
    *   **开销:** 当传递的对象很大时，值传递会产生较大的开销，因为需要复制整个对象。
    *   **安全性:** 值传递是三种方式中最安全的，因为它不会修改实参。

*   **引用传递 (Pass by Reference)**

    *   **传递内容:** 函数接收的是实参的别名，形参和实参指向的是同一块内存空间。
    *   **修改实参:** 对形参的修改会直接影响到原始的实参，因为它们实际上是同一个变量的不同名称。
    *   **空值:** 不存在空引用的情况，引用必须在声明时初始化，并且不能为 `NULL`。
    *   **开销:** 引用传递的开销很小，因为它不需要复制对象，只需要传递对象的引用。
    *   **安全性:** 引用传递相对安全，因为不存在空引用。

*   **指针传递 (Pass by Pointer)**

    *   **传递内容:** 函数接收的是实参的地址，形参是一个指针，指向实参的内存空间。
    *   **修改实参:** 通过解引用指针，可以修改指针指向的内存空间，从而修改原始的实参。
    *   **空值:** 指针可以为空，如果传递的是空指针，则需要进行判空处理，否则可能会导致程序崩溃。
    *   **开销:** 指针传递的开销较小，因为它只需要复制地址，而不需要复制对象。
    *   **安全性:** 指针传递的安全性较低，因为可能存在空指针，并且可以通过指针修改任意内存空间。

**3. 代码示例**

```cpp
#include <iostream>

using namespace std;

// 值传递
void modifyValue(int x) {
    x = 10; // 修改的是 x 的副本，不会影响实参
    cout << "Inside modifyValue: x = " << x << endl;
}

// 引用传递
void modifyReference(int &x) {
    x = 20; // 修改的是 x 的别名，会影响实参
    cout << "Inside modifyReference: x = " << x << endl;
}

// 指针传递
void modifyPointer(int *x) {
    if (x != nullptr) { // 检查指针是否为空
        *x = 30; // 通过解引用指针，修改实参
        cout << "Inside modifyPointer: *x = " << *x << endl;
    } else {
        cout << "Error: Null pointer!" << endl;
    }
}

int main() {
    int a = 1;

    cout << "Before modifyValue: a = " << a << endl;
    modifyValue(a);
    cout << "After modifyValue: a = " << a << endl;

    cout << "Before modifyReference: a = " << a << endl;
    modifyReference(a);
    cout << "After modifyReference: a = " << a << endl;

    cout << "Before modifyPointer: a = " << a << endl;
    modifyPointer(&a);
    cout << "After modifyPointer: a = " << a << endl;

    // 指针传递空指针示例
    int *ptr = nullptr;
    modifyPointer(ptr);

    return 0;
}
```

> [!tip] Const 关键字

**1. `const` 成员函数 (Const Member Functions)**

`const` 成员函数是指在类中声明为 `const` 的成员函数。它承诺**不会修改调用它的对象的状态**，即不会修改对象的任何非 `mutable` 成员变量。

*   **声明方式:**

    ```cpp
    class MyClass {
    public:
        returnType functionName(parameterList) const;
    };
    ```

    `const` 关键字放在函数声明的末尾，在参数列表之后。**在 `.cpp` `.h` 文件中均需要声明标注，在 `.cpp` 文件中写在函数体前**

*   **限制:**

    *   `const` 成员函数不能修改对象的任何非 `mutable` 成员变量。试图修改会导致编译错误。
    *   `const` 成员函数只能调用其他 `const` 成员函数（或非成员的 `const` 正确的函数）。它们不能调用非 `const` 成员函数，因为非 `const` 成员函数可能会修改对象的状态。

**2. 哪些函数可以访问 `const` 变量 (Const Objects' Member Variables)**


*   `const` 对象只能调用 `const` 成员函数。
* 非 `const` 对象可以调用任何成员函数（包括 `const` 和非 `const` 函数）。
*   `const` 成员函数可以访问任何对象的成员变量，但不能修改它们（除非使用 `mutable` 关键字）。

**3. 代码示例**

```cpp
#include <iostream>

class MyClass {
private:
    int value;
    mutable int accessCount; // mutable 成员变量可以在 const 成员函数中修改

public:
    MyClass(int val) : value(val), accessCount(0) {}

    // const 成员函数，用于获取 value 的值
    int getValue() const {
        accessCount++; // 允许修改 mutable 成员变量
        std::cout << "getValue() const called. Access count: " << accessCount << std::endl;
        return value;
    }

    // 非 const 成员函数，用于设置 value 的值
    void setValue(int val) {
        value = val;
        std::cout << "setValue() called." << std::endl;
    }

    void print() const {
        std::cout << "Value: " << value << ", Access Count: " << accessCount << std::endl;
    }
};

int main() {
    MyClass obj(10); // 非 const 对象
    std::cout << "Initial value: " << obj.getValue() << std::endl; // 调用 const 成员函数
    obj.setValue(20); // 调用非 const 成员函数
    std::cout << "New value: " << obj.getValue() << std::endl; // 再次调用 const 成员函数
    obj.print();

    const MyClass constObj(30); // const 对象
    std::cout << "Const object value: " << constObj.getValue() << std::endl; // 调用 const 成员函数
    //constObj.setValue(40); // 错误：const 对象不能调用非 const 成员函数
    constObj.print();

    return 0;
}
```

#### 返回值

> [!tip] Return by Value, Reference, Pointer

**1. 返回值传递 (return by value):**

* **机制:** 函数创建一个返回值的副本，并将这个副本复制给调用者。
* **效率:**  对于小型数据类型（例如 int, float），效率很高。但对于大型对象或自定义类，效率较低，因为需要进行对象的完整复制，这会消耗大量的时间和内存。
* **安全性:**  最安全的方式，因为调用者获得的是返回值的副本，不会直接修改函数内部的原始数据。  函数内部的改变不会影响到外部变量。
* **使用场景:**  适合返回小型数据类型或不需要修改返回值的情况。  如果返回值是大型对象且不需要修改，则可能需要考虑效率问题。


**2. 返回引用传递 (return by reference):**

* **机制:** 函数返回一个引用 (reference)，它指向函数内部已存在的对象。调用者直接操作的是这个对象本身，而不是它的副本。
* **效率:**  最高效的方式，因为避免了对象的复制。
* **安全性:**  潜在风险最高。如果函数**返回局部变量的引用，则在函数结束后，局部变量被销毁，引用就变成了悬空指针 (dangling reference)，访问它会导致程序崩溃**。  如果返回的引用指向的对象被外部修改，则函数内部的对象也会被修改。
* **使用场景:**  适合返回函数内部已存在的对象，并且允许调用者修改该对象的情况。  必须**确保返回的引用指向的对象在函数结束后仍然存在。  经常用于返回容器元素的引用或修改类成员函数的返回值**。


**3. 返回指针传递 (return by pointer):**

* **机制:** 函数返回一个指针，指向函数内部已存在的对象。调用者通过指针间接访问该对象。
* **效率:**  与引用传递类似，高效，避免了对象的复制。
* **安全性:**  与引用传递类似，也存在潜在风险。  **如果返回局部变量的指针，则在函数结束后，局部变量被销毁，指针就变成了悬空指针 (dangling pointer)，访问它会导致程序崩溃。  函数内部对象的修改，会影响外部指针指向的对象**。
* **使用场景:**  类似于引用传递，适合返回函数内部已存在的对象，并且允许调用者修改该对象的情况。  也**必须确保返回的指针指向的对象在函数结束后仍然存在**。通常用于动态内存分配，指针指向堆上的对象，调用者需要**负责释放内存**。

### Reference

There shall be no **references to references, no arrays of references, and no pointers to references. References are not objects. They do not occupy memory. — Declaring an array of nothing**

## Polymorphism 多态性

### 虚函数

**1. Virtual Function（虚函数）**

*   **定义**：Virtual Function 是在基类（Base Class）中声明的函数，使用 `virtual` 关键字修饰。它允许在派生类（Derived Class）中重写（Override）该函数，实现运行时多态性。

*   **作用**：Virtual Function 的主要作用是允许通过基类指针或引用调用派生类中重写的函数。

- **重载调用时机**
1. **Inheritance（继承）**：必须存在继承关系，即派生类继承自基类。
2. **Override（重写）**：派生类必须重写（Override）基类的 Virtual Function。
3. **Pointer or Reference（指针或引用）**：必须使用**基类的指针或引用来调用 Virtual Function(即用基类的指针或引用指向继承类的对象)**，注意如果只是基类的对象并不会调用派生类中的 Virtual Function。

```c++
#include <iostream>

class Base {
public:
    virtual void print() {
        std::cout << "Base class print" << std::endl;
    }
};

class Derived : public Base {
public:
    void print() override { // 重写基类的 virtual function
        std::cout << "Derived class print" << std::endl;
    }
};

int main() {
    Base* basePtr = new Base();
    Base* derivedPtr = new Derived();
    Derived* derivedPtr2 = new Derived();

    // 1. 使用基类指针指向基类对象
    basePtr->print(); // 输出 "Base class print"

    // 2. 使用基类指针指向派生类对象
    derivedPtr->print(); // 输出 "Derived class print" (多态)

    // 3. 使用派生类指针指向派生类对象
    derivedPtr2->print(); // 输出 "Derived class print"

    delete basePtr;
    delete derivedPtr;
    delete derivedPtr2;

    return 0;
}

```

**2. Pure Virtual Function（纯虚函数）**

*   **定义**：Pure Virtual Function 是一种特殊的 Virtual Function，在基类中声明时被赋值为 0。**包含 Pure Virtual Function 的类被称为 Abstract Class（抽象类）**。

*   **作用**：
    *   **Abstract Class 不能被实例化（创建对象）**。
    *   **派生类必须重写基类中的所有 Pure Virtual Function，才能被实例化**。

*   **示例**：

    ```cpp
    class Shape {
    public:
        virtual double getArea() = 0; // 纯虚函数
    };

    class Circle : public Shape {
    private:
        double radius;
    public:
        Circle(double r) : radius(r) {}
        double getArea() override {
            return 3.14159 * radius * radius;
        }
    };

    int main() {
        // Shape shape; // 错误：不能实例化抽象类
        Circle circle(5.0);
        std::cout << "Area of circle: " << circle.getArea() << std::endl; // 输出圆的面积
        return 0;
    }
    ```

**3. Why Constructor Cannot Be Virtual Function（为什么构造函数不能是虚函数）**

*   **原因**：
    *   **构造函数的职责**：构造函数的职责是创建并初始化对象。Virtual Function 的调用依赖于对象的 Virtual Table（虚函数表），而 Virtual Table 是在对象构造完成后才存在的。
    *   **对象类型不确定**：在构造对象时，对象的类型是确定的。Virtual Function 的目的是实现运行时多态性，允许在不知道对象具体类型的情况下调用相应的函数。但是，**构造函数必须知道对象的具体类型才能正确地创建对象**。
    *   **构造顺序**：**对象的构造是从基类到派生类的顺序进行的。如果构造函数是 Virtual Function，那么在构造基类对象时，就无法确定调用哪个派生类的构造函数**。

### 派生类继承 & constructor

- **Constructor 调用顺序:** 从 Base 到 Derived
- **Destructor 调用顺序:** 从 Derived 到 Base

**调用基类构造函数的方法：**

主要有两种方式：隐式调用和显式调用。

*   **1. 隐式调用（Implicit Call）：**

    *   **条件:** 基类有 *无参构造函数*（默认构造函数）。

    *   **行为:** 如果派生类构造函数没有在初始化列表中显式调用基类构造函数，编译器会自动在派生类构造函数体执行之前调用基类的 *无参构造函数*。

    *   **代码示例:**

        ```c++
        class Base {
        public:
            Base() {
                data = 0; // 默认初始化
                cout << "Base constructor called" << endl;
            }
        private:
            int data;
        };

        class Derived : public Base {
        public:
            Derived() { // 没有显式调用 Base 构造函数
                extraData = 10;
                cout << "Derived constructor called" << endl;
            }
        private:
            int extraData;
        };

        int main() {
            Derived d; // 先输出 "Base constructor called"，再输出 "Derived constructor called"
        }
        ```

==缺点: 如果基类 没有*无参构造函数*，则会发生编译错误。==

*   **2. 显式调用（Explicit Call）：**

    *   **方法:** 在派生类构造函数的*初始化列表*中调用基类构造函数。

    *   **语法:**

        ```c++
        Derived(参数列表) : Base(基类构造函数参数), 派生类成员初始化 {
            // 派生类构造函数体
        }
        ```

    *   **代码示例:**

        ```c++
        class Base {
        public:
            Base(int value) : data(value) { // 有参构造函数
                cout << "Base constructor called with value: " << value << endl;
            }
        private:
            int data;
        };

        class Derived : public Base {
        public:
            Derived(int value, int extra) : Base(value), extraData(extra) { // 显式调用 Base(value)
                cout << "Derived constructor called with extra: " << extra << endl;
            }
        private:
            int extraData;
        };

        int main() {
            Derived d(5, 10); // 输出 "Base constructor called with value: 5"，再输出 "Derived constructor called with extra: 10"
        }
        ```

    *   **优点:**
        * 可以传递参数给基类的有参构造函数，进行定制初始化。
        * 即使基类有无参构造函数，显式调用也能更清晰地表达初始化意图。
        *   *必须* 在基类没有无参构造函数的情况下使用。

**注意事项：**

*   **初始化列表的顺序:** 初始化列表的执行顺序与成员变量*声明*的顺序有关，而不是与初始化列表的顺序有关。基类的初始化总是先于派生类的初始化。

*   **构造函数调用链:** 如果存在多层继承（例如，A -> B -> C），则构造函数会形成一个调用链，从最顶层的基类开始，逐级向下初始化。

### 类继承权限

**总结表:**

| Inheritance Type | Base Class `public` | Base Class `protected` | Base Class `private` | Outside the `Derived` Class |
|--------------------|----------------------|-------------------------|------------------------|-----------------------------|
| `public`          | `public`             | `protected`             | Inaccessible           | Accessible                    |
| `protected`       | `protected`          | `protected`             | Inaccessible           | Inaccessible                    |
| `private`         | `private`            | `private`               | Inaccessible           | Inaccessible                    |

**重要提示:**

* 无论哪种继承方式，基类的 `private` 成员始终无法在派生类中直接访问。
* 访问权限只影响编译时的检查。 运行时，如果使用基类指针或引用指向派生类对象，仍然可以通过虚函数实现多态性。
* 默认情况下，如果省略继承方式，则默认为 `private` 继承 (对于 `class` 关键字定义的类) 或 `public` 继承 (对于 `struct` 关键字定义的结构体)。



**1. Public Inheritance (公有继承):**

*   **语法:** `class Derived : public Base { ... };`
*   **访问规则:** 这是最常见的继承方式，它尽可能地保留了基类成员的访问权限。
    *   `public` 成员在派生类中仍然是 `public`。
    *   `protected` 成员在派生类中仍然是 `protected`。
    *   `private` 成员在派生类中**不可访问** (在派生类内部，包括成员函数，都无法直接访问基类的 `private` 成员)。

*   **总结:** 基类成员的访问权限在派生类中保持不变（除了 `private` 成员）。 派生类的对象可以访问从基类继承的 `public` 成员。
*   **例子:**

    ```c++
    class Base {
    public:
        int publicVar = 1;
    protected:
        int protectedVar = 2;
    private:
        int privateVar = 3;
    };

    class Derived : public Base {
    public:
        void accessBaseMembers() {
            cout << "Public: " << publicVar << endl;      // OK
            cout << "Protected: " << protectedVar << endl;   // OK
            // cout << "Private: " << privateVar << endl;   // Error: cannot access private member
        }
    };

    int main() {
        Derived d;
        cout << "Public from object: " << d.publicVar << endl;  // OK
        // cout << "Protected from object: " << d.protectedVar << endl; // Error: protected member
        // cout << "Private from object: " << d.privateVar << endl;   // Error: private member
        return 0;
    }
    ```

**2. Protected Inheritance (保护继承):**

*   **语法:** `class Derived : protected Base { ... };`
*   **访问规则:**  限制了基类成员的外部访问权限。
    *   `public` 成员在派生类中变为 `protected`。
    *   `protected` 成员在派生类中仍然是 `protected`。
    *   `private` 成员在派生类中**不可访问**。

*   **总结:** 基类的 `public` 成员在派生类中被降级为 `protected`。 派生类的对象**不能**直接访问从基类继承的成员（即使是 `public` 成员）。  `protected` 继承通常用于实现更严格的封装，隐藏基类的接口。
*   **例子:**

    ```c++
    class Base {
    public:
        int publicVar = 1;
    protected:
        int protectedVar = 2;
    private:
        int privateVar = 3;
    };

    class Derived : protected Base {
    public:
        void accessBaseMembers() {
            cout << "Public: " << publicVar << endl;      // OK (在派生类内部可以访问)
            cout << "Protected: " << protectedVar << endl;   // OK
            // cout << "Private: " << privateVar << endl;   // Error: cannot access private member
        }
    };

    int main() {
        Derived d;
        // cout << "Public from object: " << d.publicVar << endl;  // Error: publicVar is protected
        // cout << "Protected from object: " << d.protectedVar << endl; // Error: protected member
        // cout << "Private from object: " << d.privateVar << endl;   // Error: private member
        return 0;
    }
    ```

**3. Private Inheritance (私有继承):**

*   **语法:** `class Derived : private Base { ... };`
*   **访问规则:** 这是最严格的继承方式，它完全隐藏了基类的接口。
    *   `public` 成员在派生类中变为 `private`。
    *   `protected` 成员在派生类中变为 `private`。
    *   `private` 成员在派生类中**不可访问**。

*   **总结:** 基类的所有成员（除了 `private` 成员）在派生类中都变为 `private`。 派生类的对象**不能**直接访问从基类继承的成员。  派生类可以访问基类的 `public` 和 `protected` 成员，但是这种访问仅限于派生类的内部。 私有继承通常用于实现组合 (composition) 关系，而不是 "is-a" 关系。 派生类仅仅是利用基类的实现，而不想暴露基类的接口。
*   **例子:**

    ```c++
    class Base {
    public:
        int publicVar = 1;
    protected:
        int protectedVar = 2;
    private:
        int privateVar = 3;
    };

    class Derived : private Base {
    public:
        void accessBaseMembers() {
            cout << "Public: " << publicVar << endl;      // OK (在派生类内部可以访问，但现在是 private)
            cout << "Protected: " << protectedVar << endl;   // OK (在派生类内部可以访问，但现在是 private)
            // cout << "Private: " << privateVar << endl;   // Error: cannot access private member
        }
    };

    int main() {
        Derived d;
        // cout << "Public from object: " << d.publicVar << endl;  // Error: publicVar is private
        // cout << "Protected from object: " << d.protectedVar << endl; // Error: protected member
        // cout << "Private from object: " << d.privateVar << endl;   // Error: private member
        return 0;
    }
    ```

### 运算符重载

运算符重载允许你为自定义类型重新定义标准运算符。 这使得自定义类型的使用更加直观，像内置类型一样。 本质上，运算符重载就是一种多态性，因为同一个运算符可以对不同类型的数据进行操作。

**Syntax**  
运算符重载本质上就是定义一个名为 `operator<operator>` 的成员函数或友元函数。 `<operator>` 代表你要重载的运算符符号。

```c++
#include <iostream>

class Complex {
public:
  double real;
  double imag;

  Complex(double r = 0, double i = 0) : real(r), imag(i) {}

  Complex operator+(const Complex& other) const {
    return Complex(real + other.real, imag + other.imag);
  }

  Complex operator-(const Complex& other) const {
      return Complex(real - other.real, imag - other.imag);
  }

  void print() const {
    std::cout << real << " + " << imag << "i\n";
  }
};


int main() {
  Complex c1(2, 3);
  Complex c2(4, -1);
  Complex c3 = c1 + c2; // 使用 + 运算符
  Complex c4 = c1 - c2; // 使用 - 运算符
  c3.print(); // Output: 6 + 2i
  c4.print(); // Output: -2 + 4i
  return 0;
}
```

这里，我们重载了 `+` 和 `-` 运算符，使它们能够对 `Complex` 对象进行加减运算。  `operator+` 和 `operator-` 函数的实现定义了运算符的行为。


**总结:**

C++ 的多态性使得代码更具可重用性、可扩展性和可维护性。通过继承和虚函数，你可以用统一的接口操作不同类型的对象，从而简化代码并降低耦合度。  运算符重载是多态性的一个特例，它使自定义类型更加易于使用，并提高了代码的可读性。  记住，虚函数是实现运行时多态性的关键，而运算符重载则增强了自定义类型的表达能力。  需要谨慎设计，避免重载运算符导致代码难以理解。
