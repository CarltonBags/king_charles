#!/usr/bin/env python3
"""Add German _de translations to all drink guide JSONs.
Run after add_translations.py has been constructed."""

import json, os, glob

OUT = "drink_guide"

# Execute the translations definitions from add_translations.py
exec(open("add_translations.py").read().split("# Execute")[0] if "# Execute" not in open("add_translations.py").read() else open("add_translations.py").read())

# Now process all files
files = sorted(glob.glob(f"{OUT}/*.json"))
updated = 0
missing_notes = []

for fpath in files:
    with open(fpath) as f:
        d = json.load(f)

    did = d["id"]

    # Add category translation
    d["category_de"] = CAT_DE.get(d["category"], d["category"])

    # Add subcategory translation
    d["subcategory_de"] = SUBCAT_DE.get(d["subcategory"], d["subcategory"].replace("non-alcoholic", "alkoholfrei"))

    # Add tags translations
    d["tags_de"] = [TAG_DE.get(t, t) for t in d["tags"]]

    # Add primary_notes translations
    d["taste_profile"]["primary_notes_de"] = [NOTE_DE.get(n, n) for n in d["taste_profile"]["primary_notes"]]

    # Add notes translation
    if did in NOTES_TRANSLATIONS:
        d["notes_de"] = NOTES_TRANSLATIONS[did]
    else:
        # Auto-generate a placeholder
        d["notes_de"] = f"[Übersetzung folgt] {d['notes']}"
        missing_notes.append(did)

    with open(fpath, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    updated += 1

print(f"Updated {updated} files with German translations")
if missing_notes:
    print(f"\n{len(missing_notes)} IDs still need manual notes_de translation:")
    for mid in missing_notes:
        print(f"  {mid}")
