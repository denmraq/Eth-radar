# ETH Entry Radar Mobile V0.3

Базовая версия после аудита V0.2. Главное изменение — Time Engine и запрет на принятие решений по незакрытым свечам.

## Запуск
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000
```

Открой `http://127.0.0.1:8000`.

## Что показывает Time Engine
- ACTIVE_LONG / ACTIVE_SHORT — вход подтверждён;
- WATCH_LONG / WATCH_SHORT — направление есть, но вход ещё не подтверждён;
- WAIT — преимуществ нет;
- Entry Window — ориентировочное окно ожидания подтверждения;
- P(TP first) / P(SL first) / P(neither 4h) — частоты на исторических похожих 15m-ситуациях;
- TP time 25/50/75% — распределение времени достижения TP среди успешных аналогов;
- Time invalidation — через сколько времени отсутствие развития движения делает сигнал менее актуальным.

Это аналитический прототип. Реальные ордера не отправляет.
