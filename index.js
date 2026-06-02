import fs from 'fs/promises'
import path from 'path'
import OpenAI from 'openai'
import pg from "pg"
import postgres from 'postgres'
import 'dotenv/config'






const processDocs = async () => {

    let sql
    try{
        sql = postgres(process.env.DATABASE_URL)
        console.log("successfully connected to vector store")

    }catch(e){
        throw new Error(`connection to vector store failed`)
    }

    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY
    })

    
    //create embedding 
    const DRINKS_DIR = "./drink_guide"

    const createEmbeddingText = (drink) =>{
        return `
                Drink: ${drink.name}

                Category_EN: ${drink.category}
                Subcategory_EN: ${drink.subcategory}

                Category_DE: ${drink.category_de}
                Subcategory_DE: ${drink.subcategory_de}

                Brand: ${drink.brand_or_producer}

                ABV: ${drink.abv}

                Taste:
                - Notes_EN: ${drink.taste_profile.primary_notes.join(", ")}
                - Notes_DE: ${drink.taste_profile.primary_notes_de.join(", ")}
                - Sweetness: ${drink.taste_profile.sweetness}
                - Bitterness: ${drink.taste_profile.bitterness}
                - Body: ${drink.taste_profile.body}
                - Finish: ${drink.taste_profile.finish}
                - Carbonation: ${drink.taste_profile.carbonation}

                Origin: ${drink.origin}

                Food Pairing: ${drink.food_pairings.join(", ")}

                Tags_EN: ${drink.tags.join(", ")}
                Tags_DE: ${drink.tags_de.join(", ")}

                Description_EN: ${drink.notes}
                Description_DE: ${drink.notes_de}

            `.trim()
    }

    const files = await fs.readdir(DRINKS_DIR)

    for (const file of files) {
        if(!file.endsWith(".json")) continue

        const filePath = path.join(DRINKS_DIR, file)
        const raw = await fs.readFile(filePath, "utf-8")
        const drink = JSON.parse(raw)
        console.log("drink:", drink)

        const embeddingText = createEmbeddingText(drink)
        console.log("embeddingText:", embeddingText)


        const res = await openai.embeddings.create({
            model: "text-embedding-3-small",
            input: embeddingText
        })

        const embedding = res.data[0].embedding;
        const embeddingString = `[${embedding.join(",")}]`

        await sql`
            insert into drinks (
                name,
                embedding,
                metadata
            )
            values (
                ${drink.name},
                ${embeddingString},
                ${sql.json(drink)}
            )
        `
        console.log("Inserted:", drink.name)
    }

}

processDocs()