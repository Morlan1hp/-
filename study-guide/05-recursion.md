# 第 5 章（第 6 讲）递归（Recursion）

> **本章位置**：递归是后面"减治、分治、动态规划、树和图的遍历"的共同基础。
> 本讲重点：①怎么把问题拆成更小的同类问题；②**写对基本情况（base case）**；
> ③认识"重复计算"导致的指数爆炸——这直接引出第 16、18 讲的记忆化和动态规划。

---

## 1. 递归的思路

1. **基本情况**：最小的输入直接给答案。
2. **递归情况**：把问题化成一个或几个**更小的同类问题**，再把它们的解组合起来。
3. 每次递归必须让问题**变小**，保证最终到达基本情况。

数据本身就是递归结构（链表、树）时，递归最自然。

## 2. 阶乘

```
function Fac(n)                    function Fac2(n)    ▷ 迭代版
    if n = 0 then                      result ← 1
        return 1                       while n > 0 do
    return Fac(n − 1) · n                  result ← result · n
                                           n ← n − 1
                                       return result
```
展开：F(5) = F(4)·5 = (F(3)·4)·5 = … = ((((1·1)·2)·3)·4)·5 = 120。
两者都是 Θ(n) 次乘法；但递归版要用 Θ(n) 的调用栈空间，**迭代版只用常数空间，通常更好**。

## 3. 斐波那契数（1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …）

### 3.1 直译定义的递归（很慢）
```
function Fib(n)
    if n = 0 or n = 1 then
        return 1
    return Fib(n − 1) + Fib(n − 2)
```
易懂，但**大量重复计算**：Fib(n−2) 在 Fib(n) 和 Fib(n−1) 里各算一次……
加法次数 A(n) = A(n−1) + A(n−2) + 1，增长与斐波那契数本身同阶 ≈ 1.618ⁿ ⇒ **指数级**。

### 3.2 只记住最近两个数（线性）
```
function Fib(n, a, b)              function Fib3(n)    ▷ 迭代版
    if n = 0 then                      a ← 1; b ← 0
        return a                       while n > 0 do
    return Fib(n − 1, a + b, a)            a ← a + b
                                           b ← a − b
初始调用 Fib(n, 1, 0)                      n ← n − 1
                                       return a
```
追踪 Fib(5, 1, 0)：= Fib(4,1,1) = Fib(3,2,1) = Fib(2,3,2) = Fib(1,5,3) = Fib(0,8,5) = **8**。
两个版本都是 **Θ(n)**。

> 这一对例子体现了全课的一个核心思想：**同样的问题，不同算法可以是指数级 vs 线性**。

## 4. 汉诺塔（Tower of Hanoi）

把 n 个盘子从 Init 柱移到 Fin 柱，大盘不能放在小盘上，Aux 是辅助柱。

**递归思路**：
1. 把上面 n−1 个盘子从 Init 移到 Aux（借助 Fin）；
2. 把第 n 个（最大的）盘子从 Init 移到 Fin；
3. 把 n−1 个盘子从 Aux 移到 Fin（借助 Init）。

```
function Hanoi(n, Init, Aux, Fin)
    if n > 0 then
        Hanoi(n − 1, Init, Fin, Aux)
        move the top disk from Init to Fin
        Hanoi(n − 1, Aux, Init, Fin)
```

**移动次数**：M(0) = 0，M(n) = 2M(n−1) + 1。倒推：
```
M(n) = 2M(n−1) + 1 = 2[2M(n−2) + 1] + 1 = 4M(n−2) + 2 + 1
     = 8M(n−3) + 4 + 2 + 1 = … = 2ⁿM(0) + 2ⁿ⁻¹ + … + 2 + 1 = 2ⁿ − 1
```
⇒ **Θ(2ⁿ)**。n = 64 时，每秒移一个，需要 2⁶⁴ − 1 秒 ≈ 5850 亿年。这是**最优**的，不能更少。

## 5. 找零方案数（Coin Change Ways）

澳洲硬币 5, 10, 20, 50, 100, 200 分。凑 300 分（$3）有多少种不同的组合（不计顺序）？

**拆分思路**：挑最大面额 d，所有方案分成两类：
- **不用** d：用剩下的面额凑 amount；
- **至少用一个** d：先拿一个 d，再用**所有面额（仍包括 d）**凑 amount − d。

两类不重不漏 ⇒ Ways(amount, D) = Ways(amount, D \ {d}) + Ways(amount − d, D)。

**基本情况**（每次递归要么 amount 变小、要么面额集合变小，分别考虑）：
- amount = 0：1 种（什么都不用）——**注意先判断这个**；
- amount < 0：0 种；
- D = ∅（且 amount > 0）：0 种。

```
function Ways(amount, D)
    if amount = 0 then return 1
    if amount < 0 then return 0
    if D = ∅ then return 0
    d ← SelectLargest(D)
    return Ways(amount, D \ {d}) + Ways(amount − d, D)
```
初始调用 Ways(300, {5,10,20,50,100,200})，答案是 **1022**。
（小例子：Ways(50, {5,10,20}) = **12**。）

这个递归简洁优美，但运行时间随 amount **指数增长**（同样有大量重复子问题）。
用**记忆化或动态规划**可以大大加速（第 16、18 讲）。

---

## 考点与易错

1. 写递归一定先写**基本情况**，而且基本情况的**顺序**有讲究（找零中先判 amount = 0）。
2. 递归不等于低效：线性斐波那契也是递归。低效来自**重叠子问题的重复计算**。
3. 汉诺塔：M(n) = 2M(n−1) + 1 ⇒ 2ⁿ − 1。
4. 迭代版通常省空间（常数空间 vs 递归栈 Θ(n)）。

---

## 练习

1. 朴素递归 Fib(5) 一共会调用 Fib 多少次（包括 Fib(5) 本身）？
2. 汉诺塔 n = 3 时写出全部移动步骤（柱子记为 L、M、R，从 L 移到 R）。
3. 手算 Ways(20, {5, 10})，并画出递归树。
4. 写一个递归函数 Sum(A, lo, hi) 计算 A[lo..hi] 的和，并写出递推式和复杂度。

<details>
<summary>答案</summary>

1. 设 C(n) 为调用次数：C(0) = C(1) = 1，C(n) = C(n−1) + C(n−2) + 1。
   C(2)=3, C(3)=5, C(4)=9, **C(5)=15**。
2. 共 2³ − 1 = 7 步：L→R, L→M, R→M, L→R, M→L, M→R, L→R。
3. Ways(20,{5,10}) = Ways(20,{5}) + Ways(10,{5,10})
   - Ways(20,{5}) = Ways(20,∅) + Ways(15,{5}) = 0 + … = 1（只有 5+5+5+5）
   - Ways(10,{5,10}) = Ways(10,{5}) + Ways(0,{5,10}) = 1 + 1 = 2
   - 合计 **3** 种：{5,5,5,5}、{5,5,10}、{10,10}。
4. ```
   function Sum(A, lo, hi)
       if lo > hi then return 0
       return A[lo] + Sum(A, lo + 1, hi)
   ```
   S(n) = S(n−1) + 1 ⇒ Θ(n)。
</details>
