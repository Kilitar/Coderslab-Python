import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time

# Konfigurace stránky
st.set_page_config(
    page_title="Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Nadpis a úvodní text
st.title("🚀 Data Science & AI Portfolio")
st.markdown("""
Vítejte v mém portfoliu! Tato aplikace slouží k demonstraci mých dovedností v oblasti **Data Science, Machine Learningu a práce s databázemi**. 
Je postavena na frameworku **Streamlit** a propojena s **PostgreSQL** databází.

V levém panelu si můžete nastavit připojení k lokální PostgreSQL databázi a ověřit její funkčnost.
""")

st.divider()

# Postranní panel pro konfiguraci DB
with st.sidebar:
    st.header("⚙️ Nastavení Databáze")
    st.markdown("Zadejte údaje k vaší lokální PostgreSQL databázi:")
    
    db_host = st.text_input("Host", value="localhost")
    db_port = st.text_input("Port", value="5432")
    db_name = st.text_input("Název databáze", value="postgres")
    db_user = st.text_input("Uživatel", value="postgres")
    db_pass = st.text_input("Heslo", type="password")
    
    test_db_button = st.button("🔌 Testovat Připojení", use_container_width=True)

# Funkce pro test připojení
def test_connection():
    if not db_pass:
        st.warning("⚠️ Prosím, zadejte heslo k databázi pro test připojení.")
        return
        
    connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    
    try:
        # Použití SQLAlchemy pro Pandas kompatibilitu
        engine = create_engine(connection_string)
        
        with st.spinner('Připojuji se k databázi...'):
            time.sleep(1) # Jen pro vizuální efekt
            
            # Pokus o jednoduchý dotaz
            df = pd.read_sql_query('SELECT version();', con=engine)
            
            st.success("✅ Připojení k PostgreSQL proběhlo úspěšně!")
            st.balloons()
            
            st.subheader("Informace o databázi:")
            st.code(df.iloc[0, 0])
            
            # Zobrazení ukázkové tabulky jako placeholder pro budoucí data
            st.subheader("Ukázka vizualizace (Dummy Data)")
            dummy_data = pd.DataFrame({
                'Kategorie': ['A', 'B', 'C', 'D'],
                'Hodnoty': [10, 25, 15, 30]
            })
            st.bar_chart(dummy_data.set_index('Kategorie'))
            
    except Exception as e:
        st.error(f"❌ Chyba připojení: {str(e)}")
        st.info("💡 Zkontrolujte, zda běží lokální PostgreSQL server a zda jsou přihlašovací údaje správné.")

# Hlavní část pro zobrazení výsledků testu
if test_db_button:
    test_connection()
else:
    st.info("👈 Pro otestování databáze vyplňte údaje v levém panelu a klikněte na 'Testovat Připojení'.")
