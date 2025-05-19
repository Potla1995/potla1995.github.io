---
title: "Locally Differentially Private Graph Clustering via the Power Iteration Method"
collection: publications
permalink: /publication/powerIterPrivacy
excerpt: 'We modify the power iteration method to achieve locally differentially private clustering for general graphs with constant privacy budget.'
date: 2025-05-16
venue: 'arXiv Preprint'
paperurl: 'https://arxiv.org/abs/2505.11169'
citation: 'Suppakitpaisarn, Vorapong and Mukherjee, Sayan. "Locally Differentially Private Graph Clustering via the Power Iteration Method." <i>arXiv Preprint arXiv:2505.11169</i>'
---
We propose a locally differentially private graph clustering algorithm.
Previous works have explored this problem, including approaches that apply spectral clustering to graphs generated via the randomized response algorithm.
However, these methods only achieve accurate results when the privacy budget is in $\Omega(\log n)$, which is unsuitable for many practical applications.
In response, we present an interactive algorithm based on the power iteration method. Given that the noise introduced by the largest eigenvector constant can be significant, we incorporate a technique to eliminate this constant.
As a result, our algorithm attains local differential privacy with a constant privacy budget when the graph is well-clustered and has a minimum degree of $\tilde{\Omega}(\sqrt{n})$.
In contrast, while randomized response has been shown to produce accurate results under the same minimum degree condition, it is limited to graphs generated from the stochastic block model.
We perform experiments to demonstrate that our method outperforms spectral clustering applied to randomized response results. 

[Download paper here](https://arxiv.org/pdf/2505.11169)

