#!/usr/bin/env python3
"""Build drink guide JSON files from King Charles pub menus."""

import json, os

OUT = "drink_guide"
os.makedirs(OUT, exist_ok=True)

# ── Snacks available on the menu (for food_pairings) ──────────────────────────
SNACKS = [
    "Kettle Sea Salt & Balsamic Vinegar of Modena",
    "Kettle Paprika & Roasted Onion",
    "Kettle Sea Salt & Black Pepper",
    "Kettle Honey Barbeque",
    "Kettle Sweet Chilli",
    "Kettle Matured Cheddar Cheese & Red Onions",
    "Kettle Sea Salt",
    "Kettle Rosemary",
    "Kettle Jalapeño",
    "Kettle Sweet Chilli & Sour Cream",
    "Kettle Vegan Sea Salt & Balsamic Vinegar",
    "Kettle Intense Camembert & Oak Smoked Garlic",
    "Kettle Intense Truffle and Sea Salt",
    "Tyrrell's Mature Cheddar & Chive",
    "Tyrrell's Sweet Chilli & Red Pepper",
    "Tyrrell's Sea Salt & Cider Vinegar",
    "Taylors Haggis & Cracked Black Pepper",
    "Taylors Aberdeen Angus",
    "Taylors Fiery Pickled Onions",
    "Taylors Blazing Barbeque",
    "Taylors Chip Shop Curry Sauce",
    "Ültje Studentenfutter",
    "Ültje Erdnüsse Gesalzen",
    "Ültje Kessel Erdnüsse Paprika",
]

# ── Helper ────────────────────────────────────────────────────────────────────
BASE_META = {"source_page": 1, "extraction_confidence": 0.90, "verified_date": "2025-01-01"}

def make_drink(id_, name, category, subcategory, brand, abv, origin, notes,
               primary_notes, sweetness, bitterness, body, finish, carbonation,
               food_pairings, tags, page=1):
    return {
        "id": id_,
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "brand_or_producer": brand,
        "abv": abv,
        "taste_profile": {
            "primary_notes": primary_notes,
            "sweetness": sweetness,
            "bitterness": bitterness,
            "body": body,
            "finish": finish,
            "carbonation": carbonation,
        },
        "origin": origin,
        "food_pairings": food_pairings,
        "tags": tags,
        "notes": notes,
        "metadata": {**BASE_META, "source_page": page},
    }

def write_json(drink):
    fname = f"{drink['id']}.json"
    with open(os.path.join(OUT, fname), "w") as f:
        json.dump(drink, f, indent=2, ensure_ascii=False)
    return fname

# ── Pairing helpers ───────────────────────────────────────────────────────────
def pair(*indices):
    """Select snacks by 0-based index into SNACKS."""
    return [SNACKS[i] for i in indices]

# Salty/crunchy classic pairings
PAIR_SALTY = pair(6, 0, 2)        # Sea Salt, Balsamic, Black Pepper
PAIR_CHEESE = pair(5, 13, 12)      # Mature Cheddar & Red Onion, Cheddar & Chive, Truffle
PAIR_MEATY = pair(16, 17, 18)      # Haggis, Aberdeen Angus, Pickled Onions
PAIR_SPICY = pair(4, 8, 9)         # Sweet Chilli, Jalapeño, Sweet Chilli & Sour Cream
PAIR_BBQ = pair(3, 19)             # Honey Barbeque, Blazing Barbeque
PAIR_NUTS = pair(21, 22, 20)       # Erdnüsse Gesalzen, Paprika, Studentenfutter
PAIR_SWEET_CHILLI = pair(4, 14, 3) # Sweet Chilli, Sweet Chilli & Red Pepper, Honey BBQ

# ── BEER MENU ─────────────────────────────────────────────────────────────────

# ---------- ALWAYS ON TAP (pages 2-5) ----------
drinks = []

# IPA on tap
drinks.append(make_drink(
    "pub_beer_001", "Brewdog Punk IPA", "beer", "india pale ale",
    "BrewDog", 5.6, "Ellon, Scotland",
    "Pale golden colour, tropical aroma with notes of grapefruit, pineapple and lychee over caramel malt. Bold citrus and hop flavours balanced by light caramel sweetness and spiky bitter finish.",
    ["grapefruit", "pineapple", "lychee", "caramel", "citrus"],
    "medium-low", "medium-high", "medium", "crisp, bitter", "medium",
    pair(4, 8, 6),  # Sweet Chilli, Jalapeño, Sea Salt
    ["craft", "ipa", "draft", "hoppy", "tropical"],
    page=2
))

drinks.append(make_drink(
    "pub_beer_002", "Brewdog Hazy Jane IPA", "beer", "new england ipa",
    "BrewDog", 5.6, "Ellon, Scotland",
    "Hazy golden-orange New England IPA with juicy tropical aroma of citrus, mango and passion fruit. Soft juicy notes dominate, minimal bitterness.",
    ["citrus", "mango", "passion fruit", "juicy", "tropical"],
    "medium", "low", "medium", "smooth, juicy", "medium",
    pair(4, 8, 14),  # Sweet Chilli, Jalapeño, Sweet Chilli & Red Pepper
    ["craft", "neipa", "draft", "hazy", "juicy", "tropical"],
    page=2
))

# Stout
drinks.append(make_drink(
    "pub_beer_003", "Guinness Draught", "beer", "irish dry stout",
    "Guinness", 4.2, "Dublin, Ireland",
    "Deep black Irish Dry Stout with subtle coffee and chocolate aroma. Smooth roasted malt flavour, slightly bitter with creamy silky carbonation.",
    ["roasted malt", "coffee", "chocolate", "creamy"],
    "low", "medium-low", "medium-full", "creamy, smooth", "low",
    pair(5, 16, 21),  # Cheddar & Red Onion, Haggis, Erdnüsse
    ["stout", "draft", "irish", "classic", "creamy"],
    page=2
))

# Ales
drinks.append(make_drink(
    "pub_beer_004", "Newcastle Brown Ale", "beer", "english brown ale",
    "Heineken UK", 4.7, "Newcastle upon Tyne, England",
    "Deep amber brown ale with toasted malt aroma, caramel and subtle nutty notes. Smooth toffee sweetness with gentle roasted finish. Medium bodied, soft carbonation.",
    ["toasted malt", "caramel", "toffee", "nutty"],
    "medium", "low", "medium", "smooth, roasted", "low",
    pair(16, 17, 5),  # Haggis, Angus, Cheddar
    ["brown ale", "draft", "english", "malty", "session"],
    page=2
))

drinks.append(make_drink(
    "pub_beer_005", "Fuller's London Pride", "beer", "english pale ale",
    "Fuller's Brewery", 4.7, "London, England",
    "Clear amber-gold English Pale Ale. Malty sweet aroma with biscuit and subtle floral hops. Balanced malt and hop character with hints of caramel. Medium body, smooth, slightly sweet finish.",
    ["malty", "biscuit", "caramel", "floral", "balanced"],
    "medium", "medium-low", "medium", "smooth, slightly sweet", "medium",
    pair(6, 5, 16),  # Sea Salt, Cheddar, Haggis
    ["cask", "session", "pub classic", "traditional", "balanced"],
    page=2
))

drinks.append(make_drink(
    "pub_beer_006", "Kilkenny Irish Red Ale", "beer", "irish red ale",
    "Guinness", 4.3, "Kilkenny, Ireland",
    "Deep reddish-amber Irish Red Ale with malty aroma, hints of caramel and toasted bread. Smooth malt sweet flavour with nutty and toffee notes. Creamy texture, soft sweet finish.",
    ["malty", "caramel", "toasted bread", "nutty", "toffee"],
    "medium", "low", "medium", "creamy, soft, sweet", "low",
    pair(5, 13, 16),  # Cheddar, Cheddar & Chive, Haggis
    ["red ale", "draft", "irish", "creamy", "malty"],
    page=2
))

# Pils
drinks.append(make_drink(
    "pub_beer_007", "Brinkhoff's No.1", "beer", "pilsner",
    "Brinkhoff's", 5.0, "Dortmund, Germany",
    "Clear pale golden Pils with biscuit malt and grassy hop aroma. Crisp malty flavour balanced by earthy bitterness, slightly bitter dry finish.",
    ["biscuit malt", "grassy", "earthy", "crisp"],
    "low", "medium", "light-medium", "dry, bitter", "medium-high",
    pair(6, 0, 18),  # Sea Salt, Balsamic Vinegar, Pickled Onions
    ["pilsner", "draft", "german", "crisp", "refreshing"],
    page=3
))

drinks.append(make_drink(
    "pub_beer_008", "Gösser Naturradler", "beer", "radler",
    "Gösser", 2.0, "Leoben, Austria",
    "Austrian Radler, pale yellow slightly hazy. Zesty lemon aroma, crisp tangy lemon flavour with light malt sweetness and gentle carbonation. Low alcohol, no artificial additives.",
    ["lemon", "citrus", "tangy", "light malt"],
    "medium", "very low", "light", "crisp, refreshing", "medium",
    pair(6, 4, 1),  # Sea Salt, Sweet Chilli, Paprika
    ["radler", "draft", "austrian", "low-alcohol", "citrus", "refreshing"],
    page=3
))

# Blonde
drinks.append(make_drink(
    "pub_beer_009", "La Trappe Blonde", "beer", "belgian blonde",
    "La Trappe", 6.5, "Tilburg, Netherlands",
    "Golden yellow Trappist beer with fresh fruity aroma of citrus and banana, complemented by sweet malt and subtle spice. Slightly sweet, soft bitterness, clean refreshing finish.",
    ["citrus", "banana", "malt", "spice", "fruity"],
    "medium", "medium-low", "medium", "clean, gentle bitter", "medium-high",
    pair(5, 13, 15),  # Cheddar, Cheddar & Chive, Cider Vinegar
    ["trappist", "blonde", "belgian", "draft", "fruity"],
    page=3
))

drinks.append(make_drink(
    "pub_beer_010", "Kronenbourg 1664 Blanc", "beer", "witbier",
    "Kronenbourg", 5.0, "Strasbourg, France",
    "French Witbier, hazy pale golden. Hints of citrus and exotic fruits, slightly sweet, refreshing citrus profile balanced by smooth bitterness from coriander and hops. Creamy and effervescent.",
    ["citrus", "exotic fruit", "coriander", "creamy"],
    "medium", "low", "medium", "smooth, creamy", "medium-high",
    pair(14, 4, 7),  # Sweet Chilli & Red Pepper, Sweet Chilli, Rosemary
    ["witbier", "french", "draft", "citrus", "refreshing"],
    page=3
))

# Lager
drinks.append(make_drink(
    "pub_beer_011", "Hop House 13 Lager", "beer", "lager",
    "Guinness", 5.0, "Dublin, Ireland",
    "Double-hopped lager from Guinness Open Gate Brewery. Golden amber, light hoppy aroma with floral and citrus notes. Full flavour, lively crisp refreshing finish with lingering hop character.",
    ["floral", "citrus", "hoppy", "crisp"],
    "low", "medium", "medium", "crisp, hoppy", "medium-high",
    pair(6, 18, 4),  # Sea Salt, Pickled Onions, Sweet Chilli
    ["lager", "draft", "irish", "hoppy", "crisp"],
    page=3
))

drinks.append(make_drink(
    "pub_beer_012", "Birra Moretti", "beer", "italian pale lager",
    "Heineken Italia", 4.6, "Udine, Italy",
    "Italian Pale Lager, balanced and smooth with bready malt character and delicate citrus and floral notes. Light bitterness and crisp finish.",
    ["bready malt", "citrus", "floral", "crisp"],
    "low", "low", "light", "crisp, clean", "medium",
    pair(6, 1, 2),  # Sea Salt, Paprika, Black Pepper
    ["lager", "draft", "italian", "crisp", "refreshing"],
    page=3
))

drinks.append(make_drink(
    "pub_beer_013", "Brooklyn Lager", "beer", "american amber lager",
    "Brooklyn Brewery", 5.2, "Brooklyn, New York, USA",
    "American Amber Lager, golden colour with caramel aroma, toasted malt and floral citrus notes. Balanced malt sweetness with toffee, crisp hop bitterness. Medium bodied, lingering hop finish.",
    ["caramel", "toasted malt", "floral", "citrus", "toffee"],
    "medium", "medium", "medium", "lingering hop", "medium",
    pair(17, 5, 4),  # Angus, Cheddar, Sweet Chilli
    ["lager", "draft", "american", "amber", "craft"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_014", "Brooklyn The Stonewall Inn IPA", "beer", "india pale ale",
    "Brooklyn Brewery", 5.0, "Brooklyn, New York, USA",
    "Fearless IPA for all. Unabashed notes of citrus peel and grapefruit, refreshing IPA celebrating diversity. Balanced, crisp and hoppy.",
    ["citrus peel", "grapefruit", "hoppy", "crisp"],
    "low", "medium", "medium", "crisp, hoppy", "medium",
    pair(4, 8, 6),  # Sweet Chilli, Jalapeño, Sea Salt
    ["ipa", "draft", "american", "craft", "citrus"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_015", "Carlsberg Unfiltered Beer", "beer", "lager",
    "Carlsberg", 5.0, "Copenhagen, Denmark",
    "Danish lager, hazy golden amber. Lightly malty aroma with honey, grains and subtle citrus. Gentle sweet malty flavour, moderately bitter finish. Clean, slightly dry aftertaste.",
    ["honey", "grain", "citrus", "malty"],
    "medium-low", "medium", "light-medium", "clean, slightly dry", "medium",
    pair(6, 0, 1),  # Sea Salt, Balsamic, Paprika
    ["lager", "draft", "danish", "unfiltered", "crisp"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_016", "Budweiser Budvar", "beer", "czech pale lager",
    "Budějovický Budvar", 5.0, "České Budějovice, Czech Republic",
    "Czech Pale Lager with Žatec hops and Moravian barley. Clear golden amber, crisp clean notes of fresh bread and grassy hops with malt sweetness. Medium bodied, clean dry finish.",
    ["fresh bread", "grassy hops", "malt", "crisp"],
    "low", "medium", "medium", "clean, dry, hoppy", "medium",
    pair(6, 18, 17),  # Sea Salt, Pickled Onions, Angus
    ["pilsner", "draft", "czech", "classic", "crisp"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_017", "Heineken Lager", "beer", "lager",
    "Heineken", 5.0, "Amsterdam, Netherlands",
    "Popular Dutch lager, pale golden. Light malt sweet aroma with subtle grain and floral notes. Highly carbonated, clean and crisp, slightly bitter. Served extra cold.",
    ["grain", "floral", "malt", "crisp"],
    "low", "medium-low", "light", "crisp, clean", "high",
    pair(6, 0, 18),  # Sea Salt, Balsamic, Pickled Onions
    ["lager", "draft", "dutch", "crisp", "extra cold"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_018", "Borsigplatz Style Export", "beer", "dortmunder export",
    "Borsigplatz", 5.6, "Dortmund, Germany",
    "Dortmunder Export, clear golden amber. Light malt sweet aroma with subtle grain and floral notes. Balanced malt sweet flavour, crisp dry finish with slight lingering hop bitterness.",
    ["malt", "grain", "floral", "crisp"],
    "medium-low", "medium", "medium", "crisp, dry", "medium",
    pair(6, 4, 1),  # Sea Salt, Sweet Chilli, Paprika
    ["export", "draft", "german", "dortmunder", "malty"],
    page=4
))

drinks.append(make_drink(
    "pub_beer_019", "Staropramen Premium Lager", "beer", "czech pale lager",
    "Staropramen", 5.0, "Prague, Czech Republic",
    "Czech Pale Lager, clear golden. Mild malt sweet aroma with light bread and floral notes. Balanced smooth, slightly sweet malty flavour with subtle bitterness. Gentle hop aftertaste.",
    ["bready malt", "floral", "smooth", "balanced"],
    "medium-low", "low", "medium", "gentle hop", "medium",
    pair(6, 21, 2),  # Sea Salt, Erdnüsse, Black Pepper
    ["lager", "draft", "czech", "smooth", "balanced"],
    page=4
))

# Dubbel
drinks.append(make_drink(
    "pub_beer_020", "Grimbergen Double Ambrée", "beer", "belgian dubbel",
    "Grimbergen", 6.5, "Grimbergen, Belgium",
    "Belgian Dubbel, deep amber with reddish highlights. Caramel and toasted bread aroma with dried fruits and light spice. Rich malty sweet, notes of caramel and dark fruits, mild hop bitterness. Warm, malty subtle dry finish.",
    ["caramel", "toasted bread", "dried fruits", "spice", "dark fruits"],
    "medium-high", "low", "medium-full", "warm, malty, dry", "medium",
    pair(5, 12, 16),  # Cheddar, Truffle, Haggis
    ["dubbel", "belgian", "draft", "malty", "rich"],
    page=5
))

# Helles
drinks.append(make_drink(
    "pub_beer_021", "Bayreuther Hell", "beer", "helles lager",
    "Bayreuther Bierbrauerei", 4.9, "Bayreuth, Germany",
    "Bavarian Helles Lager, pale golden clear. Light malty sweet aroma with subtle floral hops. Smooth malt-forward flavour, gentle bitterness. Medium-bodied, softly carbonated, clean, crisp and refreshing.",
    ["malty", "floral", "smooth", "crisp"],
    "medium-low", "low", "medium", "clean, crisp", "medium",
    pair(6, 1, 17),  # Sea Salt, Paprika, Angus
    ["helles", "draft", "bavarian", "crisp", "refreshing"],
    page=5
))

# Cider on tap
drinks.append(make_drink(
    "pub_beer_022", "Strongbow Cider", "cider", "dry english cider",
    "Strongbow", 4.5, "Hereford, England",
    "Light-bodied, sparkling Dry English Cider, most popular cider in the UK. Pale golden clear, fresh apple aroma with floral and citrus hints. Crisp and dry with subtle sweetness and strong apple character.",
    ["apple", "floral", "citrus", "crisp", "dry"],
    "medium-low", "very low", "light", "crisp, dry", "medium-high",
    pair(6, 15, 3),  # Sea Salt, Cider Vinegar, Honey BBQ
    ["cider", "draft", "english", "dry", "crisp"],
    page=5
))

drinks.append(make_drink(
    "pub_beer_023", "Somersby Apple Cider", "cider", "sweet cider",
    "Somersby", 4.5, "Denmark",
    "Sweet apple cider from Denmark. Golden clear, light carbonation. Fresh sweet apple aroma with floral hints. Sweet and apple-forward with mild tartness.",
    ["apple", "floral", "sweet", "mild tartness"],
    "high", "very low", "light-medium", "sweet, mild tart", "medium",
    pair(6, 3, 4),  # Sea Salt, Honey BBQ, Sweet Chilli
    ["cider", "draft", "danish", "sweet", "apple"],
    page=5
))

# Alkoholfrei on tap
drinks.append(make_drink(
    "pub_beer_024", "Bergmann Frühschicht Alkoholfrei", "beer", "non-alcoholic beer",
    "Bergmann", 0.0, "Germany",
    "Surprisingly alcohol-free. Light, hop-infused, fruity, hoppy aroma.",
    ["hoppy", "fruity", "light"],
    "low", "low", "light", "clean, hoppy", "medium",
    pair(6, 4, 1),  # Sea Salt, Sweet Chilli, Paprika
    ["alcohol-free", "draft", "german", "hoppy", "refreshing"],
    page=5
))

# ---------- GUEST TAPS (page 6) ----------
drinks.append(make_drink(
    "pub_beer_025", "Vocation Life and Death IPA", "beer", "india pale ale",
    "Vocation Brewery", 6.5, "Hebden Bridge, England",
    "Wonderfully fresh IPA with pleasant tartness and smooth malt body. Large quantities of Mosaic and Citra hops.",
    ["citrus", "tropical", "mosaic hops", "citra hops", "tart"],
    "low", "medium-high", "medium", "fresh, tart, hoppy", "medium",
    pair(4, 8, 14),  # Sweet Chilli, Jalapeño, Sweet Chilli & Red Pepper
    ["ipa", "guest tap", "english", "hoppy", "craft"],
    page=6
))

drinks.append(make_drink(
    "pub_beer_026", "Hopacabana NW Ale West Coast IPA", "beer", "west coast ipa",
    "Hopacabana", 6.8, "Germany",
    "Clear golden with slight amber. Complex interplay of Simcoe, Strata, Citra and Magnum hops: tropical fruits, citrus, passion fruit, paired with resinous earthy undertones.",
    ["tropical fruit", "citrus", "passion fruit", "resinous", "earthy"],
    "low", "medium-high", "medium", "dry, resinous", "medium",
    pair(4, 8, 6),  # Sweet Chilli, Jalapeño, Sea Salt
    ["west coast ipa", "guest tap", "hoppy", "resinous", "craft"],
    page=6
))

drinks.append(make_drink(
    "pub_beer_027", "Borbecker Salonbier", "beer", "amber ale",
    "Borbecker", 5.1, "Germany",
    "Special amber-coloured specialty beer brewed using the classic mashing process.",
    ["amber", "malty", "traditional"],
    "medium", "low", "medium", "smooth", "medium",
    pair(5, 6, 16),  # Cheddar, Sea Salt, Haggis
    ["amber ale", "guest tap", "german", "traditional"],
    page=6
))

drinks.append(make_drink(
    "pub_beer_028", "Murphy's Red Ale", "beer", "irish red ale",
    "Murphy's", 5.0, "Cork, Ireland",
    "Copper-rose gold Irish ale with light fresh hints of beer in aroma. Delicate fruitiness of raisins without sweetness. Mild subtly bitter dry aftertaste.",
    ["raisin", "fruity", "mild", "dry"],
    "low", "medium-low", "medium", "dry, subtly bitter", "medium",
    pair(5, 13, 21),  # Cheddar, Cheddar & Chive, Erdnüsse
    ["red ale", "guest tap", "irish", "malty"],
    page=6
))

drinks.append(make_drink(
    "pub_beer_029", "Estrella Damm", "beer", "lager",
    "Estrella Damm", 5.4, "Barcelona, Spain",
    "Slightly tart and refreshing, followed by sweet malty corn flavour. Delicate fruitiness with spicy tart notes. Very mild, no bitterness. Light, easy drinking, perfect thirst-quencher cold.",
    ["corn", "fruity", "spicy", "tart"],
    "medium-low", "very low", "light", "mild, refreshing", "medium",
    pair(1, 6, 15),  # Paprika, Sea Salt, Cider Vinegar
    ["lager", "guest tap", "spanish", "mild", "refreshing"],
    page=6
))

drinks.append(make_drink(
    "pub_beer_030", "Bergmann Amber Lager", "beer", "vienna lager",
    "Bergmann", 5.7, "Germany",
    "Viennese-style amber lager. Gentle fruit and subtle yeast notes on aroma. Harmonious malty body on the palate. Restrained bitterness for balance, smooth finish.",
    ["malty", "fruit", "yeast", "balanced"],
    "medium", "low", "medium-full", "smooth", "medium",
    pair(16, 17, 5),  # Haggis, Angus, Cheddar
    ["vienna lager", "guest tap", "german", "malty", "smooth"],
    page=6
))

# ---------- ALCOHOL FREE (pages 7-10) ----------
drinks.append(make_drink(
    "pub_beer_031", "BRLO Naked Alcohol-Free Pale Ale", "beer", "non-alcoholic pale ale",
    "BRLO", 0.0, "Berlin, Germany",
    "Golden amber alcohol-free Pale Ale. Fresh citrus, earthy herb and subtle sweet aroma. Bright citrus tangerine and lemon flavour, light malt sweetness with hint of pine. Light bodied, crisp, effervescent.",
    ["citrus", "tangerine", "lemon", "pine", "earthy"],
    "low", "medium-low", "light", "crisp, mild bitter", "medium-high",
    pair(6, 4, 1),
    ["alcohol-free", "pale ale", "german", "craft", "citrus"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_032", "Erdinger Alcohol Free Weizen", "beer", "non-alcoholic wheat beer",
    "Erdinger", 0.0, "Erding, Germany",
    "Alcohol-free German wheat beer. Straw yellow, fine yeast and subtle hop aroma. Rich malty and spicy flavour with hint of fruity acidity. Full-bodied and refreshing.",
    ["banana", "clove", "malty", "spicy", "fruity"],
    "medium", "very low", "medium-full", "clean, refreshing", "medium-high",
    pair(6, 11, 21),
    ["alcohol-free", "weizen", "german", "wheat", "classic"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_033", "Heineken 0.0%", "beer", "non-alcoholic lager",
    "Heineken", 0.0, "Amsterdam, Netherlands",
    "Pale golden clear non-alcoholic lager. Light malt sweetness with subtle cereal and floral notes. Mild malt character, soft bitterness. Light-bodied, smooth, moderately carbonated, refreshing.",
    ["malt", "cereal", "floral", "smooth"],
    "low", "low", "light", "smooth, refreshing", "medium",
    pair(6, 0, 2),
    ["alcohol-free", "lager", "dutch", "refreshing"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_034", "Carlsberg 0.0%", "beer", "non-alcoholic lager",
    "Carlsberg", 0.0, "Copenhagen, Denmark",
    "Non-alcoholic Pale Lager, pale golden clear. Light malt sweet aroma with grain and hop notes. Malty and slightly sweet, gentle bitterness. Light-bodied, smooth, lightly carbonated.",
    ["malt", "grain", "hops", "smooth"],
    "medium-low", "low", "light", "smooth, clean", "medium",
    pair(6, 1, 0),
    ["alcohol-free", "lager", "danish", "refreshing"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_035", "Guinness 0.0%", "beer", "non-alcoholic stout",
    "Guinness", 0.0, "Dublin, Ireland",
    "Alcohol-free version of the popular Irish stout.",
    ["roasted malt", "coffee", "chocolate"],
    "low", "medium-low", "medium", "creamy, smooth", "low",
    pair(5, 16, 21),
    ["alcohol-free", "stout", "irish", "classic"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_036", "La Trappe Nilis", "beer", "non-alcoholic trappist",
    "La Trappe", 0.0, "Tilburg, Netherlands",
    "World's first non-alcoholic 0.0% Trappist beer. Dark amber-coloured with creamy white head. Fruity and malty with pleasant bitterness and caramel-sweet finish.",
    ["caramel", "fruity", "malty", "sweet"],
    "medium", "medium-low", "medium", "caramel-sweet", "medium",
    pair(5, 12, 13),
    ["alcohol-free", "trappist", "belgian", "premium"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_037", "Kehrwieder Miami Groove Juicy Pale Ale", "beer", "non-alcoholic pale ale",
    "Kehrwieder", 0.4, "Hamburg, Germany",
    "Alcohol-free Juicy Pale Ale inspired by Miami. Tastes like piña colada – pineapple meets coconut with a hint of pink grapefruit.",
    ["pineapple", "coconut", "grapefruit", "tropical"],
    "medium", "low", "medium", "tropical, juicy", "medium",
    pair(4, 6, 3),
    ["alcohol-free", "pale ale", "german", "tropical", "juicy"],
    page=7
))

drinks.append(make_drink(
    "pub_beer_038", "Kehrwieder ü.NN Alcohol-Free IPA", "beer", "non-alcoholic india pale ale",
    "Kehrwieder", 0.4, "Hamburg, Germany",
    "First German alcohol-free India Pale Ale. Full of flavour despite no alcohol.",
    ["hoppy", "citrus", "pine", "balanced"],
    "low", "medium", "medium", "dry, hoppy", "medium",
    pair(4, 8, 6),
    ["alcohol-free", "ipa", "german", "craft", "hoppy"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_039", "Tut Gut Malz", "beer", "non-alcoholic malt drink",
    "Tut Gut", 0.0, "Germany",
    "Dark amber malty and sweet beverage. Traditional malty experience without alcohol. Rich malt, caramel and subtle sweet flavours, clean slightly sweet finish. Packed with vitamins, natural products.",
    ["malt", "caramel", "sweet"],
    "high", "very low", "medium-full", "clean, sweet", "low",
    pair(21, 20, 22),
    ["alcohol-free", "malz", "german", "vitamin", "traditional"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_040", "Brewdog Punk AF", "beer", "non-alcoholic pale ale",
    "BrewDog", 0.0, "Ellon, Scotland",
    "Non-alcoholic pale ale, golden with subtle haze. Juicy tropical aromas of pineapple, mango and grapefruit layered over grassy piney hop notes. Bright citrus-forward, clean and easy-drinking.",
    ["pineapple", "mango", "grapefruit", "grassy", "piney"],
    "low", "medium", "light", "clean, crisp", "medium",
    pair(4, 6, 14),
    ["alcohol-free", "pale ale", "scottish", "craft", "tropical"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_041", "La Chouffe Alcohol Free", "beer", "non-alcoholic belgian blonde",
    "La Chouffe", 0.4, "Achouffe, Belgium",
    "Refreshing golden non-alcoholic Belgian Blonde. Gentle grain and earthy flavour with fruity and spicy undertones. Light, smooth brightness, crisp subtly herby finish.",
    ["grain", "earthy", "fruity", "spicy", "herbal"],
    "medium-low", "low", "light", "crisp, herbal", "medium",
    pair(6, 1, 14),
    ["alcohol-free", "belgian", "blonde", "craft"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_042", "Jopen Non-IPA", "beer", "non-alcoholic india pale ale",
    "Jopen", 0.3, "Haarlem, Netherlands",
    "Lightly golden slightly cloudy non-alcoholic IPA. Balanced aroma of sweet malt and tropical fruit. Fruity sweetness, firm bitterness with earthy piney notes. Long dry pleasantly bitter finish.",
    ["tropical fruit", "malt", "earthy", "piney", "bitter"],
    "medium-low", "medium-high", "medium", "long, dry, bitter", "medium",
    pair(4, 8, 6),
    ["alcohol-free", "ipa", "dutch", "hoppy", "craft"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_043", "Lindemans Kriek 0.0%", "beer", "non-alcoholic fruit beer",
    "Lindemans", 0.0, "Vlezenbeek, Belgium",
    "Lindemans Kriek alcohol-free version. Classic fruity cherry beer without alcohol.",
    ["cherry", "sweet", "tart", "fruity"],
    "medium", "very low", "medium", "sweet-tart, fruity", "medium",
    pair(17, 12, 6),
    ["alcohol-free", "fruit beer", "belgian", "cherry", "lambic"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_044", "BRLO Naked Helles", "beer", "non-alcoholic helles",
    "BRLO", 0.0, "Berlin, Germany",
    "Non-alcoholic lager. Complete beer garden feeling without the hangover.",
    ["malty", "crisp", "clean", "light"],
    "low", "low", "light", "crisp, clean", "medium",
    pair(6, 1, 0),
    ["alcohol-free", "helles", "german", "craft", "refreshing"],
    page=8
))

drinks.append(make_drink(
    "pub_beer_045", "Brewdog Wingman Alcohol-Free", "beer", "non-alcoholic ipa",
    "BrewDog", 0.5, "Ellon, Scotland",
    "Everything you love about a fresh tropical IPA, just without alcohol. Slightly cloudy golden, velvety mouthfeel from oats and wheat.",
    ["tropical", "citrus", "hoppy", "smooth"],
    "low", "medium", "medium", "smooth, hoppy", "medium",
    pair(4, 6, 14),
    ["alcohol-free", "ipa", "scottish", "craft", "tropical"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_046", "Huyghe Delirium Alcohol-Free", "beer", "non-alcoholic belgian ale",
    "Huyghe", 0.3, "Melle, Belgium",
    "Legendary Belgian beer experience without alcohol. Spicy and fruity aroma accompanied by slight bitterness. Clear golden yellow, fine-pored head.",
    ["spicy", "fruity", "bitter", "golden"],
    "low", "medium-low", "medium", "dry, bitter", "medium-high",
    pair(5, 12, 6),
    ["alcohol-free", "belgian", "craft", "spicy"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_047", "Huyghe Paranoia Alcohol-Free", "beer", "non-alcoholic belgian ale",
    "Huyghe", 0.3, "Melle, Belgium",
    "Citrus notes, dry aftertaste, cloudy unfiltered appearance. Unique taste experience without typical non-alcoholic beer character.",
    ["citrus", "dry", "unfiltered", "crisp"],
    "low", "medium", "medium", "dry, crisp", "medium",
    pair(14, 8, 6),
    ["alcohol-free", "belgian", "craft", "unfiltered"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_048", "La Trappe Epos", "beer", "non-alcoholic trappist",
    "La Trappe", 0.0, "Tilburg, Netherlands",
    "Naturally cloudy light blonde Trappist beer with generous head. Pleasant bitterness and refreshing finish.",
    ["malty", "fruity", "bitter", "blonde"],
    "low", "medium", "medium", "refreshing, bitter", "medium",
    pair(5, 13, 15),
    ["alcohol-free", "trappist", "dutch", "premium"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_049", "Huyghe Delirium Alcohol-Free Blond", "beer", "non-alcoholic belgian blonde",
    "Huyghe", 0.3, "Melle, Belgium",
    "Belgian beer enjoyment without alcohol. Golden appearance, spicy fruity aroma, gentle bitterness. Full-bodied craft beer for conscious enjoyment.",
    ["spicy", "fruity", "golden", "balanced"],
    "low", "medium-low", "medium", "gentle bitter", "medium",
    pair(5, 12, 14),
    ["alcohol-free", "belgian", "blonde", "craft"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_050", "Brewdog Hazy Jane AF", "beer", "non-alcoholic new england ipa",
    "BrewDog", 0.5, "Ellon, Scotland",
    "Hazy AF has all the character and flavour without alcohol. Tropical fruits meet grassy notes, oats and wheat for velvety mouthfeel.",
    ["tropical", "grassy", "citrus", "velvety"],
    "low", "medium", "medium", "smooth, velvety", "medium",
    pair(4, 14, 6),
    ["alcohol-free", "neipa", "scottish", "craft", "hazy"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_051", "Liefmans Fruitesse 0.0", "beer", "non-alcoholic fruit beer",
    "Liefmans", 0.0, "Oudenaarde, Belgium",
    "Belgian alcohol-free fruit beer. Bright cherry red colour, red fruity intensity – cherries, raspberries, strawberries, blueberries, elderberries. Sparkling and light, best enjoyed on the rocks.",
    ["cherry", "raspberry", "strawberry", "blueberry", "elderberry"],
    "medium", "very low", "light", "sparkling, fruity", "medium-high",
    pair(17, 12, 6),
    ["alcohol-free", "fruit beer", "belgian", "berries", "sparkling"],
    page=9
))

drinks.append(make_drink(
    "pub_beer_052", "Mashsee Blaufrei", "beer", "non-alcoholic beer",
    "Mashsee", 0.0, "Germany",
    "Surprisingly full-bodied for non-alcoholic. Slight malt sweetness, pleasantly fruity mildly tart hop aroma reminiscent of peach and lychee.",
    ["peach", "lychee", "malty", "fruity", "tart"],
    "medium-low", "low", "medium", "fruity, tart", "medium",
    pair(6, 4, 1),
    ["alcohol-free", "german", "craft", "fruity"],
    page=10
))

drinks.append(make_drink(
    "pub_beer_053", "Kirin Ichiban Alcohol-Free", "beer", "non-alcoholic lager",
    "Kirin", 0.0, "Japan",
    "Clear barley beer with no aftertaste. By using the best pressing method and first press wort, elegant taste with less flavour interference.",
    ["barley", "clean", "mild", "elegant"],
    "low", "very low", "light", "clean, no aftertaste", "medium",
    pair(6, 0, 2),
    ["alcohol-free", "lager", "japanese", "clean"],
    page=10
))

# Alcohol-Free Ciders
drinks.append(make_drink(
    "pub_beer_054", "Thatcher's Zero Cider", "cider", "non-alcoholic cider",
    "Thatcher's", 0.0, "Somerset, England",
    "Alcohol-free pale golden cider with crisp apple sweetness and mild clean refreshing finish.",
    ["apple", "crisp", "sweet", "clean"],
    "medium", "very low", "light", "clean, refreshing", "medium",
    pair(6, 15, 3),
    ["alcohol-free", "cider", "english", "apple"],
    page=10
))

drinks.append(make_drink(
    "pub_beer_055", "Pulp Low Alcohol Apple Cider", "cider", "low-alcohol cider",
    "Pulp", 0.5, "England",
    "Crafted from home grown fresh pressed cider apples. Low alcohol, sweet but fresh flavour.",
    ["apple", "fresh", "sweet"],
    "medium-high", "very low", "light", "sweet, fresh", "medium",
    pair(6, 15, 3),
    ["low-alcohol", "cider", "english", "apple"],
    page=10
))

drinks.append(make_drink(
    "pub_beer_056", "Mac Ivors Alcohol Free Irish Cider", "cider", "non-alcoholic cider",
    "Mac Ivors", 0.5, "Northern Ireland",
    "Innovative non-alcoholic cider blend of apple wine and fresh juice from Northern Irish dessert apples. Straw-yellow, fine carbonation, light refreshing semi-dry. Only 76 calories.",
    ["apple", "fresh", "semi-dry", "light"],
    "medium", "very low", "light", "light, refreshing", "medium",
    pair(6, 15, 21),
    ["alcohol-free", "cider", "irish", "low-calorie"],
    page=10
))

drinks.append(make_drink(
    "pub_beer_057", "Somersby Zero Apple", "cider", "non-alcoholic cider",
    "Somersby", 0.0, "Denmark",
    "Refreshing apple flavour with balance of fruity and sweet notes. 0% Alcohol, 0% Sugar, 0% Calories. Long-lasting fruity flavour.",
    ["apple", "fruity", "sweet", "balanced"],
    "medium", "very low", "light", "fruity, balanced", "medium",
    pair(6, 15, 3),
    ["alcohol-free", "cider", "danish", "zero calorie"],
    page=10
))

# ---------- BOTTLES: ALES (pages 11-14) ----------
drinks.append(make_drink(
    "pub_beer_058", "Duvel Belgian Gold Ale", "beer", "belgian strong pale ale",
    "Duvel Moortgat", 8.5, "Breendonk, Belgium",
    "Belgian Strong Pale Ale, pale golden. Fragrant blend of citrus zest, apple, banana and subtle spice. Crisp and dry with pale malt sweetness. Silky smooth with lively carbonation.",
    ["citrus zest", "apple", "banana", "spice", "crisp"],
    "medium", "medium", "medium", "crisp, dry", "high",
    pair(5, 12, 6),
    ["belgian", "strong ale", "bottle", "classic", "effervescent"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_059", "Enigma Black Fuel Quadrupel", "beer", "belgian quadrupel",
    "Enigma", 9.5, "Belgium",
    "Dark brown with ruby highlights Belgian Strong Dark Ale. Rich notes of caramelised sugar, dark fruits and hint of banana. Sweet maltiness, medium-bodied, moderately carbonated. Smooth warming, lingering malt sweet finish.",
    ["caramelised sugar", "dark fruits", "banana", "malty", "warming"],
    "high", "low", "medium", "smooth, warming, sweet", "medium",
    pair(12, 5, 16),
    ["quadrupel", "belgian", "bottle", "dark ale", "rich"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_060", "Kona Big Wave Golden Ale", "beer", "golden ale",
    "Kona Brewing Co.", 4.4, "Hawaii, USA",
    "Brewed in Hawaii. Light malt sweet aroma with hints of tropical fruit. Crisp and refreshing, balanced malt profile with notes of honey and caramel. Light-bodied, smooth clean finish.",
    ["tropical fruit", "honey", "caramel", "crisp"],
    "medium", "low", "light", "smooth, clean", "medium",
    pair(6, 4, 3),
    ["golden ale", "bottle", "hawaiian", "tropical", "refreshing"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_061", "Rodenbach Grand Cru Oak Aged", "beer", "flemish red ale",
    "Rodenbach", 6.0, "Roeselare, Belgium",
    "Flemish Red Ale partially matured in wooden oak casks. Complex layers of tart red fruits, balsamic vinegar and oak, balanced by subtle sweetness similar to Madeira wine. Medium bodied, lively carbonation, dry tart finish.",
    ["tart red fruits", "balsamic", "oak", "wine-like", "complex"],
    "medium-low", "medium", "medium", "dry, tart, woody", "high",
    pair(12, 5, 15),
    ["flemish red", "oak aged", "bottle", "belgian", "sour"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_062", "Shepherd Neame Bishops Finger", "beer", "english strong ale",
    "Shepherd Neame", 5.4, "Kent, England",
    "Strong Ale brewed in Kent. Deep amber with ruby highlights. Rich malty aroma with caramel, toffee and dried fruits. Full-bodied with plums, dried apricots, pepper and cinnamon. Clean finish with subtle blood orange bitterness.",
    ["caramel", "toffee", "dried fruits", "plum", "spice"],
    "medium", "medium", "medium-full", "clean, subtle bitter", "medium",
    pair(16, 17, 5),
    ["strong ale", "bottle", "english", "kent", "malty"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_063", "Tennent's Scotch Ale", "beer", "scotch ale",
    "Tennent's", 9.0, "Glasgow, Scotland",
    "Scotch Ale with clear amber appearance, orange highlights. Rich malty aroma with caramel, toffee and dried fruits. Dark fruits and hints of spice. Smooth, well carbonated, clean subtly blood-orange finish.",
    ["caramel", "toffee", "dried fruits", "dark fruits", "spice"],
    "medium-high", "low", "medium-full", "smooth, subtle citrus", "medium",
    pair(16, 5, 12),
    ["scotch ale", "bottle", "scottish", "strong", "malty"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_064", "Wychwood Hobgoblin Gold", "beer", "golden ale",
    "Wychwood", 4.5, "Oxfordshire, England",
    "Golden ale balanced by citrus aromas and hints of hops and malt. Perfectly matched bitterness and pleasant carbonation.",
    ["citrus", "hoppy", "malty", "balanced"],
    "medium-low", "medium", "medium", "balanced, bitter", "medium",
    pair(6, 4, 5),
    ["golden ale", "bottle", "english", "citrus", "balanced"],
    page=11
))

drinks.append(make_drink(
    "pub_beer_065", "Wychwood Hobgoblin Ruby", "beer", "english amber ale",
    "Wychwood", 5.0, "Oxfordshire, England",
    "Very smooth initial taste with toffee, chocolate, and subtle fruity lemon notes. Dried fruit aromas, moderate bitterness finish.",
    ["toffee", "chocolate", "lemon", "dried fruit", "smooth"],
    "medium", "medium", "medium", "smooth, moderate bitter", "medium",
    pair(5, 16, 21),
    ["amber ale", "bottle", "english", "malty", "smooth"],
    page=12
))

drinks.append(make_drink(
    "pub_beer_066", "O'Hara's Irish Red Ale", "beer", "irish red ale",
    "O'Hara's", 4.3, "Carlow, Ireland",
    "Round and very full-bodied Irish red ale, almost like a bock beer. Caramel malt comes through clearly, hops give plenty of bite. Strong character.",
    ["caramel", "malty", "hoppy", "full-bodied"],
    "medium", "medium", "medium-full", "malty, hoppy", "medium",
    pair(16, 5, 13),
    ["red ale", "bottle", "irish", "full-bodied", "malty"],
    page=12
))

drinks.append(make_drink(
    "pub_beer_067", "Shepherd Neame Christmas Ale", "beer", "winter ale",
    "Shepherd Neame", 7.0, "Kent, England",
    "Rich malt notes complemented by dried fruits – raisins and plums. Warm undertone of cloves, cinnamon, nutmeg. Subtle hop bitterness for freshness.",
    ["raisins", "plums", "cloves", "cinnamon", "nutmeg"],
    "medium-high", "medium-low", "medium-full", "warm, spiced", "medium",
    pair(16, 5, 12),
    ["winter ale", "bottle", "english", "christmas", "spiced"],
    page=12
))

drinks.append(make_drink(
    "pub_beer_068", "Orkney Brewery Corncrake Ale", "beer", "golden ale",
    "Orkney Brewery", 4.1, "Orkney, Scotland",
    "Irresistible golden ale. New world hops compliment biscuity pale malt. Thirst-quenching with fruit flavours of lemon, apricot and peach.",
    ["lemon", "apricot", "peach", "biscuity", "fruity"],
    "medium-low", "medium", "medium", "fruity, refreshing", "medium",
    pair(6, 1, 4),
    ["golden ale", "bottle", "scottish", "fruity", "refreshing"],
    page=12
))

drinks.append(make_drink(
    "pub_beer_069", "Orkney Brewery Dark Island Ale", "beer", "scottish ale",
    "Orkney Brewery", 4.6, "Orkney, Scotland",
    "Iconic beer, gold standard-bearer for crafted premium Scottish Ales. Ripe fruity and roast coffee aromas with flavours of dark chocolate, dates and nuts from roasted malts and robust hops.",
    ["roast coffee", "dark chocolate", "dates", "nuts", "ripe fruit"],
    "medium", "medium", "medium", "roasted, rich", "medium",
    pair(16, 5, 21),
    ["scottish ale", "bottle", "premium", "roasted", "iconic"],
    page=12
))

drinks.append(make_drink(
    "pub_beer_070", "Samuel Smith Yorkshire Stingo", "beer", "english strong ale",
    "Samuel Smith", 8.0, "Yorkshire, England",
    "Strong reddish-brown beer with notes of malt, raisins, and toffee. Oak barrel aged with smooth sweet finish.",
    ["malt", "raisins", "toffee", "oak", "sweet"],
    "medium-high", "low", "medium-full", "smooth, sweet", "medium",
    pair(5, 12, 16),
    ["strong ale", "bottle", "english", "oak aged", "yorkshire"],
    page=12
))

# Blonde bottles
drinks.append(make_drink(
    "pub_beer_071", "La Chouffe Blonde", "beer", "belgian blonde",
    "La Chouffe", 8.0, "Achouffe, Belgium",
    "Golden beer, slightly hazy. Bright citrus and pear aroma with sweet banana, clove and coriander notes. Silky smooth with subtle bitterness and bright carbonation for long smooth finish.",
    ["citrus", "pear", "banana", "clove", "coriander"],
    "medium", "medium-low", "medium", "long, smooth", "high",
    pair(5, 12, 14),
    ["blonde", "belgian", "bottle", "fruity", "spicy"],
    page=12
))

# Diverse (pages 13-14)
drinks.append(make_drink(
    "pub_beer_072", "Boon Oude Geuze Lambic", "beer", "lambic - gueuze",
    "Boon", 7.0, "Lembeek, Belgium",
    "Traditional Lambic blend, hazy golden. Bright citrus notes of grapefruit and green apple, subtle oak and white wine. Tart flavour with lemongrass, apricot, vanilla and nuts. Crisp dry with lively carbonation.",
    ["grapefruit", "green apple", "oak", "lemongrass", "apricot"],
    "low", "high", "medium", "crisp, dry, oaky", "high",
    pair(15, 12, 5),
    ["lambic", "gueuze", "bottle", "belgian", "sour"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_073", "Boon Geuze Mariage Parfait", "beer", "lambic - gueuze",
    "Boon", 8.0, "Lembeek, Belgium",
    "Lambic beers aged for three years in oak barrels. Aroma of new leather, lemon and light pistachio. Spritzy and dry with bright acidity and tannic spicy finish.",
    ["lemon", "pistachio", "leather", "oak", "tannic"],
    "low", "high", "medium", "dry, tannic, spicy", "high",
    pair(15, 5, 12),
    ["lambic", "gueuze", "bottle", "belgian", "oak aged", "sour"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_074", "Enigma Winter Helheim", "beer", "winter ale",
    "Enigma", 12.0, "Belgium",
    "Malty caramel nuances harmonise with pleasant bitter accent of 31 IBU. Barley malt, hops and candy sugar for Christmas season enjoyment.",
    ["caramel", "malty", "bitter", "candy sugar"],
    "medium-high", "medium", "medium-full", "warming, bitter", "medium",
    pair(16, 5, 12),
    ["winter ale", "bottle", "belgian", "christmas", "strong"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_075", "Liefmans Glühkriek", "beer", "fruit beer",
    "Liefmans", 6.0, "Oudenaarde, Belgium",
    "Mild and full of cherry flavours with light spicy Christmas spices. Fruity sweet, beautiful combination of fruit and malt sweetness with woody notes from barrel ageing and Christmas spices – cinnamon, cloves, aniseed.",
    ["cherry", "cinnamon", "cloves", "aniseed", "woody"],
    "medium-high", "low", "medium", "fruity, sweet, spiced", "medium",
    pair(17, 12, 16),
    ["fruit beer", "bottle", "belgian", "christmas", "cherry"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_076", "Samuel Smith Winter Welcome", "beer", "winter ale",
    "Samuel Smith", 6.0, "Yorkshire, England",
    "Bright orange-reddish amber with cream-coloured head. Aromas of light caramel and spicy nuances, rounded off by light fruit and grain notes.",
    ["caramel", "spicy", "fruit", "grain", "balanced"],
    "medium", "medium-low", "medium", "balanced, smooth", "medium",
    pair(16, 5, 21),
    ["winter ale", "bottle", "english", "yorkshire", "seasonal"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_077", "Innis & Gunn The Original", "beer", "wood-aged golden ale",
    "Innis & Gunn", 6.6, "Edinburgh, Scotland",
    "Wood-aged Golden Ale, clear amber. Rich notes of vanilla, toffee and subtle hints of oak and whisky. Smooth balanced biscuity maltiness with vanilla, toffee and oak. Mellow character, lingering sweet finish.",
    ["vanilla", "toffee", "oak", "whisky", "biscuity"],
    "medium-high", "low", "medium", "mellow, sweet, oaky", "medium",
    pair(5, 12, 16),
    ["golden ale", "bottle", "scottish", "oak aged", "vanilla"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_078", "La Trappe Dubbel", "beer", "belgian dubbel",
    "La Trappe", 7.0, "Tilburg, Netherlands",
    "Dark-brown Trappist ale with fruity aroma, warm tones of vanilla, caramel and roasted chocolate. Full malty caramel-sweet taste with subtle sweet influence of dates, honey and dried fruits. Aftertaste sweet and slightly bitter.",
    ["vanilla", "caramel", "roasted chocolate", "dates", "honey"],
    "medium-high", "medium-low", "medium-full", "sweet, slightly bitter", "medium",
    pair(5, 12, 16),
    ["dubbel", "trappist", "bottle", "dutch", "rich"],
    page=13
))

drinks.append(make_drink(
    "pub_beer_079", "Harvey's Prince of Denmark", "beer", "imperial stout",
    "Harvey's", 7.5, "Lewes, England",
    "Imperial stout served at room temperature. Dark brown, complex aroma with burnt chocolate, brandy, umami and vanilla. Rich warming with leather, chocolate, liquorice and roasted malt. Dry finish with lingering bittersweet aftertaste.",
    ["burnt chocolate", "brandy", "umami", "vanilla", "liquorice"],
    "medium", "medium-high", "full", "dry, bittersweet", "low",
    pair(12, 5, 16),
    ["imperial stout", "bottle", "english", "room temp", "rich"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_080", "La Trappe Quadrupel", "beer", "belgian quadrupel",
    "La Trappe", 10.0, "Tilburg, Netherlands",
    "Deep amber Trappist ale. Rich scent of dark fruits complemented by caramel, vanilla and subtle nutty undertones. Warming and smooth with faint yeast notes, sweet dates and caramel balanced by hop bitterness. Velvety texture, long-lasting finish.",
    ["dark fruits", "caramel", "vanilla", "nutty", "dates"],
    "medium-high", "medium", "full", "long-lasting, gentle bitter", "medium",
    pair(5, 12, 16),
    ["quadrupel", "trappist", "bottle", "dutch", "complex"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_081", "Astra Special", "beer", "mixed beer",
    "Astra", 2.5, "Hamburg, Germany",
    "Lively mix from the neighbourhood made with Astra, cola and orange. With alcohol.",
    ["cola", "orange", "sweet", "fruity"],
    "high", "very low", "light", "sweet, refreshing", "medium-high",
    pair(6, 1, 4),
    ["mixed beer", "bottle", "german", "cola", "sweet"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_082", "Jopen Ongelovige Thomas", "beer", "belgian quadrupel",
    "Jopen", 10.0, "Haarlem, Netherlands",
    "Fresh hoppy quadrupel offering a whole bouquet of fruity aromas and malty caramel. 10% ABV.",
    ["fruity", "caramel", "malty", "hoppy", "complex"],
    "medium", "medium", "full", "hoppy, warming", "medium",
    pair(5, 12, 16),
    ["quadrupel", "bottle", "dutch", "hoppy", "strong"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_083", "Westmalle Trappist Dubbel", "beer", "belgian dubbel",
    "Westmalle", 7.0, "Westmalle, Belgium",
    "Belgian Trappist specialty. Rounded initial taste with silky malt blend, dry mouthfeel with honey cake, fig compote and cocoa powder. Refreshingly bitter finish of hay, grass and roasted chestnuts.",
    ["honey cake", "fig", "cocoa", "hay", "roasted chestnuts"],
    "medium-low", "medium", "medium-full", "dry, bitter, roasted", "medium",
    pair(5, 12, 21),
    ["dubbel", "trappist", "bottle", "belgian", "complex"],
    page=14
))

# FRUIT BEER (pages 14-16)
drinks.append(make_drink(
    "pub_beer_084", "Delirium Red Strong Fruit Beer", "beer", "fruit beer",
    "Huyghe", 8.5, "Melle, Belgium",
    "Deep dark red fruit beer. Soft fruity aroma with hints of almond and mildly sour cherries. Sweet and fruity flavour, smooth and velvety.",
    ["cherry", "almond", "sweet", "fruity", "velvety"],
    "high", "low", "medium", "smooth, velvety, sweet", "medium",
    pair(17, 6, 12),
    ["fruit beer", "bottle", "belgian", "cherry", "sweet"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_085", "Lindemans Apple Beer", "beer", "lambic - fruit",
    "Lindemans", 3.4, "Vlezenbeek, Belgium",
    "Hazy gold Lambic beer with strong apple fragrance, subtle buttery malt and caramel. Balanced green apple flavour, sour sweetness. Smooth crisp, refreshing finish.",
    ["green apple", "buttery malt", "caramel", "sour", "sweet"],
    "medium", "medium-low", "medium", "crisp, refreshing", "medium",
    pair(15, 6, 5),
    ["fruit beer", "lambic", "bottle", "belgian", "apple"],
    page=14
))

drinks.append(make_drink(
    "pub_beer_086", "Lindemans Cassis", "beer", "lambic - fruit",
    "Lindemans", 3.5, "Vlezenbeek, Belgium",
    "Deep reddish-purple Lambic beer. Dominant blackcurrant fragrance with subtle hints of oak and yeast. Sweet blackcurrant flavours, light acidity, dry woody finish.",
    ["blackcurrant", "oak", "yeast", "sweet", "dry"],
    "medium", "medium-low", "medium", "dry, woody", "medium",
    pair(17, 5, 12),
    ["fruit beer", "lambic", "bottle", "belgian", "blackcurrant"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_087", "Lindemans Kriek", "beer", "lambic - fruit",
    "Lindemans", 3.5, "Vlezenbeek, Belgium",
    "Deep red lambic beer with strong cherry fragrance, subtle hints of oak and yeast. Light acidity, dry woody finish.",
    ["cherry", "oak", "yeast", "sour", "dry"],
    "medium-low", "medium", "medium", "dry, woody, tart", "medium",
    pair(17, 5, 12),
    ["fruit beer", "lambic", "bottle", "belgian", "cherry"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_088", "Mongozo Exotic Banana Beer", "beer", "fruit beer",
    "Mongozo", 3.6, "Belgium",
    "Belgian fruit beer with Fairtrade banana. Ripe banana scent and sweet fruity flavour with subtle beer aftertaste. Gluten-free.",
    ["banana", "sweet", "fruity", "tropical"],
    "high", "very low", "medium", "sweet, fruity", "medium",
    pair(6, 17, 3),
    ["fruit beer", "bottle", "belgian", "banana", "fairtrade", "gluten-free"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_089", "Mongozo Exotic Mango", "beer", "fruit beer",
    "Mongozo", 3.6, "Belgium",
    "Belgian fruit beer with Fairtrade mango. Fresh mango scent and sweet fruity flavour with subtle beer aftertaste. Gluten-free.",
    ["mango", "sweet", "fruity", "tropical"],
    "high", "very low", "medium", "sweet, fruity", "medium",
    pair(6, 4, 14),
    ["fruit beer", "bottle", "belgian", "mango", "fairtrade", "gluten-free"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_090", "Mongozo Coconut", "beer", "fruit beer",
    "Mongozo", 3.6, "Belgium",
    "Belgian fruit beer with Fairtrade coconut. Exotic coconut scent and sweet fruity flavour with subtle beer aftertaste. Gluten-free.",
    ["coconut", "sweet", "exotic", "fruity"],
    "high", "very low", "medium", "sweet, fruity", "medium",
    pair(6, 4, 3),
    ["fruit beer", "bottle", "belgian", "coconut", "fairtrade", "gluten-free"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_091", "Rodenbach Fruitage", "beer", "fruit beer",
    "Rodenbach", 3.4, "Roeselare, Belgium",
    "Sweet and sour cherry-dominant fruit beer. Best way to refresh yourself on warm summer days.",
    ["cherry", "sweet", "sour", "refreshing"],
    "medium", "medium", "medium", "sweet-sour, refreshing", "medium",
    pair(17, 6, 15),
    ["fruit beer", "bottle", "belgian", "cherry", "summer"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_092", "Liefmans On The Rocks Fruitesse", "beer", "lambic - fruit",
    "Liefmans", 3.8, "Oudenaarde, Belgium",
    "Fruity, sweet and refreshingly tart. Top-fermented with special bacteria and cherries, second fermentation. Matured for 18 months in cellar.",
    ["cherry", "fruity", "sweet", "tart"],
    "medium", "medium", "medium", "sweet-tart, refreshing", "medium",
    pair(17, 6, 15),
    ["fruit beer", "lambic", "bottle", "belgian", "cherry"],
    page=15
))

drinks.append(make_drink(
    "pub_beer_093", "Boon Kriek Cherry Beer", "beer", "lambic - fruit",
    "Boon", 4.0, "Lembeek, Belgium",
    "Traditional Belgian Lambic fruit-beer, deep ruby red. Intense sour cherry aroma with hints of almond and subtle oak. Medium bodied, moderate carbonation, slightly dry finish.",
    ["sour cherry", "almond", "oak", "dry"],
    "medium-low", "medium", "medium", "slightly dry", "medium",
    pair(17, 12, 5),
    ["fruit beer", "lambic", "bottle", "belgian", "cherry"],
    page=15
))

# More Fruit Beer
drinks.append(make_drink(
    "pub_beer_094", "Rodenbach Alexander Cherry Red Ale", "beer", "flemish red ale",
    "Rodenbach", 5.6, "Roeselare, Belgium",
    "Flemish red-brown ale matured in oak casks for 2 years. Balanced sweet and sour cherry flavour with undertones of red currants, strawberries and a touch of oak.",
    ["cherry", "red currants", "strawberry", "oak", "sweet-sour"],
    "medium", "medium", "medium", "sweet-sour, oaky", "medium",
    pair(12, 5, 17),
    ["flemish red", "oak aged", "bottle", "belgian", "cherry"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_095", "Samuel Smith Organic Cherry Beer", "beer", "fruit beer",
    "Samuel Smith", 5.1, "Yorkshire, England",
    "Brewed in Yorkshire. Fruit beer combining prominent notes of sweet cherries with subtle hints of malt and yeast. Organic.",
    ["cherry", "malt", "yeast", "sweet"],
    "medium-high", "low", "medium", "sweet, malty", "medium",
    pair(6, 5, 15),
    ["fruit beer", "bottle", "english", "organic", "cherry"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_096", "Liefmans Kriek-Brut", "beer", "fruit beer",
    "Liefmans", 6.5, "Oudenaarde, Belgium",
    "Deep reddish brown Belgian fruit beer. Balanced slightly sweet and gently bitter cherry flavour with aromas of wood, almond and cherries with hint of yeast.",
    ["cherry", "wood", "almond", "yeast", "balanced"],
    "medium", "medium-low", "medium", "sweet-bitter, woody", "medium",
    pair(17, 12, 5),
    ["fruit beer", "bottle", "belgian", "cherry", "brut"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_097", "La Chouffe Cherry", "beer", "fruit beer",
    "La Chouffe", 8.0, "Achouffe, Belgium",
    "Combines La Chouffe with sour cherries. Hints of strawberry, almond, spices and sweet port wine. Full-bodied, sweet, lively with bitter note.",
    ["cherry", "strawberry", "almond", "spice", "port wine"],
    "medium-high", "medium", "medium-full", "sweet, lively, bitter", "medium",
    pair(5, 12, 17),
    ["fruit beer", "bottle", "belgian", "cherry", "strong"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_098", "Huyghe Red Strong Fruity", "beer", "fruit beer",
    "Huyghe", 8.0, "Melle, Belgium",
    "Delirium Red Strong Fruit Beer with generous helping of cherry. Fruity cherry flavor takes center stage.",
    ["cherry", "fruity", "sweet", "strong"],
    "high", "low", "medium-full", "sweet, fruity", "medium",
    pair(17, 12, 6),
    ["fruit beer", "bottle", "belgian", "cherry", "strong"],
    page=16
))

# Gluten Free beers
drinks.append(make_drink(
    "pub_beer_099", "Tennent's 1885 Lager Gluten Free", "beer", "gluten-free lager",
    "Tennent's", 5.0, "Glasgow, Scotland",
    "Clear pale gold gluten-free lager. Subtle malt sweetness with hint of grass and lemon. Moderately bitter with sweet dry finish.",
    ["malt", "grass", "lemon", "crisp"],
    "medium-low", "medium", "light-medium", "sweet, dry", "medium",
    pair(6, 0, 1),
    ["gluten-free", "lager", "bottle", "scottish", "crisp"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_100", "St. Peter's Cream Stout Gluten Free", "beer", "gluten-free stout",
    "St. Peter's", 6.5, "Suffolk, England",
    "Deep brown almost black gluten-free stout. Smooth roasted malt and coffee aroma with subtle chocolate sweetness and mild bitterness. Medium bodied, velvety slightly creamy finish.",
    ["roasted malt", "coffee", "chocolate", "velvety", "creamy"],
    "medium-low", "low", "medium", "velvety, creamy", "low",
    pair(5, 16, 12),
    ["gluten-free", "stout", "bottle", "english", "creamy"],
    page=16
))

drinks.append(make_drink(
    "pub_beer_101", "Jopen Hop Zij Met Ons IPA Gluten Free", "beer", "gluten-free india pale ale",
    "Jopen", 6.0, "Haarlem, Netherlands",
    "Golden clear Dutch gluten-free IPA. Intense tropical fruit flavour with citrus and pine notes, pronounced bitterness.",
    ["tropical fruit", "citrus", "pine", "bitter"],
    "low", "medium-high", "medium", "dry, bitter", "medium",
    pair(4, 8, 6),
    ["gluten-free", "ipa", "bottle", "dutch", "hoppy"],
    page=16
))

# IPA bottles (page 17)
drinks.append(make_drink(
    "pub_beer_102", "Duvel Tripel Hop Citra IPA", "beer", "belgian ipa",
    "Duvel Moortgat", 9.5, "Breendonk, Belgium",
    "Crisp bright golden Belgian IPA. Intense citrus aroma of grapefruit and lime with yeasty spiciness. Silky smooth, tropical with citrus notes, soft bitterness keeps it refreshing.",
    ["grapefruit", "lime", "yeasty", "spicy", "tropical"],
    "medium-low", "medium", "medium", "silky smooth, refreshing", "high",
    pair(4, 8, 14),
    ["ipa", "belgian", "bottle", "citrus", "strong"],
    page=17
))

drinks.append(make_drink(
    "pub_beer_103", "Fuller's India Pale Ale", "beer", "english ipa",
    "Fuller's Brewery", 5.3, "London, England",
    "Pale copper English IPA. Earthy and floral aroma, balanced toffee and biscuit sweetness, cut by resinous herbal hop bitterness and hints of orange peel spice.",
    ["earthy", "floral", "toffee", "biscuit", "orange peel"],
    "medium", "medium", "medium", "resinous, herbal", "medium",
    pair(16, 5, 6),
    ["ipa", "english", "bottle", "traditional", "balanced"],
    page=17
))

drinks.append(make_drink(
    "pub_beer_104", "St Austell Big Job Double IPA", "beer", "double ipa",
    "St Austell Brewery", 7.2, "Cornwall, England",
    "Intense citrusy deep golden double IPA. Bold hop bitter flavour layered with orange and pineapple, pine resin and solid caramel malt. Full bodied, smooth, warm finish with hoppy dryness.",
    ["orange", "pineapple", "pine resin", "caramel", "hoppy"],
    "medium", "high", "full", "warm, hoppy, dry", "medium",
    pair(4, 8, 16),
    ["double ipa", "bottle", "english", "bold", "hoppy"],
    page=17
))

drinks.append(make_drink(
    "pub_beer_105", "Enigma Lupulin Monster", "beer", "double ipa",
    "Enigma", 7.0, "Belgium",
    "Hoppy double IPA, deep amber gold. Tropical mango, passion fruit and citrus aroma with hint of pine and resin. Full bodied, smooth with creamy hoppy bitterness.",
    ["tropical", "mango", "passion fruit", "citrus", "pine"],
    "low", "high", "full", "creamy, hoppy, bitter", "medium",
    pair(4, 8, 14),
    ["double ipa", "bottle", "belgian", "hoppy", "tropical"],
    page=17
))

drinks.append(make_drink(
    "pub_beer_106", "Jopen Super Dupa Beer", "beer", "india pale ale",
    "Jopen", 5.5, "Haarlem, Netherlands",
    "Bright tropical IPA, zesty at first sip with pine resin and gentle bitterness balancing passion fruit and guava fruitiness. Smooth carbonation, clean dry finish.",
    ["passion fruit", "guava", "pine resin", "zesty", "tropical"],
    "low", "medium", "medium", "clean, dry", "medium",
    pair(4, 8, 14),
    ["ipa", "bottle", "dutch", "tropical", "smooth"],
    page=17
))

drinks.append(make_drink(
    "pub_beer_107", "Enigma Hopnytized Double IPA", "beer", "double ipa",
    "Enigma", 9.0, "Belgium",
    "Grapefruit and pineapple notes dominate, with mango and peach aromas. Kveik yeast makes it sparkling and particularly refreshing chilled.",
    ["grapefruit", "pineapple", "mango", "peach", "sparkling"],
    "low", "medium-high", "medium-full", "refreshing, sparkling", "medium-high",
    pair(4, 8, 14),
    ["double ipa", "bottle", "belgian", "kveik", "fruity"],
    page=18
))

# LAGER bottles (page 18)
drinks.append(make_drink(
    "pub_beer_108", "Corona Extra", "beer", "mexican lager",
    "Grupo Modelo", 4.6, "Mexico City, Mexico",
    "Pale Mexican lager, straw yellow. Light malt sweetness with subtle cereal notes. Crisp clean slightly sweet with gentle hop bitterness. Light bodied, easy to drink.",
    ["cereal", "malt", "crisp", "clean"],
    "medium-low", "low", "light", "crisp, clean", "medium-high",
    pair(6, 8, 1),
    ["lager", "bottle", "mexican", "crisp", "refreshing"],
    page=18
))

drinks.append(make_drink(
    "pub_beer_109", "Desperados", "beer", "flavoured lager",
    "Heineken", 6.0, "France",
    "World's first tequila flavoured beer. Pale golden lager, sweet malt and subtle citrus aroma with distinctive tequila note. Crisp and refreshing.",
    ["tequila", "malt", "citrus", "crisp"],
    "medium", "low", "light", "crisp, refreshing", "medium",
    pair(6, 8, 4),
    ["lager", "bottle", "french", "tequila", "flavoured"],
    page=18
))

drinks.append(make_drink(
    "pub_beer_110", "Astra Kleine Freiheit Helles", "beer", "helles lager",
    "Astra", 5.1, "Hamburg, Germany",
    "Helles Lager brewed in Hamburg. Bright clear pale straw. Light balanced malt aroma with touch of bitterness. Light bodied, very easy to drink.",
    ["malt", "balanced", "light", "clean"],
    "low", "low", "light", "clean, easy", "medium",
    pair(6, 1, 2),
    ["helles", "bottle", "german", "hamburg", "easy drinking"],
    page=18
))

# NEIPA (page 18)
drinks.append(make_drink(
    "pub_beer_111", "Jopen Blurred Lines", "beer", "new england ipa",
    "Jopen", 5.3, "Haarlem, Netherlands",
    "Dutch hazy golden IPA. Juicy tropical fruit aroma of mango and passion fruit, layered with soft herbal happiness. Medium bodied, smooth, easy drinking.",
    ["mango", "passion fruit", "herbal", "juicy", "smooth"],
    "medium", "medium-low", "medium", "smooth, easy", "medium",
    pair(4, 14, 6),
    ["neipa", "bottle", "dutch", "hazy", "juicy"],
    page=18
))

# PALE ALE (page 18)
drinks.append(make_drink(
    "pub_beer_112", "Adnams Ghost Ship Pale Ale", "beer", "english pale ale",
    "Adnams", 4.5, "Southwold, England",
    "Originally Halloween seasonal English Pale Ale. Amber with citrus and tropical fruit aroma, balanced with light biscuity malt. Bright citrus and tropical flavour, clean moderate bitterness.",
    ["citrus", "tropical", "biscuity", "clean", "balanced"],
    "medium-low", "medium", "medium", "clean, moderate bitter", "medium",
    pair(6, 4, 5),
    ["pale ale", "bottle", "english", "citrus", "session"],
    page=18
))

# PILS (page 19)
drinks.append(make_drink(
    "pub_beer_113", "Grolsch Premium Pilsner", "beer", "pilsner",
    "Grolsch", 5.0, "Enschede, Netherlands",
    "Traditional Pilsner style beer from Netherlands. Pale golden clear, light malt sweet aroma with floral hoppy flavour. Crisp and clean, easy to drink.",
    ["malt", "floral", "hoppy", "crisp"],
    "low", "medium", "light-medium", "crisp, clean", "medium",
    pair(6, 0, 18),
    ["pilsner", "bottle", "dutch", "crisp", "traditional"],
    page=19
))

# STOUT (page 19)
drinks.append(make_drink(
    "pub_beer_114", "Belhaven Black Scottish Stout", "beer", "scottish stout",
    "Belhaven", 4.2, "Dunbar, Scotland",
    "Scottish Stout bursting with roast coffee and chocolate flavours. Lightly bitter finish. Deep black, velvety texture. Roasted aroma of malt and chocolate with faint smoky note.",
    ["roast coffee", "chocolate", "smoky", "velvety"],
    "low", "medium-low", "medium-full", "lightly bitter, velvety", "low",
    pair(5, 16, 12),
    ["stout", "bottle", "scottish", "roasted", "velvety"],
    page=19
))

drinks.append(make_drink(
    "pub_beer_115", "Samuel Smith Organic Chocolate Stout", "beer", "stout",
    "Samuel Smith", 5.0, "Yorkshire, England",
    "Deep brown Yorkshire stout. Rich roasted malt and dark chocolate aroma with gentle sweetness and subtle coffee flavour. Medium bodied, velvety, very indulgent.",
    ["dark chocolate", "roasted malt", "coffee", "velvety", "indulgent"],
    "medium", "low", "medium", "velvety, sweet", "low",
    pair(12, 5, 16),
    ["stout", "bottle", "english", "organic", "chocolate"],
    page=19
))

drinks.append(make_drink(
    "pub_beer_116", "Harvey Imperial Extra Double Stout", "beer", "imperial stout",
    "Harvey's", 9.0, "Lewes, England",
    "Deep black stout served at room temperature. Rich roasted malt and dark chocolate aroma with espresso notes. Full bodied, intense with layers of coffee, dark chocolate and caramel. Heavy velvety finish.",
    ["espresso", "dark chocolate", "caramel", "roasted malt", "intense"],
    "medium", "medium-high", "full", "heavy, velvety", "low",
    pair(12, 5, 16),
    ["imperial stout", "bottle", "english", "room temp", "intense"],
    page=19
))

drinks.append(make_drink(
    "pub_beer_117", "O'Hara's Irish Stout", "beer", "irish stout",
    "O'Hara's", 4.3, "Carlow, Ireland",
    "Dry roasted malt impression with full-bodied mouthfeel. Notes of espresso and typical island hop Fuggles dominate the flavour.",
    ["espresso", "roasted malt", "dry", "hoppy"],
    "low", "medium", "medium-full", "dry, roasted", "medium",
    pair(5, 16, 21),
    ["stout", "bottle", "irish", "roasted", "dry"],
    page=19
))

drinks.append(make_drink(
    "pub_beer_118", "Orkney Brewery Dragonhead Stout", "beer", "scottish stout",
    "Orkney Brewery", 4.0, "Orkney, Scotland",
    "Brimming with rich roast malt and roast barley flavours. Aromas of bitter chocolate, roast coffee and spicy dark fruits complemented by complex bitter blend of hop varieties.",
    ["bitter chocolate", "roast coffee", "dark fruits", "spicy", "complex"],
    "low", "medium-high", "medium", "complex, bitter", "medium",
    pair(5, 16, 12),
    ["stout", "bottle", "scottish", "roasted", "complex"],
    page=19
))

# WEIZEN (page 20)
drinks.append(make_drink(
    "pub_beer_119", "Maisel's Weisse Original", "beer", "hefeweizen",
    "Maisel's", 5.2, "Bayreuth, Germany",
    "Classic German wheat beer. Hazy golden orange, aroma of banana, clove and malt sweetness. Soft banana flavour followed by subtle citrus and clean finish. Medium bodied, refreshing.",
    ["banana", "clove", "malt", "citrus", "refreshing"],
    "medium", "low", "medium", "clean, refreshing", "medium-high",
    pair(6, 21, 1),
    ["weizen", "bottle", "german", "wheat", "classic"],
    page=20
))

drinks.append(make_drink(
    "pub_beer_120", "Jopen Witte Kerst", "beer", "dubbel witbier",
    "Jopen", 7.5, "Haarlem, Netherlands",
    "Dubbel Witbier brewed for the festive season. More malts, more alcohol, more color, more flavour, more enjoyment. Full bodied big Wit.",
    ["spicy", "malty", "fruity", "festive", "full-bodied"],
    "medium", "medium-low", "medium-full", "full, warming", "medium",
    pair(5, 12, 16),
    ["witbier", "bottle", "dutch", "festive", "christmas"],
    page=20
))

# CANNED BEER (pages 21-24)
drinks.append(make_drink(
    "pub_beer_121", "Brewski Pub Ale", "beer", "english ale",
    "Brewski", 3.4, "Sweden",
    "Traditional Ale, amber-copper. Light malt sweetness and subtle biscuity aroma, floral hops. Mild caramel flavours and gentle bitterness.",
    ["malt", "biscuity", "floral", "caramel", "gentle"],
    "medium-low", "low", "medium", "gentle, bitter", "medium",
    pair(6, 5, 21),
    ["ale", "can", "swedish", "session", "traditional"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_122", "Sierra Nevada Hazy Little Thing", "beer", "new england ipa",
    "Sierra Nevada", 6.7, "California, USA",
    "Hazy golden-orange New England IPA. Tropical fruit and citrus aroma, juicy mango and pineapple flavour, balanced by mild malt sweetness and soft bitterness.",
    ["mango", "pineapple", "citrus", "juicy", "tropical"],
    "medium", "medium-low", "medium", "soft, juicy", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "american", "hazy", "juicy"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_123", "O'Hara's White Haze IPA", "beer", "new england ipa",
    "O'Hara's", 5.0, "Carlow, Ireland",
    "Cloudy foggy hazy IPA, bright golden hues. Masterful combination of Citra, Mosaic and Amarillo hops. Modern brewing meets traditional craftsmanship.",
    ["citrus", "tropical", "mosaic", "citra", "hazy"],
    "medium-low", "medium", "medium", "smooth, hoppy", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "irish", "hazy", "craft"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_124", "Beak Parade IPA", "beer", "new england ipa",
    "Beak Brewery", 6.0, "Lewes, England",
    "London Fog IPA saturated in Citra, Mosaic and Idaho 7. Brimming with fruit bubblegum flavours of mango, orange peel, pineapple and ripe flat peaches.",
    ["mango", "orange peel", "pineapple", "peach", "bubblegum"],
    "medium", "medium", "medium", "fruity, juicy", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "english", "hazy", "fruity"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_125", "Beak Peach Hazy IPA", "beer", "new england ipa",
    "Beak Brewery", 6.5, "Lewes, England",
    "Brewed with Peacharine hops from Freestyle Hops. Intense notes of stone fruit, nectarine, lime zest and mandarin.",
    ["stone fruit", "nectarine", "lime zest", "mandarin", "peach"],
    "medium", "medium", "medium", "fruity, juicy", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "english", "hazy", "peach"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_126", "Siren Soundwave IPA", "beer", "india pale ale",
    "Siren Craft Brew", 5.6, "Reading, England",
    "Hoppy IPA with tropical mango aromas and refreshing citrus notes. Delicate tart accents frame this extremely delicate IPA. Wonderfully tart and dry finish.",
    ["tropical", "mango", "citrus", "tart", "dry"],
    "low", "medium", "medium", "tart, dry", "medium",
    pair(4, 8, 6),
    ["ipa", "can", "english", "tropical", "craft"],
    page=21
))

drinks.append(make_drink(
    "pub_beer_127", "Recraft Vermont IPA", "beer", "specialty ipa",
    "Recraft", 5.9, "Poland",
    "BW-17 'BioWar' project with lower bitterness but very intense fruity aroma. Extremely refreshing, smooth and juicy. Silver medal at Good Beer competition.",
    ["fruity", "smooth", "juicy", "refreshing"],
    "medium", "medium-low", "medium", "smooth, juicy", "medium",
    pair(4, 8, 14),
    ["ipa", "can", "polish", "award-winning", "juicy"],
    page=22
))

drinks.append(make_drink(
    "pub_beer_128", "Troublebrewing Vietnow", "beer", "india pale ale",
    "Trouble Brewing", 5.5, "Ireland",
    "IPA with harmonious composition of tropical fruits, citrus notes and subtle resinousness. Fresh wave of tropical fruits, pleasantly balanced bitterness.",
    ["tropical fruits", "citrus", "resinous", "balanced"],
    "low", "medium", "medium", "balanced, bitter", "medium",
    pair(4, 8, 14),
    ["ipa", "can", "irish", "tropical", "craft"],
    page=22
))

drinks.append(make_drink(
    "pub_beer_129", "Tankbusters Alone in Space", "beer", "new england ipa",
    "Tankbusters", 6.1, "Poland",
    "Intense fruitiness with pleasantly smooth texture from wheat and oat malt. Galaxy and El Dorado hops bring tropical aromas and subtle resinousness without being too bitter.",
    ["tropical", "fruity", "smooth", "resinous", "velvety"],
    "medium", "medium-low", "medium", "smooth, velvety", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "polish", "tropical", "craft"],
    page=22
))

drinks.append(make_drink(
    "pub_beer_130", "Tankbusters Heck'n Slash", "beer", "west coast ipa",
    "Tankbusters", 6.0, "Poland",
    "Strong bitterness and typical West Coast aromas – pine needles and tropical fruits. Refreshing freshness. For lovers of hop bitterness and rustic yet modern West Coast IPA.",
    ["pine needles", "tropical fruits", "bitter", "refreshing"],
    "low", "high", "medium", "bitter, piney", "medium",
    pair(4, 8, 6),
    ["west coast ipa", "can", "polish", "bitter", "craft"],
    page=22
))

# Gluten-free cans
drinks.append(make_drink(
    "pub_beer_131", "Brewdog Punk IPA Gluten Free", "beer", "gluten-free india pale ale",
    "BrewDog", 5.4, "Ellon, Scotland",
    "Popular classic in gluten-free version. Light golden with slight haze, bold cereal malt aroma with tropical fruit flavours. Caramel sweetness, crisp bitterness.",
    ["cereal malt", "tropical fruit", "caramel", "crisp"],
    "medium", "medium", "medium", "crisp, bitter", "medium",
    pair(4, 8, 6),
    ["gluten-free", "ipa", "can", "scottish", "craft"],
    page=22
))

drinks.append(make_drink(
    "pub_beer_132", "Vocation Heart and Soul", "beer", "gluten-free india pale ale",
    "Vocation Brewery", 4.4, "Hebden Bridge, England",
    "Gluten-free IPA, clear pale gold. Intense citrus and tropical fruit aroma with grapefruit, passion fruit and mango. Mild bitterness, clean dry finish.",
    ["citrus", "grapefruit", "passion fruit", "mango", "tropical"],
    "low", "medium", "medium", "clean, dry", "medium",
    pair(4, 8, 14),
    ["gluten-free", "ipa", "can", "english", "craft"],
    page=22
))

drinks.append(make_drink(
    "pub_beer_133", "Siren Lumina", "beer", "gluten-free session ipa",
    "Siren Craft Brew", 4.2, "Reading, England",
    "Hoppy aromas of mango and pineapple. Explosive flavour, flashes of delicate citrus highlights, refreshing balanced bitterness. Pillowy soft mouthfeel, light haze.",
    ["mango", "pineapple", "citrus", "soft", "balanced"],
    "low", "medium", "medium", "soft, balanced", "medium",
    pair(4, 8, 14),
    ["gluten-free", "session ipa", "can", "english", "craft"],
    page=22
))

# Sour cans
drinks.append(make_drink(
    "pub_beer_134", "BRLO Berliner Weisse", "beer", "berliner weisse",
    "BRLO", 4.0, "Berlin, Germany",
    "Refreshing sour beer, slightly hazy. Lightly tart aroma with hints of green apple, lemon and wheat malt. Crisp refreshing with bright citrus and sour notes balanced by soft malt sweetness.",
    ["green apple", "lemon", "wheat malt", "tart", "crisp"],
    "low", "medium-high", "light", "crisp, sour, refreshing", "medium-high",
    pair(6, 0, 15),
    ["sour", "can", "german", "berlin", "refreshing"],
    page=23
))

drinks.append(make_drink(
    "pub_beer_135", "Vault City Raspberry Sour", "beer", "sour",
    "Vault City", 5.0, "Edinburgh, Scotland",
    "Bold, tart and juicy modern sour beer. Jam-packed with intense fruit aromas and flavour on a delicate sour finish from house mixed culture. Vegan friendly.",
    ["raspberry", "tart", "juicy", "fruity", "bold"],
    "low", "high", "medium", "sour, fruity", "medium",
    pair(17, 15, 6),
    ["sour", "can", "scottish", "raspberry", "vegan"],
    page=23
))

drinks.append(make_drink(
    "pub_beer_136", "Vault City Strawberry Sunday", "beer", "sour",
    "Vault City", 5.0, "Edinburgh, Scotland",
    "Mouth-watering flavours of traditional strawberries and cream with addition of lactose and smooth vanilla.",
    ["strawberry", "cream", "vanilla", "smooth", "sweet"],
    "medium", "medium-low", "medium", "smooth, creamy", "medium",
    pair(17, 5, 12),
    ["sour", "can", "scottish", "strawberry", "lactose"],
    page=23
))

drinks.append(make_drink(
    "pub_beer_137", "Vault City Cloudy Lemonade", "beer", "sour",
    "Vault City", 4.2, "Edinburgh, Scotland",
    "Tart and refreshing Cloudy Lemonade bursting with citrus from fresh lemon juice and zest. Zingy mixed fermentation base, vegan friendly, light and crushable session sour.",
    ["lemon", "citrus", "zingy", "tart", "refreshing"],
    "low", "high", "light", "tart, zesty, refreshing", "medium-high",
    pair(6, 15, 0),
    ["sour", "can", "scottish", "lemonade", "vegan"],
    page=23
))

# Pale Ale cans
drinks.append(make_drink(
    "pub_beer_138", "Troublebrewing Ambush", "beer", "pale ale",
    "Trouble Brewing", 5.0, "Ireland",
    "Deep hazy gold with large white head. Mango, fluffy clouds and pineapple on nose and taste. Soft texture, very subtle dryness. Pair with burritos, Hawaiian pizza or summer salad.",
    ["mango", "pineapple", "soft", "hazy", "tropical"],
    "medium", "medium-low", "medium", "soft, subtle dry", "medium",
    pair(4, 8, 14),
    ["pale ale", "can", "irish", "tropical", "craft"],
    page=23
))

drinks.append(make_drink(
    "pub_beer_139", "Tankbusters Hall of Fame", "beer", "pale ale",
    "Tankbusters", 5.5, "Poland",
    "Tropical aromas of pineapple, citrus and hint of coconut from Citra, Mosaic and Sabro hops. Wheat malt, oat malt and wheat flakes ensure smooth texture and well-rounded experience.",
    ["pineapple", "citrus", "coconut", "tropical", "smooth"],
    "medium", "medium-low", "medium", "smooth, well-rounded", "medium",
    pair(4, 8, 14),
    ["pale ale", "can", "polish", "tropical", "craft"],
    page=23
))

# NEIPA cans
drinks.append(make_drink(
    "pub_beer_140", "Tankbusters Paris Delight", "beer", "new england ipa",
    "Tankbusters", 5.2, "Poland",
    "Tropical freshness of pineapple enveloped in delicate sweetness. Lime and lychee provide pleasant fruity acidity. Oat flakes and wheat malt for full-bodied texture and juicy mouthfeel.",
    ["pineapple", "lime", "lychee", "fruity", "juicy"],
    "medium", "medium-low", "medium-full", "juicy, fruity", "medium",
    pair(4, 8, 14),
    ["neipa", "can", "polish", "tropical", "craft"],
    page=24
))

# DIPA cans
drinks.append(make_drink(
    "pub_beer_141", "Tankbusters Lizzard King", "beer", "double ipa",
    "Tankbusters", 7.5, "Poland",
    "Fresh mandarin and juicy passion fruit with soft almost creamy texture. Complex tropical notes of mango, citrus and hint of resinousness from Columbus, Chinook and Kohia Nelson hops.",
    ["mandarin", "passion fruit", "mango", "citrus", "resinous"],
    "medium", "medium", "medium-full", "soft, creamy, hoppy", "medium",
    pair(4, 8, 14),
    ["double ipa", "can", "polish", "tropical", "craft"],
    page=24
))

# Alcohol-free cans
drinks.append(make_drink(
    "pub_beer_142", "Northern Monk Holy Faith", "beer", "non-alcoholic pale ale",
    "Northern Monk", 0.5, "Leeds, England",
    "Rich hop notes of lemongrass, grapefruit and pine provide the corresponding power in flavour. Alcohol-free.",
    ["lemongrass", "grapefruit", "pine", "hoppy"],
    "low", "medium", "medium", "hoppy, refreshing", "medium",
    pair(4, 8, 6),
    ["alcohol-free", "pale ale", "can", "english", "craft"],
    page=24
))


# ── Now let's write them all out ──
for d in drinks:
    write_json(d)

print(f"Generated {len(drinks)} drink JSON files in '{OUT}/'")

# Count by category
from collections import Counter
cats = Counter(d['category'] for d in drinks)
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")
PYEOF