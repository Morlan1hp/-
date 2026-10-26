# COMP90038 算法与复杂度 —— 从零到满分的中文学习指南

这套教程完全按照本学期（2026 S2）两位教授的**授课顺序**编写：
第 1–14 讲由 Olya Ohrimenko 教授讲授，第 15–22 讲由 Cezary Kaliszyk 教授讲授。
所有内容都来自本仓库里的讲义（`01.pdf` … `22.pdf`）、辅导课题目与答案（`week*.pdf`、`ans*.pdf`）、
课堂录音转录和作业 1 的解答。所有手算例题都用程序核对过。

> 学习方法：每一讲按「概念 → 伪代码 → 手算演示 → 复杂度 → 考点与易错 → 练习」的顺序写。
> **一定要拿纸笔自己把每个演示重新算一遍**，再做练习、最后才看答案。这门课考的是"会做"，不是"会背"。

---

## 一、先搞清楚期末考试（来自最后一讲 Cezary 教授的原话）

| 项目 | 内容 |
|---|---|
| 时长 | 15 分钟阅读（只能读题，不能写）+ 3 小时作答 |
| 形式 | 电脑机考（Lockdown Browser），闭卷，**不需要计算器**（数字最多两位数） |
| 分值 | 占总成绩 60%；**门槛（hurdle）：考试必须拿到 30/60 才能通过本课** |
| 草稿纸 | 会发，但只有电脑上打出来的答案才算分 |
| 符号 | 赋值用 `←`（也可打 `<-`），不等号 `≠` 或 `!=` 都行；`O(n log n)`、`Theta(n)` 直接打字即可 |

### 试卷分两部分（两部分都很重要，不能只准备一半）

**第一部分：选择题 / 简答题（风格像每周小测 Weekly Quiz）**
考你是否理解课上讲过的算法，典型题目：
- 哪种排序算法适合什么场景？是否稳定（stable）、是否原地（in-place）？
- 比较复杂度类的增长速度（谁增长得更快）
- 建堆时元素怎么移动、哈希冲突怎么解决
- 给一棵 BST 插入后变 AVL，做了哪种旋转？
- 构造哈夫曼树
- **按步骤手动追踪（trace）算法**

**第二部分：算法设计题（风格像作业 Assignment）**
给你一个**没见过的新问题**，你要：
1. 用课上学过的技巧（暴力、减治、分治、变治、动态规划、贪心、问题归约……）设计算法；
2. 用**伪代码**写出来（**不能写 Python/Java 语法**，否则不给分）；
3. 分析**时间复杂度**。题目经常写"只有最优复杂度的解法才能拿满分"——如果能做到 Θ(n log n) 你却写了指数级算法，只能拿很少的分。

设计题的规则（教授原话）：
- 可以直接调用课上讲过的算法，但必须**写明是哪一个**。例如可以写 `Mergesort(A)`；只写"把数组排序"不行，因为不知道复杂度。
- 用哈希表必须说清楚：哈希函数是什么、冲突用什么方法处理。说不清就自己写出那几行。
- **只能用讲课内容里的东西**，不要用课外算法。

### 考试范围（examinable）

| 主题 | 范围 |
|---|---|
| 基础（Fundamentals）、算法分析 | 全部 |
| 暴力法与穷举搜索 | 全部，**除了凸包（convex hull）** |
| 减治（Decrease and Conquer） | 全部 |
| 分治（Divide and Conquer） | 课本 5.1–5.3；**主定理（Master Theorem）公式考试会给出，但你必须会用** |
| 变治（Transform and Conquer） | 全部 |
| 时空权衡（Time/Space Tradeoffs） | 全部，**除了 Boyer-Moore 和 KMP**（Horspool 要考！） |
| 动态规划 | 全部，**几乎每年都考，必须掌握** |
| 贪心 | 全部，**除了 Kruskal**（只讲了一页） |
| NP 完全 | **不考细节**，最多几道是/否的基础题；但"问题归约"的思想对设计题非常有用 |

---

## 二、目录（严格按授课顺序）

| # | 文件 | 对应讲次 | 主题 |
|---|---|---|---|
| 0 | [00-pseudocode-and-math.md](00-pseudocode-and-math.md) | 预备 | 伪代码写法、必备数学（求和、对数） |
| 1 | [01-introduction-and-data-structures.md](01-introduction-and-data-structures.md) | L1–L2 | 什么是算法、欧几里得算法、数组/链表/栈/队列 |
| 2 | [02-growth-rate.md](02-growth-rate.md) | L3 | 基本操作、最好/最坏/平均情况、O / Ω / Θ |
| 3 | [03-analysis-of-algorithms.md](03-analysis-of-algorithms.md) | L4 | 极限法比较增长率、循环求和、递推式与倒推法 |
| 4 | [04-brute-force.md](04-brute-force.md) | L5 | 选择排序、排序的三个性质、字符串匹配、最近点对、穷举搜索 |
| 5 | [05-recursion.md](05-recursion.md) | L6 | 阶乘、斐波那契、汉诺塔、找零方案数 |
| 6 | [06-graphs.md](06-graphs.md) | L7 | 图的概念、邻接矩阵与邻接表、图建模 |
| 7 | [07-graph-traversal.md](07-graph-traversal.md) | L8 | DFS、BFS、拓扑排序 |
| 8 | [08-decrease-by-constant.md](08-decrease-by-constant.md) | L9 | 插入排序、哨兵、希尔排序 |
| 9 | [09-decrease-by-factor.md](09-decrease-by-factor.md) | L10 | 二分查找、插值查找、Lomuto 划分、QuickSelect |
| 10 | [10-divide-and-conquer-sorting.md](10-divide-and-conquer-sorting.md) | L11 | 主定理、归并排序、快速排序（Hoare 划分） |
| 11 | [11-trees-and-closest-pair.md](11-trees-and-closest-pair.md) | L12 | 二叉树、树高、四种遍历、分治最近点对 |
| 12 | [12-heaps-and-heapsort.md](12-heaps-and-heapsort.md) | L13 | 优先队列、堆、自底向上建堆、堆排序 |
| 13 | [13-transform-and-conquer.md](13-transform-and-conquer.md) | L14 | 预排序、二叉搜索树 BST |
| 14 | [14-balanced-trees.md](14-balanced-trees.md) | L15 | AVL 树四种旋转、2–3 树 |
| 15 | [15-time-space-tradeoffs.md](15-time-space-tradeoffs.md) | L16 | 记忆化、计数排序、Horspool 字符串查找 |
| 16 | [16-hashing.md](16-hashing.md) | L17 | 哈希函数、Horner 法则、拉链法、线性探测、双重哈希、Rabin-Karp |
| 17 | [17-dynamic-programming.md](17-dynamic-programming.md) | L18 | 硬币行问题、0/1 背包、记忆化、编辑距离 |
| 18 | [18-warshall-and-floyd.md](18-warshall-and-floyd.md) | L19 | 传递闭包、全源最短路径 |
| 19 | [19-greedy-prim-dijkstra.md](19-greedy-prim-dijkstra.md) | L20 | 贪心、最小生成树 Prim、单源最短路 Dijkstra |
| 20 | [20-huffman.md](20-huffman.md) | L21 | 变长编码、前缀码、哈夫曼树 |
| 21 | [21-np-completeness.md](21-np-completeness.md) | L22 | P、NP、归约（了解即可） |
| 22 | [22-exam-strategy-and-cheatsheet.md](22-exam-strategy-and-cheatsheet.md) | 总复习 | 总表、设计题方法论、模拟题与详解 |

---

## 三、建议的学习计划

| 阶段 | 做什么 | 时间 |
|---|---|---|
| 第 1 轮：学懂 | 按顺序读 00–21，每个手算演示自己算一遍，做完每讲练习 | 约 10–14 天，每天 2 讲 |
| 第 2 轮：刷题 | 重做所有辅导课题目（week02–week12）和所有 Weekly Quiz | 3–4 天 |
| 第 3 轮：设计题 | 读 22 号文件的方法论，独立完成里面的设计题，再对答案 | 2–3 天 |
| 第 4 轮：模拟 | **学完之后**再做 LMS 上的 Practice Exam（教授特别强调不要一开始就做），限时 | 1 天 |
| 考前一天 | 只看 22 号文件的总表和每讲的"考点与易错" | — |

**拿满分的三条原则**
1. 追踪题：严格按照**课上版本**的算法走（比如快排用 Hoare 划分、QuickSelect 用 Lomuto 划分、堆用 1 开始的数组下标），每一步都写出中间状态。
2. 设计题：先写出思路（一句话），再写伪代码，最后写复杂度并说明理由。能用更低复杂度就一定要用。
3. 性质题：别死记，学会**推导**。比如"归并排序稳定吗？"——想一想合并时相等元素先取左边，所以稳定。
