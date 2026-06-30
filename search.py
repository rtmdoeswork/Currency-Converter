import re
from pathlib import Path

# ===== CONFIG =====
ROOT = Path(r"D:\Resources\Books")

BOOK_EXTENSIONS = {
    ".pdf",
    ".epub",
    ".mobi",
    ".azw3",
    ".djvu",
    ".djv",
    ".fb2",
    ".cbz",
    ".cbr",
}
# ==================


def clean_book_title(title: str) -> str:
    # 1. Remove "_OceanofPDF.com_" from the front (case-insensitive)
    # Using regex to catch it at the start (`^`) with optional spaces around it
    title = re.sub(r"^(_OceanofPDF\.com_)\s*", "", title, flags=re.IGNORECASE)

    # 2. Replace underscores and hyphens with spaces
    title = title.replace("_", " ").replace("-", " ")

    # 3. Clean up any accidental double spaces and strip edges
    title = re.sub(r"\s+", " ", title).strip()

    return title


books = []

for file in ROOT.rglob("*"):
    if file.is_file() and file.suffix.lower() in BOOK_EXTENSIONS:
        # Clean the title before adding it to the list
        cleaned_title = clean_book_title(file.stem)
        if cleaned_title:  # Ensure we don't add empty strings
            books.append(cleaned_title)

# Deduplicate and sort alphabetically (ignoring case)
books = sorted(set(books), key=str.casefold)

output = ROOT / "books.txt"

with output.open("w", encoding="utf-8") as f:
    for book in books:
        f.write(book + "\n")

print(f"Found {len(books)} books.\n")

for book in books:
    print(book)

print(f"\nSaved to: {output}")
