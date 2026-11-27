# Stock Market Analytics: Final Report

| | |
|---|---|
| **Name** | |
| **Roll no.** | |
| **Mentor** | |
| **Date** | |
| **Code / notebook link** | |

---

## 1. Problem statement
*What are you predicting (next-day direction or next-day return), for which stocks, and over what period? Why is this a reasonable question to ask?*

## 2. Data
- **Source:** (e.g. yfinance)
- **Tickers:**
- **Date range:**
- **Number of rows:**
- **Cleaning done:** (missing values, holidays, adjustments)

## 3. Exploratory analysis
*Summarise what you found in Weeks 1-2 in 4-6 lines and include 1-2 plots (e.g. price and rolling volatility, or return distribution). What patterns or surprises did you notice?*

## 4. Methods

**Features used:** (list them, e.g. lagged returns, moving averages, rolling volatility, volume change)

**Models tried:** (e.g. ARIMA, Logistic Regression, Random Forest, Gradient Boosting; LSTM is optional)

**Baseline definition:** (e.g. "always predict up" or "tomorrow's direction = today's direction")

**Train / test split:**
- Train: YYYY-MM-DD to YYYY-MM-DD
- Test: YYYY-MM-DD to YYYY-MM-DD
- *The split must be by time, never random.*

**Backtest assumptions:** (position sizing, transaction cost per trade, e.g. 0.1%)

## 5. Results

| Model | Test accuracy | Strategy return | Sharpe ratio | Max drawdown | Buy-and-hold return |
|-------|---------------|-----------------|--------------|--------------|---------------------|
| Baseline | | | | | |
| ARIMA | | | | | |
| Logistic Regression | | | | | |
| Random Forest | | | | | |
| LSTM (optional) | | | | | |

*Write "not attempted" in any row you skipped. Report every model you tried, including the ones that failed.*

## 6. Discussion
- Did any model beat the baseline? By how much, and is that difference meaningful or just noise?
- Did the strategy beat buy-and-hold after transaction costs?
- Where could look-ahead leakage have crept in, and how did you check for it?
- Where could overfitting have happened (too many features, tuning on the test set)?

## 7. Limitations and next steps
*What would you do with more time or data? What are the weaknesses of your approach?*

## 8. Reproducibility
- Python version:
- How to run your notebook or script, start to finish:
- Random seeds used (if any):

---
*This report is for educational purposes only and is not financial advice.*
