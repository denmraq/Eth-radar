
# ETH Entry Radar — iOS Edition V0.3.1

## Что это
Отдельная iPhone-версия PWA. Аналитический движок работает на сервере, iPhone показывает интерфейс и может быть установлен на главный экран как приложение.

## Что уже внутри
- ETHUSDT perpetual;
- 4H / 1H / 15m / 5m;
- решения только по закрытым свечам;
- LONG / SHORT / WAIT;
- WATCH_LONG / WATCH_SHORT;
- Time Engine;
- P(TP first), P(SL first), P(neither 4h);
- ожидаемое время до TP;
- time invalidation;
- OI, funding, RSI, EMA, ATR;
- trade-flow/CVD proxy;
- Entry / Stop / TP;
- iOS PWA manifest;
- Apple touch icon;
- service worker;
- Dockerfile / Render config.

## Как поставить на iPhone
Сначала проект должен быть опубликован по HTTPS.

После публикации:
1. Открыть адрес в Safari.
2. Нажать кнопку «Поделиться».
3. Выбрать «На экран Домой».
4. Название: ETH Radar.
5. Нажать «Добавить».

После этого ETH Radar появится отдельной иконкой и будет открываться без обычной панели браузера.

## Как разместить на сервере
Пакет подготовлен для Render, Railway, Fly.io или любого VPS с Docker/Python.

На Render можно:
1. создать новый Web Service;
2. загрузить этот проект в GitHub;
3. подключить репозиторий;
4. Render увидит `render.yaml`, либо вручную указать:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn server:app --host 0.0.0.0 --port $PORT`
5. После deploy открыть выданный HTTPS URL.

## Важно
Это аналитический прототип, не торговый робот с реальными ордерами.
До автоматической торговли нужен полноценный backtest и paper trading.
