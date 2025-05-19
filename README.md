# Solar Challenge Week 1

This repository contains the code and analysis for the Solar Challenge Week 1 project, focusing on solar farm data from Benin, Sierra Leone, and Togo.

## Project Overview
This project analyzes solar farm data to identify patterns and optimize solar panel performance. The analysis focuses on:

- Solar irradiance components (GHI, DNI, DHI)
- Environmental parameters (temperature, wind speed, humidity)
- Module performance before and after cleaning

## Key Findings

### Solar Irradiance Analysis
- All irradiance components (GHI, DNI, DHI) show right-skewed distributions
- Strong positive correlations exist between irradiance components
- GHI ranges from 0 to ~1400 W/m²

### Environmental Factors
- Temperature follows a normal distribution (10-45°C)
- Wind speed is right-skewed with most values between 0-5 m/s
- Relative humidity shows a bimodal distribution with negative correlations to other variables

### Module Performance
- Significant performance improvement after cleaning:
  - ModA: 30% improvement (236.52 → 307.23)
  - ModB: 32% improvement (228.82 → 301.97)

### Time Series Patterns
- Consistent weekly patterns in GHI
- Stable temperature trends throughout the dataset

## Recommendations
1. Implement regular cleaning schedules based on performance degradation
2. Monitor humidity levels as they negatively correlate with performance
3. Leverage correlations between variables for prediction models
4. Consider wind speed patterns for maintenance scheduling

## Project Structure
- notebooks/ : Jupyter notebooks for data analysis
- scripts/ : Reusable code scripts
- src/ : Core functionality
- tests/ : Test components

## Environment Setup

1. Clone the repo:
```bash
git clone https://github.com/duleab/solar-challenge-week1.git
cd solar-challenge-week1