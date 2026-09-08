---
layout: page
title: Methods
permalink: /methods
description: "Richard Stiskalek's statistical and computational skills: Bayesian modelling, simulation-based inference, machine learning, and scientific software in Python and JAX."
---

I build models and infer posterior distributions over their parameters conditioned on observed data. I also run computationally expensive simulations on state-of-the-art GPUs and high-performance computing clusters, optimising runtime and memory use.

I work mainly in Python with `JAX`, `NumPyro`, and `BlackJAX`, alongside `NumPy` and `SciPy`. I also use Julia, C++, and Fortran.

Here are the main methods I use; the applications are on my [Research](/research) page.

## Selection effects and incomplete data

Brighter galaxies are easier to detect. If we ignore this when analysing a survey, we can misjudge the properties of the galaxy population. I model how objects enter a sample as part of the inference, including uncertainty in the detection process. I use this approach in work on galaxy populations and measurements of the expansion rate.

## Hierarchical Bayesian models

I often combine measurements with different calibrations and sources of scatter. I use hierarchical models to estimate their shared parameters and individual offsets together, carrying calibration uncertainty through to the result. Where datasets share calibration measurements, I account for the correlations this introduces.

## Simulation-based inference

For some problems, I can simulate observations but cannot readily evaluate their likelihood. I use methods such as normalising flows to estimate parameter distributions from simulated data. I test the inference on simulations with known inputs to check for bias and whether the uncertainties are well calibrated.

## High-dimensional inference

Reconstructing the initial conditions of the Universe can require millions of parameters. I work with Hamiltonian Monte Carlo and other gradient-based samplers, using JAX to differentiate through numerical simulations and run them on GPUs. I work on reparametrisation and preconditioning to improve sampling, and use convergence diagnostics to assess the runs.

## Checking models and uncertainties

I test models on synthetic data, compare their predictions with observations, and repeat analyses with different priors and modelling assumptions. Simulations with known inputs let me check whether the method recovers those inputs and how often its uncertainty intervals contain them.

## Machine learning and software

I use normalising flows for density estimation, Gaussian processes for interpolation, and neural networks and tree-based models to study relationships in data. I am also interested in graph-based methods for spatial data.

My software runs on GPUs and high-performance computing clusters. Alongside the inference code, I write tests and workflows for generating simulations and analysing results. My projects are on [GitHub](https://github.com/Richard-Sti).
