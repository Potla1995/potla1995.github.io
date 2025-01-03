---
title: 'Number of triangles in graphs without suspensions of 4-vertex paths'
date: 2023-05-26
permalink: /posts/2023/05/suspensionFree/
tags:
  - suspension, extremal graph theory
---

This blog post has now appeared as a full paper in _Discrete Mathematics_.
See [Exact generalized Tur\'an number for $K_3$ versus suspension of $P_4$](https://sayan.mukherjee.moe/publication/hatP4Free) for details.

# Introduction: The generalized Tur\'an problem

Given graphs $T$ and $H$, the generalized extremal number $\text{ex}(n, T, H)$ is given by the maximum number of (non-induced) copies of $T$ in an $H$-free graph on $n$ vertices.
Historically speaking, one of the first papers that give a general treatment of this problem is that of [Alon and Shikhelman, 2014](https://arxiv.org/abs/1409.4192), and many researchers have since then expanded upon the theory of this generalized Tur\'an problem.

## Bipartite suspensions

In 2020, together with my PhD advisor Dhruv Mubayi, we wrote a paper where we focused on the specific case $T=K_3$ and $H$ a _suspension_ of a bipartite graph.
The original manuscript is available at [arXiv:2004.11930](https://arxiv.org/abs/2004.11930).
Among several results, we studied the case $H=\hat{P}_k$, which is the main focus of this blog post.

**In our notation, $P_k$ is the path on $k$ edges (and $k+1$ vertices)**

## Path suspensions

Our main results for suspensions of paths was the following: for $n\ge k \ge 3$,
$$\left\lfloor \frac{k-1}{2}\right\rfloor\cdot \frac{n^2}{8} \le \frac{k-1}{12}\cdot n^2 + \frac{(k-1)^2}{12}\cdot n.$$

Further, we showed that for $k=3,4,5$ we have
$$\text{ex}(n,K_3,\hat{P}_k) = \left\lfloor \frac{k-1}{2}\right\rfloor \cdot \frac{n^2}{8} + o(n^2),$$

and for $k=3$ and $k=5$ we improved the $o(n^2)$ error bound to $O(n)$.

## The work of Gerbner

Around two years after our paper was initially uploaded to arXiv, Daniel Gerbner proved in [arXiv:2203.12527](https://arxiv.org/abs/2203.12527) that for a sufficiently large $n$ (say $n\ge 8525$) and $k=3$, the result above is exact; i.e. 
$$\text{ex}(n,K_3,\hat{P}_3)=\left\lfloor n^2/8\right\rfloor.$$

Their result actually builds upon the technique of asserting that the graphs that have many triangles and are $\hat{P}_3$-free are also Berge $K_4$-free, and use this along with progressive induction to obtain the desired upper bound.

# Closing the bounds for $n\ge 8$

It was mentioned by Gerbner in their note that if the upper bound of $\lfloor n^2/8\rfloor$ can be proved for $n=8,9,10,11$, then ordinary induction can be used to prove $(1)$.

In fact, we note here that a careful analysis of the same argument used in our original manuscript, does close this bound.

## Some useful lemmas

We need a few useful lemmas which we just state here (with references):

- **Lemma 1:** (Double-counting) If $G$ is $\hat{P}_3$-free, then $3t(G)\le 2e(G)$ where $t(G)$ is the number of triangles in $G$ and $e(G)$ the number of edges.

- **Lemma 2:** (Nordhaus-Stewart) For any $G$ on $n$ vertices, $t(G)\ge \frac{e(G)}{3n}\left(4e(G)-n^2\right)$.

Lemma 1 and 2 can be found in our [original manuscript](https://arxiv.org/abs/2004.11930).

- **Assumption 1:** In what follows, we assume that every edge of the graphs are contained in at least one triangle. This can be done by simply deleting extra edges that do not contribute to any triangle.

## Base case: $n=8$ (using a computer program).

It needs to be shown that any $8$-vertex graph with at least $\lfloor 8^2/8\rfloor+1 = 9$ copies of $K_3$ contains a copy of $\hat{P}_3$.
Let us consider such a graph $G$ on $8$ vertices and $9$ triangles.
First, we observe that such a graph must have two triangles that share a common edge. If all triangles were edge disjoint, then $G$ would have at least $27$ edges.
But this would contradict **Lemma 2** as $\frac{27}{24}\cdot (108-64)=49.5$ is way above the number of triangles ($9$)!
Therefore, we can assume without loss of generality that the two triangles that share an edge are $\{(0,1,2), (0,1,3)\}$.
The total number of graphs which have the above two triangles as subgraphs then, equals $\binom{\binom83-2}{9-2}=177100560\approx 1.7\times 10^8$.

This is still not in the computationally tractable range, and we need to reduce the redundancy even further.

In that vein, we observe that no triangle in $G$ can now intersect the edges $\{02\},\{03\},\{12\},\{13\}$. They can be deleted from the set of allowed triangles.
This removes $16$ more triangles from the allowed set of triangles, giving us a total number of graphs of $\binom{\binom83-18}{9-2}\approx 1.26\times 10^7$.
A naive implementation of checking whether each graph is $\hat{P}_3$-free requires $8 \cdot 7^3$ operations, giving a total cost of around $4.94\times 10^{9}$ operations. 
This calculation requires around 10 minutes of computation time (on 7 threads) of an Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz laptop processor.

The code we used for this brute force calculation is available [here](https://github.com/Potla1995/potla1995.github.io/blob/master/_posts/triangle_count_parallel.py). Below is the output of the run.
```
Removed triangles: {(0, 3, 6) (1, 2, 5) (1, 3, 6) (0, 2, 7) (0, 2, 4) (0, 3, 5) (1, 2, 4) (1, 2, 7) (1, 3, 5) (0, 2, 6) (0, 3, 7) (0, 3, 4) (1, 2, 6) (1, 3, 4) (1, 3, 7) (0, 2, 5) }
Available triangles: {(0, 5, 7), (3, 5, 6), (1, 5, 7), (0, 1, 6), (2, 5, 7), (4, 5, 6), (4, 6, 7), (1, 4, 5), (3, 4, 7), (2, 4, 5), (3, 6, 7), (2, 3, 6), (0, 4, 7), (0, 5, 6), (0, 6, 7), (1, 5, 6), (5, 6, 7), (0, 1, 5), (2, 5, 6), (2, 6, 7), (3, 4, 6), (1, 4, 7), (0, 2, 3), (2, 4, 7), (2, 3, 5), (0, 4, 6), (1, 6, 7), (3, 5, 7), (0, 1, 4), (0, 1, 7), (4, 5, 7), (1, 2, 3), (1, 4, 6), (3, 4, 5), (2, 3, 4), (2, 3, 7), (2, 4, 6), (0, 4, 5)}
Generated 12620256 many graphs.
Finished iteration.
```

## Bonus case: $n=7$.

The program that we wrote above also outputs all possible configurations of $7$-vertex graphs with $8$ triangles. The only (upto isomorphism) such graph is given by two $K_4$'s intersecting at a vertex:

![Two K_4's intersecting at a vertex](https://github.com/Potla1995/potla1995.github.io/raw/master/_posts/7-vertex-8-triangles-P3-hat-free.png)

## Next cases $n=9, 10, 11$.

<span style="color:red">**A previous version of this proof had a mistake in the cases $n=9$ and $n=10$: contraction can introduce new triangles and it is possible that the $\hat{P}_3$'s we find in the contracted graph had the apex node at the contracted vertex.**
Said issue has been fixed now as we're only using the deletion operation.</span>

The main idea behind this proof is simply follow the steps of our original proof in [arXiv:2004.11930](https://arxiv.org/abs/2004.11930), Page 9.

We observe the following:

**Observation 1**: Let $G$ be an $n$-vertex $\hat{P}_3$-free graph for $n\in\{9,10,11\}$. If $G$ has a $K_4$, then one of the vertices of this $K_4$ must have exactly $3$ triangles through it.

*Proof sketch*.
In each of these cases, if $G$ has a $K_4=\{a,b,c,d\}$, then no other triangle can touch any edge of the $K_4$. Plus, the neighborhoods of $a, b, c$ and $d$ in $V-\{a,b,c,d\}$ are all disjoint.
Let $t(v)$ denote the number of triangles in $G$ through a vertex $v$.
By the same idea as in the proof, we find a vertex of this $K_4$ (say $a$) such that $|N_G(a)-\{b,c,d\}|\le (n-4)/4\le 1.75$ implying $t(a)=3$. $\blacksquare$

**Observation 2**: Let $G$ be an $n$-vertex $\hat{P}_3$-free graph for $n\in\{9,10,11\}$. If $G$ is $K_4$-free, then $e(G)\le 16, 20, 25$ for $n = 9, 10, 11$.

*Proof sketch*.
If $G$ has no $K_4$, then by our original proof, all triangle blocks of $G$ are books.
Then, $e(G)=2t(G)+r$ where $r$ is the number of books.
Clearly $r\ge 2$, as if $r = 1$ we would have at most $n-2$ triangles which is less than $\lfloor n^2/8\rfloor$.
Thus, we have $e(G)\ge 2t(G)+2$.

Now we use Lemma 2 (Nordhaus-Stewart) to obtain
$$\frac{e(G)-2}{2}\ge \frac{e(G)}{3n}\left(4e(G)-n^2\right),$$
implying
$$4e^2 - e\left(n^2-\frac{3n}{2}\right) + 3n\le 0,$$
leading to
$$e\le \frac18\left(n^2-\frac{3n}{2}+\sqrt{\left(n^2-\frac{3n}{2}\right)^2-48n}\right).$$
Calculating the right side gives us $e\le 16, 20, 25$ for $n = 9, 10, 11$. $\blacksquare$

Now we are all set for proving the base cases of $9, 10, 11$.

- Say $G$ has $11$ vertices and $\lfloor 11^2/8\rfloor + 1 = 16$ triangles.
If $G$ was $K_4$-free, we would have $e(G)\le 25$ (Observation 2) implying $t(G)\le (25-2)/2 = 11.5$ (Proof of Observation 2), a contradiction.
Hence $G$ must have a $K_4$.
In this case, Observation 1 gives us a vertex $a$ with $3$ triangles, deleting which gives a $G'$ on $10$ vertices and $13$ triangles.
This leads into the next case ($n=10$).

- Say $G$ has $10$ vertices and $\lfloor 10^2/8\rfloor + 1 = 13$ triangles.
Again, by the same calculation as the last case ($t(G)\le (20-2)/2 = 9$ if $G$ had no $K_4$), we find a $K_4$ inside $G$.
Say the vertices of this $K_4$ are $a,b,c,d$.
Note that $K_4$ is a triangle block by itself, and $\hat P_3$'s must be part of a single block.

    In what follows, we denote by $x_a$ the number of _external_ neighbors of $a$ (those outside the $K_4$).
    The proof of **Observation 1** gave us a vertex $a$ with $x_a\le 1$.
    Together with **Assumption 1**, this means $x_a=0$. 
    Then, $x_b+x_c+x_d\le 6$. Without loss of generality assume that $b$ only lies in one outward triangle, meaning $x_b=2$. Then, let $G'=G-a-b$. It is clear that $G'$ has $t(G)-4 = 9$ triangles on $8$ vertices, which, by the base case, has a $\hat{P}_3$.

- Say $G$ has $9$ vertices and $\lfloor 9^2/8\rfloor + 1 = 11$ triangles.
Again by **Assumption 1** we can easily find a $K_4$ on vertices $a,b,c,d$ with $x_a=0$.
Since $x_b+x_c+x_d\le 5$, we can assume without loss of generality that $x_b\le 1$ and hence again by **Assumption 1**, $x_b=0$.

    Now $x_c+x_d\le 5$, implying we may assume $x_c\le 2$. Deleting $a,b,c$ gives a graph $G'$ on $6$ vertices and at least $11-5=6$ triangles.
    It's definitely possible to prove that $G'$ has a $\hat{P}_3$ by hand, but I just ran the [above script](https://github.com/Potla1995/potla1995.github.io/blob/master/_posts/triangle_count_parallel.py), modifying the variables `num_vertices` and `num_triangles`.
    The following output was obtained:
    ```
    Removed triangles: {(1, 2, 5) (0, 2, 4) (0, 3, 5) (1, 2, 4) (1, 3, 5) (0, 3, 4) (1, 3, 4) (0, 2, 5) }
    Available triangles: {(1, 4, 5), (2, 4, 5), (0, 1, 5), (0, 2, 3), (2, 3, 5), (0, 1, 4), (1, 2, 3), (3, 4, 5), (2, 3, 4), (0, 4, 5)}
    Generated 210 many graphs.
    Finished iteration.
    ```

# Concluding Remarks

This analysis along with Gerbner's work _exactly_ determines $\text{ex}(n, K_3, \hat{P}_3)$.
We demonstrate that the values of $\text{ex}(n,K_3,\hat{P}_3)$
are given by,

- $\text{ex}(4, K_3,\hat{P}_3) = 4$, an extremal graph is $K_4$
- $\text{ex}(5, K_3,\hat{P}_3) = 4$, an extremal graph is $K_4(0,1,2,3)\sqcup\{4\}$
- $\text{ex}(6, K_3,\hat{P}_3) = 5$, an extremal graph is $K_4(0,1,2,3)\cup \text{triangle}(0,4,5)$
- $\text{ex}(7, K_3,\hat{P}_3) = 8$, an extremal graph is $K_4(0,1,2,3)\cup K_4(0,4,5,6)$
- $$\text{ex}(n,K_3,\hat{P}_3)= \lfloor n^2/8 \rfloor \text{ for }n\ge 8,$$
and an extremal graph is $K_{\lfloor n/2\rfloor,\lceil n/2\rceil}$ with a matching in the smaller part.


Closing the gaps in $\text{ex}(n,K_3,\hat{P}_k)$ for larger $k$ will require some other ideas or techniques, as our current technique does not easily generalize to larger $k$.
