# Week 1: Python Foundations + Meet the Market

**Goal:** get comfortable with Python, NumPy, pandas and matplotlib, then use them on real NSE data.

---

## Part A: Python basics
| # | Resource | Type |
|---|----------|------|
| 1 | [Kaggle: Intro to Programming](https://www.kaggle.com/learn/intro-to-programming) | Course |
| 2 | [Kaggle: Python](https://www.kaggle.com/learn/python) | Course |
| 3 | [Python basics (YouTube)](https://www.youtube.com/watch?v=kqtD5dpn9C8) | Video |

## Part B: NumPy, pandas and matplotlib
| # | Resource | Type |
|---|----------|------|
| 1 | [Intro to NumPy, pandas and Matplotlib](https://www.kaggle.com/code/chats351/introduction-to-numpy-pandas-and-matplotlib) | Notebook |
| 2 | [Kaggle: Pandas](https://www.kaggle.com/learn/pandas) | Course |
| 3 | [Kaggle: Data Visualization](https://www.kaggle.com/learn/data-visualization) | Course |
| 4 | [Video 1](https://www.youtube.com/watch?v=zI5ducyfyNc) | Video |
| 5 | [Video 2](https://www.youtube.com/watch?v=MiiANxRHSv4) | Video |
| 6 | [Pandas basics](https://www.youtube.com/watch?v=EXIgjIBu4EU&t=1215s) | Video |

> You don't need to memorise syntax. A basic understanding is enough, and you can always look things up in the docs:
> [Python](https://docs.python.org/) · [NumPy](https://numpy.org/doc/) · [Matplotlib](https://matplotlib.org/stable/index.html) · [pandas](https://pandas.pydata.org/docs/)

## Part C: Market basics
Read [market-basics.md](./market-basics.md) (about 10 minutes).

---

## Task: Meet the Market
1. Download at least 3 years of daily data for 3 NSE stocks (e.g. `RELIANCE.NS`, `TCS.NS`, `INFY.NS`) and the Nifty 50 index (`^NSEI`) using `yfinance`.
2. With pandas, compute:
   - daily returns
   - 20-day rolling volatility
   - cumulative returns
3. Create these plots (with titles, axis labels and legends):
   - closing prices
   - histogram of daily returns
   - rolling volatility
   - cumulative returns of each stock vs Nifty 50
4. Build a summary table: mean return, standard deviation, best day and worst day for each stock.
5. Write 5-6 lines: which stock was the most volatile? Do the stocks move with the Nifty? Did you notice any unusual spikes or dips?

**Stretch goals:** a correlation matrix of returns, or how the stocks behaved during the March 2020 crash.

## Submission
- Your notebook or `.py` script
- The plots
- An entry in [`docs/PROGRESS.md`](../docs/PROGRESS.md)

## What we look for
- Code runs from start to finish
- Plots are clear and labelled
- The write-up contains at least one real insight, not just numbers

## Common mistakes
- Subtracting prices instead of using `pct_change()`
- Ignoring missing data on weekends and holidays
- Plotting stocks with very different price scales on one axis (normalise first)
