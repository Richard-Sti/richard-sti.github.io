---
layout: page
title: Methods
permalink: /methods
description: "Richard Stiskalek's statistical and computational skills: Bayesian modelling, simulation-based inference, machine learning, and scientific software in Python and JAX."
---

I develop these methods in cosmology, where the structure and expansion of the Universe must be inferred from incomplete observations. [Research](/research) covers the applications.

My approach is Bayesian. I sample posterior distributions over model parameters conditioned on the observed data, so that estimates and predictions come with their uncertainties. The models are expensive to evaluate and I run them on GPUs and high-performance computing clusters, including cosmological simulation code that I write for GPUs.

I work mainly in Python with `JAX`, `NumPyro`, and `BlackJAX`, alongside `NumPy` and `SciPy`. I also use Julia, C++, and Fortran.

## Machine learning and scalable inference

I build emulators for expensive, high-dimensional models, usually on 3D fields, so that parameter inference becomes tractable. When a model can generate data but its likelihood is intractable, I use simulation-based inference and estimate the posterior from simulations alone.

I also make numerical models differentiable so that Hamiltonian Monte Carlo can reach millions of parameters, and reparametrise and precondition them where the posterior geometry is difficult. For emulation, I cut memory use to fit large models onto a single GPU and shard training across several.

My applied machine-learning work includes:

- **Probabilistic prediction:** neural-network ensembles that predict galaxy properties and their scatter from simulation data ([paper](https://arxiv.org/abs/2202.14006)).
- **Density estimation:** mixture density networks that infer distributions over unobserved galaxy luminosities from measured brightnesses ([paper](https://arxiv.org/abs/2405.09720)).
- **Graph-based learning:** benchmarking graph neural networks on 3D point clouds and branching histories to predict parameters and motions ([CosmoBench](https://arxiv.org/abs/2507.03707)).

## Combining noisy and incomplete data

I work with noisy, incomplete data in which missing observations and correlated errors can affect the result. I start with a model of the underlying population, then model individual observations, including their measurement errors and the process that determines whether they enter the dataset. I account for shared calibrations and other dependencies within this hierarchical Bayesian model, and fit it to make predictions with uncertainty at both the population and individual levels.

## Validation on simulated data

I run validation campaigns on simulated datasets with known inputs, testing the full inference pipeline for bias and calibrated uncertainty. I vary the data-generating assumptions, priors, and model choices to identify failure modes, and use sampling diagnostics to distinguish convergence problems from weak constraints in the data.

Alongside the models I write the tests and workflows that generate the simulations and analyse the output. My code is on [GitHub](https://github.com/Richard-Sti).
