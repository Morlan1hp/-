# 第 11 章（第 12 讲）更多分治：二叉树、树的遍历、分治最近点对

> **本章位置**：二叉树天生是分治结构（根 + 左子树 + 右子树），树上的算法几乎都是"对左右子树递归，再合并"。
> 本讲为第 13 讲的堆、第 14–15 讲的 BST/AVL/2-3 树打基础。
> **考试比重**：四种遍历顺序（含"由前序+中序还原树"）、树高计算、树上的递归算法设计都很常见。

---

## 1. 二叉树的术语

- 二叉树要么是**空树**（用 null 表示），要么由**根结点** + **左子树** + **右子树**组成。
- 结点字段：`T.root`（或 `T.val`）、`T.left`、`T.right`。
- **层（level）**：根在第 0 层，孩子在第 1 层……
- **高度（height）**：最大层数 = 根到最远叶子的边数。**空树高度为 −1**，只有一个结点的树高度为 0。
- **叶子（leaf）**：左右孩子都为空的结点。
- 有 n 个内部结点（真实结点）的二叉树，恰好有 **n + 1 个外部结点**（空指针 □）。

| 名称 | 定义 |
|---|---|
| 满二叉树（full binary tree） | 每个结点有 0 个或 2 个（非空）孩子 |
| 完全二叉树（complete tree） | 除最后一层外每层都填满，最后一层**从左到右**依次填 —— 堆就用它 |

## 2. 计算树高（典型分治）

```
function Height(T)
    if T = null then
        return −1
    return max(Height(T.left), Height(T.right)) + 1
```
复杂度：每个内部结点和外部结点各做一次"T 是否为空"的比较，共 n + (n+1) = **2n + 1** 次 ⇒ Θ(n)。

## 3. 四种遍历

| 遍历 | 顺序 | 口诀 |
|---|---|---|
| 前序（preorder） | 根 → 左 → 右 | 先访问根 |
| 中序（inorder） | 左 → 根 → 右 | 根在中间 |
| 后序（postorder） | 左 → 右 → 根 | 最后访问根 |
| 层序（level-order） | 一层一层，从左到右 | 用队列 |

```
function Preorder(T)                function Inorder(T)              function Postorder(T)
    if T ≠ null then                    if T ≠ null then                 if T ≠ null then
        visit T.root                        Inorder(T.left)                  Postorder(T.left)
        Preorder(T.left)                    visit T.root                     Postorder(T.right)
        Preorder(T.right)                   Inorder(T.right)                 visit T.root
```

### 讲义的树

```
              17
           /      \
         33        48
        /  \      /  \
      19    16   11   14
           /  \
          38   31
```

| 遍历 | 结果 |
|---|---|
| 前序 | 17 33 19 16 38 31 48 11 14 |
| 中序 | 19 33 38 16 31 17 11 48 14 |
| 后序 | 19 38 31 16 33 11 14 48 17 |
| 层序 | 17 33 48 19 16 11 14 38 31 |

所有遍历都是 **Θ(n)**（T(n) = T(左) + T(右) + 1）。

### 用栈做前序遍历（非递归）
```
function PreorderStack(T)
    S ← empty stack
    Push(S, T)
    while S is not empty do
        T ← Pop(S)
        if T ≠ null then
            visit T.root
            Push(S, T.right)        ▷ 先压右孩子
            Push(S, T.left)         ▷ 后压左孩子 ⇒ 左孩子先出栈（LIFO）
```

### 用队列做层序遍历
```
function LevelOrder(T)
    Q ← empty queue
    Enqueue(Q, T)
    while Q is not empty do
        T ← Dequeue(Q)
        if T ≠ null then
            visit T.root
            Enqueue(Q, T.left)
            Enqueue(Q, T.right)
```
讲义追踪：队列 17 → 33 48 → 48 19 16 → 19 16 11 14 → 16 11 14 → 11 14 38 31 → … 访问 17 33 48 19 16 11 14 38 31。

### 由两种遍历还原树（第 8 周题 53）
**前序 + 中序**可以唯一确定一棵二叉树（结点值互不相同时）：
1. 前序第一个是根；
2. 在中序里找到根，左边是左子树、右边是右子树；
3. 按左右子树的大小切分前序序列，递归。

例：前序 14 83 63 42 19 27 74 99 51 37，中序 63 83 19 42 14 27 99 51 74 37。
- 根 14；中序左边 {63, 83, 19, 42}，右边 {27, 99, 51, 74, 37}。
- 左子树：前序 83 63 42 19 → 根 83，左 63，右子树（中序 19 42，前序 42 19）根 42、左孩子 19。
- 右子树：前序 27 74 99 51 37 → 根 27，无左子树；右子树根 74，左子树 99（右孩子 51），右孩子 37。
- **后序：63 19 42 83 51 99 37 74 27 14**。

---

## 4. 分治求最近点对（Closest Pair Revisited）

暴力法 Θ(n²)（第 4 章）。分治可做到 **Θ(n log n)**：

1. **预处理**：把点按 x 坐标排序得 byX，按 y 坐标排序得 byY（Θ(n log n)）。
2. **分**：以 x 的中位数 m 为界，分成左半 P_L 和右半 P_R。
3. **治**：递归求出左边最小距离 d_L、右边最小距离 d_R，令 d = min(d_L, d_R)。
4. **合**：最近点对可能**跨越**分界线 x = m。只需考虑带状区域 m − d ≤ x ≤ m + d 内的点：
   从 byY 中按 y 序取出这些点放入数组 S；对 S 中每个点，只需与它**后面 y 坐标差小于 d 的点**比较
   （可证明每个点**最多比较 5 个**）。

```
function ClosestPair(byX[0..n−1], byY[0..n−1])     ▷ 返回最小距离
    if n ≤ 3 then return 暴力求解
    把 byX 前 ⌈n/2⌉ 个点放入 PL，其余放入 PR；byY 也按同样的划分拆成 QL、QR（保持按 y 有序）
    dL ← ClosestPair(PL, QL)
    dR ← ClosestPair(PR, QR)
    d ← min(dL, dR)
    m ← byX[⌈n/2⌉ − 1].x
    S ← byY 中所有满足 |x − m| < d 的点（仍按 y 有序），个数为 num
    dminsq ← d²
    for i ← 0 to num − 2 do
        k ← i + 1
        while k ≤ num − 1 and (S[k].y − S[i].y)² < dminsq do
            dminsq ← min((S[k].x − S[i].x)² + (S[k].y − S[i].y)², dminsq)
            k ← k + 1
    return √dminsq
```

复杂度：T(n) = 2T(n/2) + Θ(n)（合并步骤线性）⇒ Θ(n log n)；加上预排序 Θ(n log n)，**总共 Θ(n log n)**。

---

## 考点与易错

1. **空树高度 −1，单结点高度 0**（AVL 平衡因子也用这个约定）。
2. 前序 = 根左右，中序 = 左根右，后序 = 左右根，层序用队列。
3. 用栈做前序遍历时**先压右孩子**。
4. 前序 + 中序 能还原树；只有前序 + 后序一般不能唯一确定。
5. 树上递归算法的标准写法：先处理 `T = null`，再处理叶子（如需），最后递归左右并合并。
6. 分治最近点对：Θ(n log n)，合并时每点最多比 5 个邻居。

---

## 练习

1.（第 8 周题 51）树：a 的左孩子 b、右孩子 c；b 的左孩子 d；c 的右孩子 e。写出前、中、后序。
2.（第 8 周题 52）某二叉树的前序和中序都是 a, b, c, d, e。它长什么样？
3.（第 8 周题 54）下面统计叶子数的算法错在哪？请改正。
   ```
   function LeafCount(T)
       if T = null then return 0
       else return LeafCount(T.left) + LeafCount(T.right)
   ```
4.（第 8 周题 50）2ⁿ × 2ⁿ 的棋盘缺一格，用 L 形三格骨牌（tromino）铺满。设计分治算法，写出递推式并用主定理求复杂度。
5. 设计算法：判断两棵二叉树是否结构和值完全相同。复杂度？
6. 设计算法：计算二叉树中所有结点值之和。

<details>
<summary>答案</summary>

1. 前序 a b d c e；中序 d b a c e；后序 d b e c a。
2. 一根"右斜的棍子"：每个结点只有右孩子，a → b → c → d → e。
3. 它永远返回 0（从来没有数到叶子）。需要加上叶子的情况：
   ```
   function LeafCount(T)
       if T = null then return 0
       if T.left = null and T.right = null then return 1
       return LeafCount(T.left) + LeafCount(T.right)
   ```
4. n = 0（1×1 棋盘缺一格）无需铺。否则把棋盘分成四个 2ⁿ⁻¹ × 2ⁿ⁻¹ 的象限；缺格在某一个象限里，
   在中心放一块骨牌，正好盖住**另外三个象限**各一格；于是四个象限都变成"缺一格"的同类问题，递归求解。
   设 m = 4ⁿ 为格子数：T(m) = 4T(m/4) + 1，a = 4 > 4⁰ = 1 ⇒ Θ(m^{log₄4}) = **Θ(m)**，与棋盘面积成线性。
5. ```
   function Same(T1, T2)
       if T1 = null and T2 = null then return True
       if T1 = null or T2 = null then return False
       return T1.root = T2.root and Same(T1.left, T2.left) and Same(T1.right, T2.right)
   ```
   Θ(n)（n 为较小树的结点数）。
6. ```
   function TreeSum(T)
       if T = null then return 0
       return T.root + TreeSum(T.left) + TreeSum(T.right)
   ```
   Θ(n)。
</details>
