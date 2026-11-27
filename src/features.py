"""Feature engineering. Every feature at row t uses only data up to day t."""
import numpy as np
import pandas as pd


def rsi(close, window=14):
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(window).mean()
    loss = (-delta.clip(upper=0)).rolling(window).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def macd(close, fast=12, slow=26, signal=9):
    macd_line = close.ewm(span=fast, adjust=False).mean() - close.ewm(span=slow, adjust=False).mean()
    sig = macd_line.ewm(span=signal, adjust=False).mean()
    return macd_line, macd_line - sig


def add_features(df, lags=5):
    out = pd.DataFrame(index=df.index)
    out["ret"] = df["Close"].pct_change()
    for k in range(1, lags + 1):
        out[f"ret_lag{k}"] = out["ret"].shift(k)
    out["ma10_ratio"] = df["Close"] / df["Close"].rolling(10).mean() - 1
    out["ma50_ratio"] = df["Close"] / df["Close"].rolling(50).mean() - 1
    out["vol10"] = out["ret"].rolling(10).std()
    out["rsi14"] = rsi(df["Close"])
    m, h = macd(df["Close"])
    out["macd"], out["macd_hist"] = m / df["Close"], h / df["Close"]
    out["vol_chg"] = df["Volume"].pct_change()
    # Targets: tomorrow's return and direction. shift(-1) is the ONLY place we look ahead.
    out["target_ret"] = out["ret"].shift(-1)
    out["target_up"] = (out["target_ret"] > 0).astype(int)
    return out.replace([np.inf, -np.inf], np.nan).dropna()
