# Data Science & Python s AI Asistentem (Projekt)

## Cíl projektu
Projekt je součástí kurzu Data Science, se zaměřením na jazyk Python. 
Cílem je vytvořit nástroj/prostředí ("upgrade toolsetu"), který efektivně zapojí prompt coding (AI) a prezentační vrstvu přes **Streamlit**.

## Architektura a Technologie
- **Správa prostředí:** Anaconda (Conda)
- **Databáze:** PostgreSQL (připojení např. přes `psycopg2` / `SQLAlchemy` -> `pandas.read_sql`)
- **Frontend / Aplikace:** Streamlit (`streamlit run app.py`) pro interaktivní zobrazení dat a ML modelů.
- **Klíčové knihovny:**
  - `NumPy`: Numerical Computing and Array Manipulation
  - `Pandas`: Data Manipulation and Analysis
  - `Matplotlib`: Data Visualization
  - `Seaborn`: Statistical Data Visualization
  - `Scikit-learn`: Machine Learning (klasifikace, regrese, clustering)
  - `TensorFlow` / `PyTorch`: Deep Learning Frameworks

## Způsob práce (Prompt Coding Workflow)
1. **Příprava & Data Extraction:** Dodání struktury dat z databáze (PostgreSQL), AI vygeneruje SQL dotazy a kód pro rychlé načtení (Pandas).
2. **Data Processing & EDA:** AI podle zadání vyčistí data, vyřeší chybějící hodnoty a napíše vizualizace (Matplotlib, Seaborn).
3. **Machine Learning:** AI navrhne architekturu ML modelu na základě popisu problému (Scikit-learn pro klasiku, TensorFlow/PyTorch pro deep learning).
4. **Web UI:** Hotové analýzy se zabalí do Streamlit aplikace pro interaktivní zkoumání přes webový prohlížeč.

## Následující kroky (Až bude otevřen tento workspace)
1. Založit virtuální Conda prostředí (např. `conda create -n ds_course python=3.10`).
2. Nainstalovat závislosti (vygenerujeme si `environment.yml` nebo `requirements.txt`).
3. Vytvořit testovací připojení na lokální PostgreSQL.
4. Napsat a spustit první "Hello World" dashboard ve Streamlitu.

## 🔄 Synchronizace HW (Migration Strategy)
Pro snadný přenos mezi stanicí a notebookem:
- **Git:** Všechny konfigurační soubory (`.gitignore`, `environment.yml`, `bootstrap.py`) jsou v repozitáři.
- **Task Tracking:** Sledovat soubor `MIGRATION_TASKS.md` pro zjištění aktuálního stavu na daném stroji.
- **One-Command Setup:** Na novém stroji stačí spustit `python bootstrap.py` pro automatickou instalaci driverů a kontrolu služeb.
