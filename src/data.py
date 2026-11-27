"""Data loading. Uses yfinance for real NSE/BSE data, with a synthetic fallback
so every script also runs offline (use --synthetic)."""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def synthetic_prices(n=1500, seed=0, start="2018-01-01"):
    """Geometric random walk with volatility clustering. Only for testing code."""
    rng = np.random.default_rng(seed)
    vol = 0.01 + 0.005 * np.abs(np.sin(np.linspace(0, 12, n)))
    ret = rng.normal(0.0004, vol)
    close = 100 * np.exp(np.cumsum(ret))
    idx = pd.bdate_range(start, periods=n)
    high = close * (1 + np.abs(rng.normal(0, 0.005, n)))
    low = close * (1 - np.abs(rng.normal(0, 0.005, n)))
    open_ = np.r_[close[0], close[:-1]]
    volume = rng.integers(1_000_000, 5_000_000, n)
    return pd.DataFrame({"Open": open_, "High": high, "Low": low,
                         "Close": close, "Volume": volume}, index=idx)


def load_prices(ticker="RELIANCE.NS", start="2015-01-01", end=None, synthetic=False):
    """Return a DataFrame with Open, High, Low, Close, Volume indexed by date."""
    if synthetic:
        return synthetic_prices()
    DATA_DIR.mkdir(exist_ok=True)
    cache = DATA_DIR / f"{ticker.replace('^', '')}.csv"
    if cache.exists():
        return pd.read_csv(cache, index_col=0, parse_dates=True)
    import yfinance as yf
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    if df.empty:
        raise RuntimeError(f"No data for {ticker}. Check the ticker or your internet, or use --synthetic.")
    if isinstance(df.columns, pd.MultiIndex):  # newer yfinance returns multi-index columns
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    df.to_csv(cache)
    return df
