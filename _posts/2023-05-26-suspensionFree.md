---
title: 'Number of triangles in graphs without suspensions of 4-vertex paths'
date: 2023-05-26
permalink: /posts/2023/05/suspensionFree/
tags:
  - suspension, extremal graph theory
---

# Introduction: The generalized Tur\'an problem

Given graphs $T$ and $H$, the generalized extremal number $\text{ex}(n, T, H)$ is given by the maximum number of (non-induced) copies of $T$ in an $H$-free graph on $n$ vertices.
Historically speaking, one of the first papers that give a general treatment of this problem is that of [Alon and Shikhelman, 2014](https://arxiv.org/abs/1409.4192), and many researchers have since then expanded upon the theory of this generalized Tur\'an problem.

## Bipartite suspensions

In 2020, together with my PhD advisor Dhruv Mubayi, we wrote a paper where we focused on the specific case $T=K_3$ and $H$ a _suspension_ of a bipartite graph. The original manuscript is available at [arXiv:2004.11930](https://arxiv.org/abs/2004.11930). Among several results, we studied the case $H=\hat{P}_k$, which is the main focus of this blog post.

**In our notation, $P_k$ is the path on $k$ edges (and $k+1$ vertices)**

## Path suspensions

Our main results for suspensions of paths was the following: for $n\ge k \ge 3$,
$$\left\lfloor \frac{k-1}{2}\right\rfloor\cdot \frac{n^2}{8} \le \frac{k-1}{12}\cdot n^2 + \frac{(k-1)^2}{12}\cdot n.$$

Further, we showed that for $k=3,4,5$ we have
$$\text{ex}(n,K_3,\hat{P}_k) = \left\lfloor \frac{k-1}{2}\right\rfloor \cdot \frac{n^2}{8} + o(n^2),$$

and for $k=3$ and $k=5$ we improved the $o(n^2)$ error bound to $O(n)$.

## The work of Gerbner

Around two years after our paper was initially uploaded to arXiv, D\'aniel Gerbner proved in [arXiv:2203.12527](https://arxiv.org/abs/2203.12527) that for $n\ge 525$ and $k=3$, the result above is exact; i.e. 
$$(1) \qquad \text{ex}(n,K_3,\hat{P}_3)=\left\lfloor n^2/8\right\rfloor.$$

Their result actually builds upon the technique of asserting that the graphs that have many triangles and are $\hat{P}_3$-free are also Berge-$K_4$-free, and use this along with progressive induction to obtain the desired upper bound.

# Closing the bounds for $n\ge 8$

It was mentioned that if the upper bound of $\lfloor n^2/8\rfloor$ can be proved for $n=8,9,10,11$, then ordinary induction can be used to prove $(1)$.

In fact, we note here that a careful analysis of the same argument used in our original manuscript, does close this bound.


