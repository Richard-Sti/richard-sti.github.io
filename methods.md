---
layout: page
title: Methods
permalink: /methods
description: "Richard Stiskalek's statistical and computational skills: Bayesian modelling, simulation-based inference, machine learning, and scientific software in Python and JAX."
---

I develop the methods below in cosmology, where the structure and expansion of the Universe must be inferred from incomplete observations. [Research](/research) covers the applications.

My approach is Bayesian. I sample from posterior distributions over model parameters conditioned on the observed data, quantifying uncertainty in estimates and predictions. I run computationally expensive models on GPUs and high-performance computing clusters. This includes cosmological simulation code that I develop for GPUs.

I work mainly in Python with `JAX`, `NumPyro`, and `BlackJAX`, alongside `NumPy` and `SciPy`. I also use Julia, C++, and Fortran.

## Machine learning and scalable inference

I build emulators for expensive, high-dimensional models, usually working with 3D fields, to make parameter inference tractable. When a model can generate data but its likelihood is intractable, I use simulation-based inference to estimate the posterior from observed data using models trained on simulations.

I also make numerical models differentiable to support Hamiltonian Monte Carlo inference over millions of parameters. I use reparametrisation and preconditioning to improve sampling when the posterior geometry is difficult. For emulation, I reduce memory use to fit large models on a single GPU and distribute training across multiple GPUs.

My applied machine-learning work includes:

- **Probabilistic prediction:** neural-network ensembles that predict galaxy properties and their scatter from simulation data ([paper](https://arxiv.org/abs/2202.14006)).
- **Density estimation:** mixture density networks that infer distributions over unobserved galaxy luminosities from measured brightnesses ([paper](https://arxiv.org/abs/2405.09720)).
- **Graph-based learning:** benchmarking graph neural networks on 3D point clouds and branching histories to predict parameters and motions ([CosmoBench](https://arxiv.org/abs/2507.03707)).

## Combining noisy and incomplete data

I work with noisy, incomplete data in which missing observations and correlated errors can bias the inferred parameters. I start with a model of the underlying population, then model individual observations, including their measurement errors and the process that determines whether they enter the dataset. I account for shared calibrations and other dependencies within this hierarchical Bayesian model and infer its parameters to make predictions with uncertainty at both the population and individual levels.

## Validation on simulated data

I run validation campaigns on simulated datasets with known inputs, testing the full inference pipeline for bias and uncertainty calibration. I vary the data-generating assumptions, priors, and model choices to identify failure modes, and use sampling diagnostics to distinguish convergence problems from weak constraints in the data.

## Beyond cosmology

None of the above is specific to astronomy. The same approach -- a generative model of the population, explicit treatment of measurement error and selection, and validation on simulated data with known answers -- applies wherever measurements are noisy, samples are incomplete, and the forward model is expensive to evaluate. Typical examples are calibrating measurements from several instruments with shared systematics, inferring population properties from censored or truncated samples, and replacing an expensive simulator with an emulator so that inference becomes tractable.

Much of my code is on [GitHub](https://github.com/Richard-Sti).
