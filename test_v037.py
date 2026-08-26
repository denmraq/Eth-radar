import numpy as np
import pandas as pd
from radar import time_to_event_analogs

def synthetic_history(n=700):
    rng = np.random.default_rng(7)
    t = pd.date_range("2026-01-01", periods=n, freq="15min", tz="UTC")
    drift = np.sin(np.linspace(0, 24, n))*0.35 + 0.08
    close = 2200 + np.cumsum(drift + rng.normal(0, 2.2, n))
    open_ = np.r_[close[0], close[:-1]]
    high = np.maximum(open_, close) + rng.uniform(0.5, 4.5, n)
    low = np.minimum(open_, close) - rng.uniform(0.5, 4.5, n)
    vol = rng.uniform(100, 1000, n)
    return pd.DataFrame({
        "open_time": t,
        "open": open_,
        "high": high,
        "low": low,
        "close": close,
        "volume": vol,
        "close_time": t + pd.Timedelta(minutes=15),
        "quote_volume": vol*close,
        "trades": np.nan,
        "taker_buy_base": np.nan,
        "taker_buy_quote": np.nan,
        "ignore": np.nan,
    })

def test_analogs_do_not_collapse_to_zero():
    df = synthetic_history()
    out = time_to_event_analogs(df, "LONG", 0.9, 1.7, 16)
    assert out["analog_count"] >= 30
    assert out["p_tp_first"] is not None
    assert out["p_sl_first"] is not None
    assert out["p_neither"] is not None
    total = out["p_tp_first"] + out["p_sl_first"] + out["p_neither"]
    assert 99.8 <= total <= 100.2

def test_frontend_uses_explicit_stop_and_closed_ids():
    html = open("static/index.html", encoding="utf-8").read()
    assert "$('stop').textContent=val(r.stop)" in html
    assert "$('closed').textContent" in html
    assert "iOS V0.3.7" in html

def test_service_worker_version():
    sw = open("static/service-worker.js", encoding="utf-8").read()
    assert "eth-radar-ios-v037" in sw
    assert "url.pathname === '/'" in sw
