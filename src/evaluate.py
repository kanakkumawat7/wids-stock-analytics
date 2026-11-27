"""Time-ordered splitting and metrics."""
import numpy as np


def time_split(df, test_frac=0.2):
    """Chronological split. NEVER shuffle time series."""
    cut = int(len(df) * (1 - test_frac))
    return df.iloc[:cut], df.iloc[cut:]


def directional_accuracy(y_true_ret, y_pred_ret):
    return float(np.mean(np.sign(y_true_ret) == np.sign(y_pred_ret)))


def rmse(a, b):
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def mae(a, b):
    return float(np.mean(np.abs(np.asarray(a) - np.asarray(b))))


def backtest(signal_up, next_ret, cost=0.001):
    """Long when signal_up==1 else flat; subtract `cost` on every position change.
    Returns (strategy_cumulative_return, buy_and_hold_cumulative_return)."""
    signal_up, next_ret = np.asarray(signal_up), np.asarray(next_ret)
    trades = np.abs(np.diff(np.r_[0, signal_up]))
    strat = signal_up * next_ret - trades * cost
    return float(np.prod(1 + strat) - 1), float(np.prod(1 + next_ret) - 1)
