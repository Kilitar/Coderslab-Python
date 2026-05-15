# 🚀 Project Migration & Setup Status

Tento soubor slouží k synchronizaci stavu prostředí mezi pracovní stanicí a notebookem.

## 📋 Aktuální stav k 15.5.2026 (Stanice)
- [x] Python 3.10 + Conda prostředí `ds_course`
- [x] PostgreSQL 18 nainstalován a běží
- [x] SQLAlchemy 2.0 nainstalováno
- [x] Psycopg2-binary (driver) - **INSTALOVÁNO**
- [x] Openpyxl - **INSTALOVÁNO**
- [ ] Konfigurace `.env` pro DB spojení

## 🛠️ Postup pro "Dvojče" na novém HW
Při prvním spuštění na novém stroji (notebooku) proveď:
1. `git pull`
2. Spusť `python bootstrap.py` (nainstaluje `psycopg2-binary`, `sqlalchemy`, `openpyxl`)
3. **DŮLEŽITÉ:** Pokud `bootstrap.py` selže na binárkách, zkus `pip install psycopg2-binary` ručně.
4. Zkontroluj, zda běží PostgreSQL služba (`Get-Service -Name "postgresql*"`).
5. Spusť `python migrate.py` pro vytvoření databáze `coderslab` a import dat z `dump.sql`.

## 🏁 Cíl: Soubor "Migrace"
Implementace "Migrace" je nyní hotová v souboru `migrate.py`. Stačí ho spustit a databáze se postaví na nohy.
