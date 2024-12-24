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

def clean_files():
    """
    Usuwa wskazane pliki.
    """
    files_to_remove = analyze_files()  # W tym przykładzie usuwamy wszystkie
    removed_files = []
    for file in files_to_remove:
        try:
            os.remove(file["path"])
            removed_files.append(file["path"])
        except Exception as e:
            continue
    return removed_files
