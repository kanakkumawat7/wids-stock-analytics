# Stock Market Analytics: From Data to Forecasts

A beginner-friendly 4-week project on stock market analytics using Python and NSE data, from data collection and analysis to forecasting.

**WiDS 6.0 | The Analytics Club**

> The goal is to learn rigorous analysis and evaluation, not to find a money-making strategy.

---

## Overview
You will work with real Indian stock market data: download it, clean it, explore it, and build simple forecasting models. Along the way you will learn how to evaluate models honestly, including how to avoid common pitfalls like look-ahead bias and overfitting.

## What you will learn
- Python, NumPy, pandas and matplotlib for data analysis
- Market basics: OHLCV data, returns, volatility
- Statistical and time-series analysis
- Simple forecasting models, baselines and backtesting
- Writing up results clearly

## Prerequisites
- Basic programming exposure (not compulsory to have)
- No finance background needed

## Weekly plan
| Week | Topic | Materials | Output
|------|-------|-----------| ------|
| 1 | Python foundations(pandas, numpy, matplotlib, EDA, market basics) | [week1](./week1) | |
| 2 | Coming soon | | |
| 3 | Coming soon | | |
| 4 | Coming soon | | |

## Getting started
1. Clone the repository
   ```bash
   git clone https://github.com/kanakkumawat7/wids-stock-analytics.git
   cd wids-stock-analytics
   ```
2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Start with [Week 1](./week1/README.md)

## Ground rules
1. Always split data by time, never randomly. Train on the past, test on the future.
2. No look-ahead. Never use future information to predict the past.
3. Compare every model against a simple baseline.
4. Report results honestly, including negative ones.
5. Log your progress and write what you learned weekly in [`docs/PROGRESS.md`](./docs/PROGRESS.md).

## Submission
Two submissions would be required: MidTerm Submission and Final Submission. Submit your notebook or script, your plots, and a short entry in `docs/PROGRESS.md`.

## Disclaimer
This project is for educational purposes only and is not financial advice.

## Mentors
[Kanak](https://github.com/kanakkumawat7)

[Saksham Jindal](https://github.com/sakjin2)
