# Week 1: Python Foundations + Meet the Market

**Goal:** get comfortable reading Python data code, then use it to explore real NSE stock data and interpret what you see.
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
## Task
Step 1: Run the demo
    python week1/explore.py --tickers RELIANCE.NS TCS.NS INFY.NS

This downloads the data, computes returns, moving averages and rolling volatility, and saves plots in `outputs/`. If your internet is down, add `--synthetic` to test the code on fake data (the task itself needs real data).

Step 2: Read the code
Open `week1/explore.py` and `src/data.py`. You don't need to write them, but you should be able to explain in your own words what each block does (what `pct_change()` computes, what `rolling(20)` does, why we cache the data). Use the Week 1 resources above for anything unfamiliar.

Step 3: Your task
Answer these in `week1/notes.md`:
1. Which of the 3 stocks was the most volatile? How did you measure it?
2. Plot a histogram of returns for one stock. Does it look normal? What do the tails tell you?
3. Compute the correlation of daily returns between the 3 stocks. Which pair moves most closely together?

You'll need a few extra lines of code for questions 2 and 3, and the resources above are enough to figure them out. Add them to `explore.py` or to a new notebook.

**Stretch:** include the Nifty 50 (`^NSEI`) and compare each stock to it.

## Submission
- `week1/notes.md` with your answers and your histogram
- A short entry in [`docs/PROGRESS.md`](../docs/PROGRESS.md): what you learned and where you got stuck
- Your modified script or notebook, if you changed anything

## What we look for
- You ran the code and the plots were generated
- Your answers are backed by numbers from the output, not guesses
- You can explain what the code does
