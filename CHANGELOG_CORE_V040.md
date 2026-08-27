# ETH Entry Radar CORE V0.4.0

- News/Macro and Push modules are not included.
- Forward Engine rolls consumed TP levels forward instead of leaving stale targets on screen.
- V1.6 horizon floor prevents new TP1/TP2/TP3 from clustering only a few dollars above/below live price.
- Fast closed 1m layer increases market sensitivity without replacing 15m/1H/4H structure.
- Multi-window Flow 5m/15m + CVD retained.
- Market data fallback chain: Bybit -> OKX -> Binance Futures -> Coinbase where applicable.
- OI/Funding failures degrade data quality instead of crashing the whole radar where possible.
- Manual Refresh visibly shows loading, completion, timing, and errors.
