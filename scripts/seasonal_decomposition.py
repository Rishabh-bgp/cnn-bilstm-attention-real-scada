"""Additive seasonal decomposition (daily period) of the hourly series."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from statsmodels.tsa.seasonal import seasonal_decompose
from windforecast.experiment import load_series, load_config

cfg = load_config(sys.argv[1] if len(sys.argv) > 1 else "configs/default.yaml")
s = load_series(cfg)
dec = seasonal_decompose(s, model="additive", period=24)
os.makedirs("results", exist_ok=True)
dec.trend.to_frame("trend").join(dec.seasonal.rename("seasonal")).join(dec.resid.rename("resid")).to_csv("results/decomposition.csv")
print("seasonal amplitude (m/s):", float(dec.seasonal.max() - dec.seasonal.min()))
print("wrote results/decomposition.csv")
