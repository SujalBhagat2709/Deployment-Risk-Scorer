# Deployment Risk Scorer

## Overview

Deployment Risk Scorer is a Python application that estimates the risk of deploying a software release.

It evaluates practical deployment factors such as the number of changed files, test coverage, open bugs, and previous deployment failures. Based on these factors, it generates a risk score and deployment recommendation.

## Features

- Add Deployment
- Calculate Risk Score
- Identify Risk Level
- Detect Risk Factors
- Deployment Recommendation
- Highest Risk Deployment
- Deployment Summary

## Project Structure

deployment-risk-scorer/

├── deployment_risk_scorer.py
├── deployment_risk_studio.py
├── README.md
└── .gitignore

## Requirements

- Python 3.x
- No external libraries required

## Run

```bash
python deployment_risk_studio.py