# 🛠️ Vývojářské Nastavení (Development Setup)

Tento dokument slouží jako hlavní příručka pro nastavení a udržování vývojového prostředí projektu **Coderslab-Python**. Dokumentace je optimalizována pro synchronizaci mezi desktopem a notebookem.

## 🐍 Jazyk a Prostředí
- **Jazyk:** Python 3.10
- **Správa prostředí:** Anaconda / Conda
- **Název prostředí:** `ds_course`

### Instalace/Aktualizace prostředí:
Pro synchronizaci závislostí po stažení z GITu použij:
```powershell
conda env update -n ds_course -f environment.yml
```

## 🛡️ Typová Bezpečnost (TypeScript standard)
Projekt je nastaven tak, aby minimalizoval chyby a vynucoval disciplínu podobnou TypeScriptu.

- **Strict Mode:** V VS Code je zapnut `python.analysis.typeCheckingMode: "strict"`.
- **Typování:** Používáme Type Hints (PEP 484). Vyhýbáme se typu `Any`, kde je to možné.
- **Validace Dat:** Pro složitější datové struktury a validaci vstupů používáme **Pydantic**.

## 🧹 Kvalita Kódu a Formátování
Pro udržení konzistentního kódu mezi zařízeními používáme:

- **Ruff:** All-in-one linter a formatter.
  - Nahrazuje ESLint, Prettier, Flake8 a Isort.
  - Je nastaven jako výchozí formatter v VS Code.
  - Automaticky opravuje chyby a řadí importy při uložení (Format on Save).

## 🔄 Synchronizace (GIT)
- **Repozytář:** Git
- **Strategie:** Před ukončením práce na jednom stroji vždy `commit` a `push`. Na druhém stroji `pull`.
- **Ignorované soubory:** `.gitignore` je nastaven tak, aby neodesílal lokální virtuální prostředí, mezipaměť (cache) a dočasné soubory Jupyteru.

## 💻 Hardware Poznámky
- **Hlavní stroj:** Desktop (35" UltraWide)
- **Cestovní stroj:** Notebook (i5, 48GB RAM, 2TB SSD)
  - *Poznámka:* Výkon notebooku je pro tento stack (Python/DS) naprosto nadstandardní. Limitujícím faktorem bude pouze plocha 15" displeje při práci s více okny.

---
*Poslední aktualizace: 15. 5. 2026*
