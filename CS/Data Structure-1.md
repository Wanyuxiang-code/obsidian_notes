---
title: Data Structure
date: 2025-03-11
date modified: 2025-03-27
categories: CS225
tags: [CS225]
---

#CS225 

## Storage Design

**核心概念：**

在 C++ 等编程语言中，当我们创建一个变量并存储数据时，需要决定如何将这个数据存储在内存中。 这三种 " 存储方式 " 决定了变量如何与内存中的实际数据关联起来。

**1. 存储方式：引用 (Storage by Reference)**

*   **定义：** 引用就像是给已存在的变量起一个别名。它 *不是* 一个独立的变量，而是 *直接* 指向原始变量的内存地址。  一旦引用被绑定到一个变量，它就 *永远* 指向那个变量。

*   **特点：**

    *   **不占用额外内存：** 引用本身不占用额外的存储空间，它只是原始变量的另一个名字。
    *   **必须初始化：** 引用在声明时 *必须* 初始化，因为你必须告诉它要 " 引用 " 哪个已存在的变量。
    *   **不可重新绑定：** 一旦引用被初始化，它就 *不能* 改变引用的对象。  它始终指向最初绑定的变量。
    *   **修改影响原始变量：** 通过引用修改数据，会 *直接* 修改原始变量。因为引用只是原始变量的别名。

*   **示例 (C++):**

    ```c++
    int x = 10;
    int& ref = x; // ref 是 x 的引用

    ref = 20; // 修改 ref 的值，x 的值也会变为 20

    std::cout << "x: " << x << std::endl; // 输出: x: 20
    std::cout << "ref: " << ref << std::endl; // 输出: ref: 20
    ```

*   **使用场景：**

    * 当你想在函数中修改实参的值时（避免复制）。
    * 当你想用更简洁的语法来访问一个复杂的对象时。

**2. 存储方式：指针 (Storage by Pointer)**

*   **定义：** 指针是一个变量，它存储的是 *另一个变量的内存地址*。  指针本身有自己的内存地址，它存储的内容是 *目标变量的地址*。

*   **特点：**

    *   **占用额外内存：** 指针变量 *占用* 存储地址所需的内存空间（通常是 4 或 8 字节，取决于系统架构）。
    *   **可以不初始化：** 指针可以先声明，后初始化。  你可以先创建一个指针变量，然后再让它指向某个变量的地址。
    *   **可以重新绑定：** 指针可以改变指向的变量。 你可以让一个指针先指向变量 A 的地址，然后再指向变量 B 的地址。
    *   **需要解引用访问数据：** 要访问指针指向的数据，需要使用解引用操作符 `*`。
    *   **可以指向 `NULL`：** 指针可以被赋值为 `NULL`（或 `nullptr` 在 C++11 及以后），表示它当前不指向任何有效的内存地址。

*   **示例 (C++):**

    ```c++
    int x = 10;
    int* ptr = &x; // ptr 存储 x 的地址 (& 是取地址操作符)

    *ptr = 20; // 通过 ptr 修改 x 的值

    std::cout << "x: " << x << std::endl; // 输出: x: 20
    std::cout << "*ptr: " << *ptr << std::endl; // 输出: *ptr: 20
    std::cout << "ptr: " << ptr << std::endl; // 输出: ptr: x 的内存地址
    ```

*   **使用场景：**

    * 动态内存分配（`new` 和 `delete`）。
    * 在函数中修改实参的值。
    * 实现链表、树等复杂的数据结构。
    * 函数指针（指向函数的指针）。

**3. 存储方式：值 (Storage by Value)**

*   **定义：** 值存储方式是指将数据的 *实际内容* 存储在变量的内存空间中。  当你将一个变量的值赋给另一个变量时，会创建一个 *副本*。

*   **特点：**

    *   **占用相应大小的内存：** 变量占用的内存大小取决于数据的类型。
    *   **修改不影响原始数据：** 修改一个变量的值， *不会* 影响原始数据，因为你操作的是一个副本。
    *   **简单直接：** 使用起来最简单，不需要额外的操作符（如 `*` 或 `&`）。
    *   **不能为 `NULL`：** 值本身必须是一个实际的值，不能表示 " 空 " 或 " 不存在 "。

*   **示例 (C++):**

    ```c++
    int x = 10;
    int y = x; // y 的值是 x 的一个副本

    y = 20; // 修改 y 的值，x 的值不会改变

    std::cout << "x: " << x << std::endl; // 输出: x: 10
    std::cout << "y: " << y << std::endl; // 输出: y: 20
    ```

*   **使用场景：**

    * 当数据量小，并且不需要修改原始数据时。
    * 当需要确保数据独立性时。
    * 通常用于基本数据类型（`int`, `float`, `char`, `bool` 等）。

**总结对比：**

| 特性         | 引用 (Reference) | 指针 (Pointer)           | 值 (Value)  |
| ---------- | -------------- | ---------------------- | ---------- |
| 内存占用       | 无 (别名)         | 有 (存储地址)               | 有 (存储数据本身) |
| 初始化        | 必须初始化          | 可以不初始化                 | 必须初始化      |
| 重新绑定       | 不可重新绑定         | 可以重新绑定                 | 不适用        |
| 解引用访问      | 无需解引用          | 需要解引用 (`*`)            | 无需解引用      |
| 可以为 `NULL` | 不可以            | 可以 (`NULL`, `nullptr`) | 不可以        |
| 修改原始数据     | 会修改            | 视情况而定                  | 不会修改       |
| 数据生命周期     | 依赖原始数据         | 视情况而定                  | 独立         |
| 适用性        | 修改实参，简洁语法      | 动态内存，复杂数据结构            | 小数据，独立性强   |

**实际应用中的选择：**

选择哪种存储方式取决于你的具体需求。

* 如果你想确保函数能够修改实参的值，并且不需要考虑 `NULL` 值，那么引用是一个不错的选择。
* 如果你需要动态分配内存，或者需要表示 " 空 " 的状态，那么指针是必不可少的。
* 如果你只需要数据的副本，并且希望确保数据的独立性，那么值存储是最简单和安全的。

## Iterator & Container

### Iterator

**1. 基本概念**  
"Iterator" 是一种抽象的概念，它提供了一种统一的方式来访问容器中的元素，而无需了解容器的内部结构。"iterator" 可以被看作是一种智能指针，它指向容器中的一个元素，并允许您执行以下操作：

- 访问 "iterator" 指向的元素
- 将 "iterator" 移动到容器中的下一个元素
- 检查 "iterator" 是否已经到达容器的末尾

**2. 相关语法**
- 声明

```c++
std::list<Animal>::iterator it;
```

`container_type::iterator iterator_name;`

- 基本操作

- `*it`：解引用 "iterator"，返回 "iterator" 指向的元素的值。
- `it++`：将 "iterator" 移动到容器中的下一个元素。
- `it--`：将 "iterator" 移动到容器中的上一个元素（仅适用于双向 "iterator" 和随机访问 "iterator"）。
- `it + n`：将 "iterator" 向前移动 n 个元素（仅适用于随机访问 "iterator"）。
- `it - n`：将 "iterator" 向后移动 n 个元素（仅适用于随机访问 "iterator"）。
- `it[n]`：访问 "iterator" 指向的元素之后第 n 个位置的元素（仅适用于随机访问 "iterator"）。
- `it == it2`：比较两个 "iterator" 是否指向同一个位置。
- `it != it2`：比较两个 "iterator" 是否指向不同的位置。
- `it < it2`：比较两个 "iterator" 的位置（仅适用于随机访问 "iterator"）。
- `it > it2`：比较两个 "iterator" 的位置（仅适用于随机访问 "iterator"）。

```c++
#include <iostream>
#include <list>
#include <string>

struct Animal {
    std::string name;
    std::string food;
};

int main() {
    std::list<Animal> zoo;
    zoo.push_back({"giraffe", "leaves"});
    zoo.push_back({"penguin", "fish"});
    zoo.push_back({"bear", "you"});

    for (std::list<Animal>::iterator it = zoo.begin(); it != zoo.end(); ++it) {
        std::cout << it->name << " eats " << it->food << std::endl;
    }

    return 0;
}

```

**3. 不同容器中 Iterator 的行为**

- **Forward Iterators (前向迭代器):**
    
    - **能力:** 只能向前移动 (`operator++`)，可以读取 (`operator*`, `operator->`)，也可以写入 (如果不是 `const` 迭代器)。
    - **关键方法:** `++it`, `it++`, `*it`, `it->`, `it == other`, `it != other`。
    - **典型容器:** `std::forward_list`。

- **Bidirectional Iterators (双向迭代器):**
    
    - **能力:** 具备前向迭代器的所有能力，_并且_ 可以向后移动 (`operator--`)。
    - **新增关键方法:** `--it`, `it--`。
    - **典型容器:** `std::list`, `std::set`, `std::map`, `std::multiset`, `std::multimap`。

- **Random Access Iterators (随机访问迭代器):**
    
    - **能力:** 具备双向迭代器的所有能力，_并且_ 可以进行算术运算，实现跳跃式访问。
    - **新增关键方法:**
        - `it + n` / `n + it`: 向前移动 n 步。
        - `it - n`: 向后移动 n 步。
        - `it - other`: 计算两个迭代器之间的距离。
        - `it[n]`: 访问 `it` 后面第 n 个元素 (等价于 `*(it + n)`)。
        - `it < other`, `it > other`, `it <= other`, `it >= other`: 比较迭代器的位置。
    - **典型容器:** `std::vector`, `std::deque`, `std::array` (以及 C 风格的指针用于数组时)。


**关键点总结:**

- **`begin()` / `end()`:** 这是容器本身的方法，用于获取指向第一个元素的迭代器 (`begin()`) 和指向“末尾之后”位置的迭代器 (`end()`)。所有标准容器都提供。`cbegin()` / `cend()` 是对应的 const 版本，返回 `const_iterator`，不允许通过迭代器修改元素。
- **`operator++` / `operator*` / `operator->` / `operator==` / `operator!=`:** 这些是几乎所有迭代器都支持的最基本操作。
- **`operator--`:** 是区分单向和双向迭代器的关键。
- **`operator+` / `operator-` / `operator[]` / Comparison Operators (`<`, `>` etc.):** 是区分双向和随机访问迭代器的关键。



**4. 自定义实现的 Iterator**

一个 Iterator 常见需要实现的方式:
- `operator++` 指向 container 中下一个元素
- `operator!=,==`
- `operator*`,`operator->` 用来访问当前 iterator 指向的元素

```c++
template <class QE>
class Queue {
public:
    class QueueIterator : public std::iterator<std::bidirectional_iterator_tag, T> {
    public:
        QueueIterator(unsigned index);
        QueueIterator& operator++();
        bool operator==(const QueueIterator &other);
        bool operator!=(const QueueIterator &other);
        QE& operator*();
        QE* operator->();
    private:
        int location_;
        Queue & queue_;
    };

private:
    QE* arr_; // Array based Implementation
    unsigned capacity_, count_, entry_, exit_;
};

```

利用自定义实现的 iterator:

```c++
for (Queue<Animal>::QueueIterator it = zoo.begin(); it != zoo.end(); it++ ) {
    std::cout << (*it).name << " " << (*it).food << std::endl;
}
```

**5. Loop 与 Iterator 的转换**

- **Range-Based loop 与 Iterator**  
Iterator

```c++
for (std::vector<int>::iterator it = myVector.begin(); it != myVector.end(); ++it) {
    std::cout << *it << " ";
}
std::cout << std::endl;

```

Range-Based Loop

```c++
#include <vector>
#include <iostream>

std::vector<int> myVector = {1, 2, 3, 4, 5};

for (int element : myVector) { // 最简洁的形式，会拷贝元素
    std::cout << element << " ";
}
std::cout << std::endl;

// 推荐: 使用 const 引用避免拷贝，如果不需要修改元素
for (const auto& element : myVector) {
    std::cout << element << " ";
}
std::cout << std::endl;

// 如果需要修改元素
for (auto& element : myVector) {
    element *= 2; // Example: double each element
}
for (const auto& element : myVector) { // Print modified vector
    std::cout << element << " ";
}
std::cout << std::endl; // Output: 2 4 6 8 10

```

- **Traditional Loop and Iterator**  
传统的 LOOP 依赖索引，这对于需要通过链表结构的数据结构访问速度非常慢，仅适用于可通过索引直接访问的数据结构

Iterator 可以灵活地封装底层数据接口的访问形式，用户只需要显式使用迭代器即可

### Container

**容器（Container）** 是 C++ STL（标准模板库）中的一个核心概念，它们提供了一种组织和存储数据的方式，并提供了一系列操作数据的方法，比如插入、删除、遍历等。容器大多基于 **模板类（template class）**，可以存储任何类型的元素。

---
**顺序容器（Sequence Containers）**

顺序容器存储数据的方式类似于数组，但提供了更灵活的插入和删除操作。

| 容器                | 特点                                             |
| ----------------- | ---------------------------------------------- |
| `vector<T>`       | **动态数组**，支持 **随机访问（O(1)）**，末尾插入/删除快，但中间插入/删除慢。 |
| `deque<T>`        | **双端队列**，在**头尾插入/删除快**（O(1)），但不适合中间操作。         |
| `list<T>`         | **双向链表**，**中间插入/删除快（O(1)）**，但**随机访问慢（O(n)）**。  |
| `forward_list<T>` | **单向链表**，比 `list` 更节省空间，但只能单向遍历。               |
| `array<T, N>`     | **固定大小的数组**，性能类似 C 数组，不能动态调整大小。                |

---

**容器适配器（Container Adapters）**

**适配器** 是对某些容器的封装，提供特定的行为，如 **栈、队列、优先队列**。

| 适配器                 | 底层实现          | 主要特点            |
| ------------------- | ------------- | --------------- |
| `stack<T>`          | `deque` (默认)  | **后进先出（LIFO）**  |
| `queue<T>`          | `deque` (默认)  | **先进先出（FIFO）**  |
| `priority_queue<T>` | `vector` (默认) | **最大堆（默认）或最小堆** |

## Functor(函数对象)

**1. 基本概念**

函数对象是一个可以像函数一样被调用的对象，它本质上是一个类，重载了函数调用操作符 `operator()`。

- **函数对象的优点**
    
    - **可以保存状态**： 函数对象可以像类一样拥有**成员变量**，用于保存状态。
    - **可以作为参数传递**： 函数对象可以像函数指针一样**作为参数传递**给其他函数。
    - **可以提高代码的可读性**： 函数对象可以将一些复杂的逻辑封装在一个对象中，提高代码的可读性。

**2. 代码示例**

- 基本的 Functor

```c++
#include <iostream>

class Add {
public:
    int operator()(int a, int b) {
        return a + b;
    }
};

int main() {
    Add add;  // 创建仿函数对象
    int result = add(10, 20);  // 调用 operator()
    std::cout << "10 + 20 = " << result << std::endl;
    return 0;
}

```

- 带 Member Variable 的 Functor

```c++
#include <iostream>

class Counter {
private:
    int count;
public:
    Counter() : count(0) {}

    void operator()(const std::string& str) {
        count++;
        std::cout << "调用 " << count << " 次：" << str << std::endl;
    }
};

int main() {
    Counter counter;
    counter("Hello");
    counter("World");
    counter("C++ Functors");

    return 0;
}

```

- Functor 与函数模板的结合

```c++
template<class Iter, class Formatter>
void print(Iter first, Iter second, Formatter printer) {
    while ( first != second ) {
        printer( *first );
        first++;
    }
}
```

```c++
#include <iostream>

// 仿函数：加法
template <typename T>
class Add {
public:
    T operator()(T a, T b) {
        return a + b;
    }
};

// 泛型函数，接受仿函数作为参数
template <typename T, typename Functor>
T calculate(T a, T b, Functor func) {
    return func(a, b);
}

int main() {
    int x = 10, y = 20;
    double p = 1.5, q = 2.5;

    // 传入不同类型的仿函数
    std::cout << "整数加法: " << calculate(x, y, Add<int>()) << std::endl;  // 输出: 30
    std::cout << "浮点加法: " << calculate(p, q, Add<double>()) << std::endl; // 输出: 4.0

    return 0;
}

```

## Array List

### 基本概念

*   **存储方式 (Storage):** 使用一块 **连续的内存空间 (contiguous block of memory)** 来存储元素，就像 C++ 中的普通数组。
*   **核心属性 (Key Properties):**
    *   `array`: 指向动态分配的内存块的指针 (pointer)。
    *   `count` (或 `size`): 当前存储的元素数量。
    *   `capacity`: 已分配内存块总共能容纳的元素数量。
*   **不变量 (Invariant):** $0 \le count \le capacity$。
*   **优点 (Advantage):** 快速的 **随机访问 (Random Access)**。由于内存是连续的，访问任意索引 `i` 的元素 (`array[i]`) 只需要进行指针运算，时间复杂度为 $O(1)$。
*   **缺点 (Disadvantage):** 在列表的开头或中间 **插入 (Insert)** 或 **删除 (Delete)** 元素较慢，因为需要移动后续元素来填充或腾出空间。

---

### 具体操作与时间复杂度 

设 $n$ 为列表中当前的元素数量 (`count`)。

**A. 无序数组列表 (Unsorted Array List)**

元素可以按任意顺序排列。

*   **`insertAtFront(value)`:**
    *   **动作:** 在索引 0 处插入 `value`。
    *   **步骤:**
        1.  **检查扩容 (Resize Check):** 如果 `count == capacity`，执行扩容操作 (见第 3 节)。此步需要 $O(n)$ 时间复制元素。
        2.  **移动 (Shift):** 将所有现有元素 (从索引 `count-1` 到 0) 向右移动一个位置。需要移动 $n$ 个元素。
        3.  **插入:** 将 `value` 放置在 `array[0]`。
        4.  **更新:** `count` 加 1。
    *   **时间复杂度:** 主要开销在于移动元素。**$O(n)$**。（即使发生扩容，也是 $O(n)$，所以整体复杂度不变）。

*   **`insertAtIndex(index, value)`:**
    *   **动作:** 在指定的 `index` 处插入 `value`。
    *   **步骤:**
        1.  **检查扩容:** 如果 `count == capacity`，执行扩容 ($O(n)$)。
        2.  **验证 (Validation):** 检查是否 $0 \le index \le count$。
        3.  **移动:** 将从 `index` 到 `count-1` 的元素向右移动一个位置。最坏情况 ( `index = 0` ) 需要移动 $n$ 个元素，最好情况 ( `index = count` ) 移动 0 个，平均移动 $n/2$ 个。
        4.  **插入:** 将 `value` 放置在 `array[index]`。
        5.  **更新:** `count` 加 1。
    *   **时间复杂度:** 主要开销在于移动。最坏/平均情况: **$O(n)$**。最好情况 (在末尾插入，`index == count`): **$O(1)$** (假设没有扩容)。通常我们关注最坏或平均情况，所以一般记为 $O(n)$。
    *   *注意:* `push_back(value)` 是 `insertAtIndex(count, value)` 的特例。

*   **`removeAtIndex(index)`:**
    *   **动作:** 移除指定 `index` 处的元素。
    *   **步骤:**
        1.  **验证:** 检查是否 $0 \le index < count$。
        2.  **(可选) 获取值:** 如果需要返回被删除的元素，先获取 `array[index]`。
        3.  **移动:** 将从 `index+1` 到 `count-1` 的元素向左移动一个位置以填补空缺。最坏情况 ( `index = 0` ) 需要移动 $n-1$ 个元素，最好情况 ( `index = count-1` ) 移动 0 个，平均移动 $(n-1)/2$ 个。
        4.  **更新:** `count` 减 1。
    *   **时间复杂度:** 主要开销在于移动。最坏/平均情况: **$O(n)$**。最好情况 (删除末尾元素): **$O(1)$**。一般记为 $O(n)$。
    *   *注意:* `pop_back()` 是 `removeAtIndex(count-1)` 的特例。

*   **`insertAfterElement(targetValue, newValue)`:**
    *   **动作:** 找到 `targetValue` 的 *首次* 出现，并在其后插入 `newValue`。
    *   **步骤:**
        1.  **查找 (Find):** 进行 **线性扫描 (Linear Scan)** 找到 `targetValue` 的索引 (`targetIndex`)。最坏/平均情况需要 $O(n)$。如果找不到，可能什么都不做或抛出错误。
        2.  **插入:** 调用 `insertAtIndex(targetIndex + 1, newValue)`。需要 $O(n)$ 时间 (因为需要移动)。
    *   **时间复杂度:** $O(n) (\text{查找}) + O(n) (\text{插入}) = \mathbf{O(n)}$。

*   **`removeAfterElement(targetValue)`:**
    *   **动作:** 找到 `targetValue` 的 *首次* 出现，并移除其后的元素。
    *   **步骤:**
        1.  **查找:** 线性扫描找到 `targetValue` 的索引 (`targetIndex`)。需要 $O(n)$。检查 `targetValue` 是否存在且不是最后一个元素。
        2.  **移除:** 调用 `removeAtIndex(targetIndex + 1)`。需要 $O(n)$ 时间 (因为需要移动)。
    *   **时间复杂度:** $O(n) (\text{查找}) + O(n) (\text{移除}) = \mathbf{O(n)}$。

*   **`findIndex(index)`:** (常称为 `get` 或 `operator[]`)
    *   **动作:** 访问指定 `index` 处的元素。
    *   **步骤:**
        1.  **验证:** 检查是否 $0 \le index < count$。
        2.  **访问:** 返回 `array[index]`。
    *   **时间复杂度:** 通过指针算术直接访问内存 (`array + index`)。**$O(1)$**。这是数组/向量的关键优势。

*   **`findData(value)`:**
    *   **动作:** 查找 `value` *首次* 出现的索引。
    *   **步骤:**
        1.  **扫描:** 从 `array[0]` 到 `array[count-1]` 进行线性搜索。
        2.  **返回:** 如果找到，返回索引；否则返回 -1 (或其他表示未找到的值)。
    *   **时间复杂度:** 最坏情况 (值不存在或是最后一个元素) 需要检查所有 $n$ 个元素。**$O(n)$**。

**B. 有序数组列表 (Sorted Array List)**

元素按照特定顺序 (例如升序) 维护。这会改变某些操作的复杂度，特别是查找。修改列表的操作必须 *维持* 有序性。

*   **`insert(value)` (维持有序):**
    *   **动作:** 插入 `value` 并保持列表有序。
    *   **步骤:**
        1.  **检查扩容:** 如果 `count == capacity`，执行扩容 ($O(n)$)。
        2.  **查找位置 (Find Position):** 使用 **二分查找 (Binary Search)** 找到 `value` 应该插入的正确索引。需要 **$O(\log n)$** 时间。
        3.  **移动:** 将从插入索引开始的元素向右移动以腾出空间。最坏/平均情况仍需 **$O(n)$** 时间。
        4.  **插入:** 在找到的索引处放置 `value`。
        5.  **更新:** `count` 加 1。
    *   **时间复杂度:** $O(\log n) (\text{查找位置}) + O(n) (\text{移动}) = \mathbf{O(n)}$。移动操作是瓶颈。

*   **`remove(value)` (维持有序):**
    *   **动作:** 移除 `value` 的首次出现并保持列表有序。
    *   **步骤:**
        1.  **查找位置:** 使用 **二分查找** 找到 `value` 的索引。需要 **$O(\log n)$** 时间。如果找不到，则不执行任何操作。
        2.  **移动:** 将从 `index+1` 开始的元素向左移动以填补空缺。最坏/平均情况需要 **$O(n)$** 时间。
        3.  **更新:** `count` 减 1。
    *   **时间复杂度:** $O(\log n) (\text{查找}) + O(n) (\text{移动}) = \mathbf{O(n)}$。移动操作是瓶颈。

*   **`insertAtFront(value)` / `insertAtIndex(index, value)` / `insertAfterElement(...)` / `removeAtIndex(index)` / `removeAfterElement(...)`:** 如果 *字面上* 使用这些操作 (忽略有序属性)，它们会像在无序列表中一样执行 ($O(n)$)，但会 **破坏列表的有序性**。如果意图是执行等效操作 *同时维持有序性*，则通常应使用上述 `insert(value)` 或 `remove(value)` 的逻辑，时间复杂度为 $O(n)$。

*   **`findIndex(index)`:** 仍然是 **$O(1)$**。列表有序不影响直接通过索引访问。

*   **`findData(value)`:**
    *   **动作:** 查找 `value` 的索引。
    *   **步骤:** 使用 **二分查找 (Binary Search)**。
    *   **时间复杂度:** **$O(\log n)$**。这相对于无序列表的 $O(n)$ 线性搜索是一个显著的改进。

---

### 扩容策略与证明 (Resize Strategies & Proofs) - 均摊分析 (Amortized Analysis)

当 `count == capacity` 并且需要插入新元素时，底层数组已满，必须进行 **扩容 (Resize)**：

1.  **分配 (Allocate):** 分配一个新的、更大的数组。
2.  **复制 (Copy):** 将旧数组中的所有 $n$ 个元素复制到新数组中。
3.  **删除 (Delete):** 释放旧数组的内存。
4.  **更新 (Update):** 更新 `array` 指针指向新数组，并更新 `capacity`。

关键问题是：**新数组应该比旧数组大多少？**

*   **策略 1: 增加固定量 (Add a Constant Amount)** (例如 `new_capacity = capacity + C`)
    *   **例子:** 每次总是增加 10 个槽位。
    *   **问题:** 假设初始容量为 10，然后连续插入 1000 个元素。大约需要扩容 100 次 (10->20, 20->30, ..., 990->1000)。第 $k$ 次扩容大约复制 $10k$ 个元素。总复制成本与 $10 + 20 + ... + 1000$ 成正比，对于 $n=1000$ 个插入，总成本是 $O(n^2)$。这意味着每次插入的 *平均* 成本是 $O(n)$，效率很低。

*   **策略 2: 乘以一个常数因子 (Multiply by a Constant Factor)** (例如 `new_capacity = capacity * F`, 其中 `F > 1`)
    *   **例子:** 将容量 **加倍 (Doubling)** (`new_capacity = capacity * 2`)。这是最常见的策略 (例如 `std::vector` 使用)。
    *   **优点:** 扩容发生的频率呈指数级降低。让我们分析从空列表开始执行 $N$ 次 `push_back` 操作的总时间。

    **加倍策略的均摊分析 (Amortized Analysis for Doubling Strategy - `push_back`)**

    *   **目标:** 证明 $N$ 次 `push_back` 操作的总时间是 $O(N)$。
    *   **成本模型 (Cost Model):**
        * 简单插入 (无扩容): 成本 = 1 (放置元素)。
        * 带扩容的插入: 成本 = 1 (放置新元素) + $k$ (复制 $k$ 个旧元素)。我们近似为 $k$ (复制成本占主导)。
    *   **分析过程:** 假设初始容量为 1。扩容发生在 `count` 达到 1, 2, 4, 8, ..., $2^k$ 时。
        * 插入第 1 个元素: 简单成本 = 1。(容量 1)
        * 插入第 2 个元素: 需要扩容。容量 1 -> 2。复制 1 个元素。此步总成本 ≈ 1。
        * 插入第 3 个元素: 需要扩容。容量 2 -> 4。复制 2 个元素。此步总成本 ≈ 2。
        * 插入第 4 个元素: 简单成本 = 1。
        * 插入第 5 个元素: 需要扩容。容量 4 -> 8。复制 4 个元素。此步总成本 ≈ 4。
        *   ...
        * 插入第 $N$ 个元素: 假设总共执行了 $N$ 次插入。最后一次扩容发生在大小超过某个 $2^k$ 时。到插入第 $N$ 个元素为止，*所有* 扩容操作中复制的总元素数大约是 $1 + 2 + 4 + 8 + ... + 2^k$，其中 $2^k < N \le 2^{k+1}$。
    *   **总成本计算:**
        *   **总简单成本:** $N$ 次插入中每次都有 1 单位的简单成本。总计 = $N$。
        *   **总扩容 (复制) 成本:** 复制的元素总和为 $1 + 2 + 4 + ... + 2^k$。这是一个 **几何级数 (geometric series)**，其和为 $2^{k+1} - 1$。
        * 因为 $N \le 2^{k+1}$，所以 $2^{k+1} < 2N$。
        * 因此，总复制成本为 $2^{k+1} - 1 < 2N - 1$。
        *   **总成本 (Grand Total Cost)** = 总简单成本 + 总扩容成本 ≈ $N + (2N - 1) = 3N - 1$。
    *   **结论:** $N$ 次 `push_back` 操作的总成本是 $O(N)$。
    *   **每次操作的均摊成本 (Amortized Cost per Operation):** 总成本 / N = $O(N) / N = \mathbf{O(1)}$。

### 数组列表时间复杂度 (Summary Table: Array List Time Complexities)

| 操作                          | 无序 (平均/最坏) | 有序 (平均/最坏) | 注释                                             |
| :---------------------------- | :--------------- | :----------------- | :----------------------------------------------- |
| `findIndex(index)` / `get`    | $O(1)$           | $O(1)$             | 直接访问                                         |
| `findData(value)`             | $O(n)$           | $O(\log n)$        | 线性搜索 vs 二分查找                            |
| `insertAtIndex(i, v)`         | $O(n)$           | $O(n)$             | 移动是瓶颈。若按字面使用会破坏有序性。              |
| `insert(v)` (维持有序)      | 不适用 (N/A)     | $O(n)$             | $O(\log n)$ 查找 + $O(n)$ 移动                   |
| `push_back(v)` (末尾添加)   | $O(1)$ 均摊      | $O(n)$             | 无序时平均很快。有序时需查找 + 移动。                |
| `insertAtFront(v)` (开头添加) | $O(n)$           | $O(n)$             | 需要移动。若按字面使用会破坏有序性。              |
| `removeAtIndex(i)`            | $O(n)$           | $O(n)$             | 移动是瓶颈。若按字面使用会破坏有序性。              |
| `remove(v)` (维持有序)      | 不适用 (N/A)     | $O(n)$             | $O(\log n)$ 查找 + $O(n)$ 移动                   |
| `pop_back()` (末尾移除)       | $O(1)$           | $O(1)$             | 无需移动。                                       |
| `insertAfterElement(...)`     | $O(n)$           | $O(n)$             | 查找 ($O(n)$ 或 $O(\log n)$) + 插入 ($O(n)$)     |
| `removeAfterElement(...)`     | $O(n)$           | $O(n)$             | 查找 ($O(n)$ 或 $O(\log n)$) + 移除 ($O(n)$)     |

## Linked List 链表

### 基本概念

*   **概念：** 链表 是一种动态数据结构，其中元素（称为节点）不是存储在连续的内存位置中。每个节点包含数据和一个指向序列中下一个节点的指针。

*   **组成部分：**
    *   **节点（Node）：** 每个节点包含两部分：
        * 数据域（Data）：存储实际数据。
        * 指针域（Next）：存储指向下一个节点的地址。 最后一个节点的指针域通常指向 `NULL`，表示链表的结尾。
    *   **头指针（Head）：** 指向链表中的第一个节点的指针。如果链表为空，则头指针为 `NULL`。

*   **操作实现：**
    *   **插入（Insert）：** 在链表中插入一个新节点，需要修改指针。例如，在头部插入：

        1.  创建一个新节点，并将数据存储在新节点的数据域中。
        2.  将新节点的指针域指向当前的头节点。
        3.  将头指针指向新节点。

    *   **删除（Delete）：** 从链表中删除一个节点，也需要修改指针。例如，删除头节点：

        1.  将头指针指向第二个节点。
        2.  释放已删除节点的内存。

    *   **查找（Search）：** 从头节点开始，依次遍历链表，直到找到目标节点或到达链表结尾。

    *   **优点：**
        *   **动态大小（Dynamic Size）：** 链表的大小可以动态增长或缩小，不需要预先分配固定大小的内存。
        *   **插入和删除效率高（Efficient Insertion and Deletion）：** 在已知节点位置的情况下，插入和删除操作只需要修改指针，时间复杂度为 O(1)。
        *   **内存利用率高（Memory Utilization）：** 链表可以根据需要动态分配内存，不会造成内存浪费。

    *   **缺点：**
        *   **访问效率低（Inefficient Access）：** 链表中的元素不是存储在连续的内存位置中，无法通过索引直接访问，需要从头节点开始依次遍历，时间复杂度为 O(n)。
        *   **额外的内存开销（Extra Memory Overhead）：** 每个节点都需要额外的内存空间来存储指针。



**与数组实现 List 对比**

| 特性      | 链表（Linked List）        | 数组（Array） |
| ------- | ---------------------- | --------- |
| 存储方式    | 非连续内存空间                | 连续内存空间    |
| 大小      | 动态可变                   | 静态固定      |
| 访问效率    | O(n)                   | O(1)      |
| 插入/删除效率 | O(1)（已知位置）/ O(n)（未知位置） | O(n)      |
| 内存利用率   | 高                      | 可能浪费      |
| 额外内存开销  | 有（指针）                  | 无         |

### 基本函数

#### 逆向打印

**考虑递归 ->先打印剩余链表，再打印当前 head**

```c++
#include <iostream>

struct Node {
    int data;
    Node* next;
};

void reversePrint(Node* head) {
    if (head == nullptr) { // 基本情况：链表为空
        return;
    }
    reversePrint(head->next); // 递归处理剩余链表
    std::cout << head->data << " "; // 打印当前节点的数据
}

int main() {
    // 创建一个链表：1 -> 2 -> 3 -> 4 -> 5
    Node* head = new Node{1, new Node{2, new Node{3, new Node{4, new Node{5, nullptr}}}}};

    std::cout << "Reversed List: ";
    reversePrint(head); // 调用递归函数逆向打印链表
    std::cout << std::endl;

    // 释放链表内存 (为了防止内存泄漏，实际使用中需要更完善的释放代码)
    Node* current = head;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }
    head = nullptr;

    return 0;
}
```

#### 插入与删除元素

**考虑分别实现 find 函数与 get 函数**

**1. 实现 find 函数**

> [!danger] 注意**返回指针的引用**
> - 如果 `find` 函数返回的是 `ListNode *`（指针），那么你只能访问找到的节点的数据，而**无法修改链表本身的结构**。
> - 对于链表操作（特别是插入、删除），你需要修改链表节点的 `next` 指针，这时 `find` 函数必须返回 `ListNode *&`（指针的引用），才能正确地修改链表结构。

关键点：指针引用 (`pointer reference`)
- **定义**：指针的引用允许我们修改原始指针变量，而不仅仅是它所指向的值。
- **语法**：`ListNode*& ptr`，表示指向 `ListNode` 类型的指针的引用。

```c++
# include "List.h"
ListNode *& List::find_(unsigned index) const{
	ListNode * thru = head_;
	for (int i = 0; i < index; i++){
		thru = thru->next;
	}
	return thru->next;
}
```

> [!question] 为什么返回 thru->next 而不是 thru

首先，`find` 函数的目的是找到链表中指定 index 的节点。我们假设现在要在一个链表中插入一个新的节点。

1.  **定位节点**：`find` 函数首先需要找到 index 对应的节点位置。

2.  **插入新节点**：找到目标位置后，我们需要将新节点插入到链表中。这通常涉及修改指针，使得前一个节点的 `next` 指向新节点，新节点的 `next` 指向当前节点。

现在，让我们分析为什么返回 `thru->next` 而不是 `thru` 是合理的。

* 如果 `find` 函数返回 `thru`，那么在插入新节点时，我们需要知道 `thru` 节点的前一个节点才能完成插入操作。这会增加额外的操作和代码复杂度，因为我们需要重新遍历链表来找到 `thru` 的前一个节点。

* 如果 `find` 函数返回 `thru->next`，也就是 index 对应的节点，那么我们就可以直接在这个节点之前插入新节点，而无需额外的遍历操作。


**情况 1：`find` 函数返回 `thru`**

```c++
ListNode* find(unsigned index) const {
    ListNode* thru = head;
    for (unsigned i = 0; i < index; i++) {
        thru = thru->next;
    }
    return thru;
}

void insert(T& t, unsigned index) {
    ListNode* newNode = new ListNode(t);
    ListNode* current = find(index);

    // 需要找到 current 的前一个节点
    ListNode* prev = head;
    while (prev->next != current) {
        prev = prev->next;
    }

    newNode->next = current;
    prev->next = newNode;
}
```

**情况 2：`find` 函数返回 `thru->next`**

```c++
ListNode*& find(unsigned index) const {
    ListNode* thru = head;
    for (unsigned i = 0; i < index && thru != nullptr; i++) {
        thru = thru->next;
    }
    return thru->next;
}

void insert(T& t, unsigned index) {
    ListNode* newNode = new ListNode(t);
    ListNode*& current = find(index);

    newNode->next = current;
    current = newNode;
}
```

通过对比可以看出，返回 `thru->next` 可以简化插入操作，使得代码更简洁高效。

**2. 实现 get 函数**

```c++
T & List::get(unsigned index) const{
	ListNode* & ptr = find_(index);
	return ptr->data
}
```

**3. 实现 insert 函数**

```c++
void List::insert(T & t, unsigned index){
	ListNode * newnode = new ListNode(t);
	ListNode *&ptr = find_(index);
	newnode->next = ptr;
	ptr = newnode;
}
```

**注意依然用了 pointer reference 对原链表结构进行修改**

**4. 实现 remove 函数**  
**注意删除元素时需避免之前分配的内存泄露**

```c++
T& List::remove (unsigned index){
	ListNode *& ptr = find_(index);
	ListNode * oldnode = ptr;
	ptr = ptr->next;
	T& data = oldnode->data.
	delete oldnode;
	return data;
}
```

### 具体操作与时间复杂度

设 $n$ 为链表中当前的节点数量。

#### A. 单向链表 (Singly Linked List)

每个节点包含数据和一个指向下一个节点的指针。

*   **`insertAtFront(value)`:**
    *   **动作:** 在链表的头部插入一个新节点。
    *   **步骤:**
        1.  **创建节点:** 创建一个新的节点，存储 `value`。需要 $O(1)$ 时间。
        2.  **更新指针:** 将新节点的 `next` 指针指向当前的头节点，然后更新 `head` 指针指向新节点。需要 $O(1)$ 时间。
        3.  **更新尺寸:** 如果维护了 `size`，则 `size` 增加 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 所有步骤都是 $O(1)$ 操作。整体复杂度:**$O(1)$**。

*   **`insertAtIndex(index, value)`:**
    *   **动作:** 在指定的 `index` 处插入一个新节点。
    *   **步骤:**
        1.  **验证 (Validation):** 检查是否 $0 \le index \le size$。需要 $O(1)$ 时间。
        2.  **特殊情况:** 如果 `index == 0`，则调用 `insertAtFront(value)`。需要 $O(1)$ 时间。
        3.  **遍历 (Traverse):** 从 `head` 开始遍历到 `index-1` 位置的节点（即插入位置的前一个节点）。最坏情况需要遍历 $n$ 个节点，需要 $O(n)$ 时间。
        4.  **创建并插入:** 创建新节点，并更新指针以将新节点插入到链表中。需要 $O(1)$ 时间。
        5.  **更新尺寸:** 如果维护了 `size`，则 `size` 增加 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于遍历。最坏/平均情况: **$O(n)$**。最好情况（在头部插入）: **$O(1)$**。

*   **`removeAtIndex(index)`:**
    *   **动作:** 移除指定 `index` 处的节点。
    *   **步骤:**
        1.  **验证:** 检查是否 $0 \le index < size$。需要 $O(1)$ 时间。
        2.  **特殊情况:** 如果 `index == 0`，则移除头节点并更新 `head` 指针。需要 $O(1)$ 时间。
        3.  **遍历:** 从 `head` 开始遍历到 `index-1` 位置的节点。最坏情况需要 $O(n)$ 时间。
        4.  **移除:** 更新指针以绕过要删除的节点，并释放该节点的内存。需要 $O(1)$ 时间。
        5.  **更新尺寸:** 如果维护了 `size`，则 `size` 减少 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于遍历。最坏/平均情况: **$O(n)$**。最好情况（移除头节点）: **$O(1)$**。

*   **`insertAfterElement(targetValue, newValue)`:**
    *   **动作:** 找到 `targetValue` 的 *首次* 出现，并在其后插入 `newValue`。
    *   **步骤:**
        1.  **查找 (Find):** 从头节点开始遍历链表，寻找值为 `targetValue` 的节点。最坏情况需要遍历所有 $n$ 个节点，需要 $O(n)$ 时间。
        2.  **创建并插入:** 如果找到目标节点，创建新节点并插入到目标节点之后。需要 $O(1)$ 时间。
        3.  **更新尺寸:** 如果成功插入，`size` 增加 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于查找。最坏/平均情况: **$O(n)$**。

*   **`removeAfterElement(targetValue)`:**
    *   **动作:** 找到 `targetValue` 的 *首次* 出现，并移除其后的节点。
    *   **步骤:**
        1.  **查找:** 从头节点开始遍历链表，寻找值为 `targetValue` 的节点。需要 $O(n)$ 时间。
        2.  **移除:** 如果找到目标节点且其后有节点，则更新指针以绕过要删除的节点，并释放该节点的内存。需要 $O(1)$ 时间。
        3.  **更新尺寸:** 如果成功移除，`size` 减少 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于查找。最坏/平均情况: **$O(n)$**。

*   **`findIndex(index)`:** (常称为 `get`)
    *   **动作:** 访问指定 `index` 处的节点。
    *   **步骤:**
        1.  **验证:** 检查是否 $0 \le index < size$。需要 $O(1)$ 时间。
        2.  **遍历:** 从头节点开始遍历到 `index` 位置的节点。需要 $O(index)$ 时间，最坏情况是 $O(n)$。
    *   **时间复杂度:** **$O(n)$**。这是链表相对于数组的主要劣势。

*   **`findData(value)`:**
    *   **动作:** 查找 `value` *首次* 出现的索引。
    *   **步骤:**
        1.  **遍历:** 从头节点开始遍历链表，比较每个节点的值与 `value`。最坏情况需要检查所有 $n$ 个节点。
        2.  **返回:** 如果找到，返回对应的索引；否则返回 -1 或抛出异常。
    *   **时间复杂度:** 最坏情况需要检查所有节点。**$O(n)$**。

*   **`append(value)`:** (或称为 `push_back`, `insertAtBack`)
    *   **动作:** 在链表末尾添加新节点。
    *   **特殊情况: 维护了 `tail` 指针**
        *   **步骤:** 创建新节点，将 `tail->next` 指向新节点，更新 `tail` 指向新节点。所有操作都是 $O(1)$。
        *   **时间复杂度:** **$O(1)$**。
    *   **一般情况: 无 `tail` 指针**
        *   **步骤:** 遍历链表找到最后一个节点（其 `next` 为 `nullptr`），将其 `next` 指针指向新创建的节点。需要 $O(n)$ 时间遍历。
        *   **时间复杂度:** **$O(n)$**。

#### B. 有序链表 (Sorted Linked List)

元素按照特定顺序（例如升序）维护，改变了某些操作的行为和复杂度。

*   **`insert(value)` (维持有序):**
    *   **动作:** 插入 `value` 并保持链表有序。
    *   **步骤:**
        1.  **特殊情况:** 如果链表为空或 `value` 应该在头部，则在头部插入。需要 $O(1)$ 时间。
        2.  **遍历:** 从头节点开始遍历链表，找到适合插入 `value` 的位置（即找到第一个大于等于 `value` 的节点的前一个节点）。最坏情况需要遍历所有节点，需要 $O(n)$ 时间。
        3.  **创建并插入:** 创建新节点并插入到找到的位置。需要 $O(1)$ 时间。
        4.  **更新尺寸:** `size` 增加 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于遍历以找到正确的插入位置。**$O(n)$**。

*   **`remove(value)` (从有序列表中移除):**
    *   **动作:** 移除 `value` 的首次出现。
    *   **步骤:**
        1.  **特殊情况:** 如果头节点的值等于 `value`，则移除头节点。需要 $O(1)$ 时间。
        2.  **遍历:** 遍历链表找到值为 `value` 的节点。由于链表有序，一旦遇到大于 `value` 的节点，就可以确定 `value` 不存在。最坏情况需要 $O(n)$ 时间。
        3.  **移除:** 如果找到，更新指针以绕过该节点，并释放内存。需要 $O(1)$ 时间。
        4.  **更新尺寸:** 如果成功移除，`size` 减少 1。需要 $O(1)$ 时间。
    *   **时间复杂度:** 主要开销在于遍历。**$O(n)$**。

*   **`findIndex(index)`:** 与无序链表相同，仍然需要遍历。**$O(n)$**。

*   **`findData(value)`:**
    *   **动作:** 查找 `value` 在有序链表中的索引。
    *   **优化:** 由于链表有序，一旦遇到大于 `value` 的节点，就可以确定 `value` 不存在。
    *   **时间复杂度:** 尽管有优化，但最坏情况仍需遍历所有节点。**$O(n)$**。

#### 单链表与双链表对比

双向链表 (Doubly Linked List)
- **额外属性**：每个节点除了 `next` 指针外，还有一个 `prev` 指针指向前一个节点。
- **优势**：
  - 可以从任意节点**双向遍历**
  - 在已知节点位置的情况下，**删除操作**为 **O(1)** (无需查找前驱节点)
  - 实现**从尾到头的遍历**更高效

| 操作 | 单链表 | 双链表 |
|------|-------|-------|
| 内存占用 | 较小 (每个节点一个指针) | 较大 (每个节点两个指针) |
| 插入节点 | 需要知道前驱节点 | 可直接从当前节点插入 |
| 删除节点 | 需要知道前驱节点, O(n) | 可直接删除当前节点, O(1) |
| 反向遍历 | 不支持 | 支持 |

### 链表时间复杂度总结表

| 操作 | 单链表 (无 tail) | 单链表 (有 tail) | 有序链表 | 注释 |
|------|---------------|---------------|---------|------|
| `insertAtFront(v)` | $O(1)$ | $O(1)$ | $O(1)$* | * 如果值应该在头部 |
| `insertAtIndex(i, v)` | $O(n)$ | $O(n)$ | $O(n)$ | 需要遍历找位置 |
| `append(v)` / `push_back(v)` | $O(n)$ | $O(1)$ | $O(n)$ | 有 tail 指针时为 O(1) |
| `removeAtIndex(i)` | $O(n)$ | $O(n)$ | $O(n)$ | 需要遍历 |
| `insertAfterElement(...)` | $O(n)$ | $O(n)$ | $O(n)$ | 查找为瓶颈 |
| `removeAfterElement(...)` | $O(n)$ | $O(n)$ | $O(n)$ | 查找为瓶颈 |
| `findIndex(i)` / `get(i)` | $O(n)$ | $O(n)$ | $O(n)$ | 需要遍历 |
| `findData(v)` | $O(n)$ | $O(n)$ | $O(n)$ | 尽管有序链表有优化，最坏情况仍为 O(n) |
| `insert(v)` (有序) | 不适用 | 不适用 | $O(n)$ | 需要遍历找正确位置 |
| `remove(v)` (有序) | $O(n)$ | $O(n)$ | $O(n)$ | 查找为瓶颈 |

**链表与数组列表对比**

| 特性 | 链表 | 数组列表 |
|------|------|---------|
| 内存分配 | 动态、非连续 | 连续块 |
| 随机访问 | O(n) | O(1) |
| 首部插入 | O(1) | O(n) |
| 中间插入 | O(n) 查找 + O(1) 插入 | O(n) 查找 + O(n) 移动 |
| 末尾插入 | O(1) 有 tail 指针<br>O(n) 无 tail 指针 | O(1) 均摊 |
| 内存效率 | 每个元素需额外存储指针 | 可能有未使用空间 |
| 实现复杂度 | 较复杂 | 相对简单 |

链表在**频繁进行首部插入/删除**以及**需要动态增长**但**不需要频繁随机访问**的场景下表现更佳。而数组列表在**需要频繁随机访问**以及**希望内存紧凑**的场景下更合适。

## LIST ADT

### 搜索算法

**1. 二分查找 (Sorted List)**

**A. 数组列表**

```c++
template <typename T>
int binarySearchVector(const std::vector<T>& sorted_data, const T& value) {
    """
    在已排序的 std::vector 中进行二分查找。
    返回匹配元素的索引，如果未找到则返回 -1。
    时间复杂度: O(log n)
    空间复杂度: O(1) (迭代版本)
    """
    int low = 0;
    int high = static_cast<int>(sorted_data.size()) - 1; // Use int for indices

    while (low <= high) {
        // Use C++20 std::midpoint or classic way to avoid overflow
        int mid = low + (high - low) / 2;
        const T& mid_value = sorted_data[mid];

        if (mid_value == value) {
            return mid;
        } else if (value < mid_value) {
            high = mid - 1;
        } else { // value > mid_value
            low = mid + 1;
        }
    }
    return -1; // 未找到
}

```

### 排序算法

**1. 冒泡排序**

**基本思想 (Idea):** 重复地遍历列表，比较相邻的两个元素，如果它们的顺序错误就交换它们。每一轮遍历至少会将一个未排序的最大（或最小）元素 " 冒泡 " 到其最终位置。

```c++
template <typename T>
void bubbleSortVector(std::vector<T>& data) {
    """
    对 std::vector 进行冒泡排序 (原地)。
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    稳定性: 是
    """
    size_t n = data.size();
    if (n <= 1) return;

    for (size_t i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (size_t j = 0; j < n - i - 1; ++j) {
            if (data[j] > data[j + 1]) {
                std::swap(data[j], data[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) { // 优化：如果内层循环没有交换，则已排序
            break;
        }
    }
}

```

**2. 插排**  
**基本思想 (Idea):** 将列表分为 " 已排序 " 和 " 未排序 " 两部分。每次从未排序部分取出一个元素，在已排序部分找到合适的位置并插入。

```c++
template <typename T>
void insertionSortVector(std::vector<T>& data) {
    """
    对 std::vector 进行插入排序 (原地)。
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    稳定性: 是
    """
    size_t n = data.size();
    if (n <= 1) return;

    for (size_t i = 1; i < n; ++i) {
        T current_value = std::move(data[i]); // Use move for efficiency if T supports it
        int j = static_cast<int>(i) - 1; // Use signed int for index comparison with >= 0

        // 将已排序部分中大于 current_value 的元素向右移动
        while (j >= 0 && data[j] > current_value) {
            data[j + 1] = std::move(data[j]); // Move elements right
            j--;
        }
        // 插入 current_value 到正确位置
        data[j + 1] = std::move(current_value);
    }
}

```

**3. Merge Sort**
1. **分解 (Divide):** 将列表递归地分成两半，直到每个子列表只包含一个元素（或为空）。单个元素的列表自然是有序的。
2. **合并 (Conquer/Combine):** 将相邻的两个已排序的子列表 **合并 (Merge)** 成一个更大的已排序列表。重复此过程，直到整个列表合并完毕。

```c++
// Helper function to merge two sorted vectors
template <typename T>
std::vector<T> mergeVectors(const std::vector<T>& left, const std::vector<T>& right) {
    std::vector<T> result;
    result.reserve(left.size() + right.size()); // Pre-allocate memory

    size_t i = 0, j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) { // Maintains stability
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }

    // Append remaining elements
    result.insert(result.end(), left.begin() + i, left.end());
    result.insert(result.end(), right.begin() + j, right.end());

    return result;
}

template <typename T>
std::vector<T> mergeSortVector(const std::vector<T>& data) {
    """
    对 std::vector 进行归并排序。
    返回一个新的已排序 vector。
    时间复杂度: O(n log n)
    空间复杂度: O(n)
    稳定性: 是
    """
    size_t n = data.size();
    if (n <= 1) {
        return data; // Base case: 0 or 1 element is already sorted
    }

    size_t mid = n / 2;

    // Create left and right sub-vectors
    std::vector<T> left_half(data.begin(), data.begin() + mid);
    std::vector<T> right_half(data.begin() + mid, data.end());

    // Recursively sort the halves
    std::vector<T> sorted_left = mergeSortVector(left_half);
    std::vector<T> sorted_right = mergeSortVector(right_half);

    // Merge the sorted halves
    return mergeVectors(sorted_left, sorted_right);
}

```

**4. 快排**
- **基本思想 (Idea):** 也是 " 分而治之 "。选择一个 **基准元 (Pivot)**，将列表 **分区 (Partition)** 为两部分：小于基准元的和大于基准元的。然后递归地对这两个子部分进行排序。
- **时间复杂度 (Time Complexity):**
    - **最佳/平均 (Best/Average):**  $O(n\log n)$ 。
    - **最差 (Worst):** $O(n ^{2})$ (发生在基准元选择不佳，如每次都选到最小或最大元素时)。

## Stack

### 利用 Linked List 实现 stack

**1. Stack 的基本结构**  
首先定义 `Stack.h`,定义栈的相关接口，需满足以下操作
- push 向栈内增加元素
- pop 向元素从栈顶弹出，并返回该元素
- isEmpty 判断栈是否为空
- Stack() 构造函数，创建一个空栈

```c++
template <class T>
class Stack {
public:
    void push(T& t); // 将元素 t 压入栈顶
    T& pop();         // 移除栈顶元素，并返回该元素
    bool isEmpty() const; // 检查栈是否为空
    Stack();            // 构造函数，创建一个空栈

private:
    //...
};

```

**进一步定义 StackNode 结构体，作为 stack 的 private data**

```c++
template <class T>
struct StackNode {
    T& data;           // 存储的数据
    StackNode* next;   // 指向下一个节点的指针
    StackNode(T& t) : data(t), next(nullptr) {} // 构造函数
};

template <class T>
class Stack {
private:
    StackNode<T>* head; // 栈顶指针，指向链表的第一个节点
};

```

**2. Push(入栈) & Pop(出栈) 实现**

- **push 函数（Slides 21-24）**

`push` 函数用于将一个新元素压入栈顶。 具体步骤如下：

1. 创建一个新的 `StackNode`， 将数据存储在新节点中。
2. 将新节点的 `next` 指针指向当前的栈顶（`head` 指向的节点）。
3. 将 `head` 指针指向新的节点， 使得新的节点成为栈顶。

```c++
template <class T>
void Stack<T>::push(T& t) {
    StackNode<T>* newNode = new StackNode<T>(t); // 创建新节点
    newNode->next = head;                       // 新节点的 next 指针指向当前栈顶
    head = newNode;                               // head 指针指向新的节点，更新栈顶
}

```

- **pop 函数（Slides 25-27）**

`pop` 函数用于移除栈顶元素，并返回该元素的值。 具体步骤如下：

1. 检查栈是否为空， 如果为空， 则抛出一个异常或者返回一个默认值（具体取决于实现）。
2. 将 `head` 指针指向的节点（栈顶）保存到一个临时变量中。
3. 将 `head` 指针指向栈顶的下一个节点， 也就是 `head->next`。
4. 从临时变量中获取栈顶元素的数据。
5. 释放之前栈顶节点的内存（使用 `delete` 关键字）。
6. 返回栈顶元素的数据。

```c++
template <class T>
T& Stack<T>::pop() {
    if (isEmpty()) {
        throw std::out_of_range("Stack is empty"); // 栈为空，抛出异常
    }

    StackNode<T>* temp = head;    // 临时指针指向栈顶
    head = head->next;             // head 指针指向下一个节点，更新栈顶
    T& data = temp->data;           // 保存栈顶元素的数据
    delete temp;                     // 释放之前栈顶节点的内存
    return data;                     // 返回栈顶元素的数据
}

template <class T>
bool Stack<T>::isEmpty() const {
    return head == nullptr; // 如果 head 为空，则栈为空
}

```

### 利用 Array 实现 Stack

**1. Stack 的结构**  
利用数组实现栈需要预先分配一块连续的内存空间

```c++
template <class T>
class Stack {
private:
    T* array;       // 存储栈元素的数组
    unsigned size;  // 数组的总容量
    unsigned count; // 当前栈中元素的个数
public:
    Stack();        // 构造函数
    ~Stack();       // 析构函数
    void push(T& t);
    T& pop();
    bool isEmpty() const;
};

```

**2. 实现 pop 与 push**

- **push 函数**

`push` 函数用于将一个新元素压入栈顶。 具体步骤如下：

1. **检查栈是否已满**：如果 `count` 等于 `size`， 说明数组已经满了， 无法再存储新的元素。 这时，我们需要对数组进行扩容（resize）。
2. **扩容（Resize）**：
    - 创建一个新的数组， 容量是原来的两倍（或其他策略，例如 1.5 倍）。
    - 将原数组中的所有元素复制到新数组中。
    - 释放原数组的内存。
    - 更新 `array` 指针指向新的数组， 并更新 `size` 的值为新的容量。
3. **将新元素添加到栈顶**：将新元素存储到 `array[count]` 的位置， 并将 `count` 的值加 1。

```c++
template <class T>
void Stack<T>::push(T& t) {
    if (count + 1 == size) { // 检查栈是否已满
        // 扩容
        unsigned newSize = size * 2;
        T** newArray = new T*[newSize]; // 创建指针数组，防止将对象引用赋值给对象
        for (unsigned i = 0; i < count; ++i) {
            newArray[i] = array[i]; // 复制指针
        }
        delete[] array; // 释放原数组内存
        array = newArray; // 更新 array 指针
        size = newSize;   // 更新 size
    }
    array[count++] = &t; // 添加新的元素的地址
}

```

> [!danger] 为什么要利用指针数组

**1. 避免对象拷贝**

在 `push` 方法中，`T& t` 作为参数传入，而 `array[count++] = &t;` 存储的是 `t` 的地址，而不是 `t` 的副本。这样做的目的是：

- **不调用拷贝构造函数**，避免了对象的拷贝，提升了效率。
    
- **始终存储的是原对象的地址**，修改 `array` 中的元素会直接影响原对象。
    


假设 `Stack<int>` 使用 `T**` 存储对象地址：

```cpp
Stack<int> s;
int a = 10;
s.push(a);
```

- `push(a)` 只存储 `a` 的地址，而不是 `a` 的副本。
    

如果 `Stack<T>` 直接存储 `T` 而不是 `T*`，那么：

```cpp
array[count++] = t;  // 这里会触发 T 的拷贝构造
```

- `t` 会被拷贝到 `array`，如果 `T` 是一个复杂的对象（如大数据结构），会引入额外的性能开销。

**2. 允许存储不同生命周期的对象**

由于 `array` 存储的是对象的地址，而不是对象本身，因此可以存储**不同作用域的对象**，而不需要担心它们被复制。

```cpp
Stack<std::string> s;
std::string str = "Hello";
s.push(str);  // 只存储 str 的地址，而不是拷贝 str
```

如果 `Stack<T>` 存储的是对象而不是指针，则 `str` 会被复制到 `array`，而 `str` 发生改变时 `Stack` 内部的数据不会同步

**3. 避免不必要的构造和析构**

如果 `array` 直接存储 `T` 类型的对象：

```cpp
T* array = new T[size];  // 需要默认构造 T
```

- 这样会导致**所有元素都调用默认构造函数**，即使它们还未被使用。
    
- 但是 `T** array = new T*[size];` 只是分配了指针空间，并没有创建 `T` 的对象，不会有构造和析构的额外开销。
    

**4. 更灵活的管理对象**

使用指针数组还可以让 `Stack<T>` 处理**不同存储方式的对象**，比如：

- **存储在堆上的对象**
    
- **存储在栈上的对象**
    
- **共享对象**
    
- **动态分配的对象**
    

### **示例**

```cpp
Stack<std::string> s;
std::string* str = new std::string("Hello");
s.push(*str);  // 存储的是 str 的地址，而不是拷贝 str
```

这允许 `Stack<T>` 处理**大对象或不能复制的对象**（如 `std::unique_ptr`）。



- **pop 函数**

`pop` 函数用于移除栈顶元素，并返回该元素的值。 具体步骤如下：

1. **检查栈是否为空**：如果 `count` 等于 0， 说明栈为空， 无法移除元素。 这时，可以抛出一个异常或者返回一个默认值。
2. **移除栈顶元素**：将 `count` 的值减 1， 然后返回 `array[count]` 的值。

```c++
template <class T>
T& Stack<T>::pop() {
    if (isEmpty()) {
        throw std::out_of_range("Stack is empty"); // 栈为空，抛出异常
    }
    return *array[--count]; // count 减 1，并返回 array[count] 的值
}

```

**3. 构造函数与析构函数**
- **构造函数**

```c++
template <class T>
Stack<T>::Stack() : size(10), count(0) { // 初始容量为 10
    array = new T[size]; // 分配数组内存
}

```

- **析构函数**

```c++
template <class T>
Stack<T>::~Stack() {
		for (unsigned i = 0; i < count; i++){
				delete array[i]; //删除每个分配的T对象
		}
    delete[] array; // 删除指针数组
}

```

## Queue

> [!tip] 基本概述  
> 队列是一种**先进先出（First-In-First-Out，FIFO）**的线性数据结构。这意味着队列中的元素按照它们被添加的顺序排列，最先添加的元素最先被移除。  
> **基本操作**
> - enqueue(入队)：将新元素加入队尾
> - dequeue(出队)：移除队列的第一个元素

### 链表实现

```c++
#include <iostream>

template <class QE>
class Queue {
private:
    struct Node {
        QE data;
        Node* next;
        Node(QE data) : data(data), next(nullptr) {}
    };
    Node* entry_; // 指向队头（head）
    Node* exit_;  // 指向队尾（tail）
    int size_;    // 队列大小

public:
    Queue() : entry_(nullptr), exit_(nullptr), size_(0) {} // 构造函数
    ~Queue() { // 析构函数
        while (!isEmpty()) {
            dequeue();
        }
    }

    void enqueue(QE e) { // 入队
        Node* newNode = new Node(e);
        if (isEmpty()) {
            entry_ = exit_ = newNode; // 队列为空时，队头和队尾都指向新节点
        } else {
            exit_->next = newNode;   // 将新节点添加到队尾
            exit_ = newNode;        // 更新队尾指针
        }
        size_++;
    }

    QE& dequeue() { // 出队
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }
        Node* temp = entry_;          // 临时保存队头节点
        entry_ = entry_->next;     // 队头指针指向下一个节点
        QE& data = temp->data;      // 保存队头节点的数据
        delete temp;                 // 释放队头节点的内存
        size_--;
        if (entry_ == nullptr) { // 队列为空时，队尾指针也需要置空
            exit_ = nullptr;
        }
        return data;
    }

    QE& peek() { // 查看队首
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }
        return entry_->data;
    }

    bool isEmpty() { // 判空
        return size_ == 0;
    }

    int size() { // 队列大小
        return size_;
    }
};

```

### 数组实现

> [!attention] 常见注意事项  
> **1. 循环数组**  
> 数组实现时 entry 与 exit 可能会达到数组的末尾，我们可以使用取模运算将指针绕回数组的开头，实现循环利用数组空间（注意检测是否已经达到容量上限需要扩容）  
> **2. 动态扩容**  
> 当队列已满时，可以将整个数组 copy 到新的内存空间进行扩容

```c++
#include <iostream>

template <class QE>
class Queue {
private:
    QE* items_;          // 存储队列元素的数组
    unsigned capacity_;   // 数组容量
    unsigned entry_;      // 队头指针（指向下一个要出队的元素）
    unsigned exit_;       // 队尾指针（指向下一个要入队的空位置）
    unsigned count_;      // 队列中元素的个数

public:
    Queue(unsigned capacity) : capacity_(capacity), entry_(0), exit_(0), count_(0) { // 构造函数
        items_ = new QE[capacity_];
    }

    ~Queue() { // 析构函数
        delete[] items_;
    }

    void enqueue(QE e) { // 入队
        if (count_ == capacity_) {
            throw std::out_of_range("Queue is full");
        }
        items_[exit_] = e;         // 将新元素添加到队尾
        exit_ = (exit_ + 1) % capacity_; // 更新队尾指针（循环数组）
        count_++;
    }

    QE& dequeue() { // 出队
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }
        QE& data = items_[entry_];   // 保存队头元素
        entry_ = (entry_ + 1) % capacity_; // 更新队头指针（循环数组）
        count_--;
        return data;
    }

    QE& peek() { // 查看队首
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }
        return items_[entry_];
    }

    bool isEmpty() { // 判空
        return count_ == 0;
    }

    int size() { // 队列大小
        return count_;
    }
};

```

