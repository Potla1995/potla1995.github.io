---
title: "Neural Sequence Transformation"
collection: publications
permalink: /publication/neuralSeqTr
excerpt: 'Using neural networks to perform sequence transformation.'
date: 2021-11-27
venue: 'Computer Graphics Forum; Pacific Graphics Conference 2021'
paperurl: '/files/neuralSeqTr.pdf'
citation: 'Mukherjee, Sabyasachi; Mukherjee, Sayan; Hua, Binh-Son; Umetani, Nobuyuki and Meister, Daniel. "Neural Sequence Transformation." <i>Computer Graphics Forum</i> (Wiley), Volume 40, Issue 7, Pages 131-140 (2021).'
---
Monte Carlo integration is a technique for numerically estimating a definite integral by stochastically sampling its integrand.
These samples can be averaged to make an improved estimate, and the progressive estimates form a sequence that converges
to the integral value on the limit. Unfortunately, the sequence of Monte Carlo estimates converges at a rate of $O(\sqrt n)$, where
$n$ denotes the sample count, effectively slowing down as more samples are drawn. To overcome this, we can apply sequence
transformation, which transforms one converging sequence into another with the goal of accelerating the rate of convergence.
However, analytically finding such a transformation for Monte Carlo estimates can be challenging, due to both the stochastic
nature of the sequence, and the complexity of the integrand. In this paper, we propose to leverage neural networks to learn
sequence transformations that improve the convergence of the progressive estimates of Monte Carlo integration. We demonstrate
the effectiveness of our method on several canonical 1D integration problems as well as applications in light transport simulation.

+ [Download paper here](/files/neuralSeqTr.pdf)
+ Recommended citation: Mukherjee, Sabyasachi; Mukherjee, Sayan; Hua, Binh-Son; Umetani, Nobuyuki and Meister, Daniel. "Neural Sequence Transformation." <i>Computer Graphics Forum</i> (Wiley), Volume 40, Issue 7, Pages 131-140 (2021).
+ DOI: 10.1111/cgf.14407 