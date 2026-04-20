"""Strip Hebrew-contraction hyphens from visible copy."""
from pathlib import Path

path = Path(r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\index.html")
t = path.read_text(encoding="utf-8")

repls = [
    # meta description
    ('מוגבל ל-15 בעלי עסקים', 'מוגבל ל15 בעלי עסקים'),
    # problem body
    ('ב-5 שנים האחרונות', 'ב5 שנים האחרונות'),
    # insight
    ('פורץ ל-<b>Next Level</b>', 'פורץ ל<b>Next Level</b>'),
    # pullquote 3%
    ('זה ה-<span class="three">3%</span>', 'זה ה<span class="three">3%</span>'),
    # learning item 5
    ('בערך מהסעיף ה-3</span>', 'בערך מהסעיף ה3</span>'),
    # scarcity h2
    ('מוגבלת ל-<span class="accent">15</span>', 'מוגבלת ל<span class="accent">15</span>'),
    # Ensure title (if not already done)
    ('ב-3 שעות של משחק</title>', 'ב3 שעות של משחק</title>'),
]

n = 0
for old, new in repls:
    if old in t:
        t = t.replace(old, new)
        n += 1

path.write_text(t, encoding="utf-8")
print(f"applied {n}/{len(repls)}")
