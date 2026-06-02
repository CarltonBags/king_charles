import postgres from 'postgres'
import { configDotenv } from 'dotenv'

const connectionString = process.env.DATABASE_URL
const sql = postgres(connectionString)

export default sql
