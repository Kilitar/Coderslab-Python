import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def run_sql_file(cursor, file_path):
    print(f"[*] Spouštím SQL soubor: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        sql = f.read()
        cursor.execute(sql)

def migrate():
    db_name = "coderslab"
    user = "postgres"
    password = "xxxeen"  # Uživatel bude muset upravit nebo použijeme .env
    host = "localhost"
    
    # 1. Připojení k defaultní databázi pro vytvoření nové DB
    try:
        conn = psycopg2.connect(user=user, password=password, host=host)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Vytvoření databáze
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {db_name}")
            print(f"[+] Databáze '{db_name}' vytvořena.")
        else:
            print(f"[*] Databáze '{db_name}' již existuje.")
            
        cur.close()
        conn.close()
        
        # 2. Připojení k nové databázi a spuštění dumpu
        conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host)
        cur = conn.cursor()
        
        dump_path = os.path.join("DATA", "DATABASE", "dump.sql")
        run_sql_file(cur, dump_path)
        
        conn.commit()
        print("[+] Migrace úspěšně dokončena. Data jsou v databázi.")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Chyba při migraci: {e}")

if __name__ == "__main__":
    migrate()
