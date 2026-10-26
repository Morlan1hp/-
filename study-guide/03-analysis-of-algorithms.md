# 第 3 章（第 4 讲）算法分析：极限法、循环求和、递推式

> **本章位置**：上一讲给了 O/Ω/Θ 的定义，这一讲教你**实际怎么算**：
> 非递归算法 → 写成求和式；递归算法 → 写成递推式再用"倒推法（telescoping）"解出来。
> **考试比重**：设计题每题都要分析复杂度；选择题常考"比较两个函数谁增长快"。

---

## 1. 用极限比较增长率（比定义好用得多）

```
              ⎧ 0      ⇒ f 增长比 g 慢：f ∈ O(g)，但 f ∉ Θ(g)
lim f(n)/g(n) = ⎨ c > 0  ⇒ 同阶：f ∈ Θ(g)
n→∞           ⎩ ∞      ⇒ f 增长比 g 快：f ∈ Ω(g)，但 f ∉ Θ(g)
```

**例**：1000n ∈ O(n²)？ lim 1000n/n² = lim 1000/n = 0 ⇒ 是，而且 1000n 比 n² 慢。

### 洛必达法则（L'Hôpital）
若 f、g 都趋于 ∞：lim f(n)/g(n) = lim f'(n)/g'(n)。

**例（讲义）**：log₂n 与 √n 谁快？
(log₂n)' = 1/(n ln 2)，(√n)' = 1/(2√n)
lim (log₂n)/√n = lim [1/(n ln2)] / [1/(2√n)] = lim 2√n/(n ln 2) = (2/ln2)·lim 1/√n = **0**
⇒ log n 比 √n 慢。

### 所有对数同阶
log_a n = (log_a b)(log_b n)，所以 lim log_a n / log_b n = log_a b（常数）⇒ **Θ(log_a n) = Θ(log_b n)**。
又 log(n^c) = c·log n ⇒ log(n^c) ∈ Θ(log n)。

### 用 O 推理的三条规则
设 t₁ ∈ O(g₁)，t₂ ∈ O(g₂)：
1. **加法**：t₁ + t₂ ∈ O(max{g₁, g₂}) —— 顺序执行的两段代码，取较大者。
2. **常数**：c·t₁ ∈ O(g₁) —— 常数因子可以扔掉。
3. **乘法**：t₁·t₂ ∈ O(g₁·g₂) —— 嵌套循环：外层次数 × 内层代价。

### 有用的式子
Stirling 公式：n! ≈ √(2πn)·(n/e)ⁿ，所以 log(n!) ∈ Θ(n log n)，且 n! ∈ O(n^{n+½})。

---

## 2. 非递归算法的分析步骤

1. 确定输入规模 n；
2. 确定基本操作；
3. 判断是否需要分最好/最坏/平均情况（次数是否只依赖 n）；
4. 写出基本操作次数的**求和式**；
5. 化简求和式，得到阶。

### 例 1：找数组最大值
```
function MaxElement(A[0..n−1])
    max ← A[0]
    for i ← 1 to n − 1 do
        if A[i] > max then
            max ← A[i]
    return max
```
基本操作：比较 `A[i] > max`。C(n) = Σ_{i=1}^{n−1} 1 = n − 1 ∈ **Θ(n)**（最好最坏一样）。

### 例 2：选择排序（下一讲会详细讲）
```
function SelectionSort(A[0..n−1])
    for i ← 0 to n − 2 do
        min ← i
        for j ← i + 1 to n − 1 do
            if A[j] < A[min] then
                min ← j
        swap(A[i], A[min])
```
基本操作：比较 `A[j] < A[min]`。
```
C(n) = Σ_{i=0}^{n−2} Σ_{j=i+1}^{n−1} 1
     = Σ_{i=0}^{n−2} (n − 1 − i)
     = Σ_{i=0}^{n−2} (n−1) − Σ_{i=0}^{n−2} i
     = (n−1)² − (n−2)(n−1)/2
     = n(n−1)/2  ∈ Θ(n²)
```

### 例 3：矩阵乘法（n×n）
```
for i ← 0 to n−1 do
    for j ← 0 to n−1 do
        C[i,j] ← 0
        for k ← 0 to n−1 do
            C[i,j] ← C[i,j] + A[i,k] · B[k,j]
```
基本操作：乘法。M(n) = Σᵢ Σⱼ Σₖ 1 = Σᵢ Σⱼ n = Σᵢ n² = n³ ∈ **Θ(n³)**。

---

## 3. 递归算法的分析：递推式 + 倒推法

步骤：确定基本操作 → 写出**递推关系**（含初始条件）→ 求**闭式解**。

### 例 1：递归阶乘
```
function F(n)
    if n = 0 then return 1
    else return F(n − 1) · n
```
基本操作：乘法。M(0) = 0，M(n) = M(n−1) + 1。

**倒推法（telescoping / backward substitution）**：
```
M(n) = M(n−1) + 1
     = [M(n−2) + 1] + 1 = M(n−2) + 2
     = M(n−3) + 3
     = …
     = M(n−n) + n = M(0) + n = n      ⇒ Θ(n)
```

### 例 2：二分查找（递归版）
```
function BinSearch(A, lo, hi, key)
    if lo > hi then return −1
    mid ← lo + ⌊(hi − lo)/2⌋
    if A[mid] = key then return mid
    else if A[mid] > key then return BinSearch(A, lo, mid − 1, key)
    else return BinSearch(A, mid + 1, hi, key)
```
手算：A = [4, 9, 13, 22, 41, 83, 96]，找 41：
(lo,hi,mid) = (0,6,3)：A[3]=22 < 41 → (4,6,5)：A[5]=83 > 41 → (4,4,4)：A[4]=41，返回 **4**。

最坏情况递推（基本操作：比较）：C(0) = 0，C(n) = C(n/2) + 1。
**光滑性规则（smoothness rule）**允许我们假设 n = 2ᵏ：
```
C(n) = C(n/2) + 1 = C(n/4) + 2 = C(n/8) + 3 = … = C(n/n) + log₂n
     = C(1) + log₂n = (C(0) + 1) + log₂n = 1 + log₂n    ⇒ Θ(log n)
```

### 常见递推式速查（自己推一遍！）

| 递推式 | 解 | 例子 |
|---|---|---|
| T(n) = T(n−1) + 1 | Θ(n) | 递归阶乘、递归线性查找 |
| T(n) = T(n−1) + n | Θ(n²) | 快排最坏情况、递归选择排序 |
| T(n) = T(n/2) + 1 | Θ(log n) | 二分查找 |
| T(n) = T(n/2) + n | Θ(n) | QuickSelect 平均 |
| T(n) = 2T(n/2) + 1 | Θ(n) | 求树高、二叉树遍历 |
| T(n) = 2T(n/2) + n | Θ(n log n) | 归并排序 |
| T(n) = 2T(n−1) + 1 | Θ(2ⁿ) | 汉诺塔 |
| T(n) = T(n−1) + log n | Θ(n log n) | 作业 1 第 1 题 |

---

## 考点与易错

1. 用极限比较时，一定要说出极限值是 0、常数还是 ∞，并据此下结论。
2. 求和项数：Σ_{i=l}^{u} 1 = u − l + 1。
3. 倒推法要写出"第 k 步的一般形式"，再代入边界条件。
4. 递推式里 **"+1" 和 "+n" 的区别**：前者是每层常数工作，后者是每层线性工作。
5. 作业 1 的教训：T(n) = T(n−1) + Θ(log n) 的解是 Σ log i = log(n!) ∈ Θ(n log n)，不是 Θ(log n)，也不是简单的 Θ(n)。

---

## 练习

1.（第 4 周题 15）判断 f ∈ O(g)、g ∈ O(f) 还是两者都成立：
   (a) f = (n² + 1 − n²)/2，g = 2n (b) f = n² + n√n，g = n² + n
   (c) f = n log n，g = n√n/4 (d) f = n + log n，g = √n
   (e) f = 4n log n + n，g = (n² − n)/2 (f) f = (log n)²，g = 2 + log n
2.（第 7 周题 49）T(1) = 1，T(n) = T(n−1) + n/2。用倒推法求闭式。
3. 分析下面算法的比较次数：
   ```
   for i ← 0 to n − 1 do
       for j ← 0 to i do
           if A[i] = A[j] then c ← c + 1
   ```
4. 解递推式 T(1) = 1，T(n) = T(n−1) + 2。

<details>
<summary>答案</summary>

1. (a) f = 1/2 是常数 ⇒ f ∈ O(g) (b) 两者都成立（都是 Θ(n²)） (c) f ∈ O(g)（log n ≺ √n）
   (d) g ∈ O(f)（√n ≺ n） (e) f ∈ O(g) (f) g ∈ O(f)
2. T(n) = T(n−1) + n/2 = T(n−2) + (n−1)/2 + n/2 = … = T(1) + Σ_{i=2}^{n} i/2
   = 1 + (n(n+1)/2 − 1)/2 = **(n² + n + 2)/4**。检验 T(3) = (9+3+2)/4 = 7/2 ✔。
3. Σ_{i=0}^{n−1} (i + 1) = n(n+1)/2 ∈ Θ(n²)。
4. T(n) = T(n−1) + 2 = T(n−2) + 4 = … = T(1) + 2(n−1) = 2n − 1 ∈ Θ(n)。
</details>
