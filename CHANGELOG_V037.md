# ETH Entry Radar iOS V0.3.7

Исправлено:
- Historical analogs: переход на nearest-neighbour выборку, чтобы Time Engine не обнулялся из-за слишком жёстких фильтров.
- STOP всегда рассчитывается backend и передаётся готовым числом.
- LAST CLOSED 15m выводится через явный DOM lookup, без конфликтов browser globals.
- Убрано устаревание iPhone UI: HTML/API/service-worker идут с no-store; service-worker кэширует только иконки/manifest.
- Итоговый сигнал по-прежнему только LONG или SHORT.
- Диапазон входа ОТ–ДО, STOP, TP1/TP2/TP3 и R:R остаются обязательными для выбранной стороны.

Важно: исторические аналоги — статистика похожих закрытых 15m состояний, не гарантия результата.
