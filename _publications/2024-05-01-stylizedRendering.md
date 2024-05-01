---
title: "Stylized Rendering as a Function of Expectation"
collection: publications
permalink: /publication/stylizedRendering
excerpt: 'A step towards integrating non-photorealistic stylizations into physically-based rendering systems.'
date: 2024-05-01
venue: 'ACM Transactions on Graphics (SIGGRAPH 2024)'
paperurl: 'https://doi.org/10.1145/3658161'
citation: 'Rex West and Sayan Mukherjee. "Stylized Rendering as a Function of Expectation." <i>ACM Trans. Graph. 43, 4, Article 96 (July 2024)</i>, 19 pages.'
---

![Teaser](/files/stylizedRenderingTeaser.png)	

We propose a generalization of the rendering equation that captures both the realistic light transport of physically-based rendering (PBR) and a subset of non-photorealistic rendering (NPR) stylizations in a principled manner.
The proposed formulation is based on the key observation that both classical transport and certain NPR stylizations can be modeled as a function of expectation.
Given this observation, we generalize the recursive integrals of the rendering equation to recursive functions of expectation.
As estimating functions of expectation can be challenging, especially recursive ones, we provide a toolkit for unbiased and biased estimation comprising prior work, general strategies, and a novel build-your-own strategy for constructing more complex unbiased estimators from simpler unbiased estimators.
We then use this toolkit to construct a complete estimator for the proposed recursive formulation, and implement a sampling algorithm that is both conceptually simple and leverages many of the components of an ordinary path tracer.
To demonstrate the practicality of the proposed method we showcase how it captures several existing stylizations like color mapping, cel shading, and cross-hatching, fuses NPR and PBR visuals, and allows us to explore visuals that were previously challenging under existing formulations.

[Accepted Version](/files/stylizedRendering.pdf)

[Supplemental Material](/files/stylizedRenderingSupplemental.pdf)

