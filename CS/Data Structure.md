---
title: Data Structure
date: 2025-03-11
date modified: 2025-03-13
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

## Array Based List

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

## Skip List