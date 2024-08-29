# MODELLING SPACE-CHARGE-LIMITED CURRENT (SCLC) IN SEMICONDUCTORS

[![Jungstershark - SCLC-Modelling](https://img.shields.io/static/v1?label=Jungstershark&message=SCLC-Modelling&color=blue&logo=github)](https://github.com/Jungstershark/SCLC-Modelling "Go to GitHub repo")
[![stars - SCLC-Modelling](https://img.shields.io/github/stars/Jungstershark/SCLC-Modelling?style=social)](https://github.com/Jungstershark/SCLC-Modelling)
[![forks - SCLC-Modelling](https://img.shields.io/github/forks/Jungstershark/SCLC-Modelling?style=social)](https://github.com/Jungstershark/SCLC-Modelling)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

## Overview

This repository contains the code and results for modeling the transition from field emission to space-charge-limited current (SCLC) in semiconductors. The study explores the behavior of current conduction under varying electron emission conditions, based on the Fowler-Nordheim and Child-Langmuir laws.

## Project Background

The research investigates how current conduction transitions from field emission to SCLC, which is crucial for applications in both low-current devices (like EMP-resilient electronics) and high-current industrial systems. The models account for both collision and non-collision scenarios, providing valuable insights for semiconductor design.

## Key Models

- *JV-model.py:* Simulates J-V characteristics under different emission conditions.
- *lau-model.py:* Models SCLC using Fowler-Nordheim and Child-Langmuir laws.
- *thermionic-v2.py:* Focuses on thermionic emission processes.

## How to Use

### Prerequisites

Install the required libraries:
```bash
pip install -r requirements.txt
```

### Running the Scripts

- *JV-model.py:* Run with python JV-model.py to generate J-V plots.
- *lau-model.py:* Execute with python lau-model.py for log-log J(E) vs. V(E) plots.
- *thermionic-v2.py:* Run python thermionic-v2.py for thermionic emission analysis.

## Future Work

Plans include refining the models for broader applications and incorporating more complex emission surfaces.

## Poster
<div align="center">
    <img src="/Poster.png" alt="Poster" width="600" height="800">
</div>
