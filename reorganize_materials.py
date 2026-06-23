import os
import shutil

src_root = r"x:\PROJECTS\coderslab-python\DATA\SESSION2_MATERIALS"
dest_root = r"x:\PROJECTS\coderslab-python\DATA\SESSION2_MATERIALS"

def clean_and_create_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)

def reorganize():
    print("[*] Reorganizing course materials into day-by-day folders...")

    # 1. Day 3 - PostgreSQL
    day3_dest = os.path.join(dest_root, "03_Day 3 - PostgreSQL")
    clean_and_create_dir(day3_dest)
    # Move exercise subfolders
    day3_src_notebooks = os.path.join(src_root, "05_Python_Classes", "5-4_Session 2 preparation", "session-2-preparation", "02_PostgreSQL")
    if os.path.exists(day3_src_notebooks):
        for item in os.listdir(day3_src_notebooks):
            shutil.move(os.path.join(day3_src_notebooks, item), os.path.join(day3_dest, item))
    # Copy database file
    db_src = os.path.join(src_root, "05_Python_Classes", "5-4_Session 2 preparation", "session-2-preparation", "01_Preparing for session", "01_Database")
    if os.path.exists(db_src):
        shutil.copytree(db_src, os.path.join(day3_dest, "01_Database"))
    print("  [+] Organized: 03_Day 3 - PostgreSQL")

    # 2. Day 4 - API
    day4_dest = os.path.join(dest_root, "04_Day 4 - API")
    clean_and_create_dir(day4_dest)
    day4_src = os.path.join(src_root, "05_Python_Classes", "5-4_Session 2 preparation", "session-2-preparation", "03_API")
    if os.path.exists(day4_src):
        for item in os.listdir(day4_src):
            shutil.move(os.path.join(day4_src, item), os.path.join(day4_dest, item))
    print("  [+] Organized: 04_Day 4 - API")

    # 3. Day 5 - Pandas
    day5_dest = os.path.join(dest_root, "05_Day 5 - Pandas")
    clean_and_create_dir(day5_dest)
    day5_src = os.path.join(src_root, "05_Python_Classes", "5-8_Session 3 preparation", "03_Day 1")
    if os.path.exists(day5_src):
        for item in os.listdir(day5_src):
            shutil.move(os.path.join(day5_src, item), os.path.join(day5_dest, item))
    # Copy data files
    data_src = os.path.join(src_root, "05_Python_Classes", "5-8_Session 3 preparation", "01_Data")
    if os.path.exists(data_src):
        shutil.copytree(data_src, os.path.join(day5_dest, "01_Data"))
    print("  [+] Organized: 05_Day 5 - Pandas")

    # 4. Day 6 - Pandas cont.
    day6_dest = os.path.join(dest_root, "06_Day 6 - Pandas cont.")
    clean_and_create_dir(day6_dest)
    day6_src = os.path.join(src_root, "05_Python_Classes", "5-8_Session 3 preparation", "04_Day 2")
    if os.path.exists(day6_src):
        for item in os.listdir(day6_src):
            shutil.move(os.path.join(day6_src, item), os.path.join(day6_dest, item))
    # Copy data files
    if os.path.exists(data_src):
        shutil.copytree(data_src, os.path.join(day6_dest, "01_Data"))
    print("  [+] Organized: 06_Day 6 - Pandas cont.")

    # 5. Day 7 - Plots
    day7_dest = os.path.join(dest_root, "07_Day 7 - Plots")
    clean_and_create_dir(day7_dest)
    day7_src = os.path.join(src_root, "05_Python_Classes", "5-12_Session 4 preparation", "02_Charts")
    if os.path.exists(day7_src):
        for item in os.listdir(day7_src):
            shutil.move(os.path.join(day7_src, item), os.path.join(day7_dest, item))
    # Copy plot preps
    plot_prep_src = os.path.join(src_root, "05_Python_Classes", "5-12_Session 4 preparation", "01_Preparing for session")
    if os.path.exists(plot_prep_src):
        shutil.copytree(plot_prep_src, os.path.join(day7_dest, "01_Preparing for session"))
    print("  [+] Organized: 07_Day 7 - Plots")

    # 6. Day 8 - Web scraping
    day8_dest = os.path.join(dest_root, "08_Day 8 - Web scraping")
    clean_and_create_dir(day8_dest)
    day8_src = os.path.join(src_root, "05_Python_Classes", "5-12_Session 4 preparation", "03_Web scraping")
    if os.path.exists(day8_src):
        for item in os.listdir(day8_src):
            shutil.move(os.path.join(day8_src, item), os.path.join(day8_dest, item))
    # Copy plot preps
    if os.path.exists(plot_prep_src):
        shutil.copytree(plot_prep_src, os.path.join(day8_dest, "01_Preparing for session"))
    print("  [+] Organized: 08_Day 8 - Web scraping")

    # 7. Day 9 - Generating PDF
    day9_dest = os.path.join(dest_root, "09_Day 9 - Generating PDF")
    clean_and_create_dir(day9_dest)
    day9_src = os.path.join(src_root, "05_Python_Classes", "5-16_Session 5 preparation")
    if os.path.exists(day9_src):
        for item in os.listdir(day9_src):
            shutil.move(os.path.join(day9_src, item), os.path.join(day9_dest, item))
    print("  [+] Organized: 09_Day 9 - Generating PDF")

    # 8. Day 10 - Workshop
    day10_dest = os.path.join(dest_root, "10_Day 10 - Workshop")
    clean_and_create_dir(day10_dest)
    day10_src = os.path.join(src_root, "05_Python_Classes", "5-18_Day 10 - Workshop")
    if os.path.exists(day10_src):
        for item in os.listdir(day10_src):
            shutil.move(os.path.join(day10_src, item), os.path.join(day10_dest, item))
    print("  [+] Organized: 10_Day 10 - Workshop")

    # 9. Python Prework
    prework_dest = os.path.join(dest_root, "00_Python_Prework")
    clean_and_create_dir(prework_dest)
    prework_src = os.path.join(src_root, "04_Python_Prework", "4-2_Basics of Python programming - individual work", "02_Basics of Python programming - Individual work.en")
    if os.path.exists(prework_src):
        for item in os.listdir(prework_src):
            shutil.move(os.path.join(prework_src, item), os.path.join(prework_dest, item))
    print("  [+] Organized: 00_Python_Prework")

    # 10. Clean up raw source directories
    print("[*] Cleaning up empty source directories...")
    for item in ["00_Prework", "01_Intro_DA", "04_Python_Prework", "05_Python_Classes"]:
        p = os.path.join(src_root, item)
        if os.path.exists(p):
            shutil.rmtree(p)
            print(f"  [-] Removed raw directory: {item}")

    print("[+] Reorganization completed successfully!")

if __name__ == "__main__":
    reorganize()
