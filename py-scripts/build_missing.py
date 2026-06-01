#!/usr/bin/env python3
"""Build missing drink guide entries from pages 25-43 of Beer Menu.pdf (ciders, specials, clearance)."""

import json, os

OUT = "drink_guide"
os.makedirs(OUT, exist_ok=True)

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

BASE_META = {"source_page": 1, "extraction_confidence": 0.90, "verified_date": "2025-01-01"}

def pair(*indices):
    return [SNACKS[i] for i in indices]

PAIR_SALTY = pair(6, 0, 2)
PAIR_CHEESE = pair(5, 13, 12)
PAIR_MEATY = pair(16, 17, 18)
PAIR_SPICY = pair(4, 8, 9)
PAIR_SWEET = pair(6, 3, 4)      # Sea Salt, Honey BBQ, Sweet Chilli
PAIR_FRUITY = pair(6, 15, 17)    # Sea Salt, Cider Vinegar, Angus
PAIR_CIDER = pair(6, 15, 5)      # Sea Salt, Cider Vinegar, Cheddar
PAIR_NUTS = pair(21, 22, 20)       # Studentenfutter, Erdnüsse Gesalzen, Paprika
PAIR_CITRUS = pair(6, 15, 0)      # Sea Salt, Cider Vinegar, Balsamic Vinegar

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

drinks = []

# =============================================================================
# PAGE 25 ── CIDERS (BOTTLES)
# =============================================================================

drinks.append(make_drink(
    "pub_beer_153", "Magners Original Cider", "cider", "irish cider",
    "Magners", 4.5, "Clonmel, Ireland",
    "Ireland's favourite cider. Clear and golden with fresh apple and mild floral notes, balanced by a gentle acidity with a clean refreshing finish.",
    ["apple", "floral", "fresh", "clean", "balanced"],
    "medium", "very low", "light-medium", "clean, refreshing", "medium",
    PAIR_CIDER, ["cider", "irish", "bottle", "apple", "classic"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_154", "Magners Red Berries", "cider", "berry cider",
    "Magners", 4.5, "Clonmel, Ireland",
    "Ruby-red cider with a fresh red berry aroma and flavours of strawberry, raspberry and apple. Subtle sweetness and tart finish.",
    ["strawberry", "raspberry", "apple", "red berry", "tart"],
    "medium", "low", "medium", "tart, fruity", "medium",
    PAIR_SWEET, ["cider", "irish", "bottle", "berry", "fruity"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_155", "Magners Pear Cider", "cider", "pear cider",
    "Magners", 4.5, "Clonmel, Ireland",
    "Pale golden cider with a fresh pear aroma and sweet pear and apple flavours, balanced by a sweet acidity and smooth finish.",
    ["pear", "apple", "sweet", "smooth", "fresh"],
    "medium-high", "very low", "medium", "smooth, sweet", "medium",
    PAIR_SWEET, ["cider", "irish", "bottle", "pear", "fruity"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_156", "Toffee Apple Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Dessert-style cider with a rich sweet toffee and caramel flavour with hints of apple.",
    ["toffee", "caramel", "apple", "sweet", "dessert"],
    "high", "very low", "medium", "sweet, toffee, caramel", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "toffee", "sweet", "dessert"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_157", "Raspberry & Lime Cider", "cider", "flavoured cider",
    "Unknown", 3.4, "Unknown",
    "Sweet cider with a fresh raspberry flavour balanced by a hint of zesty lime and crisp apple undertones.",
    ["raspberry", "lime", "zesty", "apple", "sweet"],
    "medium-high", "low", "light-medium", "sweet, zesty, crisp", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "raspberry", "lime"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_158", "Apple & Pear Cider", "cider", "fruit cider",
    "Unknown", 4.0, "Unknown",
    "Sweet cider with a fresh apple and pear flavour and a refreshing finish.",
    ["apple", "pear", "sweet", "fresh", "refreshing"],
    "high", "very low", "light-medium", "refreshing, sweet", "medium",
    PAIR_SWEET, ["cider", "fruit", "bottle", "apple", "pear"],
    page=25
))

drinks.append(make_drink(
    "pub_beer_159", "Raspberry & Blackberry Cider", "cider", "berry cider",
    "Unknown", 4.0, "Unknown",
    "Deep ruby-red coloured sweet cider tasting like ripe raspberries and blackberries.",
    ["raspberry", "blackberry", "ripe", "sweet", "berry"],
    "high", "very low", "medium", "sweet, berry", "medium",
    PAIR_SWEET, ["cider", "berry", "bottle", "raspberry", "blackberry"],
    page=25
))

# =============================================================================
# PAGE 26 ── CIDERS (continued)
# =============================================================================

drinks.append(make_drink(
    "pub_beer_160", "Orange & Lemon Cider", "cider", "citrus cider",
    "Unknown", 4.0, "Unknown",
    "Sweet cider with a fresh citrus orange flavour with a punch of zesty lemon.",
    ["orange", "lemon", "citrus", "zesty", "sweet"],
    "medium-high", "low", "light", "zesty, citrus", "medium",
    PAIR_SWEET, ["cider", "citrus", "bottle", "orange", "lemon"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_161", "Rascal Cider", "cider", "berry cider",
    "Unknown", 4.5, "Unknown",
    "Full-bodied amber cider with a sweet red berry aroma of strawberry layered with crisp apple.",
    ["strawberry", "apple", "red berry", "crisp", "sweet"],
    "medium-high", "very low", "medium-full", "crisp, fruity", "medium",
    PAIR_CIDER, ["cider", "berry", "bottle", "amber", "strawberry"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_162", "Gold Cider", "cider", "apple cider",
    "Unknown", 4.8, "Unknown",
    "Bright golden crisp apple cider with subtle honey and floral notes and a balanced sweetness with a clean tart finish.",
    ["apple", "honey", "floral", "crisp", "tart"],
    "medium", "low", "medium", "clean, tart, crisp", "medium",
    PAIR_CIDER, ["cider", "apple", "bottle", "golden", "crisp"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_163", "Haze Cider", "cider", "apple & pear cider",
    "Unknown", 4.5, "Unknown",
    "Hazy amber orange, this juicy apple and pear cider is smooth and fruity with a gentle tartness.",
    ["apple", "pear", "juicy", "smooth", "tart"],
    "medium", "low", "medium", "smooth, tart, juicy", "medium",
    PAIR_CIDER, ["cider", "fruit", "bottle", "hazy", "juicy"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_164", "Rosé Sweet Sparkling Cider", "cider", "sparkling rosé cider",
    "Unknown", 4.5, "Unknown",
    "Pale pink sparkling cider with sweet red berry and apple notes with a smooth finish and light fizz.",
    ["red berry", "apple", "sweet", "sparkling", "smooth"],
    "medium-high", "very low", "light", "smooth, light fizz", "medium-high",
    PAIR_SWEET, ["cider", "rosé", "bottle", "sparkling", "berry"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_165", "Blood Orange Cider", "cider", "citrus cider",
    "Unknown", 4.0, "Unknown",
    "Bright orange cider with a zesty blood orange flavour with a hint of apple sweetness.",
    ["blood orange", "apple", "zesty", "citrus", "sweet"],
    "medium", "low", "light", "zesty, citrus, sweet", "medium",
    PAIR_SWEET, ["cider", "citrus", "bottle", "blood orange", "zesty"],
    page=26
))

drinks.append(make_drink(
    "pub_beer_166", "Thatcher's Apple & Blackcurrant", "cider", "fruit cider",
    "Thatcher's", 4.0, "Somerset, England",
    "Rich, refreshingly fruity cider made from the sweetest dessert apples, with a fresh berry aroma and strong natural blackcurrant flavour. Rich and fruity perfection.",
    ["blackcurrant", "apple", "berry", "fruity", "rich"],
    "medium-high", "very low", "medium", "rich, fruity", "medium",
    PAIR_CIDER, ["cider", "fruit", "bottle", "english", "blackcurrant"],
    page=26
))

# =============================================================================
# PAGE 27 ── CIDERS (continued)
# =============================================================================

drinks.append(make_drink(
    "pub_beer_167", "Gladiator Cider", "cider", "strong cider",
    "Unknown", 8.4, "Unknown",
    "Strong rustic cider with a deep golden colour and strong apple character with a subtle fruity undertone.",
    ["apple", "strong", "rustic", "fruity", "golden"],
    "medium-low", "medium", "medium-full", "strong, rustic, apple", "medium",
    PAIR_MEATY, ["cider", "strong", "bottle", "rustic", "apple"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_168", "Colider", "cider", "flavoured cider",
    "Unknown", 3.4, "Unknown",
    "Sweet blend of apples and cola, creating a distinct balanced sweet taste with a tangy twist.",
    ["cola", "apple", "sweet", "tangy", "unique"],
    "high", "very low", "light-medium", "sweet, tangy", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "cola", "sweet"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_169", "Passion Fruit Martini Cider", "cider", "flavoured cider",
    "Unknown", 3.4, "Unknown",
    "Tropical passion fruit and hints of citrus and apple are the key flavours of this slightly hazy cider.",
    ["passion fruit", "citrus", "apple", "tropical", "hazy"],
    "medium", "low", "light-medium", "tropical, fruity", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "passion fruit", "tropical"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_170", "Raspberry Lemonade Cider", "cider", "flavoured cider",
    "Unknown", 3.4, "Unknown",
    "Pink and lightly sparkling cider with sweet raspberry flavours balanced by a tangy lemon.",
    ["raspberry", "lemon", "tangy", "sweet", "sparkling"],
    "medium-high", "low", "light", "sweet, tangy, sparkling", "medium-high",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "raspberry", "lemon"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_171", "Apples & Pears Cider", "cider", "pear cider",
    "Unknown", 4.0, "Unknown",
    "Made from 88% pear and 12% apple. Sweet in taste with a delicious, almost exotic flavour.",
    ["pear", "apple", "sweet", "exotic", "delicious"],
    "high", "very low", "medium", "sweet, exotic", "medium",
    PAIR_SWEET, ["cider", "pear", "bottle", "sweet", "exotic"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_172", "Rhubarb Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Refreshing apple cider infused with rhubarb juice with a crisp clean finish.",
    ["rhubarb", "apple", "crisp", "clean", "refreshing"],
    "medium", "low", "light-medium", "crisp, clean, rhubarb", "medium",
    PAIR_CIDER, ["cider", "flavoured", "bottle", "rhubarb", "crisp"],
    page=27
))

drinks.append(make_drink(
    "pub_beer_173", "Rhubarb & Mango Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Refreshing apple cider infused with rhubarb and mango juice with a sweet tropical twist.",
    ["rhubarb", "mango", "apple", "tropical", "sweet"],
    "medium-high", "very low", "light-medium", "sweet, tropical, crisp", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "rhubarb", "mango", "tropical"],
    page=27
))

# =============================================================================
# PAGE 28 ── CIDERS (continued)
# =============================================================================

drinks.append(make_drink(
    "pub_beer_174", "Low Alcohol Apple Cider", "cider", "low-alcohol cider",
    "Unknown", 0.5, "Unknown",
    "Crafted from home grown, fresh pressed cider apples, this low alcohol option has a sweet but fresh flavour.",
    ["apple", "sweet", "fresh", "crisp", "clean"],
    "medium-high", "very low", "light", "sweet, fresh", "medium",
    PAIR_CIDER, ["cider", "low-alcohol", "bottle", "apple", "fresh"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_175", "Mango & Lime Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Refreshing apple cider infused with tropical mango juice with zesty lime twists.",
    ["mango", "lime", "apple", "tropical", "zesty"],
    "medium-high", "low", "light-medium", "tropical, zesty, sweet", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "mango", "lime", "tropical"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_176", "Orange & Pineapple Cider", "cider", "flavoured cider",
    "Unknown", 3.4, "Unknown",
    "Tropical blend of orange and pineapple juices infused into fresh apple cider for an exotic but refreshing finish.",
    ["orange", "pineapple", "apple", "tropical", "exotic"],
    "medium-high", "very low", "light-medium", "exotic, refreshing", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "orange", "pineapple"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_177", "Raspberry Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Refreshing apple cider infused with bright crushed raspberries with a sweet fruity twist.",
    ["raspberry", "apple", "bright", "sweet", "fruity"],
    "high", "very low", "light-medium", "sweet, raspberry", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "raspberry", "fruity"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_178", "Strawberry Daiquiri Cider", "cider", "cocktail-inspired cider",
    "Unknown", 3.4, "Unknown",
    "Cocktail-inspired cider combining the flavours of juicy strawberries, limes and a subtle rum note.",
    ["strawberry", "lime", "rum", "sweet", "cocktail"],
    "medium-high", "very low", "medium", "sweet, cocktail-inspired", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "cocktail", "strawberry", "daiquiri"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_179", "Cosmo Cider", "cider", "cocktail-inspired cider",
    "Unknown", 3.4, "Unknown",
    "Cocktail-inspired cider combining the flavours of cranberries and a squeeze of lime.",
    ["cranberry", "lime", "sweet", "tart", "cocktail"],
    "medium", "medium-low", "light", "cranberry, lime", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "cocktail", "cosmo", "cranberry"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_180", "Pornstar Martini Cider", "cider", "cocktail-inspired cider",
    "Unknown", 4.0, "Unknown",
    "Cocktail-inspired cider combining the flavours of passion fruit and vanilla.",
    ["passion fruit", "vanilla", "sweet", "tropical", "cocktail"],
    "medium-high", "very low", "medium", "sweet, vanilla, tropical", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "cocktail", "passion fruit", "vanilla"],
    page=28
))

drinks.append(make_drink(
    "pub_beer_181", "Mango Daiquiri Cider", "cider", "cocktail-inspired cider",
    "Unknown", 3.4, "Unknown",
    "Cocktail-inspired cider combining the flavours of juicy mango and pine with a rum twist.",
    ["mango", "pine", "rum", "tropical", "cocktail"],
    "medium-high", "very low", "medium", "tropical, cocktail-inspired", "medium",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "cocktail", "mango", "daiquiri"],
    page=28
))

# =============================================================================
# PAGE 29 ── CIDERS (continued)
# =============================================================================

drinks.append(make_drink(
    "pub_beer_182", "Strawberry & Lime Cider", "cider", "flavoured cider",
    "Unknown", 4.0, "Unknown",
    "Fruity cider, sweet and fresh with a blend of strawberries and zesty limes. Lightly sparkling and smooth drinking experience.",
    ["strawberry", "lime", "sweet", "fresh", "zesty"],
    "medium-high", "very low", "light", "sweet, zesty, sparkling", "medium-high",
    PAIR_SWEET, ["cider", "flavoured", "bottle", "strawberry", "lime"],
    page=29
))

drinks.append(make_drink(
    "pub_beer_183", "Wild Berries Cider", "cider", "berry cider",
    "Unknown", 4.0, "Unknown",
    "Fruity cider, sweet and fresh with a blend of wild berries. Lightly sparkling and smooth drinking experience.",
    ["wild berries", "sweet", "fresh", "fruity", "smooth"],
    "high", "very low", "light", "sweet, berry, sparkling", "medium-high",
    PAIR_SWEET, ["cider", "berry", "bottle", "wild berries", "sweet"],
    page=29
))

drinks.append(make_drink(
    "pub_beer_184", "Holly Golightly Cider", "cider", "low-alcohol cider",
    "Unknown", 0.5, "Unknown",
    "Low alcohol cider, sweet and slightly acidic with a lingering apple aftertaste.",
    ["apple", "sweet", "slightly acidic", "light", "lingering"],
    "medium-high", "low", "light", "sweet, apple, lingering", "medium",
    PAIR_CIDER, ["cider", "low-alcohol", "bottle", "apple", "light"],
    page=29
))

drinks.append(make_drink(
    "pub_beer_185", "Magners Berry Cider", "cider", "berry cider",
    "Magners", 4.0, "Clonmel, Ireland",
    "Blend of red berries and apple, sweeter than Original with a clean lingering fruity finish.",
    ["red berries", "apple", "sweet", "fruity", "clean"],
    "high", "very low", "medium", "sweet, fruity, clean", "medium",
    PAIR_SWEET, ["cider", "irish", "bottle", "berry", "sweet"],
    page=29
))

# =============================================================================
# PAGE 30 ── SOMERSBY CANS
# =============================================================================

drinks.append(make_drink(
    "pub_beer_186", "Somersby Orange Spritz", "cider", "citrus cider",
    "Somersby", 4.5, "Denmark",
    "Sparkling cider with the taste of bittersweet oranges: refreshing combination of pleasant bitterness and fruity sweetness. Intense fruity orange aroma and light herbal notes. Pleasantly bitter with long-lasting sweetness and acidity.",
    ["orange", "bittersweet", "herbal", "fruity", "sparkling"],
    "medium", "medium-low", "light-medium", "bittersweet, long-lasting", "medium-high",
    PAIR_CIDER, ["cider", "can", "danish", "orange", "sparkling"],
    page=30
))

drinks.append(make_drink(
    "pub_beer_187", "Somersby Mango & Lime", "cider", "fruit cider",
    "Somersby", 4.5, "Denmark",
    "Refreshingly fruity cider with the taste of juicy-sweet mango and sparkling, slightly tart lime. Intense mango aromas with a hint of lime. Balanced between sweet and tart notes, long-lasting and refreshing.",
    ["mango", "lime", "sweet", "tart", "tropical"],
    "medium-high", "medium-low", "light-medium", "refreshing, tropical", "medium-high",
    PAIR_SWEET, ["cider", "can", "danish", "mango", "lime"],
    page=30
))

drinks.append(make_drink(
    "pub_beer_188", "Somersby Blackberry", "cider", "berry cider",
    "Somersby", 4.5, "Denmark",
    "Refreshing cider meets the intense flavor of blackberries. Mild sweetness and slightly tart notes create a true explosion of flavor. Long-lasting blackberry flavor, pleasant acidity, and lingering sweetness.",
    ["blackberry", "sweet", "tart", "berry", "intense"],
    "medium", "medium-low", "light-medium", "long-lasting, berry, tart", "medium-high",
    PAIR_SWEET, ["cider", "can", "danish", "blackberry", "berry"],
    page=30
))

# =============================================================================
# PAGE 31 ── OTHERS
# =============================================================================

drinks.append(make_drink(
    "pub_beer_189", "Apfel Räuber (Orchard Thieves)", "cider", "apple & raspberry cider",
    "Orchard Thieves", 4.5, "Ireland",
    "Light-bodied, fizzy cider with a pale golden colour with a touch of pink. Tastes of fresh green apples with bright raspberry sweetness. Balanced and refreshing.",
    ["green apple", "raspberry", "fizzy", "sweet", "refreshing"],
    "medium-high", "very low", "light", "balanced, refreshing", "high",
    PAIR_SWEET, ["cider", "can", "irish", "apple", "raspberry"],
    page=31
))

drinks.append(make_drink(
    "pub_beer_190", "Gwatkin Dry Oak Craft Cider", "cider", "oak-aged cider",
    "Gwatkin", 6.0, "Herefordshire, England",
    "Dry Oak Craft cider made using a blend of the finest Herefordshire cider apples laid down and matured in seasoned oak vats, combining the crisp flavour of the timber and the fruit.",
    ["oak", "apple", "dry", "crisp", "woody"],
    "low", "medium", "medium", "dry, oaky, crisp", "medium",
    PAIR_CIDER, ["cider", "oak aged", "bottle", "english", "craft", "dry"],
    page=31
))

drinks.append(make_drink(
    "pub_beer_191", "BRLO Wild Berries Cider", "cider", "berry cider",
    "BRLO", 4.5, "Berlin, Germany",
    "Tangy organic apple meets sweet wild berries. Fruity, dry finish with notes of blackberry and cherry.",
    ["wild berries", "blackberry", "cherry", "apple", "dry"],
    "medium", "medium", "medium", "fruity, dry", "medium",
    PAIR_CIDER, ["cider", "german", "bottle", "organic", "berry"],
    page=31
))

drinks.append(make_drink(
    "pub_beer_192", "BrewDog Hawkes Dead and Berried", "cider", "mixed berry cider",
    "BrewDog", 4.0, "Ellon, Scotland",
    "Packed to the rafters with blackberry, raspberry and blueberry, on a brisk dessert apple base. Fermented with wine yeast to delicately balance the sweet berry front. Deep, lush, dead drinkable.",
    ["blackberry", "raspberry", "blueberry", "apple", "lush"],
    "medium", "low", "medium", "deep, lush, fruity", "medium",
    PAIR_SWEET, ["cider", "scottish", "bottle", "berry", "craft"],
    page=31
))

drinks.append(make_drink(
    "pub_beer_193", "Samuel Smith Organic Cider", "cider", "organic apple cider",
    "Samuel Smith", 5.0, "Yorkshire, England",
    "Semi-dry cider with brilliant straw colour, light body, pure apple taste and a gentle apple blossom finish. Made in a small independent British brewery, the oldest in Yorkshire. Organic and gluten-free.",
    ["apple", "apple blossom", "semi-dry", "pure", "organic"],
    "medium-low", "low", "light", "gentle, apple blossom", "medium",
    PAIR_CIDER, ["cider", "english", "bottle", "organic", "gluten-free", "yorkshire"],
    page=31
))

# =============================================================================
# PAGE 35 ── ADDITIONAL SPIRITS (from Beer Menu)
# =============================================================================

# Many of these overlap with the spirits PDFs already processed,
# but some are unique to this page. Let me add spirits not yet covered.

spirits_page = 35

# Schnapps / Liqueurs
drinks.append(make_drink(
    "pub_spirit_001", "Ficken Schnapps", "spirit", "schnapps",
    "Ficken", 35.0, "Germany",
    "Popular German party schnapps with a bold, warming character.",
    ["herbal", "warming", "strong", "bold"],
    "medium", "medium", "full", "warming, bold", "none",
    PAIR_MEATY, ["schnapps", "german", "party", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_002", "Berliner Luft", "spirit", "peppermint liqueur",
    "Berliner Luft", 18.0, "Berlin, Germany",
    "Iconic Berlin peppermint liqueur. Cool, refreshing minty character perfect as a shot.",
    ["peppermint", "cool", "refreshing", "sweet", "minty"],
    "high", "very low", "light", "cool, minty", "none",
    PAIR_SWEET, ["liqueur", "german", "berlin", "mint", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_003", "Ketten Fett", "spirit", "herbal liqueur",
    "Ketten Fett", 35.0, "Germany",
    "German herbal liqueur with a distinctive warming character and complex spice notes.",
    ["herbal", "spicy", "warming", "complex"],
    "medium", "medium", "medium-full", "warming, herbal", "none",
    PAIR_MEATY, ["liqueur", "german", "herbal", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_004", "Bärenjäger", "spirit", "honey liqueur",
    "Bärenjäger", 33.0, "Germany",
    "German honey liqueur. Smooth, sweet and warming with rich floral honey notes.",
    ["honey", "floral", "sweet", "smooth", "warming"],
    "high", "very low", "medium", "smooth, honey, sweet", "none",
    PAIR_SWEET, ["liqueur", "german", "honey", "sweet", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_005", "Killerpitsch", "spirit", "herbal liqueur",
    "Killerpitsch", 35.0, "Germany",
    "Strong German herbal liqueur with bold, warming character. Popular party shot.",
    ["herbal", "strong", "warming", "bold"],
    "medium", "high", "full", "strong, warming, herbal", "none",
    PAIR_MEATY, ["liqueur", "german", "strong", "herbal", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_006", "BVB Bömsken Haselnuss", "spirit", "hazelnut liqueur",
    "BVB Bömsken", 20.0, "Germany",
    "German hazelnut liqueur. Sweet, nutty and smooth with rich roasted hazelnut flavour.",
    ["hazelnut", "nutty", "sweet", "smooth", "roasted"],
    "high", "very low", "medium", "sweet, nutty, smooth", "none",
    PAIR_NUTS, ["liqueur", "german", "hazelnut", "sweet", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_007", "Berentzen Maracuja", "spirit", "passion fruit liqueur",
    "Berentzen", 16.0, "Germany",
    "German passion fruit liqueur. Sweet, tropical and fruity with vibrant maracuja flavour.",
    ["passion fruit", "tropical", "sweet", "fruity", "vibrant"],
    "high", "very low", "light", "sweet, tropical, fruity", "none",
    PAIR_SWEET, ["liqueur", "german", "passion fruit", "fruity", "shot"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_008", "Prinz Hausschnaps Marille", "spirit", "apricot schnapps",
    "Prinz", 40.0, "Austria",
    "Traditional Austrian apricot schnapps. Clean, fruity spirit with bright apricot character.",
    ["apricot", "fruity", "clean", "bright"],
    "medium", "medium", "medium", "clean, fruity, warming", "none",
    PAIR_SWEET, ["schnapps", "austrian", "apricot", "fruit brandy"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_009", "Alpenschnaps Williams Birne", "spirit", "pear schnapps",
    "Alpenschnaps", 40.0, "Austria",
    "Traditional Austrian pear schnapps. Clean, fruity spirit with bright Williams pear character.",
    ["pear", "fruity", "clean", "bright", "smooth"],
    "medium", "medium", "medium", "clean, fruity, pear", "none",
    PAIR_SWEET, ["schnapps", "austrian", "pear", "fruit brandy"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_010", "Alpenschnaps Haselnuss", "spirit", "hazelnut schnapps",
    "Alpenschnaps", 35.0, "Austria",
    "Traditional Austrian hazelnut schnapps. Nutty, smooth and warming.",
    ["hazelnut", "nutty", "smooth", "warming"],
    "medium", "very low", "medium", "nutty, warming", "none",
    PAIR_NUTS, ["schnapps", "austrian", "hazelnut", "nutty"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_011", "Alpenschnaps Obstler", "spirit", "fruit schnapps",
    "Alpenschnaps", 40.0, "Austria",
    "Traditional Austrian fruit schnapps distilled from apples and pears. Clean, fruity and warming.",
    ["apple", "pear", "fruity", "clean", "warming"],
    "medium", "medium", "medium", "clean, fruity, warming", "none",
    PAIR_SWEET, ["schnapps", "austrian", "fruit", "obstler"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_012", "Echter Nordhäuser Doppelkorn", "spirit", "grain spirit",
    "Nordhäuser", 38.0, "Nordhausen, Germany",
    "Classic German double-distilled grain spirit from Nordhausen. Clean, neutral and warming.",
    ["grain", "clean", "neutral", "warming"],
    "very low", "medium", "medium", "clean, warming", "none",
    PAIR_MEATY, ["grain spirit", "german", "korn", "traditional"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_013", "Krämer Dortmunder Tropfen", "spirit", "herbal liqueur",
    "Krämer", 40.0, "Dortmund, Germany",
    "Traditional Dortmund herbal liqueur with complex botanical character and warming finish.",
    ["herbal", "botanical", "warming", "complex"],
    "medium", "medium-high", "medium-full", "warming, herbal, complex", "none",
    PAIR_MEATY, ["liqueur", "german", "dortmund", "herbal"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_014", "Licor 43", "spirit", "spanish liqueur",
    "Licor 43", 31.0, "Cartagena, Spain",
    "Golden Spanish liqueur made with 43 ingredients including citrus, vanilla, and aromatic herbs. Sweet, complex and versatile.",
    ["vanilla", "citrus", "herbal", "sweet", "complex"],
    "high", "very low", "medium-full", "sweet, complex, vanilla", "none",
    PAIR_SWEET, ["liqueur", "spanish", "vanilla", "citrus", "complex"],
    page=spirits_page
))

# Aperol, Limoncello, Ouzo, Ramazzotti etc. are also on this page
drinks.append(make_drink(
    "pub_spirit_015", "Ramazzotti Amaro", "spirit", "italian amaro",
    "Ramazzotti", 30.0, "Milan, Italy",
    "Classic Italian amaro with a bittersweet herbal profile. Orange peel, gentian and other botanicals.",
    ["orange peel", "herbal", "bittersweet", "gentian", "complex"],
    "medium", "medium-high", "medium", "bittersweet, herbal, long", "none",
    PAIR_MEATY, ["amaro", "italian", "herbal", "bittersweet", "digestif"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_016", "Limoncello di Capri", "spirit", "lemon liqueur",
    "Limoncello di Capri", 30.0, "Capri, Italy",
    "Traditional Italian lemon liqueur from the island of Capri. Sweet, bright and intensely lemony.",
    ["lemon", "citrus", "sweet", "bright", "zesty"],
    "high", "very low", "medium", "sweet, lemony, bright", "none",
    PAIR_SWEET, ["liqueur", "italian", "lemon", "citrus", "digestif"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_017", "Sourz Mango", "spirit", "fruit liqueur",
    "Sourz", 15.0, "England",
    "Tropical mango flavoured liqueur. Sweet and tangy with vibrant mango character. Perfect for shots or cocktails.",
    ["mango", "tropical", "sweet", "tangy"],
    "high", "very low", "light", "sweet, tangy, mango", "none",
    PAIR_SWEET, ["liqueur", "fruit", "mango", "shot", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_018", "Sourz Blackcurrant", "spirit", "fruit liqueur",
    "Sourz", 15.0, "England",
    "Blackcurrant flavoured liqueur. Sweet and tangy with deep berry character.",
    ["blackcurrant", "berry", "sweet", "tangy"],
    "high", "very low", "light", "sweet, tangy, berry", "none",
    PAIR_SWEET, ["liqueur", "fruit", "blackcurrant", "shot", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_019", "Sourz Raspberry", "spirit", "fruit liqueur",
    "Sourz", 15.0, "England",
    "Raspberry flavoured liqueur. Sweet and tangy with bright raspberry character.",
    ["raspberry", "berry", "sweet", "tangy", "bright"],
    "high", "very low", "light", "sweet, tangy, raspberry", "none",
    PAIR_SWEET, ["liqueur", "fruit", "raspberry", "shot", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_020", "Sourz Red Berry", "spirit", "fruit liqueur",
    "Sourz", 15.0, "England",
    "Mixed red berry flavoured liqueur. Sweet and tangy with a blend of strawberry, raspberry and redcurrant.",
    ["red berry", "strawberry", "raspberry", "sweet", "tangy"],
    "high", "very low", "light", "sweet, tangy, berry", "none",
    PAIR_SWEET, ["liqueur", "fruit", "berry", "shot", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_021", "Sourz Apple", "spirit", "fruit liqueur",
    "Sourz", 15.0, "England",
    "Apple flavoured liqueur. Sweet and tangy with crisp green apple character.",
    ["apple", "sweet", "tangy", "crisp", "green"],
    "high", "very low", "light", "sweet, tangy, apple", "none",
    PAIR_SWEET, ["liqueur", "fruit", "apple", "shot", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_022", "Mexicaner", "spirit", "spicy shot",
    "Mexicaner", 20.0, "Germany",
    "Spicy tomato-based shot with a distinctive kick. Popular party drink.",
    ["tomato", "spicy", "savoury", "bold"],
    "low", "medium", "medium", "spicy, savoury", "none",
    PAIR_MEATY, ["shot", "german", "spicy", "tomato", "party"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_023", "Aperol", "spirit", "italian aperitif",
    "Aperol", 11.0, "Padua, Italy",
    "Iconic Italian aperitif with a bright orange hue. Bittersweet with notes of orange, gentian, rhubarb and cinchona. Perfect for Aperol Spritz.",
    ["orange", "bittersweet", "herbal", "rhubarb", "gentian"],
    "medium", "medium-low", "light", "bittersweet, refreshing", "none",
    PAIR_CITRUS, ["aperitif", "italian", "orange", "bittersweet", "spritz"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_024", "Campari Bitter", "spirit", "italian bitter",
    "Campari", 25.0, "Milan, Italy",
    "Iconic Italian bitter liqueur with a distinctive red colour. Intense herbal bitterness balanced by sweet orange and cherry notes.",
    ["bitter", "orange", "cherry", "herbal", "intense"],
    "medium-low", "high", "medium", "bitter, long, herbal", "none",
    PAIR_CITRUS, ["bitter", "italian", "classic", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_025", "Cointreau", "spirit", "triple sec",
    "Cointreau", 40.0, "Angers, France",
    "Premium French orange liqueur. Crystal clear with a perfect balance of sweet and bitter orange peels. Essential for cocktails.",
    ["orange", "citrus", "balanced", "sweet", "bitter"],
    "medium-high", "medium-low", "medium", "smooth, orange, balanced", "none",
    PAIR_CITRUS, ["liqueur", "french", "orange", "triple sec", "cocktail"],
    page=spirits_page
))

drinks.append(make_drink(
    "pub_spirit_026", "Drambuie", "spirit", "scotch liqueur",
    "Drambuie", 40.0, "Scotland",
    "Scottish liqueur made with aged Scotch whisky, heather honey, herbs and spices. Rich, sweet and warming.",
    ["honey", "whisky", "herbal", "spicy", "warming"],
    "high", "low", "medium-full", "sweet, warming, honey", "none",
    PAIR_MEATY, ["liqueur", "scottish", "whisky", "honey", "herbal"],
    page=spirits_page
))

# =============================================================================
# PAGE 36 ── SPECIAL DRINKS / COCKTAILS
# =============================================================================
specials_page = 36

drinks.append(make_drink(
    "pub_special_001", "Liverpool Kiss", "special", "beer cocktail",
    "House", 4.0, "Pub Classic",
    "Guinness and blackcurrant. A classic British pub mix — rich stout softened by sweet blackcurrant.",
    ["stout", "blackcurrant", "sweet", "rich", "berry"],
    "medium", "low", "medium", "sweet, roasty, berry", "low",
    PAIR_SWEET, ["cocktail", "guinness", "blackcurrant", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_002", "Baby Guinness", "special", "layered shot",
    "House", 17.0, "Pub Classic",
    "2cl Tia Maria and 2cl Bailey's Irish Cream. A layered shot that looks like a tiny pint of Guinness.",
    ["coffee", "cream", "sweet", "smooth", "velvety"],
    "high", "very low", "medium-full", "smooth, creamy, coffee", "none",
    PAIR_SWEET, ["shot", "layered", "baileys", "tia maria", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_003", "Jäger Bomb", "special", "bomb shot",
    "House", 7.0, "Pub Classic",
    "Jägermeister dropped into a glass of Red Bull. Energising shot with herbal kick.",
    ["herbal", "energising", "sweet", "spicy"],
    "medium-high", "medium", "light", "energising, herbal, sweet", "high",
    PAIR_SPICY, ["shot", "jägermeister", "red bull", "energy", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_004", "Black Velvet", "special", "beer cocktail",
    "House", 4.0, "Pub Classic",
    "Guinness and Strongbow Cider. A classic British pub mix — stout and cider create a smooth, slightly tart combination.",
    ["stout", "apple", "smooth", "tart", "balanced"],
    "medium-low", "low", "medium", "smooth, tart, balanced", "low",
    PAIR_CIDER, ["cocktail", "guinness", "cider", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_005", "Black and Tan", "special", "beer cocktail",
    "House", 4.5, "Pub Classic",
    "Guinness layered on Hop House 13 or Kilkenny. Two beers creating a striking layered effect.",
    ["stout", "ale", "malty", "balanced", "layered"],
    "medium", "medium", "medium", "smooth, malty, layered", "medium-low",
    PAIR_MEATY, ["cocktail", "guinness", "layered", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_006", "Snakebite", "special", "beer cocktail",
    "House", 4.0, "Pub Classic",
    "Brinkhoff's Pils, Strongbow Cider and blackcurrant. A refreshing and dangerously drinkable pub classic.",
    ["pilsner", "apple", "blackcurrant", "refreshing", "tart"],
    "medium", "low", "light", "tart, refreshing, fruity", "medium-high",
    PAIR_CIDER, ["cocktail", "pilsner", "cider", "blackcurrant", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_007", "Irish Car Bomb", "special", "bomb shot",
    "House", 8.0, "Pub Classic",
    "Guinness, Bailey's Irish Cream and Paddy's Whiskey. A rich, creamy boilermaker that must be drunk quickly.",
    ["stout", "cream", "whiskey", "rich", "creamy"],
    "medium-high", "low", "full", "rich, creamy, warming", "low",
    PAIR_MEATY, ["cocktail", "guinness", "baileys", "whiskey", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_008", "B-52", "special", "layered shot",
    "House", 30.0, "Pub Classic",
    "Bailey's, Grand Marnier and Tia Maria layered in a shot glass. A classic after-dinner shooter.",
    ["coffee", "orange", "cream", "sweet", "layered"],
    "high", "very low", "medium-full", "sweet, creamy, layered", "none",
    PAIR_SWEET, ["shot", "layered", "baileys", "grand marnier", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_009", "Slippery Nipple", "special", "layered shot",
    "House", 20.0, "Pub Classic",
    "Bailey's, Sambuca and Grenadine. A sweet, layered shot with anise and berry notes.",
    ["anise", "cream", "berry", "sweet", "layered"],
    "high", "very low", "medium", "sweet, creamy, anise", "none",
    PAIR_SWEET, ["shot", "layered", "baileys", "sambuca", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_010", "Irish Flag", "special", "layered shot",
    "House", 25.0, "Pub Classic",
    "Bailey's, Crème de Menthe and Grand Marnier layered to resemble the Irish flag. Green, white and orange.",
    ["mint", "orange", "cream", "sweet", "layered"],
    "high", "very low", "medium", "sweet, minty, creamy", "none",
    PAIR_SWEET, ["shot", "layered", "irish flag", "mint", "pub classic"],
    page=specials_page
))

drinks.append(make_drink(
    "pub_special_011", "Cement Mixer", "special", "curdled shot",
    "House", 15.0, "Pub Classic",
    "Bailey's and Lime Juice. The lime curdles the cream — a novelty shot with a unique texture.",
    ["cream", "lime", "tart", "curdled", "unique"],
    "medium", "high", "medium", "tart, textured, unusual", "none",
    PAIR_CITRUS, ["shot", "baileys", "lime", "novelty", "pub classic"],
    page=specials_page
))

# =============================================================================
# PAGES 37-43 ── CLEARANCE / SALE ITEMS
# =============================================================================
# These are short-dated stock at reduced prices.
# Many are duplicates of existing entries with different pricing.

# Page 37 - Alcohol Free clearance
drinks.append(make_drink(
    "pub_beer_194", "Maisel & Friends Alcohol-Free", "beer", "non-alcoholic pale ale",
    "Maisel & Friends", 0.5, "Bayreuth, Germany",
    "Hazy honey-yellow non-alcoholic Pale Ale with fruity peach, citrus and apricot aroma. Lightly biscuity and malty, balanced with floral fruity hops and notes of passion fruit, mango and grapefruit. Clearance item.",
    ["peach", "citrus", "apricot", "passion fruit", "mango"],
    "medium-low", "low", "light-medium", "biscuity, fruity", "medium",
    PAIR_SALTY, ["alcohol-free", "pale ale", "german", "clearance", "fruity"],
    page=37
))

drinks.append(make_drink(
    "pub_beer_195", "Sierra Nevada Trail Pass IPA", "beer", "non-alcoholic ipa",
    "Sierra Nevada", 0.5, "California, USA",
    "Non-alcoholic IPA delivering full hop flavours of grapefruit and lime, bright orange in the glass, and crisp bitterness — without compromising on taste. Clearance item.",
    ["grapefruit", "lime", "orange", "crisp", "hoppy"],
    "low", "medium", "medium", "crisp, bitter, citrus", "medium",
    PAIR_SPICY, ["alcohol-free", "ipa", "american", "clearance"],
    page=37
))

drinks.append(make_drink(
    "pub_beer_196", "Adnams Ghost Ship 0.5%", "beer", "non-alcoholic pale ale",
    "Adnams", 0.5, "Southwold, England",
    "Brewed with pale ale, rye crystal and cara malts. Citra and American hop varieties create great citrus flavours. Clearance item.",
    ["citrus", "citra hops", "malty", "crisp", "clean"],
    "medium-low", "medium", "medium", "crisp, citrus", "medium",
    PAIR_SALTY, ["alcohol-free", "pale ale", "english", "clearance", "citra"],
    page=37
))

drinks.append(make_drink(
    "pub_beer_197", "La Chouffe Sans Alcool", "beer", "non-alcoholic belgian blonde",
    "La Chouffe", 0.4, "Achouffe, Belgium",
    "The great taste of La Chouffe — fruity bouquet, hint of spice, unbeatable freshness — only without the alcohol. Clearance item.",
    ["fruity", "spicy", "fresh", "balanced", "citrus"],
    "medium-low", "low", "medium", "fresh, spicy, fruity", "medium",
    PAIR_CHEESE, ["alcohol-free", "belgian", "blonde", "clearance", "spicy"],
    page=37
))

# Page 38 - Bottles clearance
drinks.append(make_drink(
    "pub_beer_198", "Liefmans On The Rocks Peach", "beer", "fruit beer",
    "Liefmans", 3.8, "Oudenaarde, Belgium",
    "Sparkling beer with orange-pink hue, served On The Rocks. Fruity aromas of peach, mango, apricot and lime. A unique and refreshing serving ritual. Clearance item.",
    ["peach", "mango", "apricot", "lime", "sparkling"],
    "medium-high", "very low", "medium", "fruity, sparkling, refreshing", "medium-high",
    PAIR_SWEET, ["fruit beer", "belgian", "clearance", "peach", "on the rocks"],
    page=38
))

drinks.append(make_drink(
    "pub_beer_199", "St. Peter Best Bitter", "beer", "english bitter",
    "St. Peter's", 3.7, "Suffolk, England",
    "English Bitter with clear amber colour and orange highlights. Rich malty aroma with notes of caramel and gentle roast. Malty and balanced by restrained bitterness. Clearance item.",
    ["caramel", "malty", "roasted", "balanced", "gentle"],
    "medium", "medium", "medium", "malty, restrained bitter", "medium",
    PAIR_CIDER, ["english bitter", "bottle", "english", "clearance", "malty"],
    page=38
))

drinks.append(make_drink(
    "pub_beer_200", "Brewski Broen Session IPA", "beer", "session ipa",
    "Brewski", 6.4, "Sweden",
    "Swedish brewed session IPA, orange yellow in colour with exotic fruity aroma. Full-bodied with balanced fruity hoppy flavour and hints of bitterness. Clearance item.",
    ["exotic fruit", "fruity", "hoppy", "balanced", "full-bodied"],
    "medium-low", "medium", "medium-full", "fruity, hoppy", "medium",
    PAIR_SPICY, ["session ipa", "bottle", "swedish", "clearance"],
    page=38
))

drinks.append(make_drink(
    "pub_beer_201", "Jopen Northsea IPA", "beer", "india pale ale",
    "Jopen", 6.5, "Haarlem, Netherlands",
    "Rich fruitiness followed by strong but well-integrated bitterness. American hop varieties strike a beautiful balance between tropical sweetness and resinous dryness. Clearance item.",
    ["tropical", "resinous", "bitter", "fruity", "balanced"],
    "medium-low", "medium-high", "medium", "resinous, dry, bitter", "medium",
    PAIR_SPICY, ["ipa", "bottle", "dutch", "clearance", "hoppy"],
    page=38
))

drinks.append(make_drink(
    "pub_beer_202", "Brewski Other Hans IPA", "beer", "india pale ale",
    "Brewski", 6.9, "Sweden",
    "Juicy IPA with mango flavour and a hint of pine resin, balanced by moderate bitterness and a soft refreshing finish. Clearance item.",
    ["mango", "pine resin", "juicy", "balanced", "refreshing"],
    "medium", "medium", "medium", "soft, refreshing, pine", "medium",
    PAIR_SPICY, ["ipa", "bottle", "swedish", "clearance", "juicy"],
    page=38
))

# Page 39 - More clearance
drinks.append(make_drink(
    "pub_beer_203", "Brewski I'm Monk-ish IPA", "beer", "india pale ale",
    "Brewski", 6.5, "Sweden",
    "Collaboration with Monkish. Soft hoppy flavour with a touch of sweet mango and a hazy deep golden colour. Clearance item.",
    ["mango", "hoppy", "soft", "hazy", "sweet"],
    "medium", "medium-low", "medium", "soft, fruity, hazy", "medium",
    PAIR_SPICY, ["ipa", "bottle", "swedish", "clearance", "collaboration"],
    page=39
))

drinks.append(make_drink(
    "pub_beer_204", "Samuel Smith Nut Brown Ale", "beer", "english brown ale",
    "Samuel Smith", 5.0, "Yorkshire, England",
    "Full-bodied brown ale with aromas of walnuts, roasted barley and a pleasantly dry finish. Clearance item.",
    ["walnut", "roasted barley", "nutty", "full-bodied", "dry"],
    "medium-low", "low", "medium-full", "dry, nutty, roasted", "medium",
    PAIR_CHEESE, ["brown ale", "bottle", "english", "clearance", "nutty"],
    page=39
))

drinks.append(make_drink(
    "pub_beer_205", "Stone Arrogant Bastard Ale", "beer", "american strong ale",
    "Stone Brewing", 7.2, "California, USA",
    "Deep red, almost brownish hue with a distinctive creamy head. Sweet malt notes of caramel and hop aromas of dark fruits. Bold and unapologetic. Clearance item.",
    ["caramel", "dark fruits", "hoppy", "bold", "aggressive"],
    "medium", "medium-high", "full", "bold, aggressive, hoppy", "medium",
    PAIR_MEATY, ["strong ale", "bottle", "american", "clearance", "bold"],
    page=39
))

drinks.append(make_drink(
    "pub_beer_206", "Two Tribes Campfire Hazy IPA", "beer", "new england ipa",
    "Two Tribes", 5.2, "England",
    "Full-bodied, hazy IPA inspired by campfire sessions. Tropical fruit flavours and a hint of coconut. Best enjoyed with friends. Clearance item.",
    ["tropical", "coconut", "hazy", "full-bodied", "fruit"],
    "medium", "medium-low", "medium-full", "tropical, creamy, hazy", "medium",
    PAIR_SPICY, ["neipa", "bottle", "english", "clearance", "coconut"],
    page=39
))

drinks.append(make_drink(
    "pub_beer_207", "Allgäuer Büble Radler Naturtrüb", "beer", "radler",
    "Allgäuer Büble", 2.3, "Allgäu, Germany",
    "Naturally cloudy radler. Pleasantly tangy with fruity-fresh aroma of ripe citrus fruits — lemons, limes and oranges. Slight hint of hops. Balanced finesse. Clearance item.",
    ["lemon", "lime", "orange", "citrus", "tangy"],
    "medium", "low", "light", "tangy, citrus, balanced", "medium",
    PAIR_SALTY, ["radler", "bottle", "german", "clearance", "naturtrüb"],
    page=39
))

# Page 40 - Clearance
drinks.append(make_drink(
    "pub_beer_208", "Delirium Nocturnum", "beer", "belgian strong dark ale",
    "Huyghe", 8.5, "Melle, Belgium",
    "Dark, top-fermented strong beer with bottle fermentation. Aromas of red fruits and toasted bread, with notes of chocolate and toffee. Clearance item.",
    ["red fruits", "toasted bread", "chocolate", "toffee", "dark"],
    "medium", "medium-low", "full", "rich, toasty, chocolate", "medium",
    PAIR_CHEESE, ["belgian", "strong dark ale", "bottle", "clearance"],
    page=40
))

drinks.append(make_drink(
    "pub_beer_209", "Innis & Gunn Lager", "beer", "scottish lager",
    "Innis & Gunn", 4.6, "Edinburgh, Scotland",
    "Fresh lager brewed and refined with Golding oats. Round, tangy, and refreshing but never boring. Clearance item.",
    ["malt", "tangy", "round", "refreshing", "smooth"],
    "medium", "low", "medium", "tangy, refreshing", "medium",
    PAIR_SALTY, ["lager", "bottle", "scottish", "clearance", "oat"],
    page=40
))

drinks.append(make_drink(
    "pub_beer_210", "Superfreunde Hell", "beer", "helles lager",
    "Superfreunde", 5.0, "Germany",
    "Clear golden Helles Lager with clean and balanced taste. Lightly sweet malt and subtle hop bitterness. Soft aroma with gentle floral hops and breadiness. Clearance item.",
    ["malt", "floral", "bready", "clean", "balanced"],
    "medium-low", "low", "light-medium", "clean, balanced", "medium",
    PAIR_SALTY, ["helles", "bottle", "german", "clearance"],
    page=40
))

drinks.append(make_drink(
    "pub_beer_211", "Belhaven Scottish Stout", "beer", "scottish stout",
    "Belhaven", 7.0, "Dunbar, Scotland",
    "Brewed with three specialty malts for a pleasantly smooth beer with intense roasted aromas reminiscent of coffee and dark chocolate. Clearance item.",
    ["coffee", "dark chocolate", "roasted", "smooth", "intense"],
    "low", "medium", "medium-full", "roasted, smooth, intense", "low",
    PAIR_CHEESE, ["stout", "bottle", "scottish", "clearance", "roasted"],
    page=40
))

# Page 41 - Cans clearance
drinks.append(make_drink(
    "pub_beer_212", "Two Tribes Metro Land Session IPA", "beer", "session ipa",
    "Two Tribes", 3.8, "England",
    "Fruity aromas of lemon peel, papaya and guava with medium hop bitterness and a golden, slightly cloudy colour. Clearance item.",
    ["lemon peel", "papaya", "guava", "fruity", "sessionable"],
    "low", "medium", "light-medium", "fruity, crisp", "medium",
    PAIR_SPICY, ["session ipa", "can", "english", "clearance"],
    page=41
))

drinks.append(make_drink(
    "pub_beer_213", "BrewDog Elvis Juice IPA", "beer", "india pale ale",
    "BrewDog", 5.1, "Ellon, Scotland",
    "Grapefruit overkill. Intense US aroma hops with orange and pine notes on a caramel malt base. Tangy, bold and citrus-forward. Clearance item.",
    ["grapefruit", "orange", "pine", "caramel", "tangy"],
    "medium-low", "medium-high", "medium", "tangy, bold, citrus", "medium",
    PAIR_SPICY, ["ipa", "can", "scottish", "clearance", "grapefruit"],
    page=41
))

drinks.append(make_drink(
    "pub_beer_214", "BrewDog Kiezkeule IPA", "beer", "india pale ale",
    "BrewDog", 5.8, "Ellon, Scotland",
    "Refreshing citrus notes followed by tropical fruits and floral notes that complement the stable malt body. Skilfully balances hops and malt. Clearance item.",
    ["citrus", "tropical", "floral", "balanced", "refreshing"],
    "medium-low", "medium", "medium", "balanced, hoppy, citrus", "medium",
    PAIR_SPICY, ["ipa", "can", "scottish", "clearance"],
    page=41
))

drinks.append(make_drink(
    "pub_beer_215", "Stone Buenaveza Salt & Lime Lager", "beer", "mexican-style lager",
    "Stone Brewing", 4.7, "California, USA",
    "Pale golden Mexican-style lager with light corn aroma and malt sweetness. Refreshing bright lime flavour and touch of saltiness. Clearance item.",
    ["corn", "lime", "salt", "crisp", "refreshing"],
    "medium-low", "very low", "light", "bright, salty, lime", "medium",
    PAIR_SPICY, ["lager", "can", "american", "clearance", "mexican-style"],
    page=41
))

# Page 42 - Tankbusters clearance
drinks.append(make_drink(
    "pub_beer_216", "Tankbusters Time to Fly DNEIPA", "beer", "double neipa",
    "Tankbusters", 7.0, "Poland",
    "Juicy Double New England IPA with Riwaka, Motueka, Citra and Elani hops. Intense notes of tropical fruits — passion fruit and mango — with distinct citrus and lime accents. Clearance item.",
    ["passion fruit", "mango", "citrus", "lime", "juicy"],
    "medium", "medium-low", "medium-full", "juicy, tropical, hazy", "medium",
    PAIR_SPICY, ["double neipa", "can", "polish", "clearance"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_217", "Tankbusters Introduction DDH Canadian IPA", "beer", "canadian ipa",
    "Tankbusters", 5.4, "Poland",
    "Fruity, refreshing and hoppy DDH Canadian IPA with aromas of pear, grapes and watermelon. Clearance item.",
    ["pear", "grape", "watermelon", "fruity", "refreshing"],
    "medium", "medium-low", "medium", "fruity, refreshing, hoppy", "medium",
    PAIR_SPICY, ["ipa", "ddh", "can", "polish", "clearance"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_218", "Tankbusters Book of Hops Riwaka & Elani", "beer", "new england ipa",
    "Tankbusters", 6.1, "Poland",
    "Aromas of kumquat, passion fruit, mango and white fruits explode in the glass. Riwaka and Elani hops create harmonious, fruity balance with clear, powerful character. Clearance item.",
    ["kumquat", "passion fruit", "mango", "white fruits", "tropical"],
    "medium", "medium-low", "medium", "tropical, fruity, balanced", "medium",
    PAIR_SPICY, ["neipa", "can", "polish", "clearance", "tropical"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_219", "Tankbusters All My Heroes Are Dead IPA", "beer", "india pale ale",
    "Tankbusters", 5.5, "Poland",
    "Pleasant mild bitterness perfectly complemented by tropical and lime aromas from Citra BBC, Motueka and Cascade BBC hops. Clearance item.",
    ["tropical", "lime", "citrus", "mild bitter", "balanced"],
    "medium-low", "medium", "medium", "mild, tropical, balanced", "medium",
    PAIR_SPICY, ["ipa", "can", "polish", "clearance"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_220", "Tankbusters Fresh Squeeze Gose", "beer", "fruit gose",
    "Tankbusters", 4.5, "Poland",
    "Modern fruit gose with cool, herbal aroma of cucumber paired with tangy citrus freshness of lime. Pear adds a soft, juicy component. Slightly sour and salty. Clearance item.",
    ["cucumber", "lime", "pear", "tangy", "herbal"],
    "low", "medium", "light-medium", "tangy, herbal, refreshing", "medium-high",
    PAIR_SALTY, ["gose", "can", "polish", "clearance", "cucumber"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_221", "Tankbusters Liquid Poetry TIPA", "beer", "triple ipa",
    "Tankbusters", 9.1, "Poland",
    "Intense triple IPA with juicy hop notes and a creamy texture. Perfect for cool evenings. Clearance item.",
    ["juicy", "hoppy", "creamy", "intense", "warming"],
    "medium", "medium-high", "full", "creamy, intense, hoppy", "medium",
    PAIR_SPICY, ["triple ipa", "can", "polish", "clearance", "strong"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_222", "Tankbusters Cold as Ice 2 NEIPA", "beer", "new england ipa",
    "Tankbusters", 5.8, "Poland",
    "Refreshing NEIPA with intense lime and lychee aromas. Juicy, fruity and smooth — the perfect summer beer. Clearance item.",
    ["lime", "lychee", "juicy", "fruity", "smooth"],
    "medium", "medium-low", "medium", "juicy, smooth, refreshing", "medium",
    PAIR_SPICY, ["neipa", "can", "polish", "clearance", "summer"],
    page=42
))

drinks.append(make_drink(
    "pub_beer_223", "Brewski T-Horse Double NEIPA", "beer", "double neipa",
    "Brewski", 8.5, "Sweden",
    "New England style double IPA, thick and creamy, dominated by tropical flavours of mango and candied pineapple. A little sweetness balanced by a long, soft bitterness. Clearance item.",
    ["mango", "candied pineapple", "tropical", "creamy", "sweet"],
    "medium", "medium-low", "medium-full", "long, soft bitter, tropical", "medium",
    PAIR_SPICY, ["double neipa", "can", "swedish", "clearance"],
    page=42
))

# Page 43 - More cans clearance
drinks.append(make_drink(
    "pub_beer_224", "Sierra Nevada Torpedo IPA", "beer", "india pale ale",
    "Sierra Nevada", 7.2, "California, USA",
    "Tropical citrus notes meet caramel from pale and caramel malts. Subtle spicy accents. Dry, finely sparkling and powerful — an IPA that shows character with every sip. Clearance item.",
    ["citrus", "tropical", "caramel", "spicy", "dry"],
    "medium-low", "medium-high", "medium-full", "dry, sparkling, powerful", "medium-high",
    PAIR_SPICY, ["ipa", "can", "american", "clearance"],
    page=43
))

drinks.append(make_drink(
    "pub_beer_225", "Sierra Nevada Trail Pass Brewveza", "beer", "non-alcoholic mexican-style lager",
    "Sierra Nevada", 0.5, "California, USA",
    "Straw yellow Mexican-style Blonde Ale. Crisp and clean aroma with hint of lime zest. Light malt sweetness balanced by mild hop bitterness with refreshing citrus lime twist. Clearance item.",
    ["lime zest", "malt", "crisp", "clean", "refreshing"],
    "medium-low", "low", "light", "crisp, refreshing, lime", "medium",
    PAIR_SPICY, ["alcohol-free", "can", "american", "clearance", "mexican-style"],
    page=43
))

drinks.append(make_drink(
    "pub_beer_226", "Sierra Nevada Trail Pass Golden", "beer", "non-alcoholic golden ale",
    "Sierra Nevada", 0.5, "California, USA",
    "Bright and clear golden ale. Gentle floral hop aroma with hints of citrus and honeyed malts. Balanced sweetness from pale malts, delicate citrus fruitiness and mild hop bitterness. Clean, smooth and easy drinking. Clearance item.",
    ["floral", "citrus", "honey", "malt", "smooth"],
    "medium", "low", "light", "clean, smooth, refreshing", "medium",
    PAIR_SALTY, ["alcohol-free", "can", "american", "clearance"],
    page=43
))

drinks.append(make_drink(
    "pub_beer_227", "Cloudwater Happy Easy Pale Ale", "beer", "pale ale",
    "Cloudwater", 3.4, "Manchester, England",
    "Easy-drinking pale ale seamlessly blending contemporary softness with time-honoured drinkability. Smooth body and dry finish allowing juicy flavours to linger. The epitome of sessionability. Clearance item.",
    ["juicy", "smooth", "dry", "balanced", "sessionable"],
    "medium-low", "medium-low", "light-medium", "dry, juicy, lingering", "medium",
    PAIR_SPICY, ["pale ale", "can", "english", "clearance", "session"],
    page=43
))

drinks.append(make_drink(
    "pub_beer_228", "Borussia Brauerei Pils", "beer", "pilsner",
    "Borussia Brauerei", 4.9, "Dortmund, Germany",
    "German Pils brewed with aromatic hops. Uncomplicated, classically hoppy. Clearance item.",
    ["hoppy", "classic", "clean", "crisp", "aromatic"],
    "low", "medium", "light-medium", "crisp, hoppy", "medium-high",
    PAIR_SALTY, ["pilsner", "can", "german", "clearance", "dortmund"],
    page=43
))

drinks.append(make_drink(
    "pub_beer_229", "Garage Beer Co. SANTAKO West Coast IPA", "beer", "west coast ipa",
    "Garage Beer Co.", 6.4, "Barcelona, Spain",
    "Celiac and vegan friendly West Coast IPA. Citrus and pine aroma with a touch of peach. Hint of sweetness from light caramel malt. Clearance item.",
    ["citrus", "pine", "peach", "caramel", "crisp"],
    "medium-low", "medium-high", "medium", "crisp, bitter, piney", "medium",
    PAIR_SPICY, ["west coast ipa", "can", "spanish", "clearance", "gluten-free"],
    page=43
))

# =============================================================================
# WRITE ALL FILES
# =============================================================================
for d in drinks:
    write_json(d)

from collections import Counter
cats = Counter(d['category'] for d in drinks)
print(f"Generated {len(drinks)} drink JSON files in '{OUT}/'")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")
