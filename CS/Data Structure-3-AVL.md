---
title: Data Structure-3
date: 2025-04-09
date modified: 2025-04-09
categories: CS225
tags:
  - CS225
---

#CS225 
## AVL

### Motivation

-   **BST 的局限性 (BST Limitation):** 一个普通的二叉搜索树 (Binary Search Tree, BST) 的高度 ($h$) 范围可以从 $lg(n)$ (最佳情况，树比较平衡) 到 $n$ (最坏情况，树倾斜得像一个链表，或称为 "stick" 形状)。由于 BST 的基本操作 (插入 insert, 删除 delete, 查找 find) 的时间复杂度都是 $O(h)$，在最坏情况下，这些操作会变成 $O(n)$。这对于性能来说并不理想。
-   **目标 (Goal):** 我们希望有一种数据结构，既能保持 BST 的性质 (元素有序，便于高效搜索)，又能*保证*结构的平衡，确保树的高度 $h$ 始终接近最优的 $O(log n)$。这就引出了**高度平衡树 (Height-Balanced Trees)** 的概念。

### AVL 属性：定义高度平衡

-   **高度平衡因子 (Height Balance Factor, b):** 对于树中的任意节点 `t`，其平衡因子定义为：
    $$
    b(t) = height(t \rightarrow right) - height(t \rightarrow left)
    $$
    其中 `height(NULL)` (空节点的高度) 通常定义为 -1。
-   **AVL 条件 (AVL Condition):** 如果对于树中的**每一个节点 `t`**，其平衡因子 $b(t)$ 都在集合 $\{-1, 0, 1\}$ 中，那么这棵树就是一棵 AVL 树。换句话说，任何节点的左子树和右子树的高度差最多为 1。
-   **不平衡检测 (Imbalance Detection):** 如果在插入或删除操作后，任何节点 `t` 的平衡因子满足 $b(t) \ge 2$ 或 $b(t) \le -2$，那么 AVL 属性就被破坏了，这棵树需要在该节点处进行**再平衡 (rebalancing)**

### 关键实现细节：存储高度

-   为了能高效地检查平衡因子并执行旋转，AVL 树通常会在**每个节点结构中直接存储以该节点为根的子树的高度 (height)**。
    ```cpp
  
    struct TreeNode {
        T key;             // 键值
        unsigned height; // 存储以此节点为根的子树的高度
        TreeNode *left;    // 左子节点指针
        TreeNode *right;   // 右子节点指针
    };
    ```

-   这使得计算平衡因子和在旋转后更新高度都可以在**常数时间 ($O(1)$)** 内完成，正如 ("height adjustment in const time" - 高度调整是常数时间操作)。如果不存储高度，计算它就需要遍历子树，这将使得平衡过程慢得多。

### 恢复平衡：AVL 旋转 (AVL Rotations)

-   **目的 (Purpose):** 当在某个节点 (我们称之为 `z`) 检测到不平衡时，我们使用旋转操作来恢复 AVL 属性 ($|b| \le 1$)，同时关键地要**保持 BST 的搜索属性 (BST search property)**。旋转是局部的指针修改操作，花费 $O(1)$ 时间。

[[Data Structure-2#核心旋转操作]]

-   **四种旋转情况 (The Four Rotation Cases):** 根据导致不平衡的插入/删除路径 (相对于从修改点向上回溯时遇到的第一个不平衡节点 `z`) 识别了四种情况。
    1.  **左旋 (Left Rotation, L / RR Case):**
        -   **触发条件 (Trigger):** 节点 `z` 不平衡，$b(z) = 2$，并且不平衡是由于插入到 `z` 的*右*子节点 (`y`) 的*右*子树中引起的。(路径：右-右，Right-Right)。
        -   **条件检查:** `balance(z) == 2` 并且 `balance(z->right) == 1`。(注意：删除时 `balance(z->right)` 也可能为 0)。
        -   **操作 (Action):** 围绕 `z` 执行一次**左旋 (Left Rotation)**。`y` 成为这个子树的新根。
        -   **比喻 (Analogy):** 修正一个向右倾斜过度的 ">" 形状。
    2.  **右旋 (Right Rotation, R / LL Case):**
        -   **触发条件 (Trigger):** 节点 `z` 不平衡，$b(z) = -2$，并且不平衡是由于插入到 `z` 的*左*子节点 (`y`) 的*左*子树中引起的。(路径：左-左，Left-Left)。
        -   **条件检查:** `balance(z) == -2` 并且 `balance(z->left) == -1`。(注意：删除时 `balance(z->left)` 也可能为 0)。
        -   **操作 (Action):** 围绕 `z` 执行一次**右旋 (Right Rotation)**。`y` 成为新根。
        -   **比喻 (Analogy):** 修正一个向左倾斜过度的 "<" 形状。
    3.  **左右旋 (Left-Right Rotation, LR Case):**
        -   **触发条件 (Trigger):** 节点 `z` 不平衡，$b(z) = -2$，但！不平衡是由于插入到 `z` 的*左*子节点 (`y`) 的*右*子树中引起的。(路径：左-右，Left-Right，一个 "之" 字形)。
        -   **条件检查:** `balance(z) == -2` 并且 `balance(z->left) == 1`。
        -   **操作 (Action):** 这是一个两步过程：
            1.  围绕子节点 `y` (`z->left`) 执行一次**左旋 (Left Rotation)**。
            2.  围绕原始不平衡节点 `z` 执行一次**右旋 (Right Rotation)**。
            "之" 字路径上的孙子节点 (`x`) 成为新根。
        -   **比喻 (Analogy):** 在旋转之前，先把 "<" 形的弯折处捋直。
    4.  **右左旋 (Right-Left Rotation, RL Case):**
        -   **触发条件 (Trigger):** 节点 `z` 不平衡，$b(z) = 2$，但！不平衡是由于插入到 `z` 的*右*子节点 (`y`) 的*左*子树中引起的。(路径：右-左，Right-Left，一个 "之" 字形)。
        -   **条件检查:** `balance(z) == 2` 并且 `balance(z->right) == -1`。
        -   **操作 (Action):** 这是一个两步过程：
            1.  围绕子节点 `y` (`z->right`) 执行一次**右旋 (Right Rotation)**。
            2.  围绕原始不平衡节点 `z` 执行一次**左旋 (Left Rotation)**。
            "之" 字路径上的孙子节点 (`x`) 成为新根。
        -   **比喻 (Analogy):** 在旋转之前，先把 ">" 形的弯折处捋直。

-   **确定旋转方式 (Finding the Rotation):** 要确定在不平衡节点 `t` 处应执行哪种旋转，你需要检查它的平衡因子 `b(t)` *以及*不平衡方向上的子节点的平衡因子 (如果 `b(t) == -2` 则检查 `t->left`，如果 `b(t) == 2` 则检查 `t->right`)。这个子节点的平衡因子会告诉你这是直线型的 "stick" (LL/RR) 还是 "之" 字形的 "zig-zag" (LR/RL)。

### AVL 插入 (AVL Insertion)

-   **过程:** AVL 插入通常递归实现。对于给定节点 `t` 和键 `x`：
    1.  **在正确位置插入 (Insert at proper place):** 执行标准的 BST 递归插入。如果 `t` 是 NULL，创建一个高度为 0 的新节点。如果 `x < t->key`，向左递归；如果 `x > t->key`，向右递归。
    2.  **(递归调用返回后) 检查不平衡 (Check for imbalance):** 计算平衡因子 `b(t) = height(t->right) - height(t->left)`。
    3.  **如有必要，执行旋转 (Rotate, if necessary):** 如果 $|b(t)| > 1$，根据 `b(t)` 和相关子节点的平衡因子 (如旋转部分和 C++ 代码所述) 确定正确的旋转情况 (LL, RR, LR, RL)。执行旋转。旋转函数返回修改后子树的*新*根，这会更新指针 (`t` 在 C++ 代码中)。
    4.  **更新高度 (Update height):** 更新当前节点 `t` 的高度: `t->height = 1 + max(height(t->left), height(t->right))`。


Implementation

```c++

#include <algorithm> // for std::max
#include <iostream>  // for potential debugging output

// --- 1. 节点结构 (Node Structure) ---
template <typename T>
struct TreeNode {
    T key;              // 节点存储的键值 (Key)
    int height;         // 以此节点为根的子树的高度 (Height)
    TreeNode *left;     // 指向左子节点的指针 (Left child pointer)
    TreeNode *right;    // 指向右子节点的指针 (Right child pointer)

    // 构造函数 (Constructor)
    TreeNode(T k, TreeNode* l = nullptr, TreeNode* r = nullptr)
        : key(k), height(0), left(l), right(r) {} // 新节点高度初始为 0
};

// --- 2. 辅助函数 (Helper Functions) ---

// 获取节点高度 (安全地处理空指针)
// Get the height of a node (handles NULL safely)
template <typename T>
int height(TreeNode<T>* node) {
    if (node == nullptr) {
        return -1; // 空树的高度定义为 -1 (Height of NULL node is -1)
    }
    return node->height;
}

// 更新节点高度
// Update the height of a node based on its children's heights
template <typename T>
void updateHeight(TreeNode<T>* node) {
    if (node != nullptr) {
        node->height = 1 + std::max(height(node->left), height(node->right));
    }
}

// 获取平衡因子
// Get the balance factor of a node
template <typename T>
int getBalance(TreeNode<T>* node) {
    if (node == nullptr) {
        return 0; // 空节点的平衡因子为 0 (Balance factor of NULL node is 0)
    }
    // Balance factor = height(right subtree) - height(left subtree)
    return height(node->right) - height(node->left);
}


// --- 3. 旋转操作 (Rotation Operations) ---
// 右旋 (LL Case) -围绕 z 进行
// Right Rotation (for LL Imbalance) - Pivot is z
template <typename T>
TreeNode<T>* rightRotate(TreeNode<T>* z) {
    TreeNode<T>* y = z->left;       // y 是 z 的左孩子
    TreeNode<T>* T3 = y->right;     // T3 是 y 的右子树

    // 执行旋转
    y->right = z;
    z->left = T3;

    // 更新高度 (必须先更新 z, 再更新 y)
    // Update heights (must update z first, then y)
    updateHeight(z);
    updateHeight(y);

    // 返回旋转后子树的新根 (y)
    // Return the new root of the subtree (y)
    return y;
}

// 左旋 (RR Case) - 围绕 z 进行
// Left Rotation (for RR Imbalance) - Pivot is z
template <typename T>
TreeNode<T>* leftRotate(TreeNode<T>* z) {
    TreeNode<T>* y = z->right;      // y 是 z 的右孩子
    TreeNode<T>* T2 = y->left;      // T2 是 y 的左子树

    // 执行旋转
    y->left = z;
    z->right = T2;

    // 更新高度 (必须先更新 z, 再更新 y)
    // Update heights (must update z first, then y)
    updateHeight(z);
    updateHeight(y);

    // 返回旋转后子树的新根 (y)
    // Return the new root of the subtree (y)
    return y;
}

// 左右旋 (LR Case) - 先对 y 左旋，再对 z 右旋
// Left-Right Rotation (for LR Imbalance) - Left rotate y, then right rotate z
template <typename T>
TreeNode<T>* leftRightRotate(TreeNode<T>* z) {
    // 对 z 的左孩子 y 进行左旋
    // Left rotate the left child y
    z->left = leftRotate(z->left);
    // 对 z 进行右旋，并返回新根
    // Right rotate z and return the new root
    return rightRotate(z);
}

// 右左旋 (RL Case) - 先对 y 右旋，再对 z 左旋
// Right-Left Rotation (for RL Imbalance) - Right rotate y, then left rotate z
template <typename T>
TreeNode<T>* rightLeftRotate(TreeNode<T>* z) {
    // 对 z 的右孩子 y 进行右旋
    // Right rotate the right child y
    z->right = rightRotate(z->right);
    // 对 z 进行左旋，并返回新根
    // Left rotate z and return the new root
    return leftRotate(z);
}

// --- 4. 插入操作 (Insertion Operation) ---
// (基于幻灯片中的 insert_ 递归辅助函数模板)
// (Based on the recursive helper function template `insert_` from the slides)
template <class T>
class AVLTree { // 假设这些函数在一个 AVLTree 类中
public:
    TreeNode<T>* root = nullptr;

    void insert(const T & x) {
        root = insert_(x, root);
    }

private:
    TreeNode<T>* insert_(const T & x, TreeNode<T>* t) {
        // 1. 执行标准 BST 插入 (Perform standard BST insert)
        if (t == nullptr) {
            return new TreeNode<T>(x); // 创建新节点，高度为 0
        }

        if (x < t->key) {
            t->left = insert_(x, t->left);
        } else if (x > t->key) {
            t->right = insert_(x, t->right);
        } else {
            // 不允许重复键 (Duplicate keys not allowed or handle as needed)
            return t;
        }

        // 2. 更新当前节点的高度 (Update height of the current node)
        updateHeight(t);

        // 3. 获取平衡因子并检查是否失衡 (Get balance factor and check for imbalance)
        int balance = getBalance(t);

        // 4. 如果失衡，执行相应的旋转 (If unbalanced, perform rotations)

        // LL Case (左子树过高，且插入发生在左子树的左侧)
        if (balance < -1 && x < t->left->key) { // 或者检查 getBalance(t->left) <= -1 (标准通常用-1)
             return rightRotate(t);
        }

        // RR Case (右子树过高，且插入发生在右子树的右侧)
        if (balance > 1 && x > t->right->key) { // 或者检查 getBalance(t->right) >= 1 (标准通常用 1)
            return leftRotate(t);
        }

        // LR Case (左子树过高，但插入发生在左子树的右侧)
        if (balance < -1 && x > t->left->key) { // 或者检查 getBalance(t->left) == 1
            return leftRightRotate(t);
        }

        // RL Case (右子树过高，但插入发生在右子树的左侧)
        if (balance > 1 && x < t->right->key) { // 或者检查 getBalance(t->right) == -1
            return rightLeftRotate(t);
        }

        // 5. 返回 (可能已旋转或未旋转的) 子树根节点
        // Return the (possibly rotated) subtree root
        return t;
    }

    // --- 5. 删除操作 (Deletion Operation - 伪代码/概念) ---
    /*
    TreeNode<T>* remove_(const T& x, TreeNode<T>* t) {
        // 1. 执行标准 BST 删除 (Perform standard BST delete)
        if (t == nullptr) { return t; } // 未找到 (Not found)

        if (x < t->key) {
            t->left = remove_(x, t->left);
        } else if (x > t->key) {
            t->right = remove_(x, t->right);
        } else {
            // 找到节点 (Node found)
            if (t->left == nullptr || t->right == nullptr) {
                // 0 或 1 个子节点 (0 or 1 child)
                TreeNode<T>* temp = t->left ? t->left : t->right;
                if (temp == nullptr) { // 无子节点 (No child)
                    temp = t;
                    t = nullptr;
                } else { // 一个子节点 (One child)
                    *t = *temp; // 拷贝内容 (Copy contents)
                }
                delete temp; // 删除旧节点或临时节点 (Delete old node or temp)
                // 注意: 如果使用拷贝内容的方式，需要确保正确处理指针和内存
            } else {
                // 2 个子节点 (2 children)
                // 找到中序后继 (或前驱) (Find inorder successor (or predecessor))
                TreeNode<T>* temp = findMin(t->right); // 假设有 findMin 函数
                // 拷贝后继的值到当前节点 (Copy successor's key)
                t->key = temp->key;
                // 从右子树中删除该后继 (Delete the successor from right subtree)
                t->right = remove_(temp->key, t->right);
            }
        }

        // 如果树在删除后变为空 (If tree became empty after deletion)
        if (t == nullptr) {
          return t;
        }

        // (关键步骤) 从删除点向上回溯，更新高度并检查平衡
        // (Key Step) Backtrack from deletion point, update height & check balance

        // 2. 更新高度 (Update height)
        updateHeight(t);

        // 3. 获取平衡因子 (Get balance factor)
        int balance = getBalance(t);

        // 4. 检查并执行旋转 (Check and perform rotations)
        //    (需要检查左右子节点的平衡因子来确定是单旋还是双旋)
        // LL Case (可能由右侧删除引起左侧过高)
        if (balance < -1 && getBalance(t->left) <= 0) { // 可能为 -1 或 0
            return rightRotate(t);
        }
        // LR Case
        if (balance < -1 && getBalance(t->left) > 0) { // 必须为 1
            return leftRightRotate(t);
        }
        // RR Case (可能由左侧删除引起右侧过高)
        if (balance > 1 && getBalance(t->right) >= 0) { // 可能为 1 或 0
            return leftRotate(t);
        }
        // RL Case
        if (balance > 1 && getBalance(t->right) < 0) { // 必须为 -1
            return rightLeftRotate(t);
        }

        // 5. 返回节点 (Return node)
        return t;
    }

    // (需要 findMin 辅助函数)
    TreeNode<T>* findMin(TreeNode<T>* node) {
        TreeNode<T>* current = node;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current;
    }
    */
}; // end of AVLTree class definition
```



### AVL 删除 (AVL Deletion)

-   **过程 (Process):**
    1.  执行标准的 BST 删除 (找到节点，处理 0/1 个子节点的情况，或者找到**中序前驱 (In-Order Predecessor, IOP)** / **中序后继 (In-Order Successor, IOS)**，交换值，然后删除叶子节点或只有单个子节点的节点)。
    2.  **回溯并重新平衡 (Retrace and Rebalance):** 从被*删除*节点的父节点开始，沿着路径向根节点回溯。
    3.  在每个祖先节点处，更新其高度并检查其平衡因子。
    4.  如果发现不平衡，执行适当的旋转 (LL, RR, LR, RL) 来恢复平衡。
-   **与插入的关键区别 (Key Difference from Insertion):** 删除可能更复杂，因为**一次删除可能需要多次旋转** (最坏情况下需要 $O(log n)$ 次旋转)，因为在一个层级修复不平衡可能会导致更高层级的祖先节点变得不平衡。再平衡过程必须沿着路径一直进行，直到到达根节点或整个路径都恢复平衡。

**注意AVL的删除可能存在多次旋转，在每一次向下调用结束以后都要注意Retain Balance**

**总结要点:**

1.  **节点高度:** `TreeNode` 结构中包含 `height` 成员。
2.  **辅助函数:** `height()` 用于安全获取高度，`updateHeight()` 用于更新高度，`getBalance()` 用于计算平衡因子。
3.  **旋转:** 四种旋转 (`rightRotate`, `leftRotate`, `leftRightRotate`, `rightLeftRotate`) 是核心，它们在 $O(1)$ 时间内完成指针调整并更新受影响节点的高度。
4.  **插入:** 递归地执行 BST 插入，然后在回溯时更新高度、检查平衡，并在必要时调用适当的旋转函数。插入最多只需要一次旋转 (单或双)。
5.  **删除:** 同样递归地执行 BST 删除 (可能涉及查找前驱/后继)，然后在回溯时更新高度、检查平衡。与插入不同，删除**可能需要在多个层级上进行旋转**才能完全恢复平衡，因此检查和旋转逻辑在每次递归返回时都要执行。删除的旋转条件判断（特别是子节点的平衡因子）比插入稍有不同，需要考虑子节点平衡因子为 0 的情况。


### AVL 树高度分析

-   **目标：** 证明 AVL 树的高度 $h$ 是 $O(log n)$，其中 $n$ 是树中节点的数量。这意味着 AVL 树的高度最多与节点数的对数成正比，确保了高效的查找、插入和删除操作。
-   **证明策略：**
    1.  **定义 N(h):** 定义函数 $N(h)$ 为高度为 $h$ 的 AVL 树所能拥有的**最少节点数**。这是证明的关键。
    2.  **导出递推关系:** 为了保证 AVL 树的平衡性（任意节点的左右子树高度差不超过 1），具有最少节点的 AVL 树的构造方式是让一个子树的高度为 $h-1$，另一个子树的高度为 $h-2$。因此得到递推关系：
        $$
        N(h) = 1 + N(h-1) + N(h-2)
        $$
    3.  **基本情况:**
        -   $N(-1) = 0$
        -   $N(0) = 1$
        -   $N(1) = 2$
    4.  **简化递推式:**
        -   $N(h) > 2 \cdot N(h-2)$
    5.  **猜测：**
        -   $N(h) > 2^{h/2}$

-   **归纳证明 (Inductive Proof):**
    1.  **定理:** 高度为 $h$ 的 AVL 树至少有 $2^{h/2}$ 个节点。
    2.  **基本情况 (Base Cases):**
        -   $h=1$: $N(1) = 2 > 2^{1/2} \approx 1.414$ (成立)
        -   $h=2$: $N(2) = 4 > 2^{2/2} = 2$ (成立)
    3.  **归纳假设 (Inductive Hypothesis):** 假设对于所有 $j < h$，都有 $N(j) > 2^{j/2}$ 成立。
    4.  **归纳步骤 (Inductive Step):** 证明 $N(h) > 2^{h/2}$。
        -   $N(h) > 2 \cdot N(h-2) > 2 \cdot 2^{(h-2)/2} = 2^{h/2}$
        -   因此，归纳步骤成立。
-   **结论:** 高度为 h 的 AVL 树最少节点数 N(h) > 2^(h/2)
-   **倒推:**
    -   $n \ge N(h) > 2^{h/2}$
    -   $log(n) > h/2$
    -   $h < 2 \cdot log(n)$
-   **最终结论:** $h = O(log n)$。 这意味着 AVL 树的高度最多与节点数的对数成正比，确保了高效的操作性能。

### 红黑树与 AVL 树的比较

| 特性 (Feature)            | 红黑树 (Red-Black Tree)                    | AVL 树 (AVL Tree)                |
| ----------------------- | --------------------------------------- | ------------------------------- |
| 最大高度 (Max Height)       | $2 \cdot lg(n)$                         | $1.44 \cdot lg(n)$              |
| 插入旋转 (Insert Rotations) | 常数次 (Constant)                          | 最多 1 次 (单旋或双旋) (Max 1)          |
| 删除旋转 (Remove Rotations) | 常数次 (Constant)                          | $O(log n)$                      |
| 查找旋转 (Find Rotations)   | 0                                       | 0                               |
| 平衡性 (Balance)           | 弱平衡 (Weaker)                            | 强平衡 (Stronger)                  |
| 适用性 (Applicability)     | 更适用于频繁的插入和删除操作 (Frequent Insert/Delete) | 更适用于查找操作较多的场景 (Frequent Search) |

**要点:**

-   **平衡性:** AVL 树比红黑树更平衡，因此查找操作通常更快。
-   **旋转:** AVL 树在插入和删除操作时可能需要更多的旋转来维持平衡，这可能会影响性能。红黑树的旋转次数受到限制，通常更适合频繁的插入和删除操作。
-   **实际应用:** 红黑树在实际应用中更为常见，因为它们在平衡性和旋转次数之间取得了较好的折衷。例如，Java 的 `TreeMap` 和 C++ 的 `std::map` 都使用红黑树实现。



### 数据结构复杂度比较 



| 操作 (Operation) | 未排序数组 (Unsorted Array) | 排序数组 (Sorted Array) | 未排序链表 (Unsorted List) | 排序链表 (Sorted List) | 一般二叉树 (Binary Tree) | BST (二叉搜索树) | AVL 树 (AVL Tree) |
| :--------------- | :-------------------------- | :---------------------- | :------------------------- | :--------------------- | :----------------------- | :----------------------- | :---------------------- |
| **查找 (Find)**  | $O(n)$                      | $O(\log n)$             | $O(n)$                     | $O(n)$                 | $O(n)$                   | $O(h)$                   | $O(\log n)$             |
| **插入 (Insert)**| $O(1)$ (摊销 Amortized)     | $O(n)$                  | $O(1)$ (头插 Head Insert)  | $O(n)$                 | $O(n)$                   | $O(h)$                   | $O(\log n)$             |
| **删除 (Remove)**| $O(n)$ (查找+移动/交换)     | $O(n)$ (查找+移动)      | $O(n)$ (查找+删除)         | $O(n)$ (查找+删除)     | $O(n)$                   | $O(h)$                   | $O(\log n)$             |
| **遍历 (Traverse)**| $O(n)$                      | $O(n)$                  | $O(n)$                     | $O(n)$                 | $O(n)$                   | $O(n)$                   | $O(n)$                  |

**复杂度解释:**

1.  **未排序数组 (Unsorted Array):**
    -   查找: 最坏情况需要检查每个元素。
    -   插入: 在末尾添加是 $O(1)$ (如果有空间)，但可能需要调整大小 (摊销 Amortized $O(1)$)。幻灯片显示 $O(1)$, 可能假设是简单追加或在已知位置插入。
    -   删除: 需要先找到元素 ($O(n)$)，然后移动元素 ($O(n)$) 或与最后一个元素交换 ($O(1)$)。幻灯片写 `find + O(1)`，意味着找到后与末尾交换。总时间是 $O(n)$。
    -   遍历: 访问每个元素。

2.  **排序数组 (Sorted Array):**
    -   查找: 可以使用二分搜索 (binary search)，效率很高 ($O(\log n)$)。
    -   插入: 需要找到正确的位置 ($O(\log n)$ 或 $O(n)$)，然后移动元素 ($O(n)$)。总时间 $O(n)$。幻灯片写 `find + O(n)`，即 $O(\log n) + O(n) = O(n)$。
    -   删除: 需要找到元素 ($O(\log n)$)，然后移动元素填补空位 ($O(n)$)。总时间 $O(n)$。幻灯片写 `find + O(n)`，即 $O(\log n) + O(n) = O(n)$。
    -   遍历: 访问每个元素。

3.  **未排序链表 (Unsorted Linked List):**
    -   查找: 可能需要沿着指针 (pointer) 遍历整个列表。
    -   插入: 在头部插入是 $O(1)$。在其他位置插入需要先找到位置 ($O(n)$)。幻灯片显示 $O(1)$，意指头插。
    -   删除: 需要找到节点 ($O(n)$)，然后更新指针 ($O(1)$)。总时间 $O(n)$。幻灯片写 `find + O(1)`。
    -   遍历: 访问每个元素。

4.  **排序链表 (Sorted Linked List):**
    -   查找: 即使已排序，仍需从头线性遍历。
    -   插入: 找到正确位置 ($O(n)$) 并更新指针 ($O(1)$)。总时间 $O(n)$。幻灯片写 `find + O(1)`。
    -   删除: 找到节点 ($O(n)$) 并更新指针 ($O(1)$)。总时间 $O(n)$。幻灯片写 `find + O(1)`。
    -   遍历: 访问每个元素。

5.  **一般二叉树 (Binary Tree, 不一定是 BST):**
    -   查找/插入/删除: 在最坏情况下 (例如，树倾斜成链表状)，操作可能需要 $O(n)$ 时间。

6.  **BST (二叉搜索树 Binary Search Tree):**
    -   查找/插入/删除: 性能取决于树的高度 (height) $h$。在最佳/平均情况下，$h \approx \log n$。在最坏情况下 (倾斜树)，$h = n$。所以复杂度是 $O(h)$。插入/删除涉及查找位置/节点 ($O(h)$)，然后执行少量指针更新或简单修复 (如用后继/前驱替换)，因此 `find + O(1)` 实际上意味着 $O(h)$。
    -   遍历: 仍需访问每个节点。

7.  **AVL 树 (AVL Tree, 一种平衡 BST):**
    -   **核心思想:** AVL 树维护平衡因子 (balance factor) 并执行旋转 (rotation) 操作，以确保树的高度 $h$ 始终为 $O(\log n)$。
    -   查找/插入/删除: 由于高度保证是对数级的，这些操作都是 $O(\log n)$。插入和删除包括查找位置的成本 ($O(\log n)$) 以及可能沿路径向上的旋转成本 (也是 $O(\log n)$)。
    -   遍历: 仍需访问每个节点。

**结论:** 对于搜索密集型应用，AVL 树提供了有保证的对数时间 ($O(\log n)$) 查找、插入和删除性能，相比普通 BST (最坏情况 $O(n)$) 和线性结构具有显著优势。

### Application
#### 一维范围搜索 (1D Range-based Searches)

这部分内容将平衡 BST (如 AVL 树) 的概念应用于解决查找特定范围内所有数据点的问题。

**问题:** 给定一组一维 (1D) 点 $p = \{p_1, p_2, ..., p_n\}$，找出所有满足 $low \le p_i \le high$ 的点 $p_i$。例如：找出在区间 $[11, 42]$ 内的点。

**方法一：排序数组 (Sorted Array)**
1.  **预处理 (Preprocessing):** 创建点的排序数组。成本: $O(n \log n)$。
2.  **查询 (Query):**
    -   使用二分搜索找到第一个 $\ge low$ 的元素的索引：$O(\log n)$。
    -   使用二分搜索找到最后一个 $\le high$ 的元素的索引：$O(\log n)$。
    -   遍历这两个索引之间的数组元素，收集结果。如果范围内有 $k$ 个点，此步骤耗时 $O(k)$。
3.  **总查询时间 (假设数组已排序):** $O(\log n + k)$。
4.  **总时间 (包括排序):** $O(n \log n + k)$。幻灯片上的 $O(n \log n + k)$ 指的是从头开始的这个总时间。

**方法二：平衡 BST (例如 AVL 树)**
1.  **预处理:** 从点构建一个平衡 BST。成本: $O(n \log n)$ (插入 $n$ 个元素，每个 $O(\log n)$)。幻灯片演示了（隐式平衡的）构建过程。Slide 35 展示了示例点 {3, 6, 11, 33, 41, 44, 55} 的一个可能的平衡 BST。
2.  **查询 (查找 $[low, high]$ 内的点):**
    -   核心思想是遍历树，但要“剪枝” (prune branches)，即跳过那些不可能包含目标范围内点的子树。
    -   **算法:** 我们可以定义一个递归函数 (recursive function)，例如 `findInRange(node, low, high, results)`:
        1.  如果 `node` 为空，返回。
        2.  检查左子树: 如果当前节点值可能 $\ge low$，则左子树 *可能* 包含范围内的值。
        If `node.value >= low`:
           `findInRange(node.left, low, high, results)`
        3.  检查当前节点: 如果当前节点值在范围内，添加它。
        If `low <= node.value <= high`:
           将 `node.value` 添加到 `results`。
        4.  检查右子树: 如果当前节点值可能 $\le high$，则右子树 *可能* 包含范围内的值。
        If `node.value <= high`:
           `findInRange(node.right, low, high, results)`
    -   **示例追踪 (Search for [11, 42]):**
        - 从根 (33) 开始。`33 >= 11`，向左走。`33 <= 42`，最终会向右走。
        - 向左到 (6)。`6 < 11`，只需检查右边。
        - 从 (6) 向右到 (11)。`11 >= 11`，检查左边 (空)。`11 >= 11` 且 `11 <= 42`，添加 11。`11 <= 42`，检查右边 (叶子 33)。
        - 从 (11) 向右到叶子 (33)。`33 >= 11`，检查左边 (空)。`33 >= 11` 且 `33 <= 42`，添加 33。`33 <= 42`，检查右边 (空)。
        - 回溯到根 (33)。左边已检查。`33 >= 11` 且 `33 <= 42`，添加 33 (取决于实现细节，通常在遍历中添加叶子节点或值)。`33 <= 42`，向右走。
        - 从 (33) 向右到 (44)。`44 >= 11`，向左走。`44 > 42`，所以 *不* 向右走。
        - 从 (44) 向左到 (41)。`41 >= 11`，检查左边 (空)。`41 >= 11` 且 `41 <= 42`，添加 41。`41 <= 42`，检查右边 (叶子 44)。
        - 从 (41) 向右到叶子 (44)。`44 >= 11`，检查左边 (空)。`44 > 42`，不添加。`44 > 42`，不检查右边。

    -   **时间复杂度 (Slides 45-48):**
        - 找到树的相关部分 (大致是从根到范围内最小和最大元素的路径)：$O(\log n)$。
        - 访问实际在范围内的 $k$ 个节点：$O(k)$。
        - **总查询时间:** $O(\log n + k)$。这种方法效率高，因为我们不需要检查查询范围之外的树的部分。
        - Slide 48 正确地总结了查询复杂度。提到的 $O(n \log n)$ 指的是初始建树时间。

**技术比喻:** 在 BST 中进行一维范围搜索，就像在图书馆的特定区域找书。你使用目录 (树结构) 快速定位到大致的起点和终点 ($O(\log n)$)，然后在书架的那个特定区域走动，收集所有符合条件的书 ($O(k)$)。



#### 二维范围搜索与 kD 树 (2D Range-based Searches & kD-Trees) 
这部分将思想扩展到二维 (2D) 数据。

**问题:**
1.  给定二维点 $p = \{(x_1, y_1), ..., (x_n, y_n)\}$，找出矩形区域 $[(x_1, y_1), (x_2, y_2)]$ 内的所有点。
2.  找到距离查询点 $(x_q, y_q)$ 最近的点 (Nearest Neighbor Search)。

**挑战:** 标准的 BST 只能按一个维度排序。我们如何有效地在二维 (或更高维度) 中搜索？

**解决方案思路：kD 树 (k-dimensional Tree)**
-   幻灯片通过展示如何构建一个分割 (partition) 二维空间的树结构来引入这个概念。
-   **构建原则 (Slides 51-60):**
    1.  它是一棵二叉树，概念上类似于 BST。
    2.  与总是使用相同键进行比较不同，用于分割的 **维度 (dimension) 在树的每一层交替 (alternate)** 进行。
    3.  **第 0 层 (根节点):** 根据点的 **x 坐标** 进行分割。通常选择 x 坐标的中位数 (median) 作为分割值。$x < x_{median}$ 的点进入左子树，$x \ge x_{median}$ 的点进入右子树。这对应于二维空间中的一条垂直分割线 (Slide 54)。
    4.  **第 1 层:** 该层的所有节点根据点的 **y 坐标** 进行分割。在左子节点的点集中找到 y 坐标的中位数并分割。对右子节点的点集做同样操作。这对应于在先前区域内的水平分割线 (Slides 55 & 56)。
    5.  **第 2 层:** 再次根据 **x 坐标** 进行分割 (Slides 57 & 58)。
    6.  **继续:** 随着树的深度增加，循环使用维度 (x, y, x, y, ...) 进行分割。
-   **树结构:**
    -   **内部节点 (Internal Nodes):** 代表分割维度和分割值 (即分割线/面)。("Inner nodes are partitions")
    -   **叶节点 (Leaf Nodes):** 代表实际的数据点 (或一小桶点)。("Leaf nodes are points")
-   Slide 60 明确将此结构命名为 **kD-Tree**，并展示了空间的最终分割方式以及对应的树结构。

**技术比喻:** 构建 kD 树就像递归地切蛋糕。首先，你沿着中间垂直切一刀 (x 轴分割)。然后，你把得到的两半分别水平切开 (y 轴分割)。接着，你把得到的四个象限再分别垂直切开，以此类推，将空间分割成越来越小的矩形区域。

**核心要点:** kD 树是一种将二叉搜索树概念应用于处理多维数据 (multi-dimensional data) 的方法，它通过在不同树层级交替使用不同维度来进行空间分割。这使得在多维空间中进行高效的范围搜索和最近邻搜索成为可能 (尽管实际的搜索算法比一维情况更复杂，可能在后续课程中讲解)。


