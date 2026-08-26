# ETH Entry Radar iOS V0.3.7.2 COMPLETE

Полный пакет ETH Entry Radar для iPhone/PWA и Render.

## Итоговый сигнал
Radar всегда выбирает одну сторону:
- LONG
- SHORT

WAIT / WATCH / NEUTRAL не используются как итоговый торговый сигнал.
При сигнале показывается диапазон входа ОТ–ДО, Stop и TP.

## Данные
- ETHUSDT perpetual
- 4H / 1H / 15m / 5m
- решения по закрытым свечам
- RSI / EMA / ATR
- OI / funding
- trade-flow/CVD proxy
- Time Engine / historical analogs при наличии выборки
- Data Confidence

Публичные рыночные данные берутся через Bybit V5 public market API. Для Render рекомендуется регион Frankfurt (EU Central), а не US-регион.

## Render
Build Command:
`pip install -r requirements.txt`

Start Command:
`uvicorn server:app --host 0.0.0.0 --port $PORT`

## iPhone
После успешного deploy открыть HTTPS-адрес в Safari → Поделиться → На экран «Домой» → Добавить.

Это аналитический прототип. Реальные ордера не отправляет.
