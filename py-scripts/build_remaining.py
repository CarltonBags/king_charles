#!/usr/bin/env python3
"""Build remaining drink guide JSON files: Gins, Soft Drinks, Whiskies, Bourbons, Irish Whiskeys, and extra Tankbuster cans."""

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
PAIR_BBQ = pair(3, 19)
PAIR_NUTS = pair(21, 22, 20)
PAIR_CITRUS = pair(6, 15, 0)
PAIR_MIXED = pair(6, 4, 1)

# ── Helper ────────────────────────────────────────────────────────────────────
def make_spirit(id_, name, category, subcategory, brand, abv, origin, notes,
                primary_notes, sweetness, bitterness, body, finish,
                food_pairings, tags, carbonation="none", page=1):
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

def make_soft(id_, name, category, subcategory, brand, origin, notes,
              primary_notes, sweetness, bitterness, body, finish,
              food_pairings, tags, carbonation="none", page=1):
    return {
        "id": id_,
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "brand_or_producer": brand,
        "abv": 0.0,
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
# GINS (from Gins & Softdrinks.pdf, pages 2-5)
# =============================================================================
gin_page = 2  # start page of gins in the PDF

drinks.append(make_spirit(
    "pub_gin_001", "Beefeater London Dry", "gin", "london dry gin",
    "Beefeater", 40.0, "London, England",
    "One London distillery, 9 stills and as many botanicals make the world's most awarded gin under the supervision of the world's most experienced Master Distiller. A quintessential London dry gin made with big juniper character and strong citrus notes, this is an authentic London dry for those that enjoy the real taste of gin.",
    ["juniper", "citrus", "classic", "dry"],
    "low", "medium", "medium", "dry, crisp", PAIR_CITRUS,
    ["gin", "london dry", "classic", "citrus", "juniper"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_002", "Bombay Sapphire", "gin", "london dry gin",
    "Bombay Sapphire", 40.0, "Laverstoke, England",
    "World famous gin in its distinctive blue bottle. Every drop contains 10 hand-selected botanicals from exotic locations around the world. Vapour infused to capture their bright, vibrant flavours.",
    ["juniper", "citrus", "floral", "balanced", "smooth"],
    "low", "medium-low", "medium", "bright, vibrant", PAIR_CITRUS,
    ["gin", "london dry", "classic", "vapour infused", "balanced"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_003", "Bosford Rose", "gin", "flavoured gin",
    "Bosford", 37.5, "England",
    "Gin of juniper, coriander, angelica, lemon and orange peel, blended with strawberry and raspberry flavours and a hint of sugar for a light sweetness to soften the sometimes-bitter taste gin is known for.",
    ["strawberry", "raspberry", "juniper", "citrus", "sweet"],
    "medium-high", "low", "medium", "sweet, soft, fruity", PAIR_SALTY,
    ["gin", "flavoured", "pink gin", "berry", "sweet"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_004", "Caorunn", "gin", "scottish london dry gin",
    "Caorunn", 41.8, "Speyside, Scotland",
    "A slightly spicy, full-bodied and invigorating gin with a clean and crisp finish. A modern London Dry gin infused with classic Celtic soul, using 5 locally foraged botanicals.",
    ["spicy", "full-bodied", "crisp", "floral", "clean"],
    "low", "medium-low", "medium-full", "clean, crisp", PAIR_CHEESE,
    ["gin", "scottish", "celtic", "craft", "botanical"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_005", "City of London Gin", "gin", "london dry gin",
    "City of London Distillery", 41.3, "London, England",
    "Classic, perfectly balanced gin from the heart of London. Uses angelica, liquorice and coriander seeds as botanicals. Fresh oranges, lemons and pink grapefruit give it an unmistakably piquant, fruity note.",
    ["orange", "lemon", "pink grapefruit", "juniper", "piquant"],
    "medium-low", "medium-low", "medium", "fruity, piquant", PAIR_CITRUS,
    ["gin", "london dry", "classic", "citrus", "balanced"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_006", "Copperhead The Gibson", "gin", "savoury gin",
    "Copperhead", 40.0, "Belgium",
    "Unique savoury style of gin. The original 5 Copperhead botanicals are joined by 13 carefully selected spices traditionally used in pickling: mace, pepper, cassia, bay leaf, ginger, allspice, fennel and dill seeds, plus a touch of eight-year-old Genever for a smooth and complex taste.",
    ["savoury", "spice", "pepper", "ginger", "herbal"],
    "low", "medium", "medium-full", "smooth, complex, savoury", PAIR_MEATY,
    ["gin", "savoury", "gibson", "spiced", "craft"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_007", "Edinburgh Dry", "gin", "london dry gin",
    "Edinburgh Gin", 43.0, "Edinburgh, Scotland",
    "Unmistakable London Dry born in Edinburgh. The finest grain spirit brought together with an original balance of 14 botanicals. An award-winning gin, a labour of love and the heart of the Edinburgh range.",
    ["juniper", "balanced", "floral", "citrus", "classic"],
    "low", "medium", "medium", "clean, classic", PAIR_CHEESE,
    ["gin", "london dry", "scottish", "classic", "award-winning"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_008", "Edinburgh Seaside", "gin", "scottish gin",
    "Edinburgh Gin", 43.0, "Edinburgh, Scotland",
    "Tastes like a cool crisp breeze over windswept golden sands. Softly sweet, mineralistic gin using botanicals foraged on beaches around Edinburgh, reminiscent of a bracing walk on a Scottish beach.",
    ["mineral", "sea salt", "sweet", "coastal", "herbal"],
    "medium-low", "low", "medium", "crisp, mineral, salt-kissed", PAIR_SALTY,
    ["gin", "scottish", "coastal", "mineral", "foraged"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_009", "Ferdinand's Saar Quince", "gin", "fruit gin",
    "Ferdinand's", 30.0, "Saar, Germany",
    "Freshly harvested Muscat quinces, a rare Pear Quince strain, growing behind the distillery as well as an infusion of Rausch Kabinett are the basis for this regional homage to British Sloe Gin.",
    ["quince", "pear", "fruity", "sweet", "floral"],
    "medium-high", "low", "medium", "fruity, sweet, lingering", PAIR_CHEESE,
    ["gin", "fruit", "german", "quince", "regional"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_010", "Fifty Pounds", "gin", "london dry gin",
    "Fifty Pounds", 43.5, "London, England",
    "A London Dry Gin that spans the centuries. Historic in essence, modern in spirit. From the botanicals used to the method of production and bottling, Fifty Pounds Gin pays tribute to London's rich gin history.",
    ["juniper", "balanced", "classic", "smooth", "herbal"],
    "low", "medium", "medium", "smooth, classic", PAIR_CITRUS,
    ["gin", "london dry", "classic", "premium", "historic"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_011", "Gordon's Dry", "gin", "london dry gin",
    "Gordon's", 37.5, "London, England",
    "Award-winning classic London Dry gin. First bottled in the early 1900s with its distinctive export label still used today.",
    ["juniper", "citrus", "classic", "dry", "crisp"],
    "low", "medium", "medium", "dry, crisp", PAIR_CITRUS,
    ["gin", "london dry", "classic", "export", "traditional"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_012", "Gordon's Pink", "gin", "flavoured gin",
    "Gordon's", 37.5, "London, England",
    "Inspired by an 1880s Gordon's recipe. Perfectly crafted to balance the refreshing taste of Gordon's with natural sweetness of raspberries and strawberries, with the tang of redcurrant. Made using only natural fruit flavours.",
    ["raspberry", "strawberry", "redcurrant", "sweet", "tangy"],
    "medium-high", "very low", "medium", "sweet, berry, tangy", PAIR_SALTY,
    ["gin", "flavoured", "pink gin", "berry", "natural"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_013", "Hendricks", "gin", "scottish gin",
    "Hendrick's", 44.0, "Girvan, Scotland",
    "An unusual gin created from eleven fine botanicals. The curious, yet marvellous, infusions of rose and cucumber imbue this spirit with its uniquely balanced flavour resulting in an impeccably smooth distinct gin.",
    ["rose", "cucumber", "floral", "smooth", "balanced"],
    "low", "very low", "medium", "smooth, floral, cucumber", PAIR_CITRUS,
    ["gin", "scottish", "cucumber", "rose", "premium"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_014", "Monkey 47 Schwarzwald Dry Gin", "gin", "dry gin",
    "Monkey 47", 47.0, "Black Forest, Germany",
    "Distilled from 47 predominantly unusual but regional botanicals such as lingonberries, blended with natural spring water. A German gin uniting British traditions, Indian spices and the rich landscape of the Black Forest.",
    ["lingonberry", "spice", "floral", "complex", "botanical"],
    "low", "medium", "medium-full", "complex, lingering, botanical", PAIR_CHEESE,
    ["gin", "german", "black forest", "complex", "botanical"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_015", "Ophir", "gin", "spiced gin",
    "Ophir", 42.5, "England (Opihr Distillery)",
    "OPIHR Spices of the Orient Gin crafted with exotic hand-picked botanicals: spicy Cubeb berries from Indonesia, Black Pepper from India and Coriander from Morocco. Distilled using the London Dry method since 1761.",
    ["cubeb pepper", "black pepper", "coriander", "spicy", "exotic"],
    "low", "medium-high", "medium", "spicy, warm, exotic", PAIR_SPICY,
    ["gin", "spiced", "oriental", "exotic", "london dry"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_016", "Sipsmith London Dry Gin", "gin", "london dry gin",
    "Sipsmith", 41.6, "London, England",
    "In 2009, London's first copper distillery in 189 years was set up. Award-winning gin handcrafted in small batches. A London Dry Gin of truly uncompromising quality and character, back in the city where gin first earned its name.",
    ["juniper", "citrus", "classic", "smooth", "balanced"],
    "low", "medium", "medium", "smooth, classic", PAIR_CITRUS,
    ["gin", "london dry", "small batch", "craft", "award-winning"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_017", "Tanqueray London Dry Gin", "gin", "london dry gin",
    "Tanqueray", 43.1, "London, England",
    "Back in the 1830s Charles Tanqueray wasn't afraid to mix his bold ideas. His ingenious pursuit for perfection paid off, creating Tanqueray London Dry, a perfectly balanced gin and one of the most awarded gins in the world.",
    ["juniper", "balanced", "classic", "bold", "smooth"],
    "low", "medium", "medium", "smooth, balanced", PAIR_CITRUS,
    ["gin", "london dry", "classic", "award-winning", "premium"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_018", "Tanqueray Flor de Sevilla Distilled Gin", "gin", "flavoured gin",
    "Tanqueray", 41.3, "London, England",
    "A zesty, fruitful gin offering a bold and bittersweet taste of the sun-soaked Mediterranean. Seville oranges distilled with orange blossom and the four classic London Dry botanicals: juniper, coriander, angelica, and liquorice.",
    ["seville orange", "orange blossom", "juniper", "citrus", "bittersweet"],
    "medium", "medium-low", "medium", "zesty, fruity, bittersweet", PAIR_CITRUS,
    ["gin", "flavoured", "orange", "seville", "citrus"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_019", "Tanqueray No 10", "gin", "premium london dry gin",
    "Tanqueray", 47.3, "London, England",
    "The first ultra-premium gin. Distilled in small batches with the four original London Dry botanicals plus fresh whole grapefruits, oranges, limes and chamomile flowers. An explosion of fresh citrus with every sip.",
    ["citrus", "grapefruit", "lime", "chamomile", "juniper"],
    "low", "medium", "medium-full", "explosive citrus, smooth", PAIR_CITRUS,
    ["gin", "premium", "small batch", "citrus", "chamomile"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_020", "The Botanist", "gin", "islay dry gin",
    "The Botanist", 46.0, "Islay, Scotland",
    "A gin that's the essence of Islay. Made from 22 hand-foraged local botanicals, distilled slowly and patiently. A representation of the place, communicating a love for the land through the art of distillation.",
    ["juniper", "herbal", "floral", "citrus", "botanical"],
    "low", "medium-low", "medium", "herbal, floral, complex", PAIR_CHEESE,
    ["gin", "islay", "botanical", "foraged", "craft", "scottish"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_021", "Whitley Neil London Dry Gin", "gin", "london dry gin",
    "Whitley Neill", 42.0, "England",
    "Slightly softer and much smoother than traditional gins, with rich notes of juniper and citrus, pot-pourri and exotic spices. Long finish with subtle fade of herbs, cocoa and candied lemon peels.",
    ["juniper", "citrus", "spicy", "herbal", "cocoa"],
    "medium-low", "medium-low", "medium", "long, herbal, cocoa", PAIR_CITRUS,
    ["gin", "london dry", "smooth", "exotic", "spiced"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_022", "Whitley Neil Rhubarb & Ginger Gin", "gin", "flavoured gin",
    "Whitley Neill", 43.0, "England",
    "The essence of rhubarb adds a tart crisp edge to the smooth gin base whilst ginger extract warms the palate for a full-bodied finish.",
    ["rhubarb", "ginger", "tart", "crisp", "warming"],
    "medium", "medium-low", "medium-full", "full-bodied, warming", PAIR_SPICY,
    ["gin", "flavoured", "rhubarb", "ginger", "spiced"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_023", "Whitley Neil Blood Orange Gin", "gin", "flavoured gin",
    "Whitley Neill", 43.0, "England",
    "A handcrafted gin bursting with the sweet citrus fruit flavour of Sicilian blood oranges. Bright, zesty aromas head up a clean, citrus gin with a smooth, crisp taste of the Mediterranean sun.",
    ["blood orange", "zesty", "citrus", "sweet", "bright"],
    "medium", "low", "medium", "smooth, crisp, citrus", PAIR_CITRUS,
    ["gin", "flavoured", "blood orange", "citrus", "craft"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_024", "Whitley Neil Lemongrass & Ginger Gin", "gin", "flavoured gin",
    "Whitley Neill", 43.0, "England",
    "Lemongrass blended with warming ginger and a variety of exotic herbs and spices giving this gin its distinctive, fragrant, citrusy taste. A handcrafted gin of exceptional quality.",
    ["lemongrass", "ginger", "citrus", "fragrant", "exotic"],
    "medium-low", "medium-low", "medium", "citrusy, fragrant, warming", PAIR_SPICY,
    ["gin", "flavoured", "lemongrass", "ginger", "exotic"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_025", "Whitley Neil Distiller's Cut Gin", "gin", "london dry gin",
    "Whitley Neill", 43.0, "England",
    "Soft and rounded aroma with present juniper, followed by bittersweet candied orange flavour. Strong flavour notes of candied orange, white pepper and solid juniper. Pleasant oily texture, earthy and woody with orange persisting through the finish.",
    ["candied orange", "juniper", "white pepper", "earthy", "woody"],
    "medium", "medium-low", "medium-full", "oily, earthy, orange", PAIR_CHEESE,
    ["gin", "london dry", "premium", "candied orange", "complex"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_026", "Whitley Neil Peach Gin", "gin", "flavoured gin",
    "Whitley Neill", 43.0, "England",
    "A taste of summer. Sweet and fruity peach balances well alongside hints of orange and lemon. Fresh sweet peach aromas meld with citrus and juniper. Sweet peach and citrus persist with a touch of peppery juniper on the finish.",
    ["peach", "orange", "lemon", "sweet", "fruity"],
    "medium-high", "very low", "medium", "sweet, peach, citrus", PAIR_SALTY,
    ["gin", "flavoured", "peach", "summer", "fruity"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_027", "Whitley Neil Quince Gin", "gin", "flavoured gin",
    "Whitley Neill", 43.0, "England",
    "Distinctive flavour of Turkish quince, with a long, fruity finish. Aroma of fresh stone fruits, hints of juniper and citrus zest. Quince dominates the palate, giving way to sweetness of apricots and peaches, finishing with orange blossoms and zesty grapefruits.",
    ["quince", "apricot", "peach", "orange blossom", "grapefruit"],
    "medium-high", "very low", "medium", "long, fruity, zesty", PAIR_CITRUS,
    ["gin", "flavoured", "quince", "stone fruit", "fruity"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_028", "Martin Miller's Westbourne Strength", "gin", "london dry gin",
    "Martin Miller's", 45.2, "England / Iceland",
    "Unconventional English distillation of the finest botanicals, blended with the purest Icelandic water. A modern classic dry gin based on the best traditions of English distillers, perfectly balanced.",
    ["juniper", "citrus", "balanced", "crisp", "smooth"],
    "low", "medium", "medium", "clean, balanced, crisp", PAIR_CITRUS,
    ["gin", "london dry", "premium", "icelandic water", "classic"],
    page=gin_page
))

drinks.append(make_spirit(
    "pub_gin_029", "MOM Love Gin", "gin", "flavoured gin",
    "MOM", 37.5, "Germany",
    "A premium pink gin with a vibrant strawberry taste and a soft finish that ends in a sea of unrepeatable sensation.",
    ["strawberry", "sweet", "soft", "floral", "vibrant"],
    "medium-high", "very low", "medium", "soft, strawberry, smooth", PAIR_SALTY,
    ["gin", "flavoured", "pink gin", "strawberry", "premium"],
    page=gin_page
))

# =============================================================================
# SOFT DRINKS (from Gins & Softdrinks.pdf, page 6)
# =============================================================================
soft_page = 6

drinks.append(make_soft(
    "pub_softdrink_001", "Afri Cola", "soft_drink", "cola",
    "Afri Cola", "Germany",
    "Classic German cola soft drink with a distinctive caffeine kick and balanced sweetness.",
    ["cola", "sweet", "caffeine", "classic"],
    "high", "very low", "light", "sweet, refreshing",
    PAIR_SALTY, ["soft drink", "cola", "german", "caffeinated"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_002", "Afri Cola Zero", "soft_drink", "zero cola",
    "Afri Cola", "Germany",
    "Sugar-free version of the classic German cola with the same distinctive taste, sweetened with sweeteners.",
    ["cola", "sweet", "caffeine", "zero sugar"],
    "medium", "very low", "light", "sweet, crisp",
    PAIR_SALTY, ["soft drink", "cola", "german", "zero sugar", "caffeinated"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_003", "Bluna Orange", "soft_drink", "orange soda",
    "Bluna", "Germany",
    "Classic German orange-flavoured carbonated soft drink, fruity and refreshing.",
    ["orange", "fruity", "sweet", "citrus"],
    "high", "very low", "light", "sweet, citrusy",
    PAIR_SALTY, ["soft drink", "orange", "german", "fruity"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_004", "Bluna Zitrone", "soft_drink", "lemon soda",
    "Bluna", "Germany",
    "Classic German lemon-flavoured carbonated soft drink, crisp and zesty.",
    ["lemon", "zesty", "sweet", "citrus", "refreshing"],
    "medium", "low", "light", "crisp, zesty",
    PAIR_CITRUS, ["soft drink", "lemon", "german", "citrus"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_005", "Rhodius Tafelwasser", "soft_drink", "sparkling water",
    "Rhodius", "Germany",
    "Classic German table water, pure sparkling mineral water. Clean, neutral and refreshing.",
    ["mineral", "clean", "neutral", "refreshing"],
    "very low", "very low", "very light", "clean, neutral",
    PAIR_SALTY, ["soft drink", "water", "german", "sparkling", "mineral"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_006", "Apfelschorle", "soft_drink", "apple spritzer",
    "House", "Germany",
    "Traditional German apple juice spritzer. Half apple juice, half sparkling water. Refreshing and lightly sweet.",
    ["apple", "crisp", "light", "refreshing", "fruity"],
    "medium", "very low", "light", "crisp, refreshing",
    PAIR_SALTY, ["soft drink", "apple", "german", "spritzer", "classic"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_007", "Rhodius Gourmet Classic", "soft_drink", "sparkling mineral water",
    "Rhodius", "Germany",
    "Premium German classic sparkling mineral water with fine perlage.",
    ["mineral", "clean", "neutral", "refreshing", "fine bubbles"],
    "very low", "very low", "very light", "clean, elegant",
    PAIR_SALTY, ["soft drink", "water", "german", "sparkling", "premium"],
    carbonation="medium-high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_008", "Rhodius Gourmet Natur", "soft_drink", "still mineral water",
    "Rhodius", "Germany",
    "Premium German natural still mineral water. Pure and clean.",
    ["mineral", "clean", "neutral", "pure"],
    "very low", "very low", "very light", "clean, pure",
    PAIR_SALTY, ["soft drink", "water", "german", "still", "premium"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_009", "Fevertree Indian Tonic Water", "soft_drink", "tonic water",
    "Fever-Tree", "England",
    "Premium Indian tonic water made with the finest quinine from the Congo and citrus botanical oils. Perfect for gin & tonic.",
    ["quinine", "citrus", "bitter", "botanical", "crisp"],
    "low", "medium", "light", "crisp, bitter, botanical",
    PAIR_CITRUS, ["soft drink", "tonic", "premium", "mixer", "quinine"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_010", "Fevertree Mediterranean Tonic Water", "soft_drink", "tonic water",
    "Fever-Tree", "England",
    "Premium Mediterranean tonic water infused with essential oils from Mediterranean lemon, thyme and rosemary. Aromatic and refreshing.",
    ["lemon", "thyme", "rosemary", "herbal", "citrus"],
    "low", "medium-low", "light", "herbal, aromatic, crisp",
    PAIR_CITRUS, ["soft drink", "tonic", "premium", "mediterranean", "mixer"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_011", "Fevertree Ginger Beer", "soft_drink", "ginger beer",
    "Fever-Tree", "England",
    "Premium ginger beer made with a blend of three gingers from Nigeria, Cochin and the Ivory Coast. Spicy, warming and refreshing.",
    ["ginger", "spicy", "warming", "sweet", "zesty"],
    "medium", "medium", "light-medium", "spicy, warming",
    PAIR_SPICY, ["soft drink", "ginger beer", "premium", "spicy", "mixer"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_012", "Fevertree Ginger Ale", "soft_drink", "ginger ale",
    "Fever-Tree", "England",
    "Premium ginger ale with a clean, refreshing ginger taste. Less spicy than ginger beer, more delicate and balanced.",
    ["ginger", "mild", "sweet", "refreshing", "clean"],
    "medium", "very low", "light", "clean, refreshing",
    PAIR_SALTY, ["soft drink", "ginger ale", "premium", "mild", "mixer"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_013", "Elephant Bay Rose Water", "soft_drink", "flavoured water",
    "Elephant Bay", "Unknown",
    "Delicate rose-flavoured water. Floral and refreshing with a subtle sweetness.",
    ["rose", "floral", "subtle", "sweet", "refreshing"],
    "medium", "very low", "light", "floral, delicate",
    PAIR_SALTY, ["soft drink", "flavoured water", "rose", "floral"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_014", "Elephant Bay Blueberry", "soft_drink", "flavoured water",
    "Elephant Bay", "Unknown",
    "Blueberry-flavoured water. Fruity and sweet with a deep berry character.",
    ["blueberry", "berry", "fruity", "sweet", "refreshing"],
    "medium-high", "very low", "light", "fruity, sweet",
    PAIR_SALTY, ["soft drink", "flavoured water", "blueberry", "berry"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_015", "Elephant Bay Peach", "soft_drink", "flavoured water",
    "Elephant Bay", "Unknown",
    "Peach-flavoured water. Sweet and fruity with a refreshing character.",
    ["peach", "fruity", "sweet", "refreshing"],
    "medium-high", "very low", "light", "fruity, refreshing",
    PAIR_SALTY, ["soft drink", "flavoured water", "peach", "fruity"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_016", "Elephant Bay Lemon", "soft_drink", "flavoured water",
    "Elephant Bay", "Unknown",
    "Lemon-flavoured water. Zesty and citrus-forward with a refreshing finish.",
    ["lemon", "citrus", "zesty", "refreshing"],
    "medium", "low", "light", "zesty, citrus",
    PAIR_CITRUS, ["soft drink", "flavoured water", "lemon", "citrus"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_017", "Orangina", "soft_drink", "citrus soda",
    "Orangina", "France",
    "Iconic French citrus soda with real orange pulp. Sweet, tangy, gently sparkling with a unique cloudy appearance.",
    ["orange", "citrus", "tangy", "pulp", "sweet"],
    "high", "low", "light-medium", "tangy, fruity",
    PAIR_SALTY, ["soft drink", "orange", "french", "iconic", "pulp"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_018", "Orangina Rouge", "soft_drink", "citrus soda",
    "Orangina", "France",
    "Orangina variant with red fruits. Sweet, fruity blend of orange and red berry flavours with the classic pulp texture.",
    ["orange", "red berries", "fruity", "sweet", "tangy"],
    "high", "low", "light-medium", "fruity, berry, tangy",
    PAIR_SALTY, ["soft drink", "berry", "french", "pulp", "fruity"], carbonation="medium",
    page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_019", "Schweppes Bitter Lemon", "soft_drink", "bitter lemon",
    "Schweppes", "Germany",
    "Classic bitter lemon soft drink. Lemon and quinine create a refreshingly bitter-sweet, crisp and clean taste.",
    ["lemon", "quinine", "bitter", "crisp", "citrus"],
    "medium-low", "medium", "light", "bitter-sweet, crisp",
    PAIR_CITRUS, ["soft drink", "bitter lemon", "classic", "mixer", "quinine"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_020", "Schweppes Wild Berry", "soft_drink", "berry soda",
    "Schweppes", "Germany",
    "Wild berry flavoured soft drink. Fruity, sweet and refreshing with a blend of berry flavours.",
    ["wild berry", "fruity", "sweet", "refreshing"],
    "high", "very low", "light", "sweet, berry",
    PAIR_SALTY, ["soft drink", "berry", "fruity", "sweet"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_021", "Vaihinger Apfelsaft", "soft_drink", "apple juice",
    "Vaihinger", "Germany",
    "Pure German apple juice. Naturally sweet with a clean, crisp apple flavour.",
    ["apple", "fruity", "sweet", "crisp", "natural"],
    "medium-high", "very low", "light-medium", "clean, sweet",
    PAIR_SALTY, ["soft drink", "juice", "apple", "german", "natural"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_022", "Vaihinger Orangensaft", "soft_drink", "orange juice",
    "Vaihinger", "Germany",
    "Pure German orange juice. Sweet, tangy, and naturally bright with a rich citrus flavour.",
    ["orange", "citrus", "tangy", "sweet", "natural"],
    "medium-high", "low", "medium", "tangy, bright",
    PAIR_SALTY, ["soft drink", "juice", "orange", "german", "natural"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_023", "Möller Banane Saft", "soft_drink", "banana juice",
    "Möller", "Germany",
    "Pure banana juice. Rich, creamy and naturally sweet with authentic banana flavour.",
    ["banana", "creamy", "sweet", "rich", "natural"],
    "high", "very low", "medium-full", "sweet, creamy",
    PAIR_NUTS, ["soft drink", "juice", "banana", "german", "natural"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_024", "Vaihinger Sauerkirschen Saft", "soft_drink", "sour cherry juice",
    "Vaihinger", "Germany",
    "Pure German sour cherry juice. Tart, fruity and deeply flavoured with authentic cherry character.",
    ["sour cherry", "tart", "fruity", "rich", "natural"],
    "medium", "medium", "medium", "tart, fruity, lingering",
    PAIR_NUTS, ["soft drink", "juice", "sour cherry", "german", "natural"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_025", "Vaihinger Johannisbeersaft", "soft_drink", "blackcurrant juice",
    "Vaihinger", "Germany",
    "Pure German blackcurrant juice. Rich, tart and deeply fruity with intense berry character.",
    ["blackcurrant", "tart", "rich", "berry", "intense"],
    "medium", "medium", "medium", "tart, rich, berry",
    PAIR_NUTS, ["soft drink", "juice", "blackcurrant", "german", "natural"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_026", "Vaihinger Tomate", "soft_drink", "tomato juice",
    "Vaihinger", "Germany",
    "Pure German tomato juice. Savoury, rich and full-bodied with authentic tomato flavour.",
    ["tomato", "savoury", "rich", "umami", "smooth"],
    "low", "very low", "medium", "savoury, smooth",
    PAIR_MEATY, ["soft drink", "juice", "tomato", "german", "savoury"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_027", "Granini Cranberry Saft", "soft_drink", "cranberry juice",
    "Granini", "Germany",
    "Premium cranberry juice. Tart, fruity and refreshing with a characteristic cranberry sharpness.",
    ["cranberry", "tart", "fruity", "sharp", "refreshing"],
    "medium-low", "medium", "light", "tart, sharp, fruity",
    PAIR_CITRUS, ["soft drink", "juice", "cranberry", "german", "premium"],
    carbonation="none",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_028", "YUNIQ Yuzu Lemonade", "soft_drink", "lemonade",
    "YUNIQ", "Germany",
    "Premium yuzu lemonade. Exotic Japanese citrus with a unique aromatic and tangy flavour, refreshing and sophisticated.",
    ["yuzu", "citrus", "aromatic", "tangy", "exotic"],
    "medium", "medium-low", "light", "aromatic, tangy",
    PAIR_CITRUS, ["soft drink", "lemonade", "yuzu", "premium", "exotic"],
    carbonation="medium-high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_029", "Spezi", "soft_drink", "cola-orange mix",
    "Spezi", "Germany",
    "Iconic German soft drink combining cola with orange flavour. Sweet, fruity and refreshing with a unique taste.",
    ["cola", "orange", "sweet", "fruity", "refreshing"],
    "high", "very low", "light", "sweet, fruity",
    PAIR_SALTY, ["soft drink", "cola", "orange", "german", "iconic", "caffeinated"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_030", "Red Bull", "soft_drink", "energy drink",
    "Red Bull", "Austria",
    "The iconic energy drink that gives you wings. Sweet, tangy with a distinctive taste and caffeine kick.",
    ["sweet", "tangy", "caffeine", "energising"],
    "high", "very low", "light", "sweet, tangy, stimulating",
    PAIR_SALTY, ["soft drink", "energy drink", "caffeinated", "stimulating", "iconic"],
    carbonation="high",     page=soft_page
))

drinks.append(make_soft(
    "pub_softdrink_031", "Red Bull Sugarfree", "soft_drink", "energy drink",
    "Red Bull", "Austria",
    "Sugar-free version of the iconic energy drink with the same distinctive taste and caffeine kick, sweetened with sweeteners.",
    ["sweet", "tangy", "caffeine", "zero sugar"],
    "medium", "very low", "light", "sweet, tangy, stimulating",
    PAIR_SALTY, ["soft drink", "energy drink", "caffeinated", "zero sugar", "stimulating"],
    carbonation="high",     page=soft_page
))

# =============================================================================
# ADDITIONAL TANKBUSTER CANS (from Tankbuster Dosen.pdf)
# =============================================================================
tank_page = 1  # starting page in Tankbuster Dosen.pdf

drinks.append(make_spirit(
    "pub_beer_143", "Tankbusters The Book of Hops Vol.9: Superdelic - Alora", "beer", "new england ipa",
    "Tankbusters", 6.1, "Poland",
    "DDH Dual Hop NEIPA featuring Superdelic and Alora hops. A double dry-hopped New England IPA bursting with intense hop character.",
    ["tropical", "citrus", "hoppy", "intense", "hazy"],
    "medium-low", "medium", "medium", "smooth, hoppy",
    PAIR_SPICY, ["neipa", "ddh", "can", "polish", "craft", "hazy"],
    carbonation="medium",     page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_144", "Tankbusters All My Heroes Are Dead", "beer", "session neipa",
    "Tankbusters", 5.5, "Poland",
    "A tribute to the 80's and 90's. Session version of New England DDH with a mix of Citra and Cascade hops. Nostalgic IPA — Bitter-Smooth-Tropical.",
    ["tropical", "citrus", "bitter", "smooth", "nostalgic"],
    "medium-low", "medium", "medium", "bitter, smooth, tropical",
    PAIR_SPICY, ["neipa", "session", "can", "polish", "craft", "citra"],
    carbonation="medium",
    page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_145", "Tankbusters Follow the Light", "beer", "west coast ipa",
    "Tankbusters", 4.8, "Poland / UK",
    "A truly refreshing West Coast IPA with unmistakable herbalism in both aroma and taste. Hopped with Citra, Nectaron and Harlequin U.K. varieties. Collaboration brew with Abbeydale U.K.",
    ["herbal", "citrus", "refreshing", "hoppy", "crisp"],
    "low", "medium", "medium", "crisp, herbal",
    PAIR_SPICY, ["west coast ipa", "can", "polish", "collaboration", "craft"],
    carbonation="medium",
    page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_146", "Tankbusters Citrus Smash", "beer", "fruited ipa",
    "Tankbusters", 5.0, "Poland",
    "Mandarin Oat IPA. Brewed with Azacca BBC, Citra Cryo, Hallertauer Blanc and real mandarin juice. A fruited IPA with bright citrus punch and smooth oat body.",
    ["mandarin", "citrus", "fruity", "smooth", "bright"],
    "medium", "medium-low", "medium", "fruity, citrus, smooth",
    PAIR_SPICY, ["ipa", "fruited", "can", "polish", "craft", "citrus"],
    carbonation="medium",
    page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_147", "Tankbusters Prankster (2025)", "beer", "new england ipa",
    "Tankbusters", 5.5, "Poland",
    "NZ NEIPA brewed with Citra, Rakau, Mosaic, Wa-iti, Kohatu and Azacca hops. Birthday celebration brew with IBU Craft Beers from Gliwice. Tropical and juicy.",
    ["tropical", "citrus", "juicy", "hazy", "complex"],
    "medium", "medium-low", "medium", "juicy, tropical",
    PAIR_SPICY, ["neipa", "can", "polish", "nz hops", "craft", "celebratory"],
    carbonation="medium",     page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_148", "Tankbusters Hack'n'Slash 2", "beer", "west coast ipa",
    "Tankbusters", 6.5, "Poland",
    "Distinct, hoppy West Coast IPA with intense bitterness. Balanced citrus, pine and resin notes blend with grapefruit and tropical fruit aromas. Bright golden color, clean texture — classic American style.",
    ["grapefruit", "pine", "resin", "citrus", "tropical"],
    "low", "high", "medium", "bitter, piney, resinous",
    PAIR_SPICY, ["west coast ipa", "can", "polish", "bitter", "craft"],
    carbonation="medium",
    page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_149", "Tankbusters Introduction Vol. 2 Canadian IPA", "beer", "india pale ale",
    "Tankbusters", 5.6, "Poland",
    "Top-fermented IPA combining classic IPA features with a unique Canadian twist. Dominated by fruity notes of mandarin, pineapple and peach, balanced with a distinct but pleasant bitterness.",
    ["mandarin", "pineapple", "peach", "fruity", "balanced"],
    "medium", "medium", "medium", "fruity, balanced bitter",
    PAIR_SPICY, ["ipa", "can", "polish", "canadian", "fruity", "craft"],
    carbonation="medium",
    page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_150", "Tankbusters The Crown Is Mine", "beer", "india pale ale",
    "Tankbusters", 5.8, "Poland",
    "IPA showcasing three forms of Citra hops: Citra Lupomax, Citra BBC, and Citra Spectrum. An intense celebration of the Citra hop.",
    ["citra", "citrus", "hoppy", "intense", "bright"],
    "low", "medium-high", "medium", "hoppy, citrus",
    PAIR_SPICY, ["ipa", "can", "polish", "citra", "craft", "hoppy"],
    carbonation="medium",     page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_151", "Tankbusters Musashi's Legacy", "beer", "japanese ipa",
    "Tankbusters", 5.0, "Poland",
    "DDH Japanese IPA combining modern brewing techniques with Japanese precision. Double dry-hopped for rich aroma of citrus, pineapple and subtle floral notes. Light golden, intense yet balanced bitterness with fruity sweetness. Harmonious — bold yet refined.",
    ["citrus", "pineapple", "floral", "balanced", "refined"],
    "medium", "medium", "medium", "harmonious, refined",
    PAIR_SPICY, ["ipa", "ddh", "can", "polish", "japanese", "craft"],
    carbonation="medium",     page=tank_page
))

drinks.append(make_spirit(
    "pub_beer_152", "Browar Fortuna Miłosław Bezalkoholowe IPA", "beer", "non-alcoholic ipa",
    "Browar Fortuna", 0.5, "Miłosław, Poland",
    "A distinct IPA with hoppy aroma and flavour but without alcohol. Dry-hopped with Citra, Amarillo, Chinook and Lubelski hops. Sencha Earl Grey tea completes the citrus and resin profile.",
    ["citrus", "resin", "earl grey", "hoppy", "tea"],
    "low", "medium", "medium", "citrus, resin, tea",
    PAIR_SPICY, ["alcohol-free", "ipa", "can", "polish", "tea", "craft"],
    carbonation="medium",     page=tank_page
))

# =============================================================================
# SCOTTISH WHISKY - Lower Shelf (page 2-3 of Whiskeys PDF)
# =============================================================================
scotch_page = 2

drinks.append(make_spirit(
    "pub_whisky_001", "Ardbeg 10 Year Old", "whisky", "islay single malt",
    "Ardbeg", 46.0, "Islay, Scotland",
    "Revered around the world as the peatiest, smokiest, most complex single malt of them all. Yet it does not flaunt the peat; rather it gives way to the natural sweetness of the malt to produce a whisky of perfect balance. Named World Whisky of the Year in 2008.",
    ["peat", "smoke", "sweet malt", "complex", "balanced"],
    "medium-low", "medium", "full", "smoky, long, balanced", PAIR_MEATY,
    ["scotch", "islay", "single malt", "peated", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_002", "Bowmore 12 Years Old", "whisky", "islay single malt",
    "Bowmore", 40.0, "Islay, Scotland",
    "Puffs of peat smoke and pools of honey, sharpened by lemon zest. Both complex and perfectly balanced. Subtle lemon and sweet heather honey complement Bowmore's trademark peat smoke, leading to a delicious, long and mellow finish.",
    ["peat smoke", "honey", "lemon", "heather", "mellow"],
    "medium", "medium-low", "medium", "long, mellow, smoky-sweet", PAIR_CHEESE,
    ["scotch", "islay", "single malt", "peated", "balanced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_003", "Cragganmore 12 Years Old", "whisky", "speyside single malt",
    "Cragganmore", 40.0, "Speyside, Scotland",
    "Hugely complex with a combination of sweet floral fragrances, riverside herbs and flowers with honey and vanilla. Strong malty taste with hints of sweet wood smoke and sandalwood. Long, malt-driven finish with light smoke.",
    ["floral", "honey", "vanilla", "malt", "sandalwood"],
    "medium", "low", "medium", "long, malt-driven, light smoke", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "floral", "complex"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_004", "Glendronach 12 Years Old", "whisky", "highland single malt",
    "Glendronach", 43.0, "Highlands, Scotland",
    "Superb richly sherry casked single malt matured for at least 12 years in a combination of the finest Spanish Pedro Ximénez and Oloroso sherry casks. Natural colour, sweet, creamy dram.",
    ["sherry", "sweet", "creamy", "dried fruit", "rich"],
    "medium-high", "very low", "medium-full", "sweet, creamy, sherried", PAIR_CHEESE,
    ["scotch", "highland", "single malt", "sherry cask", "creamy"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_005", "Glenfarclas 10 Years Old", "whisky", "speyside single malt",
    "Glenfarclas", 40.0, "Speyside, Scotland",
    "Sweet, quite light, pleasant. Oranges and brown sugar/caramel, mixed with mocha and sugared cereals. A little vanilla. An approachable Speyside dram.",
    ["orange", "caramel", "mocha", "cereal", "vanilla"],
    "medium", "low", "light", "sweet, light, smooth", PAIR_NUTS,
    ["scotch", "speyside", "single malt", "sweet", "approachable"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_006", "Glenlivet 12 Years Old Double Oak", "whisky", "speyside single malt",
    "The Glenlivet", 40.0, "Speyside, Scotland",
    "One of the most popular malts in the world. Matured in traditional oak, then American oak casks that impart notes of vanilla and give the whisky its distinctive smoothness.",
    ["vanilla", "oak", "smooth", "honey", "fruity"],
    "medium", "low", "medium", "smooth, vanilla, oaky", PAIR_NUTS,
    ["scotch", "speyside", "single malt", "classic", "smooth"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_007", "Glenmorangie Original 10 Years Old", "whisky", "highland single malt",
    "Glenmorangie", 40.0, "Highlands, Scotland",
    "Known for its mellow tones and delicacy of flavour. A smooth whisky which welcomes you with a rush of citrus, then holds your attention with layers of luscious flavour, from orange to honey and creamy vanilla, with bursts of peach.",
    ["citrus", "orange", "honey", "vanilla", "peach"],
    "medium", "low", "medium", "mellow, creamy, fruity", PAIR_CHEESE,
    ["scotch", "highland", "single malt", "mellow", "classic"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_008", "Isle of Jura 10 Years Old", "whisky", "island single malt",
    "Isle of Jura", 40.0, "Jura, Scotland",
    "Crafted in exceptionally tall stills, matured for 10 years in American White Oak ex-bourbon barrels and finished in Oloroso Sherry casks from Jerez. Sweet, smooth with flavours of rich dark chocolate and vanilla cream.",
    ["dark chocolate", "vanilla cream", "sherry", "sweet", "smooth"],
    "medium", "low", "medium", "sweet, smooth, chocolate", PAIR_CHEESE,
    ["scotch", "island", "single malt", "sherry finish", "smooth"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_009", "Johnnie Walker Black Label", "whisky", "blended scotch",
    "Johnnie Walker", 40.0, "Scotland",
    "Blended to perfection using single malt and grain whiskies from more than 29 distilleries, spending 12 years in a cask growing into a vibrant body of flavour. Rich, smooth and complex.",
    ["rich", "smooth", "smoky", "fruity", "vanilla"],
    "medium", "low", "medium", "smooth, rich, complex", PAIR_MEATY,
    ["scotch", "blended", "classic", "smooth", "complex"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_010", "Laphroaig 10 Years Old", "whisky", "islay single malt",
    "Laphroaig", 40.0, "Islay, Scotland",
    "Full-bodied single malt with a surprising sweetness leading into a long, warming finish. Complicated notes of smoke, seaweed, peat and a hint of salt — like a bracing day on Scotland's rugged coast.",
    ["peat", "smoke", "seaweed", "salt", "sweet"],
    "medium-low", "medium", "full", "long, warming, medicinal", PAIR_MEATY,
    ["scotch", "islay", "single malt", "peated", "iconic"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_011", "Monkey Shoulder Batch 27", "whisky", "blended malt scotch",
    "Monkey Shoulder", 40.0, "Speyside (Highland), Scotland",
    "A blend of malt whiskies from Speyside, selected in small batches and married together. Zesty orange, vanilla, honey and spiced oak on the nose. Mellow vanilla with spicy hints on the palate.",
    ["orange", "vanilla", "honey", "spiced oak", "mellow"],
    "medium", "low", "medium", "mellow, spicy, smooth", PAIR_NUTS,
    ["scotch", "blended malt", "speyside", "smooth", "spiced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_012", "Old Pulteney 12 Years Old", "whisky", "highland single malt",
    "Old Pulteney", 40.0, "Highlands, Scotland",
    "Winner of numerous gold medals. Dry, medium-bodied and smooth, redolent of honey and cream, faintly salty with a slight spicy note and a sweet long-lasting finish. The maritime malt.",
    ["honey", "cream", "salty", "spicy", "sweet"],
    "medium", "low", "medium", "sweet, long-lasting, maritime", PAIR_CHEESE,
    ["scotch", "highland", "single malt", "maritime", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_013", "The Singleton 12 Years Old", "whisky", "speyside single malt",
    "The Singleton", 40.0, "Speyside, Scotland",
    "Whisky from both Pedro Ximenez Oloroso seasoned casks and refill ex-bourbon casks hand selected for honey notes and nutty intensity. Soft cooked apples, luscious brown sugar, hints of creamy coffee and roasted nutty notes.",
    ["honey", "nutty", "cooked apple", "brown sugar", "coffee"],
    "medium", "low", "medium", "creamy, nutty, sweet", PAIR_NUTS,
    ["scotch", "speyside", "single malt", "honey", "nutty"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_014", "Isle of Jura Rum Cask Finish", "whisky", "island single malt",
    "Isle of Jura", 40.0, "Jura, Scotland",
    "Jura Cask Editions celebrate the connection between land and spirit. This rum cask edition explores Caribbean cask finishes. Mouth-wateringly smooth, vibrant whisky delivering flavours of sweet vanilla, fudge, coconut and spiced tropical notes.",
    ["vanilla", "fudge", "coconut", "spiced", "tropical"],
    "medium-high", "low", "medium", "smooth, tropical, sweet", PAIR_NUTS,
    ["scotch", "island", "single malt", "rum cask", "tropical"],
    page=scotch_page
))

# =============================================================================
# SCOTTISH WHISKY - Middle Shelf (pages 4-5)
# =============================================================================
drinks.append(make_spirit(
    "pub_whisky_015", "Aberlour 12 Years Old", "whisky", "speyside single malt",
    "Aberlour", 48.0, "Speyside, Scotland",
    "Rich with a citrus character. Traditional Oak and seasoned Sherry butts are both used to great effect, as the mellowed spirits within are combined to deliver a subtly balanced flavour.",
    ["citrus", "sherry", "oak", "balanced", "mellow"],
    "medium", "low", "medium-full", "balanced, citrus, sherried", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "sherry cask", "balanced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_016", "Balvenie 12 Years Old DoubleWood", "whisky", "speyside single malt",
    "The Balvenie", 40.0, "Speyside, Scotland",
    "Gains its distinctive character from being matured in two different wood types. Each stage lends different qualities. Pioneered the 'wood finishing' technique in 1982, launched 1993.",
    ["vanilla", "oak", "honey", "spice", "smooth"],
    "medium", "low", "medium", "smooth, woody, honeyed", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "wood finish", "classic"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_017", "Ardbeg Uigeadail", "whisky", "islay single malt",
    "Ardbeg", 54.2, "Islay, Scotland",
    "A special vatting that marries Ardbeg's traditional deep, smoky notes with luscious, raisiny tones of old ex-Sherry casks. Voted favourite Ardbeg by the 120,000+ strong Ardbeg Committee. Full flavoured and rich with winter spices, honey glazed smoke and chewy treacle. Waves of deep smoky tones like a fine Montecristo cigar.",
    ["peat", "smoke", "sherry", "raisin", "spice"],
    "medium", "medium", "full", "smoky, rich, spicy, long", PAIR_MEATY,
    ["scotch", "islay", "single malt", "cask strength", "sherry", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_018", "Bowmore 15 Years Old", "whisky", "islay single malt",
    "Bowmore", 43.0, "Islay, Scotland",
    "Rich raisins and gentle smoke lead to a delicious chocolaty centre. Matured first in bourbon barrels then Oloroso casks — the final three years in Oloroso sherry casks give the rich, deep colour and robust warming finish.",
    ["raisin", "chocolate", "smoke", "sherry", "warming"],
    "medium", "medium-low", "medium-full", "robust, warming, chocolaty", PAIR_CHEESE,
    ["scotch", "islay", "single malt", "sherry finish", "complex"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_019", "Glenfiddich 15 Years Old", "whisky", "speyside single malt",
    "Glenfiddich", 40.0, "Speyside, Scotland",
    "Matured using the Solera process in oloroso sherry, bourbon and new oak casks. Delicious single malt with fine extracts of honey and vanilla. Delicate flavours beautifully integrated and fresh.",
    ["honey", "vanilla", "oak", "sherry", "fresh"],
    "medium", "low", "medium", "delicate, integrated, fresh", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "solera", "balanced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_020", "Glenkinchie 12 Years Old", "whisky", "lowland single malt",
    "Glenkinchie", 43.0, "Lowlands, Scotland",
    "Very aromatic and flowery, like breathing in a country garden. Noticeable vanilla, cut flowers — daffodil, blossom and hints of lily — and a clean, toasty note beneath. Becomes increasingly sweet and creamy with fresh citrus.",
    ["floral", "vanilla", "toasty", "citrus", "creamy"],
    "medium", "very low", "medium", "sweet, creamy, floral", PAIR_CHEESE,
    ["scotch", "lowland", "single malt", "floral", "delicate"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_021", "Glenmorangie The Lasanta 12 Years Old", "whisky", "highland single malt",
    "Glenmorangie", 43.0, "Highlands, Scotland",
    "Begins with giraffe-high stills yielding a delicate and fruity spirit, then matured in bourbon and sherry casks for 12 years. A mouth-watering odyssey bursting with rich spiciness and sun-drenched sweetness.",
    ["spicy", "sherry", "dried fruit", "orange", "chocolate"],
    "medium-high", "low", "medium-full", "rich, spicy, sweet", PAIR_CHEESE,
    ["scotch", "highland", "single malt", "sherry finish", "spicy"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_022", "Bruichladdich The Classic Laddie", "whisky", "islay single malt",
    "Bruichladdich", 50.0, "Islay, Scotland",
    "The definitive Bruichladdich. Showcasing the classic, floral and elegant house style. Made from 100% Scottish barley, trickle distilled, non-chill filtered and colouring free.",
    ["floral", "elegant", "malty", "maritime", "fresh"],
    "medium-low", "low", "medium", "elegant, floral, clean", PAIR_CHEESE,
    ["scotch", "islay", "single malt", "unpeated", "artisanal"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_023", "Glenmorangie The Quinta Ruban 14 Years Old", "whisky", "highland single malt",
    "Glenmorangie", 46.0, "Highlands, Scotland",
    "A whisky journey into the wild. Begins soft and fruity, then aged 14 years in bourbon casks and port casks from Portugal. Walnut and black pepper, mandarin orange and melted marshmallow, dark chocolate and peppermint.",
    ["walnut", "mandarin orange", "dark chocolate", "peppermint", "port"],
    "medium", "medium-low", "medium-full", "complex, chocolate-minty", PAIR_CHEESE,
    ["scotch", "highland", "single malt", "port finish", "complex"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_024", "Highland Park 12 Years Old", "whisky", "island single malt",
    "Highland Park", 40.0, "Orkney, Scotland",
    "Spicy and well-rounded, packed with flavours of sun-kissed Seville oranges and rich fruitcake spiced with cinnamon, nutmeg and cloves. Molten heather honey in waves of heathery peat smoke.",
    ["seville orange", "fruitcake", "cinnamon", "nutmeg", "heather honey"],
    "medium", "medium-low", "medium", "spicy, well-rounded, heather smoke", PAIR_MEATY,
    ["scotch", "island", "single malt", "orkney", "balanced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_025", "Glenfarclas 12 Years Old", "whisky", "speyside single malt",
    "Glenfarclas", 43.0, "Speyside, Scotland",
    "Lots of sherry and honey on the nose with subtle hints of spice, oak and smoke. Medium-bodied mouthful. Sherry sweetness immediately comes through with fruitcake, raisins, oak and spice. Beautifully balanced.",
    ["sherry", "honey", "raisin", "oak", "spice"],
    "medium", "low", "medium", "balanced, sherried, fruity", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "sherry", "balanced"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_026", "Kilchoman Sanaig", "whisky", "islay single malt",
    "Kilchoman", 46.0, "Islay, Scotland",
    "Named after an inlet on Islay's rugged Atlantic coast. Vatting of both sherry and bourbon casks. High proportion of Oloroso sherry influence adding dried fruits and spices to classic Kilchoman citrus sweetness and peat smoke character.",
    ["peat smoke", "citrus", "dried fruit", "spice", "sherry"],
    "medium", "medium", "medium-full", "smoky, sherried, spiced", PAIR_MEATY,
    ["scotch", "islay", "single malt", "sherry cask", "peated"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_027", "Harvey's Lewes Blend", "whisky", "blended scotch",
    "Harvey's Brewery", 43.4, "Lewes, England",
    "Over a hundred years ago Harvey's Brewery were blending and bottling spirits. This succession of the original blend celebrates continuing passion for the finest spirits. Rated 89.5/100 in Jim Murray's Whisky Bible.",
    ["balanced", "smooth", "malty", "classic", "heritage"],
    "medium", "low", "medium", "smooth, classic, balanced", PAIR_CHEESE,
    ["scotch", "blended", "english", "heritage", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_028", "Oban 14 Years Old Single Malt", "whisky", "highland single malt",
    "Oban", 43.0, "Highlands, Scotland",
    "Flavours of orange peel, smoke, sea salt, and honey distinguish this full-bodied highland malt. Maritime and rich.",
    ["orange peel", "smoke", "sea salt", "honey", "maritime"],
    "medium", "medium-low", "medium-full", "full-bodied, maritime, smoky", PAIR_MEATY,
    ["scotch", "highland", "single malt", "maritime", "classic"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_029", "Mortlach 12 Year Old", "whisky", "speyside single malt",
    "Mortlach", 43.4, "Speyside, Scotland",
    "An ode to the 'Wee Witchie', Mortlach's smallest yet most essential still. Double cask matured in both European and American oak to enhance the distinctively rich and robust character that makes Mortlach whiskies legendary.",
    ["rich", "robust", "oak", "spicy", "meaty"],
    "medium", "medium", "full", "rich, robust, oaky", PAIR_MEATY,
    ["scotch", "speyside", "single malt", "rich", "double cask"],
    page=scotch_page
))

# =============================================================================
# SCOTTISH WHISKY - Top Shelf (pages 6-7)
# =============================================================================
drinks.append(make_spirit(
    "pub_whisky_030", "Caol Ila 18 Years Old", "whisky", "islay single malt",
    "Caol Ila", 43.0, "Islay, Scotland",
    "Mellow, golden and sweetly smoky, evoking the sun sinking low over the dying embers of a beach bonfire. The hidden treasure of Islay, pronounced 'Cull Eela'. Fine, smoky whisky from the rugged eastern coast.",
    ["smoke", "mellow", "sweet", "maritime", "golden"],
    "medium", "medium-low", "medium", "sweetly smoky, mellow, long", PAIR_MEATY,
    ["scotch", "islay", "single malt", "aged", "refined"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_031", "Lagavulin 16 Years Old", "whisky", "islay single malt",
    "Lagavulin", 43.0, "Islay, Scotland",
    "Aged in oak casks for at least 16 years, this much sought-after Single Malt has the massive peat-smoke flavour that's typical of southern Islay, while also offering richness and a dryness that turns it into a truly interesting dram.",
    ["peat", "smoke", "rich", "dry", "complex"],
    "low", "medium", "full", "dry, smoky, rich, long", PAIR_MEATY,
    ["scotch", "islay", "single malt", "classic", "peated"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_032", "Highland Park 18 Years Old", "whisky", "island single malt",
    "Highland Park", 43.0, "Orkney, Scotland",
    "Matured in first-fill sherry seasoned European and American oak casks. A sophisticated medley of ripe cherries dusted with bittersweet cocoa, freshly harvested honeycomb and candied orange peel. A whisper of Orkney's salty seaspray in aromatic peat smoke.",
    ["cherry", "cocoa", "honeycomb", "orange peel", "peat smoke"],
    "medium", "medium-low", "full", "sophisticated, salty, smoky", PAIR_MEATY,
    ["scotch", "island", "single malt", "orkney", "premium", "aged"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_033", "Lagavulin 2022 Distillers Edition", "whisky", "islay single malt",
    "Lagavulin", 43.0, "Islay, Scotland",
    "A limited Distillers Edition with two-parted maturation for more depth and complexity. Personally selected casks perfectly matched to Lagavulin's character. Preserving the perfection of the original while strongly accentuating selected taste nuances.",
    ["peat", "smoke", "complex", "rich", "sherry"],
    "low", "medium", "full", "deep, complex, smoky, long", PAIR_MEATY,
    ["scotch", "islay", "single malt", "distillers edition", "limited"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_034", "Six Kingdoms Mortlach 15 Year Special Edition", "whisky", "speyside single malt",
    "Mortlach", 46.0, "Speyside, Scotland",
    "Game of Thrones Six Kingdoms special edition. Aged 15 years, presented in a metallic gold canister featuring the Three-Eyed Raven. Mortlach's signature 2.81 times distillation process, as complex and unique as the Three-Eyed Raven itself.",
    ["rich", "complex", "fruity", "spicy", "meaty"],
    "medium", "medium", "full", "complex, rich, meaty", PAIR_MEATY,
    ["scotch", "speyside", "single malt", "game of thrones", "special edition"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_035", "Talisker 18 Year Old", "whisky", "island single malt",
    "Talisker", 45.8, "Isle of Skye, Scotland",
    "Wonderful sweetness and warmth, intertwined with just a thread of smoke. Rich and soft but still assertive. Named 'Best Single Malt Whisky in the World 2007' at the World Whiskies Awards. A single malt masterpiece.",
    ["smoke", "pepper", "sweet", "maritime", "warming"],
    "medium", "medium", "full", "warming, smoky, peppery, long", PAIR_MEATY,
    ["scotch", "island", "single malt", "skye", "award-winning", "aged"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_036", "Royal Salute 21 Year The Signature Blend", "whisky", "blended scotch",
    "Royal Salute", 40.0, "Scotland",
    "Crafted in celebration of Queen Elizabeth II's Coronation. A selection of rare and exceptional Scotch whiskies aged for a minimum of 21 years. Sophisticated and opulent, housed in an iconic sapphire blue flagon. Multi award-winning blend unchanged since 1953.",
    ["elegant", "rich", "floral", "fruity", "opulent"],
    "medium", "low", "full", "opulent, elegant, regal", PAIR_CHEESE,
    ["scotch", "blended", "premium", "royal", "aged", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_037", "The Glenlivet 18 Year Batch Reserve", "whisky", "speyside single malt",
    "The Glenlivet", 40.0, "Speyside, Scotland",
    "Over 18 years, the Master Distiller takes this expression through first and second-fill American oak (for tropical fruitiness) and ex-sherry oak (for spicy complexity). Complex, yet elegant and balanced. Won more awards than any other Glenlivet expression.",
    ["tropical fruit", "spicy", "oak", "elegant", "balanced"],
    "medium", "low", "medium", "elegant, complex, balanced", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "aged", "award-winning"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_038", "Mortlach 16 Year Old", "whisky", "speyside single malt",
    "Mortlach", 43.4, "Speyside, Scotland",
    "Inspired by the iconic first bottling of the 16-year-old released in 1992. Matured in only Sherry casks to impart rich, fruity, and fragrant notes atop the beasty complexity synonymous with Mortlach.",
    ["sherry", "fruity", "fragrant", "rich", "complex"],
    "medium", "medium", "full", "rich, sherried, complex", PAIR_MEATY,
    ["scotch", "speyside", "single malt", "sherry cask", "aged"],
    page=scotch_page
))

drinks.append(make_spirit(
    "pub_whisky_039", "Glenfiddich 18 Year Small Batch", "whisky", "speyside single malt",
    "Glenfiddich", 40.0, "Speyside, Scotland",
    "Married in small batches of no more than 150 casks, each individually numbered. Remarkably rich aroma with ripe orchard fruit, baked apple and robust oak. Luxurious dried fruit, candy peel and dates with elegant oak notes. Warming, distinguished finish.",
    ["orchard fruit", "baked apple", "oak", "dried fruit", "date"],
    "medium", "low", "medium-full", "warming, distinguished, oaky", PAIR_CHEESE,
    ["scotch", "speyside", "single malt", "small batch", "aged"],
    page=scotch_page
))

# =============================================================================
# IRISH WHISKEY (page 8)
# =============================================================================
irish_page = 8

drinks.append(make_spirit(
    "pub_whisky_040", "Bushmills 10 Year Old", "irish_whiskey", "single malt irish whiskey",
    "Bushmills", 40.0, "Bushmills, Northern Ireland",
    "A marriage of single malts matured for at least 10 years in hand-selected bourbon barrels and sherry butts. Zesty and fresh on the nose, followed by notes of ripe fruit, creamy vanilla and soft toasted wood.",
    ["ripe fruit", "vanilla", "toasted wood", "zesty", "creamy"],
    "medium", "very low", "medium", "creamy, smooth, toasted", PAIR_CHEESE,
    ["irish", "single malt", "aged", "smooth", "triple distilled"],
    page=irish_page
))

drinks.append(make_spirit(
    "pub_whisky_041", "Bushmills Black Bush", "irish_whiskey", "blended irish whiskey",
    "Bushmills", 40.0, "Bushmills, Northern Ireland",
    "Combines a high amount of single malt whiskey matured in former Oloroso sherry casks with a sweet, batch-distilled grain whiskey. Rich, fruity notes and a deep intense character, balanced by incredible smoothness.",
    ["sherry", "fruity", "rich", "intense", "smooth"],
    "medium", "low", "medium-full", "rich, smooth, sherried", PAIR_CHEESE,
    ["irish", "blended", "sherry cask", "rich", "smooth"],
    page=irish_page
))

drinks.append(make_spirit(
    "pub_whisky_042", "Bushmills Original", "irish_whiskey", "blended irish whiskey",
    "Bushmills", 40.0, "Bushmills, Northern Ireland",
    "The cornerstone of the Bushmills family. A smooth and versatile triple distilled blend matured in both bourbon and sherry casks resulting in fresh fruit and vanilla notes.",
    ["fresh fruit", "vanilla", "malt", "smooth", "balanced"],
    "medium", "low", "light-medium", "smooth, fresh, balanced", PAIR_NUTS,
    ["irish", "blended", "triple distilled", "smooth", "classic"],
    page=irish_page
))

drinks.append(make_spirit(
    "pub_whisky_043", "Jameson", "irish_whiskey", "blended irish whiskey",
    "Jameson", 40.0, "Cork, Ireland",
    "A light floral fragrance, peppered with spicy wood and sweet notes. The perfect balance of spicy, nutty and vanilla notes with hints of sweet sherry and exceptional smoothness.",
    ["floral", "spicy wood", "nutty", "vanilla", "sherry"],
    "medium", "low", "medium", "smooth, balanced, nutty", PAIR_NUTS,
    ["irish", "blended", "triple distilled", "classic", "smooth"],
    page=irish_page
))

drinks.append(make_spirit(
    "pub_whisky_044", "Paddy", "irish_whiskey", "blended irish whiskey",
    "Paddy", 40.0, "Cork, Ireland",
    "Triple distilled the same way in County Cork for nearly a quarter-millennium. Malty, fresh, and woody with hints of spice, honey and vanilla on the nose. Light and crisp taste with hints of nuts, malt and charred wood.",
    ["malty", "woody", "honey", "vanilla", "nutty"],
    "medium", "very low", "light", "light, crisp, charred", PAIR_NUTS,
    ["irish", "blended", "triple distilled", "heritage", "crisp"],
    page=irish_page
))

drinks.append(make_spirit(
    "pub_whisky_045", "Tullamore Dew", "irish_whiskey", "blended irish whiskey",
    "Tullamore Dew", 40.0, "Tullamore, Ireland",
    "The original triple blend Irish whiskey known the world over for its smooth and gentle complexity. Derived from three types of grain, triple distillation and the blend of all three Irish whiskeys. Complex yet approachable.",
    ["malt", "grain", "gentle", "complex", "smooth"],
    "medium", "low", "medium", "smooth, gentle, complex", PAIR_NUTS,
    ["irish", "blended", "triple distilled", "classic", "smooth"],
    page=irish_page
))

# =============================================================================
# BOURBON & TENNESSEE WHISKEY (pages 9-10)
# =============================================================================
bourbon_page = 9

drinks.append(make_spirit(
    "pub_whisky_046", "Four Roses", "bourbon", "kentucky straight bourbon",
    "Four Roses", 40.0, "Kentucky, USA",
    "Smooth and mellow Bourbon with a long and soft finish. Unique aromas and flavours for cocktails, on the rocks, or with a splash. A worldwide favourite.",
    ["caramel", "vanilla", "oak", "mellow", "smooth"],
    "medium", "low", "medium", "long, soft, mellow", PAIR_MEATY,
    ["bourbon", "kentucky", "american", "smooth", "classic"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_047", "Jack Daniel's Old No. 7", "bourbon", "tennessee whiskey",
    "Jack Daniel's", 40.0, "Lynchburg, Tennessee, USA",
    "Mellowed drop by drop through 10-feet of sugar maple charcoal, then matured in handcrafted barrels. Judged by look, aroma and taste as Jack Daniel himself did it over a century ago.",
    ["caramel", "vanilla", "charcoal", "oak", "mellow"],
    "medium", "low", "medium", "mellow, smooth, classic", PAIR_MEATY,
    ["tennessee whiskey", "american", "charcoal mellowed", "classic", "iconic"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_048", "Jim Beam", "bourbon", "kentucky straight bourbon",
    "Jim Beam", 40.0, "Kentucky, USA",
    "Elegant, smooth, refined. Four years of aging in newly charred American white oak barrels. Every drop is worth the effort, sticking to the great-great-grandfather's recipe.",
    ["caramel", "vanilla", "oak", "smooth", "classic"],
    "medium", "low", "medium", "smooth, oaky, refined", PAIR_MEATY,
    ["bourbon", "kentucky", "american", "classic", "smooth"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_049", "Jim Beam Devil's Cut", "bourbon", "kentucky straight bourbon",
    "Jim Beam", 45.0, "Kentucky, USA",
    "The liquid extracted from the barrel wood is blended with extra-aged Kentucky straight bourbon whiskey and bottled at 90 proof. Premium bourbon with extra depth and complexity. Robust flavour with deep colour, aroma and character.",
    ["caramel", "oak", "vanilla", "robust", "complex"],
    "medium-low", "medium", "medium-full", "robust, deep, oaky", PAIR_MEATY,
    ["bourbon", "kentucky", "american", "premium", "robust"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_050", "Knob Creek", "bourbon", "kentucky straight bourbon",
    "Knob Creek", 50.0, "Kentucky, USA",
    "Patiently aged in white oak barrels. Unflinching balance of deep, pre-Prohibition-style bourbon with a robust oak taste, complemented with hints of smooth vanilla and layered caramel. Full flavour.",
    ["oak", "vanilla", "caramel", "robust", "deep"],
    "medium-low", "medium", "full", "robust, oaky, vanilla", PAIR_MEATY,
    ["bourbon", "kentucky", "american", "premium", "full-bodied"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_051", "Jack Daniel's Tennessee Fire", "bourbon", "flavoured whiskey",
    "Jack Daniel's", 35.0, "Lynchburg, Tennessee, USA",
    "Warm cinnamon liqueur blended with the bold character of Jack Daniel's Old No. 7 for a classic spirit with a surprisingly warm finish.",
    ["cinnamon", "spicy", "warming", "sweet", "smooth"],
    "high", "very low", "medium", "warm, cinnamon, sweet", PAIR_SPICY,
    ["tennessee whiskey", "flavoured", "cinnamon", "sweet", "warming"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_052", "Jack Daniel's Tennessee Apple", "bourbon", "flavoured whiskey",
    "Jack Daniel's", 35.0, "Lynchburg, Tennessee, USA",
    "The unique character of Jack Daniel's Tennessee Whiskey coupled with crisp green apple for a fresh and rewarding taste. Bold, refreshing, and exceptionally smooth.",
    ["green apple", "crisp", "sweet", "smooth", "refreshing"],
    "medium-high", "very low", "light-medium", "crisp, apple, smooth", PAIR_SALTY,
    ["tennessee whiskey", "flavoured", "apple", "sweet", "smooth"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_053", "Jack Daniel's Tennessee Rye", "bourbon", "tennessee rye whiskey",
    "Jack Daniel's", 45.0, "Lynchburg, Tennessee, USA",
    "Rye whiskey made Jack's way. Crafted with 70-percent rye grain bill, natural spring water from Cave Spring Hollow, and Jack's time-honored charcoal mellowing process. Only from Lynchburg, Tennessee.",
    ["rye", "spicy", "pepper", "charcoal", "bold"],
    "low", "medium-high", "medium", "spicy, bold, mellowed", PAIR_MEATY,
    ["tennessee whiskey", "rye", "american", "charcoal mellowed", "bold"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_054", "Jack Daniel's Single Barrel Select", "bourbon", "tennessee whiskey",
    "Jack Daniel's", 47.0, "Lynchburg, Tennessee, USA",
    "Bottled at 94-proof. Layers subtle notes of caramel and spice with bright fruit notes and sweet aromatics for a Tennessee Whiskey with one-of-a-kind flavor.",
    ["caramel", "spice", "bright fruit", "sweet", "complex"],
    "medium", "medium", "medium-full", "complex, caramel, spicy", PAIR_MEATY,
    ["tennessee whiskey", "single barrel", "premium", "american", "complex"],
    page=bourbon_page
))

drinks.append(make_spirit(
    "pub_whisky_055", "Woodford Reserve", "bourbon", "kentucky straight bourbon",
    "Woodford Reserve", 43.2, "Kentucky, USA",
    "The art of making fine bourbon since 1812 on a National Historic Landmark site. Perfectly balanced taste comprised of more than 200 detectable flavor notes, from bold grain and wood to sweet aromatics, spice, and fruit & floral notes.",
    ["grain", "oak", "caramel", "spice", "fruit"],
    "medium", "medium", "medium", "balanced, complex, elegant", PAIR_MEATY,
    ["bourbon", "kentucky", "american", "premium", "historic", "complex"],
    page=bourbon_page
))

# =============================================================================
# WRITE ALL FILES
# =============================================================================
for d in drinks:
    write_json(d)

# Count by category
from collections import Counter
cats = Counter(d['category'] for d in drinks)
print(f"Generated {len(drinks)} drink JSON files in '{OUT}/'")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")
