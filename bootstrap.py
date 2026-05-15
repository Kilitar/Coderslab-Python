import subprocess
import sys
import os

def check_package(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=== Antigravity Bootstrap Tool ===")
    
    # 1. Check Python Version
    print(f"[*] Python version: {sys.version.split()[0]}")
    
    # 2. Check Required Packages
    required = ["sqlalchemy", "psycopg2"]
    missing = []
    
    for pkg in required:
        if check_package(pkg):
            print(f"[+] {pkg}: Installed")
        else:
            print(f"[-] {pkg}: MISSING")
            missing.append(pkg)
            
    if missing:
        print("\n[!] Attempting to install missing packages...")
        # Prefer installing psycopg2-binary for easier setup
        if "psycopg2" in missing:
            run_command("pip install psycopg2-binary")
        if "sqlalchemy" in missing:
            run_command("pip install sqlalchemy")
            
    # 3. Check for PostgreSQL
    print("\n[*] Checking PostgreSQL Service...")
    # This is Windows specific for the current user's setup
    if run_command("Get-Service -Name 'postgresql*'"):
        print("[+] PostgreSQL service found and handled.")
    else:
        print("[!] PostgreSQL service NOT found. Please install PostgreSQL 18.")

    print("\n=== Bootstrap Complete ===")

if __name__ == "__main__":
    main()
