---
title: Data Structure-6-Heaps
date: 2025-04-29
date modified: 2025-04-29
categories: CS225
tags:
  - CS225
---

#CS225 


## Heap Overview

本节主要包括了 **堆 (Heap)** 这种数据结构，特别是 **最小堆 (Min-Heap)**。核心内容包括：

1.  **堆的基本概念和数组实现**
2.  **堆的核心操作：插入 (Insert / `heapifyUp`)**
3.  **堆的核心操作：删除最小值 (RemoveMin / `heapifyDown`)**
4.  **堆的构建 (BuildHeap)**
5.  **堆排序 (Heap Sort)**
6.  **堆作为优先队列 (Priority Queue) 的实现**

## (最小) 堆 ((Min) Heap) 的概念与数组表示

*   **定义 (Definition):**
    *   堆是一种特殊的基于树的数据结构。我们主要关注 **最小堆 (Min-Heap)**。
    *   **关键属性 (Key Properties):**
        1.  **结构属性 (Structure Property):** 堆是一棵 **完全二叉树 (Complete Binary Tree)**。这意味着除了最底层外，其他层都被完全填满，并且最底层的节点尽可能地靠左排列。
        2.  **堆序属性 (Heap Order Property):** 对于最小堆，任意节点的值都 **小于或等于 (less than or equal to)** 其子节点的值。这保证了根节点 (root) 始终是堆中的最小值。
*   **递归定义 (Recursive Definition):**
    *   一个完全二叉树 `T` 是一个最小堆，当且仅当：
        -   `T` 是空树，或者
        -   `T` 由根节点 `r`、左子树 `TL` 和右子树 `TR` 构成 (`T = {r, TL, TR}`)，并且：
            -   `r` 的值小于或等于 `TL` 和 `TR` 的根节点的值 (如果子树存在)。
            -   `TL` 和 `TR` 本身也都是最小堆。
*   **数组表示 (Array Representation):**
    *   堆非常适合用数组 (Array) 或动态数组 (Vector) 存储，效率很高。
    *   通常按照 **层序遍历 (Level Order Traversal)** 的顺序将树节点映射到数组元素。
    *   **重要约定:** 数组 **索引 0 通常不使用**，堆元素从索引 1 开始存储。这样做可以简化父子节点索引的计算。
    *   **索引映射 (Index Mapping) (基于 1 的索引):** 对于数组中索引为 `i` 的节点：
        -   **左子节点 (Left Child):** 索引为 $2 \times i$
        -   **右子节点 (Right Child):** 索引为 $2 \times i + 1$
        -   **父节点 (Parent):** 索引为 $\lfloor i / 2 \rfloor$ (即 C++ 中的整数除法 `i / 2`)
    *   **代码实现 (辅助函数):**
        ```cpp
        // 假设在 Heap<T> 类中
        private:
          size_t parent(size_t index) const {
            // assumes index > 0
            return index / 2;
          }

          size_t leftChild(size_t index) const {
            return 2 * index;
          }

          size_t rightChild(size_t index) const {
            return 2 * index + 1;
          }

          bool isLeaf(size_t index) const {
            // 如果节点的左孩子索引超出了堆的大小，它就是叶子节点
            return leftChild(index) > size_;
          }

          // 存储堆元素的动态数组 (使用 std::vector)
          std::vector<T> item_;
          // 当前堆中的元素数量
          size_t size_;

          // 注意：item_[0] 不存储有效数据
        ```

## Heap Operation
### 堆操作：插入 (Insert)

*   **目标:** 向堆中添加一个新元素，同时保持堆的结构属性和堆序属性。
*   **过程:**
    1.  **维护结构:** 将新元素添加到数组末尾的下一个可用位置 (即 `index = size_ + 1`)。
    2.  **恢复堆序 (`heapifyUp` / Percolate Up / 上滤):** 新加入的元素可能比其父节点小，违反了最小堆序。需要将这个新元素与其父节点比较：如果新元素更小，则交换它们。重复此过程，将元素沿着祖先路径向上移动，直到它不再小于其父节点或达到根节点 (index 1)。
*   **数组扩容 (`_growArray`):** 如果数组已满 (`size_ + 1 >= item_.size()` 或 `size_ == capacity_`)，需要先进行扩容 (通常容量加倍)。这是一个 **摊销 (Amortized)** 操作。
*   **代码实现:**
    ```cpp
    // 假设在 Heap<T> 类中
    public:
      void insert(const T& key) {
        // 1. 检查是否需要扩容 (假设 item_ 是 std::vector)
        //    注意：因为我们用 index 0，所以当 size_ + 1 == item_.size() 时就需要扩容
        if (size_ == item_.size()) {
          _growArray(); // 假设这个函数将 item_ 的容量加倍
        }

        // 2. 增加大小并将元素放在末尾
        size_++;
        item_[size_] = key;

        // 3. 上滤以恢复堆序
        _heapifyUp(size_);
      }

    private:
      void _heapifyUp(size_t index) {
        // 如果已经是根节点，停止
        if (index <= 1) {
          return;
        }

        size_t p_idx = parent(index);

        // 如果当前节点小于父节点，则交换并继续向上递归
        if (item_[index] < item_[p_idx]) {
          std::swap(item_[index], item_[p_idx]);
          _heapifyUp(p_idx);
        }
      }

      void _growArray() {
         // 实现数组扩容，例如将容量加倍
         // 对于 std::vector，可以直接 resize 或 reserve
         // 如果使用原始数组，则需要分配新内存、复制、释放旧内存
         size_t new_capacity = (item_.size() == 0) ? 2 : item_.size() * 2; // 初始大小为2，之后加倍
         item_.resize(new_capacity);
      }
    ```
*   **运行时间 (Running Time):** **$O(\log n)$** (不考虑摊销的扩容成本)。`heapifyUp` 最多比较和交换 $\log n$ 次。

### 堆操作：删除最小值 (RemoveMin)

*   **目标:** 从最小堆中移除并返回最小值 (即根节点)，同时保持堆的属性。
*   **过程:**
    1.  **获取最小值:** 根节点 (index 1) 就是最小值，先保存它。
    2.  **维护结构:** 将堆中 **最后一个元素** (在数组索引 `size_` 处) 移动到根节点 (index 1) 的位置。然后将堆的大小减一 (`size_--`)。
    3.  **恢复堆序 (`heapifyDown` / Percolate Down / 下滤):** 根节点的新值可能比其子节点大，违反了堆序。需要将这个节点与其 **较小的 (smaller)** 子节点进行比较。如果该节点大于其较小子节点，则交换它们。重复此过程，将元素沿着路径向下移动 (总是与较小子节点交换)，直到它不再大于其任何子节点或到达叶节点。
*   **代码实现:**
    ```cpp
    // 假设在 Heap<T> 类中
    public:
      T removeMin() {
        if (isEmpty()) {
          throw std::out_of_range("Heap is empty");
        }

        // 1. 保存根节点 (最小值)
        T minValue = item_[1];

        // 2. 将最后一个元素移到根
        item_[1] = item_[size_];

        // 3. 减小堆大小
        size_--;

        // 4. 从根开始下滤以恢复堆序
        if (!isEmpty()) { // 如果堆不为空，才需要下滤
             _heapifyDown(1);
        }

        // 5. 返回最小值
        return minValue;
      }

      bool isEmpty() const {
        return size_ == 0;
      }

    private:
      void _heapifyDown(size_t index) {
        // 如果是叶子节点，停止
        if (isLeaf(index)) {
          return;
        }

        // 找到较小孩子的索引
        size_t minChildIdx = _minChildIndex(index);

        // 如果当前节点大于其较小的孩子，则交换并继续向下递归
        if (item_[index] > item_[minChildIdx]) {
          std::swap(item_[index], item_[minChildIdx]);
          _heapifyDown(minChildIdx);
        }
      }

      // 辅助函数：找到 index 节点的较小孩子的索引
      size_t _minChildIndex(size_t index) const {
         size_t left = leftChild(index);
         size_t right = rightChild(index);

         // 如果右孩子不存在 (意味着只有左孩子，因为是完全二叉树)
         if (right > size_) {
             return left;
         } else {
             // 返回左右孩子中较小者的索引
             return (item_[left] < item_[right]) ? left : right;
         }
      }
    ```
*   **运行时间 (Running Time):** **$O(\log n)$**。`heapifyDown` 最多比较和交换 $\log n$ 次。

### 堆的构建 (BuildHeap)

*   **目标:** 给定一个包含 $n$ 个元素的无序数组，高效地将其原地转换为一个有效的堆。
*   **方法:**
    1.  排序法: 错误，排序后的数组不一定是堆。
    2.  重复插入法: 正确，但时间复杂度为 $O(n \log n)$。
    3.  **自底向上堆化 (Bottom-Up Heapify / Floyd's Algorithm):** 最高效的方法。
        -   **原理:** 数组中从索引 $\lfloor n / 2 \rfloor + 1$ 到 $n$ 的所有元素都是叶节点，天然满足堆属性。
        -   **过程:** 从最后一个 **非叶节点** (索引为 `parent(n)` 即 $\lfloor n / 2 \rfloor$) 开始，**向前** 遍历到根节点 (索引 1)。对遍历到的每个节点 `i`，调用 `_heapifyDown(i)`。
        -   **正确性:** 当对节点 `i` 调用 `_heapifyDown` 时，由于是自底向上处理，其左右子树 (如果存在) 已经满足堆属性。`_heapifyDown(i)` 会将 `item_[i]` 调整到以 `i` 为根的子树中的正确位置，使得整个子树成为一个堆。当处理到根节点 1 时，整个数组就变成了堆。
*   **代码实现:**

```cpp
    // 假设在 Heap<T> 类中
    public:
      // 构造函数：从一个现有 vector 构建堆
      Heap(const std::vector<T>& unsorted_items) {
        // 预留空间，index 0 不用
        item_.resize(unsorted_items.size() + 1);
        size_ = unsorted_items.size();

        // 将元素复制到 item_[1...size_]
        for (size_t i = 0; i < size_; ++i) {
          item_[i + 1] = unsorted_items[i];
        }

        // 调用 buildHeap 过程
        buildHeap();
      }

    // private or public depending on desired API
    // (通常作为构造函数的一部分或内部辅助函数)
    private:
      void buildHeap() {
        // 从最后一个非叶子节点开始，向前到根节点
        for (size_t i = parent(size_); i > 0; i--) {
          _heapifyDown(i);
        }
      }
    ```
*   **运行时间分析 (Running Time Analysis):** **$O(n)$**。虽然看起来是 $O(n \log n)$ (调用 $n/2$ 次 $O(\log n)$ 的 `heapifyDown`)，但精确分析表明，大部分 `heapifyDown` 操作作用在高度较低的子树上。所有 `heapifyDown` 操作的总工作量之和可以被证明是线性的。

### 堆排序 (Heap Sort)

*   **目标:** 利用堆结构对一个数组进行排序。
*   **标准算法 (原地升序排序 - In-place, Ascending Order):**
    1.  **建堆 (Build Heap):** 对输入的数组 `A` (大小为 $n$) 调用 `buildHeap`，但要建成 **最大堆 (Max-Heap)** (父节点 >= 子节点)。时间复杂度 $O(n)$。 *需要修改 `heapifyDown` 和 `buildHeap` 以处理 Max-Heap*。
    2.  **排序阶段 (Sorting Phase):**
        -   重复 $n-1$ 次 (for `i` from $n$ down to 2):
            a.  **交换 (Swap):** 交换堆顶元素 `A[1]` (当前最大值) 与当前堆的最后一个元素 `A[i]`。此时，数组末尾 `A[i]` 存放的是已排序好的元素 (当前找到的最大值)。
            b.  **减小堆大小 (Reduce Heap Size):** 将堆的有效大小视为 `i-1` (逻辑上排除 `A[i]`)。
            c.  **恢复堆序 (Restore Heap Property):** 对新的根节点 `A[1]` 调用 `_heapifyDown_max(1)`，在大小为 `i-1` 的堆上恢复最大堆属性。时间复杂度 $O(\log i)$。
*   **Slides 中的方法 (使用 Min-Heap):**
    *   如果使用 Min-Heap 并将 `removeMin` 的结果依次放入新数组，得到升序序列 (非原地)。
    *   如果使用 Min-Heap **原地** 排序 (如 Slide 54-56 演示的交换根和末尾元素)，最终数组会变成 **降序 (Descending Order)**。
*   **代码实现 (原地降序排序，使用已实现的 Min-Heap 类):**

    ```cpp
    // 这是一个全局函数，或者可以集成到 Heap 类中
    // 假设 arr 是一个包含元素的 std::vector (1-based index for simplicity here)
    template <typename T>
    void heapSortDescending(std::vector<T>& arr) {
        // 假设 arr[0] 不用，元素在 arr[1...n]
        if (arr.size() <= 1) return; // 0 或 1 个元素，无需排序

        // 1. 构建最小堆 (需要一个临时 Heap 对象或直接在 arr 上操作)
        //    这里为了演示，假设我们能在 arr 上直接操作 buildHeap
        //    (需要调整 buildHeap 和 heapifyDown 为能在外部数组上工作)
        size_t n = arr.size() - 1; // 实际元素数量
        // buildMinHeapOnArray(arr, n); // <--- 需要一个这样的函数

        // 2. 排序阶段
        for (size_t i = n; i > 1; i--) {
            // a. 交换根 (最小值) 与当前堆末尾元素
            std::swap(arr[1], arr[i]);

            // b. 减小堆大小 (逻辑上)，并对新根 heapifyDown
            // heapifyDownOnArray(arr, 1, i - 1); // <--- 需要这样的函数
        }
        // 排序后，arr[1...n] 变为降序
    }
    // 注意：实际实现 Heap Sort 通常直接在数组上操作，
    // 而不是依赖一个 Heap 类实例，上述代码仅为示意。
    ```
*   **运行时间 (Running Time):** **$O(n \log n)$** (建堆 $O(n)$ + 排序 $O(n \log n)$)。
*   **特点 (Properties):**
    *   **空间复杂度:** **$O(1)$** (如果是原地排序版本)。
    *   **不稳定性 (Not Stable):** 相等元素的相对顺序可能改变。

## 堆作为优先队列 (Priority Queue - PQ) 的实现

*   **优先队列 (Priority Queue):** 一种抽象数据类型 (ADT)，支持插入元素和提取具有最高 (或最低) 优先级的元素 (`removeMin` 或 `removeMax`)。
*   **堆的优势 (Heap's Advantage):**
    *   堆是实现优先队列的一种非常高效和常用的方式。
    *   **性能对比 (Performance Comparison):**



| 实现方式                  | `insert`        | `removeMin`     | `buildHeap` (批量构建) |
| :-------------------- | :-------------- | :-------------- | :----------------- |
| 无序数组 (Unsorted Array) | $O(1)$          | $O(n)$          | $O(n)$             |
| 无序链表                  | $O(1)$          | $O(n)$          | $O(n)$             |
| 有序数组 (Sorted Array)   | $O(n)$          | $O(1)$          | $O(n \log n)$      |
| 有序链表                  | $O(n)$          | $O(1)$          | $O(n\log n)$       |
| AVL 树 (AVL Tree)      | $O(\log n)$     | $O(\log n)$     | $O(n \log n)$      |
| **二叉堆 (Binary Heap)** | **$O(\log n)$** | **$O(\log n)$** | **$O(n)$**         |


-    堆在 `insert` 和 `removeMin` 操作上提供了很好的 $O(\log n)$ 平衡，并且 `buildHeap` 操作非常快 ($O(n)$)。
-   **应用抽象 (Array Abstractions):**
    -   展示了抽象层次：底层是 **数组 (Array)** -> 基于数组实现 **堆 (Heap)** -> 堆用来实现 **优先队列 (PQ)** -> PQ 用于各种应用 (如任务列表 ToDo List, 图算法 Graph Implementation 等)。
