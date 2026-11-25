# R-FACTOR Hackathon 2026 - Template Repository

## Kick-off (10:15 - 10:45)
1. Clona questo repo.
2. Copia `.env.example` in `.env` e inserisci le chiavi API.
3. Assegnazione ruoli:
   - **Junior 1 (Frontend)**: Inizia a sviluppare la UI nella cartella `/frontend` leggendo i dati mock in `/data/input`.
   - **Junior 2 (AI/Backend)**: Mette a punto i prompt in `/ai-core/prompts` e collega le chiamate API in `llm_client.py`.
   - **Senior**: Coordina, sblocca colli di bottiglia e compila i file in `/docs` per la giuria.

## Struttura
- `/data/input`: File JSON con i dati simulati per le 3 sfide.
- `/data/contracts`: Schema JSON che il frontend si aspetta dal motore AI.
- `/ai-core`: Wrapper per le chiamate LLM (OpenAI/Anthropic/Gemini/Ollama) e fallback offline.
- `/frontend`: (Da inizializzare) Streamlit o Next.js.
- `/docs`: File essenziali per le slide e il pitch.
