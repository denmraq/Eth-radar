
import pandas as pd, numpy as np
from radar import indicators, time_to_event_analogs, classify_stage

def make_df(n=400):
    t=pd.date_range("2026-01-01", periods=n, freq="15min", tz="UTC")
    base=2000+np.sin(np.arange(n)/8)*20+np.arange(n)*0.08
    close=base+np.sin(np.arange(n)/3)*2
    df=pd.DataFrame({
        "open_time":t, "open":close-1, "high":close+5, "low":close-5, "close":close,
        "volume":1000.0, "close_time":t+pd.Timedelta(minutes=15)
    })
    return df

def test_indicators_columns():
    x=indicators(make_df())
    for c in ["ema20","ema50","rsi14","atr14","atr_pct","prior20_high","prior20_low"]:
        assert c in x.columns

def test_stage():
    assert classify_stage("LONG",80,20,False)=="ACTIVE_LONG"
    assert classify_stage("WAIT",60,30,False)=="WATCH_LONG"
    assert classify_stage("WAIT",30,60,False)=="WATCH_SHORT"
    assert classify_stage("WAIT",50,50,False)=="WAIT"

def test_time_engine_probabilities():
    out=time_to_event_analogs(make_df(), "LONG", .8, 1.2, 12)
    if out["analog_count"]:
        total=out["p_tp_first"]+out["p_sl_first"]+out["p_neither"]
        assert abs(total-100)<=0.2
