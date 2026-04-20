"""
Remove em-dashes from user-visible copy without changing the wording.
Replaces ` — ` with natural punctuation (., ,) based on context.
"""
import re
from pathlib import Path

path = Path(r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\index.html")
text = path.read_text(encoding="utf-8")

# Ordered replacements (longest / most specific first) so we don't double-match
replacements = [
    # title tag
    ("<title>FreshBiz — איך", "<title>FreshBiz · איך"),

    # hero
    ("ביננו — אתה יודע", "ביננו, אתה יודע"),
    ('<span class="cite">— FreshBiz', '<span class="cite">FreshBiz'),

    # problem / 82
    ("מתחת לאף שלהם — ובעיקר", "מתחת לאף שלהם. ובעיקר"),
    ("די להתקע על אותו מחזור —", "די להתקע על אותו מחזור."),

    # insight
    ("(והמחרפן)</b> — הוא", "(והמחרפן)</b>, הוא"),
    ("ופתאום רואים אותו בכל מקום — המוח", "ופתאום רואים אותו בכל מקום. המוח"),
    ("כמה קשה תעבוד</b> — אם", "כמה קשה תעבוד</b>, אם"),

    # pullquote open
    ('המוח שלך</span> — לראות', 'המוח שלך</span>, לראות'),

    # wall
    ("מצליחים יותר — עם פחות", "מצליחים יותר, עם פחות"),
    ("כי הכי מתסכל — זה לדעת", "כי הכי מתסכל, זה לדעת"),
    ("שאתה עושה</b> — ולהתחיל", "שאתה עושה</b>, ולהתחיל"),

    # parts
    ("שלא תוכל לשכוח — דרך חוויה", "שלא תוכל לשכוח. דרך חוויה"),
    ("הקדמה קצרה — לאן העולם", "הקדמה קצרה. לאן העולם"),
    ("משחק האסטרטגיה והיזמות — שעתיים", "משחק האסטרטגיה והיזמות. שעתיים"),

    # sharks
    ("בפריים־טיים — כי המשחק", "בפריים־טיים, כי המשחק"),

    # perm
    ("<span class=\"accent\">יתרון תחרותי</span> — גם לך מותר.",
     "<span class=\"accent\">יתרון תחרותי</span>. גם לך מותר."),

    # videos
    ("ואם עדיין לא הבנת מה זה — סרטון", "ואם עדיין לא הבנת מה זה. סרטון"),

    # why
    ("כדי ללמוד באמת משהו — <span", "כדי ללמוד באמת משהו. <span"),
    ("ביוקר — <b>בכסף", "ביוקר. <b>בכסף"),
    ("בסביבת \"מעבדה\" — מזווית", "בסביבת \"מעבדה\", מזווית"),
    ("במקום רק לדבר על עסקים — נחווה", "במקום רק לדבר על עסקים. נחווה"),
    ("מטרות שלכם — בלי להיכנע", "מטרות שלכם, בלי להיכנע"),
    ("בדרך חדשה — כאלה שמתחת", "בדרך חדשה, כאלה שמתחת"),

    # learnings
    ("חמישה דברים — <span class=\"accent\">ואחד", "חמישה דברים. <span class=\"accent\">ואחד"),
    ("במקום לדבר על עסקים — <span", "במקום לדבר על עסקים. <span"),
    ("להסתבך — הכל דרך המשחק", "להסתבך. הכל דרך המשחק"),
    ("ליצור ולזהות הזדמנויות</span> — ובעיקר", "ליצור ולזהות הזדמנויות</span>, ובעיקר"),
    ("אז מי שקורא את זה — מקבל", "אז מי שקורא את זה, מקבל"),

    # guarantee
    ("<p>תראה — לא מדובר", "<p>תראה, לא מדובר"),
    ("אני מוכן להתחייב לך בלב שלם —", "אני מוכן להתחייב לך בלב שלם."),
    ("שלא קיבלת את הערך — קח", "שלא קיבלת את הערך, קח"),

    # scarcity
    ("<p>והאמת — בכל פתיחת", "<p>והאמת, בכל פתיחת"),

    # form submit toast
    ("'מעולה — תועבר לדף אישור ✓'", "'מעולה! תועבר לדף אישור ✓'"),

    # not-list bullet — swap decorative em-dash for a restrained dot
    ('  content: "—";\n  color: var(--magenta);\n  margin-inline-end: 8px;\n  font-weight: 700;',
     '  content: "•";\n  color: var(--magenta);\n  margin-inline-end: 8px;\n  font-weight: 700;'),
]

changed = 0
missed = []
for i, (old, new) in enumerate(replacements):
    if old in text:
        text = text.replace(old, new)
        changed += 1
    else:
        missed.append(i)

print(f"applied {changed}/{len(replacements)}")
if missed:
    print("missed indices:", missed)

# save first
path.write_text(text, encoding="utf-8")

# count any remaining em-dashes inside text nodes (not CSS comments)
remaining = re.findall(r">[^<]*?—[^<]*?<", text)
non_comment = [r for r in remaining if "--" not in r[:30] and "/*" not in r]
print(f"saved. remaining dashes in visible text: {len(non_comment)}")
