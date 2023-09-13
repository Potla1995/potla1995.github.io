---
title: "Robustness for Spectral Clustering of General Graphs under Local Differential Privacy"
collection: publications
permalink: /publication/privacyClustering
excerpt: 'Spectral clustering is robust for social networks in general with privacy budget $\epsilon=O(\log n)$, and this result is tight.'
date: 2023-09-13
venue: 'Preprint'
paperurl: ''
citation: 'Mukherjee, Sayan and Suppakitpaisarn, Vorapong. "Robustness for Spectral Clustering of General Graphs under Local Differential Privacy." <i>(preprint)</i>'
---
Spectral clustering is a widely used algorithm to find clusters in networks.
Several researchers have studied the stability of spectral clustering under local differential privacy with the additional assumption that the underlying networks are generated from the stochastic block model (SBM).
However, we argue that this assumption is too restrictive since social networks do not originate from the SBM.
Thus, we delve into an analysis for general graphs in this work.
Our primary focus is the edge flipping method -- a common technique for protecting local differential privacy.
On a positive side, our findings suggest that even when the edges of an $n$-vertex graph satisfying some reasonable well-clustering assumptions are flipped with a probability of $O(\log n/n)$, the clustering outcomes are largely consistent.
Empirical tests further corroborate these theoretical findings.
Conversely, although clustering outcomes have been stable for dense and well-clustered graphs produced from the SBM, we show that in general, spectral clustering may yield highly erratic results on certain dense and well-clustered graphs when the flipping probability is $\omega(\log n/n)$.
This indicates that the best privacy budget obtainable for general graphs is $\Theta(\log n)$.

[Download paper here](/files/privacyClustering.pdf)

