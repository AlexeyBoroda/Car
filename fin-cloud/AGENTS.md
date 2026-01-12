# AGENTS.md

Правила работы coding-agent (OpenAI Codex) в этом репозитории.

## Контекст
Облачная система управленческой отчетности:
- вход: Excel-анкеты INPUT_01..INPUT_10
- выход: ОДДС (cash), ОПУ и Баланс (accrual), KPI-дашборд, CHECKS, экспорт

Язык: русский. В текстах не использовать длинное тире, только дефис.

## Тех ограничения
- Python 3.10+ (не использовать возможности 3.11+)
- FastAPI, SQLAlchemy 2.x, Alembic, PostgreSQL, Redis, Celery
- pandas + openpyxl для ingestion Excel

## Финансовая методология (критично)
- ОДДС - кассовый метод (факт оплат)
- ОПУ и Баланс - метод начислений
- Потери/брак/списания - в COGS отдельной категорией
- Переменные расходы канала (комиссии, реклама MP) - OPEX, не COGS

## Команды проекта
- deps: `docker compose up -d postgres redis minio`
- backend run: `cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- tests: `cd backend && pytest -q`
- lint/format: `cd backend && ruff check . && ruff format .`

## Правила внесения изменений
1) Сначала короткий план (5-10 пунктов), потом маленькие атомарные изменения.
2) Перед завершением задачи запускать тесты и линтер.
3) Любые изменения контрактов Excel фиксировать в `docs/input_contract.md`.
4) Новые сущности/поля фиксировать в `docs/data_dictionary.md`.

## CHECKS формат
Возвращать ошибки в формате:
`{code, severity, file, sheet, row, column, message}`

## Где смотреть требования
- `docs/spec_summary.md`
- `docs/accounting_rules.md`
