# Python equivalent of: cat notes.txt
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)
print(f"Total characters: {len(text)}")