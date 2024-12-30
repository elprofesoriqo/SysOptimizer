import os
from app.models.clean import CleanFile

def analyze_files():
    """
    Analizuje system w poszukiwaniu plików do usunięcia.
    """
    # Przykładowe wyszukiwanie plików tymczasowych w katalogu /tmp
    temp_files = []
    for root, dirs, files in os.walk("/tmp"):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path) / (1024 * 1024)  # Rozmiar w MB
            last_accessed = os.path.getatime(file_path)
            temp_files.append(CleanFile(
                path=file_path,
                size=size,
                file_type="temporary",
                last_accessed=last_accessed
            ).dict())
    return temp_files

import subprocess
import json

def clean_temp_files():
    try:
        subprocess.run(["modules/sys_cleaner.exe"], check=True)
        with open("clean_report.json", "r") as file:
            result = json.load(file)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}

