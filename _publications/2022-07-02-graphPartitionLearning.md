---
title: "Learning Graph Partitions"
collection: publications
permalink: /publication/graphPartitionLearning
excerpt: 'Tight query complexity bounds for learning graph partitions.'
date: 2022-07-02
venue: 'Conference on Learning Theory 2022'
paperurl: 
citation: 'Mukherjee, Sayan. "Learning Graph Partitions." <i>arXiv preprint</i> arXiv:2112.07897 (2021).'
---
Given a partition of a graph into connected components, the membership oracle asserts whether any
two vertices of the graph lie in the same component or not. We prove that for $n \ge k \ge 2$, learning the
components of an $n$-vertex hidden graph with $k$ components requires at least $\frac12 (n − k)(k − 1)$ membership
queries. This proves the optimality of the $O(nk)$ algorithm proposed by _Reyzin and Srivastava (2007)_ for
this problem, improving on the best known information-theoretic bound of $\Omega(n \log k)$ queries. Further,
we construct an oracle that can learn the number of components of $G$ in asymptotically fewer queries
than learning the full partition, thus answering another question posed by the same authors. Lastly, we
introduce a more applicable version of this oracle, and prove asymptotically tight bounds of  $\widetilde \Theta(m)$ queries
for both learning and verifying an $m$-edge hidden graph $G$ using this oracle.

[Download paper here](/files/graphPartitionLearning.pdf)

Recommended citation: Mukherjee, Sayan. "Learning Graph Partitions." <i>arXiv preprint</i> arXiv:2112.07897 (2021).