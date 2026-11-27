# Market Basics

## NSE and Nifty 50
The National Stock Exchange (NSE) is where shares are traded in India. The Nifty 50 is an index tracking 50 large companies, often used as a measure of the overall market.

## OHLCV data
Each trading day is summarised by:
- **Open:** first traded price
- **High/Low:** highest and lowest price of the day
- **Close:** last traded price
- **Volume:** number of shares traded

## Returns
Daily return = (today's close - yesterday's close) / yesterday's close
In pandas: `df["Close"].pct_change()`

## Volatility
How much returns fluctuate. Usually measured as the standard deviation of returns. A higher value means a riskier stock.

## Tickers
On `yfinance`, NSE stocks end in `.NS` (e.g. `TCS.NS`) and the Nifty 50 is `^NSEI`.

## Moving averages
The average of the last N closing prices (e.g. 20 days). It smooths out daily noise and shows the trend.

## Distribution of returns
Most days have small returns, with a few very large ones. If you plot a histogram, the "tails" are the extreme days. Stock returns usually have heavier tails than a normal (bell curve) distribution, which means big moves happen more often than a simple model would predict.

## Correlation
A number between -1 and 1 showing how closely two series move together. Near 1 means they tend to move up and down together, near 0 means no relationship, and near -1 means they move in opposite directions. In pandas: `returns.corr()`.

## Adjusted prices
`yfinance` returns prices adjusted for splits and dividends, so they can differ slightly from the prices shown on NSE's website.

## Further reading
- [Zerodha Varsity: Introduction to Stock Markets](https://zerodha.com/varsity/modules/)
- [Investopedia: returns](https://www.investopedia.com/terms/r/return.asp)
- [Investopedia: volatility](https://www.investopedia.com/terms/v/volatility.asp)
