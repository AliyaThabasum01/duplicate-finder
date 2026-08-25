import os
import hashlib
from collections import defaultdict


def file_hash(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


folder = input("Enter folder path: ").strip()

if not os.path.isdir(folder):
    print("❌ Folder not found.")
    exit()

files = defaultdict(list)

for root, _, filenames in os.walk(folder):
    for filename in filenames:
        path = os.path.join(root, filename)

        try:
            files[file_hash(path)].append(path)
        except (PermissionError, OSError):
            pass

duplicates = [paths for paths in files.values() if len(paths) > 1]

print("\n🔎 Duplicate Finder")
print("=" * 40)

if not duplicates:
    print("✅ No duplicate files found.")
else:
    for group in duplicates:
        print("\nDuplicate files:")
        for path in group:
            print(f"  • {path}")
