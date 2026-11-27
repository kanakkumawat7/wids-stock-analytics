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

## Further reading
- Zerodha Varsity: Introduction to Stock Markets
- Investopedia: returns and volatility
