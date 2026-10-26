# 第 7 章（第 8 讲）图的遍历：DFS、BFS、拓扑排序

> **本章位置**：遍历是"穷举搜索"在图上的体现，也是大量图算法的骨架。
> **考试比重**：非常高。选择题会让你写出 DFS/BFS 访问顺序、压栈/出栈顺序、拓扑序；
> 设计题经常要求"改造 DFS/BFS"来解决新问题（连通性、有环、二着色、最短步数……）。

**本章统一约定**（和课上一致）：从字母序最小的结点开始，**邻居按字母序**考虑。

---

## 1. 深度优先搜索 DFS（Depth-First Search）

**思想**：从一个结点出发，一直往"深处"走到没有未访问的邻居，再**回溯**到最近的、还有未访问邻居的结点。
回溯 = **栈**（后进先出）；递归实现时用的是系统调用栈。

```
function DFS(⟨V, E⟩)
    mark each node in V with 0
    count ← 0
    for each v in V do
        if v is marked with 0 then
            DfsExplore(v)

function DfsExplore(v)
    count ← count + 1
    mark v with count               ▷ 记录访问顺序
    for each edge (v, w) do         ▷ w 是 v 的邻居
        if w is marked with 0 then
            DfsExplore(w)
```
外层 `for` 循环保证图**不连通**时也能访问所有结点（每次进入 DfsExplore 就是一个新的连通分量）。

### 手算演示

```
   d ───── b ───── a ───── c ───── f ───── g
   │        \     /
   │         \   /
   h ─────────  e

   边：a-b, a-c, a-e, b-d, b-e, c-f, d-h, e-h, f-g
```
邻接表（字母序）：
```
a: b c e      b: a d e      c: a f      d: b h
e: a b h      f: c g        g: f        h: d e
```

从 a 开始 DFS：
1. 访问 a，第一个未访问邻居 b → 访问 b
2. b 的邻居：a(已访问)，d → 访问 d
3. d 的邻居：b(已访问)，h → 访问 h
4. h 的邻居：d(已访问)，e → 访问 e
5. e 的邻居 a、b、h 都已访问 → **e 出栈**（回溯）
6. h 没有未访问邻居 → h 出栈；d 出栈；b 的下一个邻居 e 已访问 → b 出栈
7. 回到 a，下一个邻居 c → 访问 c → f → g
8. g、f、c 依次出栈；a 的邻居 e 已访问 → a 出栈

**访问（压栈）顺序**：a b d h e c f g
**出栈顺序**：e h d b g f c a

Levitin 的紧凑记法：下标"压栈序号, 出栈序号"：
a₁,₈ b₂,₄ d₃,₃ h₄,₂ e₅,₁ c₆,₇ f₇,₆ g₈,₅

### DFS 树 / 森林与边的分类（无向图）
- **树边（tree edge）**：DFS 第一次到达新结点时走的边：a-b, b-d, d-h, h-e, a-c, c-f, f-g。
- **回边（back edge）**：指向一个**已访问的祖先**（不是父结点）的边：e-a, e-b。
- 连通图得到一棵 DFS 树；不连通图得到 DFS 森林（每个分量一棵）。

### 复杂度
| 图的表示 | 复杂度 | 原因 |
|---|---|---|
| 邻接矩阵 | **Θ(\|V\|²)** | 对每个 v 要扫描整行 |
| 邻接表 | **Θ(\|V\| + \|E\|)** | 每个结点访问一次，每条边看两次 |

DFS 对有向图同样适用。

---

## 2. 广度优先搜索 BFS（Breadth-First Search）

**思想**：先访问起点的所有邻居，再访问邻居的邻居……一层一层往外扩。用**队列**（先进先出）。

```
function BFS(⟨V, E⟩)
    mark each node in V with 0
    count ← 0
    Q ← empty queue
    for each v in V do
        if v is marked with 0 then
            count ← count + 1
            mark v with count
            Enqueue(Q, v)
            while Q is not empty do
                u ← Dequeue(Q)
                for each edge (u, w) do
                    if w is marked with 0 then
                        count ← count + 1
                        mark w with count       ▷ 入队时就标记！
                        Enqueue(Q, w)
```

### 手算演示（同一张图，从 a 开始）

| 出队 | 新入队的邻居 | 队列（出队后） |
|---|---|---|
| — | a | a |
| a | b, c, e | b c e |
| b | d（a、e 已标记） | c e d |
| c | f | e d f |
| e | h | d f h |
| d | —（b、h 已标记） | f h |
| f | g | h g |
| h | — | g |
| g | — | 空 |

**BFS 访问顺序**：a b c e d f h g
- 树边：a-b, a-c, a-e, b-d, c-f, e-h, f-g
- **交叉边（cross edge）**：b-e、d-h（连接已访问的非父子结点）
- 复杂度与 DFS 相同：矩阵 Θ(V²)，邻接表 Θ(V + E)。

### BFS 的特长：无权图最短路径
BFS 按"层"访问，第一次到达某结点时走的就是**边数最少**的路径。
只要在入队时记录 `dist[w] ← dist[u] + 1`，就能求出起点到所有点的最短步数。

---

## 3. DFS / BFS 的经典应用（设计题素材）

### 3.1 判断连通 / 数连通分量
跑一遍 DFS，外层循环中**调用 DfsExplore 的次数 = 连通分量数**。连通 ⇔ 只调用一次。
给每个结点标上分量编号：
```
function Components(⟨V, E⟩)
    mark each node with 0
    comp ← 0
    for each v in V do
        if v is marked with 0 then
            comp ← comp + 1
            Explore(v, comp)

function Explore(v, comp)
    mark v with comp
    for each edge (v, w) do
        if w is marked with 0 then
            Explore(w, comp)
```

### 3.2 判断无向图是否有环
**无向图有环 ⇔ DFS 森林中存在回边**（或 BFS 森林中存在交叉边）。
关键：遇到已访问的邻居时，要**排除父结点**（父子之间那条树边不算环）。

```
function Cyclic(⟨V, E⟩)
    mark each node with 0
    for each v in V do
        if v is marked with 0 then
            if HasCycle(v, null) then return True
    return False

function HasCycle(v, parent)
    mark v with 1
    for each edge (v, w) do
        if w is marked with 0 then
            if HasCycle(w, v) then return True
        else if w ≠ parent then
            return True            ▷ 回边 ⇒ 有环
    return False
```
> 第 5 周题 30 给的错误算法正是**忘了排除父结点**：只有一条边 a-b 的图，从 a 到 b 后，
> b 看到已访问的 a 就报告"有环"，这是错的。

### 3.3 二着色（二分图）判定（第 6 周题 36）
DFS 时给相邻结点涂相反颜色，一旦发现某个邻居和自己同色就失败。
```
function IsTwoColourable(⟨V, E⟩)
    for each v in V do colour[v] ← 0
    for each v in V do
        if colour[v] = 0 then
            if not Paint(v, 1) then return False
    return True

function Paint(v, c)
    colour[v] ← c
    for each edge (v, w) do
        if colour[w] = c then return False
        if colour[w] = 0 then
            if not Paint(w, 3 − c) then return False
    return True
```
复杂度同 DFS：Θ(V + E)。

---

## 4. 拓扑排序（Topological Sorting）

**问题**：有向图中边 (a, b) 表示"a 必须在 b 之前"。求一个结点的线性顺序 v₁, …, vₙ，使每条边 (vᵢ, vⱼ) 都有 vᵢ 在 vⱼ 前面。
**只有 DAG 才有拓扑序**（有环就无解）。一个 DAG 可能有多个拓扑序。

### 方法 1：DFS，取出栈顺序的**逆序**
理由：若有边 (u, v)，DFS 中 v 一定比 u 先出栈，逆过来 u 就在 v 前面。

### 方法 2：源点删除法（source removal，减治思想）
反复找一个**入度为 0**（没有入边）的结点（源点），输出它，并删除它和它的出边。
缺点：每次都要找源点（可以用入度数组 + 队列优化到 Θ(V + E)）。

### 手算演示
DAG：a→c, b→c, b→d, c→e, d→e, e→f（平局按字母序）

**DFS 法**：
- 从 a：a → c → e → f。f 无出边，出栈；e、c、a 依次出栈。
- 从 b：b → d（c 已访问）→ d 的邻居 e 已访问，d 出栈；b 出栈。
- 出栈顺序：f e c a d b → **逆序：b d a c e f**

**源点删除法**：
| 当前源点 | 选择 | 输出序列 |
|---|---|---|
| a, b | a | a |
| b | b | a b |
| c, d | c | a b c |
| d | d | a b c d |
| e | e | a b c d e |
| f | f | a b c d e f |

两个答案不同，但**都正确**（拓扑序不唯一）。检查方法：逐条边看起点是否在终点前面。

---

## 考点与易错

1. DFS 用栈（递归），BFS 用队列。**BFS 在入队时标记**，否则同一结点会入队多次。
2. 必须严格按"邻居字母序"走，否则顺序题会错。
3. 出栈顺序 ≠ 访问顺序。拓扑排序用的是**出栈顺序的逆序**。
4. 邻接矩阵 Θ(V²)，邻接表 Θ(V+E)——问复杂度时要说明用的是哪种表示。
5. 无向图判环要排除父结点；BFS 可以求无权图最短步数，DFS 不行。
6. 拓扑序可能不唯一；有环的有向图没有拓扑序。

---

## 练习

1.（第 5 周题 27）图 a-b, a-c, b-c, c-d, c-e, d-e，从 a 开始写 DFS 访问顺序、出栈顺序，以及 BFS 顺序。
2.（第 6 周题 35）BFS 怎么判断无向图有环？DFS 和 BFS 谁找环更快？
3. 设计算法：给定无权无向图 G 和两个结点 s、t，求 s 到 t 的最少边数（不可达返回 ∞）。写出复杂度。
4. 对 DAG：a→b, a→d, b→c, d→c, d→e, c→f, e→f 用 DFS 法求拓扑序（字母序）。
5. 一个有向图用 DFS 法得到的"逆出栈序"是否总是拓扑序？什么情况下会出问题？

<details>
<summary>答案</summary>

1. DFS 访问：a b c d e；出栈：e d c b a。（树边 a-b, b-c, c-d, d-e；回边 c-a, e-c。）
   BFS：a b c d e（a 的邻居 b、c；b 的邻居都已标记；c 的邻居 d、e）。
2. 无向图有环 ⇔ BFS 森林中有**交叉边**（遇到已标记且不是父结点的邻居）。没有绝对赢家：
   环在"深处一条长链的末端"时 DFS 先找到；环在起点附近而图很深时 BFS 先找到。
3. ```
   function MinEdges(⟨V, E⟩, s, t)
       for each v in V do dist[v] ← ∞
       dist[s] ← 0
       Q ← empty queue; Enqueue(Q, s)
       while Q is not empty do
           u ← Dequeue(Q)
           if u = t then return dist[t]
           for each edge (u, w) do
               if dist[w] = ∞ then
                   dist[w] ← dist[u] + 1
                   Enqueue(Q, w)
       return dist[t]
   ```
   用邻接表 Θ(|V| + |E|)。
4. 从 a：a→b→c→f；f、c、b 出栈；a→d（c 已访问）→ e（f 已访问），e、d、a 出栈。
   出栈序 f c b e d a，逆序 **a d e b c f**。（检查：a<b, a<d, b<c, d<c, d<e, c<f, e<f ✔）
5. 只有图是 DAG 时才是拓扑序。若图有环，DFS 也会给出一个顺序，但某条边必然"反向"——
   所以使用前要先确认无环（有向图 DFS 中遇到"还在栈中的结点"就说明有环）。
</details>
