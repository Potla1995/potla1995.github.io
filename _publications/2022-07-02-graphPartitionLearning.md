---
title: "Tight query complexity bounds for learning graph partitions"
collection: publications
permalink: /publication/graphPartitionLearning
excerpt: 'Tight query complexity bounds for learning graph partitions.'
date: 2022-07-02
venue: 'Conference on Learning Theory 2022'
paperurl: 'https://arxiv.org/pdf/2112.07897.pdf'
citation: 'Liu, Xizhi, and Mukherjee, Sayan. "Tight query complexity bounds for learning graph partitions." <i>35th Conference on Learning Theory (COLT). Proceedings in Machine Learning Research</i> (2022).'
---
Given a partition of a graph into connected components, the membership oracle asserts whether any two vertices of the graph lie in the same component or not.
We prove that for $n\ge k\ge 2$, learning the components of an $n$-vertex hidden graph with $k$ components requires at least $(k-1)n-\binom k2$ membership queries.
Our result improves on the best known information-theoretic bound of $\Omega(n\log k)$ queries, and exactly matches the query complexity of the algorithm introduced by Reyzin and Srivastava (2007) for this problem.
Additionally, we introduce an oracle, with access to which one can learn the number of components of $G$ in asymptotically fewer queries than learning the full partition, thus answering another question posed by the same authors.
Lastly, we introduce a more applicable version of this oracle, and prove asymptotically tight bounds of $\widetilde\Theta(m)$ queries for both learning and verifying an $m$-edge hidden graph $G$ using it.

[Download paper here](/files/graphPartitionLearning.pdf)

Video Presentation: [Link](https://recorder-v3.slideslive.com/#/share?share=67452&s=38c27581-0819-43de-afde-241b948c717f) (works only on chromium-based browsers)
