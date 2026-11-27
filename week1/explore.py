"""Week 1: load data, compute returns/moving averages, make plots.
Run:  python week1/explore.py --tickers RELIANCE.NS TCS.NS INFY.NS
      python week1/explore.py --synthetic
"""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src.data import load_prices

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(exist_ok=True)

p = argparse.ArgumentParser()
p.add_argument("--tickers", nargs="+", default=["RELIANCE.NS", "TCS.NS", "INFY.NS"])
p.add_argument("--synthetic", action="store_true")
a = p.parse_args()

for t in (["SYNTHETIC"] if a.synthetic else a.tickers):
    df = load_prices(t, synthetic=a.synthetic)
    df["ret"] = df["Close"].pct_change()
    df["ma20"], df["ma50"] = df["Close"].rolling(20).mean(), df["Close"].rolling(50).mean()
    print(f"\n{t}: {len(df)} rows, {df.index[0].date()} to {df.index[-1].date()}")
    print(df["ret"].describe().round(4).to_string())

    fig, ax = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    df[["Close", "ma20", "ma50"]].plot(ax=ax[0], title=f"{t} price and moving averages")
    df["ret"].plot(ax=ax[1], title="Daily returns", lw=0.6)
    df["ret"].rolling(20).std().plot(ax=ax[2], title="20-day rolling volatility")
    plt.tight_layout()
    f = OUT / f"week1_{t.replace('.', '_')}.png"
    plt.savefig(f, dpi=120); plt.close()
    print("saved", f)

# TODO (your task): answer in week1/notes.md
#  1. Which stock was most volatile? How did you measure it?
#  2. Plot the histogram of returns. Does it look normal? Look at the tails.
#  3. Compute the correlation of daily returns between your 3 stocks.
