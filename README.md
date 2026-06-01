
We are building a drink guide for an english pub. you need to look into the folder menu_files and check the menu files. Convert each drink in there into a single .json file with the proposed structure from the json-schema below. create a new folder for that. the food pairings must only contain snacks from the menu that are available to be served alongside. 



JSON-Structure:

{
  "id": "pub_drink_001",
  "name": "Fuller's London Pride",
  "category": "beer",
  "subcategory": "english ale",
  "brand_or_producer": "Fuller's Brewery",
  "abv": 4.7,
  "taste_profile": {
    "primary_notes": ["malty", "toasty", "smooth"],
    "sweetness": "medium",
    "bitterness": "medium-low",
    "body": "medium",
    "finish": "clean, slightly dry",
    "carbonation": "medium"
  },
  "origin": "London, England",
    "food_pairings": ["fish & chips", "ploughman's lunch", "roast beef"]

  "tags": ["cask", "session", "pub classic", "traditional", "balanced"],
  "notes": "Balanced malt-forward ale. Served from cask at natural temperature. Not filtered or pasteurised.",
  "metadata": {
    "source_page": 4,
    "extraction_confidence": 0.96,
    "verified_date": "2024-06-15"
  }
}
