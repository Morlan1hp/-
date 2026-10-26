# 第 22 章 总复习：速查表 + 设计题方法论 + 模拟题

> 这一章是考前最后几天的主力材料。前半部分是**全课速查表**（选择题靠它），
> 后半部分是**设计题方法论和模拟题**（第二部分大题靠它）。

---

# 第一部分：速查表

## 1. 增长率排序
```
1 ≺ log log n ≺ log n ≺ (log n)² ≺ √n ≺ n ≺ n log n ≺ n² ≺ n³ ≺ 2ⁿ ≺ 3ⁿ ≺ n! ≺ nⁿ
```
- 对数底数无关：Θ(log₂n) = Θ(ln n)；log(n^c) ∈ Θ(log n)
- 2ⁿ⁻¹ ∈ Θ(2ⁿ)，但 (n−1)! ∉ Θ(n!)；log(n!) ∈ Θ(n log n)
- 比较方法：lim f/g = 0（f 慢）、常数（同阶）、∞（f 快），可用洛必达

## 2. 主定理（考试会给出公式，但要会用）
T(n) = aT(n/b) + Θ(n^d)：
- a < b^d ⇒ Θ(n^d)
- a = b^d ⇒ Θ(n^d log n)
- a > b^d ⇒ Θ(n^{log_b a})

## 3. 常见递推式
| 递推式 | 解 | 算法 |
|---|---|---|
| T(n) = T(n−1) + 1 | Θ(n) | 线性递归 |
| T(n) = T(n−1) + n | Θ(n²) | 快排最坏、插入排序最坏 |
| T(n) = 2T(n−1) + 1 | Θ(2ⁿ) | 汉诺塔 |
| T(n) = T(n/2) + 1 | Θ(log n) | 二分查找 |
| T(n) = T(n/2) + n | Θ(n) | QuickSelect 平均 |
| T(n) = 2T(n/2) + 1 | Θ(n) | 树遍历、求树高 |
| T(n) = 2T(n/2) + n | Θ(n log n) | 归并排序、快排最好 |
| T(n) = T(n−1) + log n | Θ(n log n) | 作业 1 |

## 4. 排序算法总表（选择题高频）

| 算法 | 最好 | 平均 | 最坏 | 原地 | 稳定 | 要点 |
|---|---|---|---|---|---|---|
| 选择排序 | n² | n² | n² | ✔ | ✘ | 只交换 n−1 次；输入不敏感 |
| 插入排序 | **n** | n² | n² | ✔ | ✔ | 有序/几乎有序时线性；小数组好 |
| 希尔排序 | — | ~n^1.25 | ~n^1.5 | ✔ | ✘ | 间隔 1,4,13,40…；最后 1-排序 |
| 归并排序 | n log n | n log n | n log n | ✘ | ✔ | Θ(n) 额外空间；链表/外部排序首选 |
| 快速排序 | n log n | n log n | **n²** | ✔ | ✘ | 有序输入最坏；三数取中；平均最快 |
| 堆排序 | n log n | n log n | n log n | ✔ | ✘ | 最坏有保证；真正原地 |
| 计数排序 | n + k | n + k | n + k | ✘ | ✔ | 键范围小；不比较键 |

**怎么选**：数据几乎有序 → 插入排序；需要稳定 + 保证 n log n → 归并；内存紧 + 保证 n log n → 堆排序；
随机数据追求平均最快 → 快排；键是小范围整数 → 计数排序；链表 → 归并。
**基于比较的排序下界 Ω(n log n)**。

## 5. 查找与选择

| 算法 | 前提 | 时间 |
|---|---|---|
| 线性查找 | 无 | Θ(n) |
| 二分查找 | 有序数组 | Θ(log n)（最坏和平均） |
| 插值查找 | 有序 + 均匀分布 | 平均 O(log log n)，最坏 O(n) |
| QuickSelect（第 k 小） | 无 | 平均 Θ(n)，最坏 Θ(n²) |
| 暴力字符串匹配 | 无 | 最坏 O(mn)，自然文本平均接近 Θ(n) |
| Horspool | 预处理 Θ(m + 字母表) | 最坏 O(mn)，平均很快 |

## 6. 数据结构操作代价

| 结构 | 查找 | 插入 | 删除 | 备注 |
|---|---|---|---|---|
| 无序数组 | Θ(n) | Θ(1) | Θ(n) | |
| 有序数组 | Θ(log n) | Θ(n) | Θ(n) | |
| 链表 | Θ(n) | Θ(1)（已知位置） | Θ(1)（已知位置） | |
| BST | 平均 Θ(log n)，最坏 Θ(n) | 同左 | 同左 | 有序插入退化 |
| AVL / 2–3 树 | Θ(log n) | Θ(log n) | Θ(log n) | |
| 堆（优先队列） | 找最大 Θ(1) | Θ(log n) | 删最大 Θ(log n) | 建堆 Θ(n) |
| 哈希表 | 期望 Θ(1) | 期望 Θ(1) | 拉链法容易 | 不能有序遍历 |

## 7. 图算法

| 算法 | 问题 | 时间 | 关键条件 |
|---|---|---|---|
| DFS / BFS | 遍历、连通性、环、二着色、拓扑排序 | 邻接表 Θ(V+E)；矩阵 Θ(V²) | DFS 用栈，BFS 用队列 |
| BFS | 无权图最短步数 | Θ(V+E) | |
| 拓扑排序 | DAG 线性化 | Θ(V+E) | DFS 逆出栈序 / 源点删除 |
| Warshall | 传递闭包 | Θ(V³) | k 在最外层 |
| Floyd | 所有点对最短路 | Θ(V³) | 无负权环 |
| Prim | 最小生成树 | O(E log V)（堆） | 连通图 |
| Dijkstra | 单源最短路 | O(E log V)（堆） | **非负权** |

## 8. 设计策略一览

| 策略 | 思想 | 代表 |
|---|---|---|
| 暴力 / 穷举 | 直接按定义；生成所有候选再检查 | 选择排序、字符串匹配、TSP、背包穷举 |
| 减治（减常数） | n → n−1 | 插入排序、源点删除拓扑排序 |
| 减治（减因子/可变） | n → n/2 等 | 二分查找、插值查找、QuickSelect、欧几里得 |
| 分治 | 分成多个子问题，递归，合并 | 归并、快排、树遍历、最近点对 |
| 变治 | 换实例/换表示/归约 | 预排序、BST、AVL、2–3 树、堆、霍纳法则 |
| 时空权衡 | 用空间换时间 | 记忆化、计数排序、Horspool、哈希 |
| 动态规划 | 递推 + 重叠子问题 + 填表 | 硬币行、背包、编辑距离、Warshall、Floyd |
| 贪心 | 局部最优、不回头 | Prim、Dijkstra、哈夫曼 |

## 9. 手算题的"标准版本"（务必按课上的版本走）
- **选择排序**：每轮找最小，与 A[i] 交换。
- **插入排序**：`while j ≥ 0 and v < A[j]`，右移。
- **Lomuto**：p = A[lo]，`if A[i] < p: s++, swap(A[s], A[i])`，最后 swap(A[lo], A[s])。
- **QuickSelect**：用 Lomuto；去右边时 k ← k − (s − lo + 1)。
- **Hoare**：p = A[lo]；i 从左找 ≥ p，j 从右找 ≤ p；i < j 交换；交错后 swap(A[lo], A[j])。
- **归并**：左半 ⌊n/2⌋ 个；相等取左边。
- **堆**：1 开始的数组；自底向上从 ⌊n/2⌋ 到 1，一直下沉；与较大孩子交换。
- **AVL**：平衡因子 = 左高 − 右高（空树 −1）；在最低失衡点旋转。
- **2–3 树**：溢出时中间键上升。
- **Horspool**：Shift 只看 P[0..m−2]；用 T[i] 查表。
- **线性探测**：冲突往后，到末尾绕回 0。
- **Warshall/Floyd**：k 在最外层。
- **Prim/Dijkstra**：每轮取最小，只更新其邻居；平局按字母序（除非题目另有规定）。
- **哈夫曼**：每次合并两个最小的权重。

---

# 第二部分：设计题方法论

## 10. 拿到一道新题，先问自己这些问题

| 题目中的信号 | 想到的技巧 |
|---|---|
| "有没有两个元素……"、"重复"、"最常出现" | **预排序** + 线性扫描（Θ(n log n)），或**哈希表**（期望 Θ(n)） |
| 数组**有序**，要求 O(log n) | **二分查找**（及其变体） |
| "最小的满足条件的值"，且条件对值**单调** | **在答案上二分**（作业 1 第 3 题就是这样） |
| 第 k 小、中位数，要求线性 | **QuickSelect**（平均 Θ(n)） |
| 反复取最大/最小，或"前 k 个" | **堆** |
| 能分成两半独立求解再合并，要求 n log n | **分治**（改造归并排序，如数逆序对） |
| "最多/最少/最大价值/方案数"，且有"选或不选第 i 个"的结构 | **动态规划** |
| 关系、网络、依赖、可达性、步数 | **建图**：结点是什么？边是什么？ |
| 依赖/先后顺序 | **拓扑排序**（DAG） |
| 无权图最少步数 | **BFS** |
| 带权最短路（单源，非负） | **Dijkstra**；所有点对 → **Floyd** |
| 可达性、连通、环、二着色 | **DFS/BFS**（记得 visited 数组！） |
| 把所有点用最小代价连起来 | **Prim（MST）** |
| 输入规模很小（n ≤ 20） | 穷举也许就够了（但看题目对复杂度的要求） |

## 11. 答题模板（每个部分都可能有分）

1. **思路**（1–3 句话）：用什么技巧，为什么正确。
2. **伪代码**：课程风格（`←`、`for … to … do`、`function`），写清输入输出、数组下标起点、初始化。
   调用课上算法要写名字（`Mergesort(A)`、`Dijkstra(G, s)`）；用哈希表要写哈希函数和冲突处理。
3. **正确性**（简短）：关键不变式，或为什么不会漏解。
4. **复杂度**：逐部分分析再相加，如"排序 Θ(n log n) + 扫描 Θ(n) = Θ(n log n)"。
   如果题目要求"最优复杂度"，想一想能不能更快。
5. **检查**：用一个小例子在草稿纸上跑一遍；检查边界（空、一个元素、全相同、不存在）。

## 12. 常见失分点
- 用了 Python/Java 语法（`def`、`==`、`{}`、`len(A)`、`i++`）。
- 写"把数组排序"而不说用什么排序。
- DFS/BFS 忘记 visited 标记 ⇒ 死循环（作业 1 第 2 题的错误算法就是这个问题）。
- DP 只写了代码，没写**子问题定义**、**递推关系**和**边界**。
- 复杂度只给结论不给理由，或混淆 O 和 Θ。
- 贪心算法没有理由就声称最优。
- 能做到 Θ(n log n) 却写了 Θ(n²)。

---

# 第三部分：模拟设计题（先自己做，再看答案）

### 题 1（预排序 / 哈希）
给定 n 个整数的数组 A，判断是否有某个值出现**超过 n/2 次**（多数元素）。要求 O(n log n)。

<details>
<summary>答案</summary>

**思路**：排序后，若存在多数元素，它一定占据中间位置 A[⌊n/2⌋]。取出候选，再数一遍确认。
```
function HasMajority(A[0..n−1])
    Mergesort(A)
    c ← A[⌊n/2⌋]
    count ← 0
    for i ← 0 to n − 1 do
        if A[i] = c then count ← count + 1
    return count > n/2
```
**复杂度**：Mergesort Θ(n log n) + 扫描 Θ(n) = Θ(n log n)。
（也可用哈希表统计次数，期望 Θ(n)：表大小取质数 m ≈ 2n，h(k) = k mod m，拉链法，每个链结点存 (键, 计数)。）
</details>

### 题 2（分治 / 二分查找变体）
有序数组 A[0..n−1]（可能有重复），求值 x 出现的次数。要求 O(log n)。

<details>
<summary>答案</summary>

**思路**：用两次二分查找分别找到 x 第一次出现和最后一次出现的位置。
```
function FirstOcc(A[0..n−1], x)
    lo ← 0; hi ← n − 1; ans ← −1
    while lo ≤ hi do
        m ← ⌊(lo + hi)/2⌋
        if A[m] = x then
            ans ← m; hi ← m − 1          ▷ 记下来，继续往左找
        else if A[m] < x then
            lo ← m + 1
        else
            hi ← m − 1
    return ans

function LastOcc(A[0..n−1], x)          ▷ 同上，但找到后 lo ← m + 1 继续往右找
    …

function Count(A[0..n−1], x)
    f ← FirstOcc(A, x)
    if f = −1 then return 0
    return LastOcc(A, x) − f + 1
```
**复杂度**：两次二分，每次 Θ(log n)（区间每轮减半），共 Θ(log n)。
</details>

### 题 3（动态规划：最大子数组和）
数组 A[1..n]（有正有负），求和最大的**连续**子数组的和。要求 Θ(n)。

<details>
<summary>答案</summary>

**子问题**：S(i) = 以 A[i] **结尾**的连续子数组的最大和。
**递推**：以 A[i] 结尾的子数组要么只有 A[i]，要么是"以 A[i−1] 结尾的最优子数组"再接上 A[i]：
S(1) = A[1]；S(i) = max(A[i], S(i−1) + A[i])。答案是 max_{1≤i≤n} S(i)。
```
function MaxSubarray(A[1..n])
    S[1] ← A[1]
    best ← S[1]
    for i ← 2 to n do
        S[i] ← max(A[i], S[i − 1] + A[i])
        if S[i] > best then best ← S[i]
    return best
```
**复杂度**：一次循环 Θ(n)，空间 Θ(n)（可降到 Θ(1)）。
例：A = −2, 1, −3, 4, −1, 2, 1, −5, 4 ⇒ S = −2, 1, −2, 4, 3, 5, 6, 1, 5，答案 6（子数组 4, −1, 2, 1）。
</details>

### 题 4（动态规划：网格收集硬币）
r × c 的网格，每格 C[i, j] 有 0 或 1 枚硬币。机器人从左上角 (1,1) 出发，每步只能**向右或向下**，到达右下角 (r, c)。最多能收集多少硬币？

<details>
<summary>答案</summary>

**子问题**：F(i, j) = 走到格子 (i, j) 时最多收集的硬币数。
**递推**：只能从上方或左方到达：F(i, j) = max(F(i−1, j), F(i, j−1)) + C[i, j]，
边界 F(0, j) = 0，F(i, 0) = 0。答案 F(r, c)。
```
function RobotCoins(C[1..r, 1..c])
    for j ← 0 to c do F[0, j] ← 0
    for i ← 1 to r do
        F[i, 0] ← 0
        for j ← 1 to c do
            F[i, j] ← max(F[i − 1, j], F[i, j − 1]) + C[i, j]
    return F[r, c]
```
**复杂度**：Θ(rc) 时间和空间。按行从上到下、每行从左到右填表，保证用到的格子已算好。
</details>

### 题 5（动态规划：最长递增子序列）
数组 A[1..n]，求最长的**严格递增子序列**（不要求连续）的长度。多项式时间即可。

<details>
<summary>答案</summary>

**子问题**：L(i) = 以 A[i] 结尾的最长递增子序列长度。
**递推**：L(i) = 1 + max({0} ∪ {L(j) | 1 ≤ j < i 且 A[j] < A[i]})。答案 max_i L(i)。
```
function LIS(A[1..n])
    best ← 0
    for i ← 1 to n do
        L[i] ← 1
        for j ← 1 to i − 1 do
            if A[j] < A[i] and L[j] + 1 > L[i] then
                L[i] ← L[j] + 1
        if L[i] > best then best ← L[i]
    return best
```
**复杂度**：两重循环 Θ(n²)。
例：A = 3, 1, 4, 1, 5, 9, 2, 6 ⇒ L = 1, 1, 2, 1, 3, 4, 2, 4，答案 4（如 3, 4, 5, 9）。
</details>

### 题 6（图建模 + BFS：迷宫，第 1 讲的问题）
n × n 迷宫，部分格子是障碍，只能上下左右走。求从 (1,1) 到 (n,n) 的最少步数（走不到返回 −1）。

<details>
<summary>答案</summary>

**建模**：每个非障碍格子是一个结点，上下左右相邻的两个非障碍格子之间有一条边。无权图最短路 ⇒ **BFS**。
```
function MazeSteps(Blocked[1..n, 1..n])
    if Blocked[1, 1] or Blocked[n, n] then return −1
    for each cell (i, j) do dist[i, j] ← ∞
    dist[1, 1] ← 0
    Q ← empty queue; Enqueue(Q, (1, 1))
    while Q is not empty do
        (i, j) ← Dequeue(Q)
        if (i, j) = (n, n) then return dist[n, n]
        for each (a, b) in {(i−1, j), (i+1, j), (i, j−1), (i, j+1)} do
            if 1 ≤ a ≤ n and 1 ≤ b ≤ n and not Blocked[a, b] and dist[a, b] = ∞ then
                dist[a, b] ← dist[i, j] + 1
                Enqueue(Q, (a, b))
    return −1
```
**复杂度**：n² 个结点，每个最多 4 条边，每个格子入队一次 ⇒ Θ(n²)（与格子数成线性）。
</details>

### 题 7（图：判断是否为树）
给定无向图 ⟨V, E⟩（邻接表），判断它是不是一棵树。

<details>
<summary>答案</summary>

**思路**：树 = 连通 + 无环 ⇔ 连通且 |E| = |V| − 1。
```
function IsTree(⟨V, E⟩)
    if |E| ≠ |V| − 1 then return False
    mark each node in V with 0
    pick any node v₀
    count ← 0
    Explore(v₀)                       ▷ 普通 DFS，每访问一个新结点 count ← count + 1
    return count = |V|                ▷ 一次 DFS 访问到所有结点 ⇔ 连通
```
（也可以用第 7 章的 Cyclic 判断无环，再检查连通。）
**复杂度**：邻接表 DFS Θ(|V| + |E|)。
</details>

### 题 8（拓扑排序 + DP：最少学期数）
n 门课，先修关系是一个 DAG（边 u → v 表示 u 是 v 的先修课）。每学期可以修任意多门课，但先修课必须在更早的学期修完。最少需要几个学期？

<details>
<summary>答案</summary>

**思路**：课程 v 最早能在第 S(v) 学期修，S(v) = 1 + max{S(u) | (u, v) ∈ E}（没有先修课时为 1）。
按**拓扑序**处理，保证算 S(v) 时所有先修课已算好。答案是 max S(v)，即 DAG 中最长路径的结点数。
```
function MinSemesters(⟨V, E⟩)
    T ← TopologicalSort(⟨V, E⟩)        ▷ DFS 逆出栈序
    for each v in V do S[v] ← 1
    for each u in T (按拓扑序) do
        for each edge (u, v) do
            if S[u] + 1 > S[v] then S[v] ← S[u] + 1
    return max_{v ∈ V} S[v]
```
**复杂度**：拓扑排序 Θ(|V| + |E|) + 每条边处理一次 Θ(|E|) = Θ(|V| + |E|)。
</details>

### 题 9（堆：合并 k 个有序数组）
k 个有序数组，共 N 个元素，合并成一个有序数组。要求 O(N log k)。

<details>
<summary>答案</summary>

**思路**：用大小为 k 的**最小堆**，存每个数组当前最前面的元素（附带它来自哪个数组、下标）。
每次弹出最小的放进结果，再把同一数组的下一个元素插入堆。
```
function MergeK(L₁, …, L_k)
    H ← 由 (Lᵢ[1], i, 1)（i = 1..k，非空数组）构成的数组
    把 H 用自底向上方法建成最小堆            ▷ Θ(k)
    R ← empty array
    while H is not empty do
        (x, i, p) ← EjectMin(H)              ▷ O(log k)
        append x to R
        if p + 1 ≤ length(Lᵢ) then
            Inject(H, (Lᵢ[p + 1], i, p + 1))  ▷ O(log k)
    return R
```
**复杂度**：每个元素进出堆各一次，堆大小 ≤ k ⇒ O(N log k)。
</details>

### 题 10（在答案上二分）
给定正整数 N，求 ⌊√N⌋，只用加减乘和比较。要求 O(log N) 次乘法。

<details>
<summary>答案</summary>

**思路**：条件 "x² ≤ N" 对 x 是单调的（小的 x 都满足，大的都不满足），所以可以在 [0, N] 上二分，找最后一个满足的 x。
```
function ISqrt(N)
    lo ← 0; hi ← N
    while lo < hi do
        m ← ⌊(lo + hi + 1)/2⌋          ▷ 取上中位数，保证区间缩小
        if m · m ≤ N then
            lo ← m                      ▷ m 满足，答案 ≥ m
        else
            hi ← m − 1                  ▷ m 不满足，答案 < m
    return lo
```
**不变式**：答案始终在 [lo, hi] 中。每轮区间大约减半 ⇒ Θ(log N) 轮，每轮一次乘法。
（对比第 2 周答案里从 1 开始逐个试的 Sqrt：Θ(√N) 次。）
</details>

### 题 11（变治 + 哈希：两个数组作为多重集合是否相等）
两个长度为 n 的整数数组 A、B，判断 B 是否是 A 的一个重新排列。给出 Θ(n log n) 的确定性算法，以及期望 Θ(n) 的算法。

<details>
<summary>答案</summary>

**确定性**：Mergesort(A)，Mergesort(B)，逐位比较。Θ(n log n)。
**期望线性**：哈希表（质数大小 m ≈ 2n，h(k) = k mod m，拉链法，链结点存 (键, 计数)）。
扫描 A：每个键计数 +1；扫描 B：每个键计数 −1，若找不到键或计数变成负数则返回 False。全部处理完返回 True。
每次哈希操作期望 O(1) ⇒ 期望 Θ(n)。
</details>

### 题 12（DP：背包变体——恰好装满）
n 个物品重量 w₁..wₙ（正整数），问能否选出一些物品使总重**恰好**为 W（这就是子集和问题）。给出伪多项式算法。

<details>
<summary>答案</summary>

**子问题**：P(i, j) = 能否从前 i 个物品中选出总重恰好为 j 的子集（True/False）。
**递推**：P(0, 0) = True，P(0, j) = False（j > 0）；
P(i, j) = P(i−1, j) or (j ≥ wᵢ and P(i−1, j − wᵢ))。答案 P(n, W)。
```
function SubsetSumDP(w[1..n], W)
    P[0, 0] ← True
    for j ← 1 to W do P[0, j] ← False
    for i ← 1 to n do
        for j ← 0 to W do
            P[i, j] ← P[i − 1, j]
            if j ≥ w[i] and P[i − 1, j − w[i]] then
                P[i, j] ← True
    return P[n, W]
```
**复杂度**：Θ(nW)——伪多项式（第 21 章）。
</details>

---

## 13. 考前清单
- [ ] 能默写：选择/插入/归并/快排（Hoare）/Lomuto/QuickSelect/二分/堆的下沉与建堆/DFS/BFS/Warshall/Floyd/Prim/Dijkstra/哈夫曼/硬币行/背包 的伪代码
- [ ] 能手算本指南里每一个"手算演示"，并和答案一致
- [ ] 能说出每个排序算法的最好/平均/最坏、是否稳定、是否原地，并能**举反例**说明不稳定
- [ ] 能熟练用主定理，以及用倒推法解 T(n) = T(n−1) + f(n)
- [ ] 重做所有 Weekly Quiz 和辅导课题目
- [ ] 学完后再做 Practice Exam，限时
- [ ] 考试时：先做有把握的选择题，留足时间给设计题；每道设计题都要写复杂度
