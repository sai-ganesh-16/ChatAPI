# Notes & AI Chat API

### Setup
1. Clone repo and open in VS Code.
2. Create a `.env` file and add: `GROQ_API_KEY=your_key_here`
3. Install dependencies: `pip install -r requirements.txt`
4. Run server: `uvicorn main:app --reload`

### Testing
- Go to `http://127.0.0.1:8000/docs` to use the Swagger UI.
- Test the `/chat` endpoint by changing the `mode` parameter.
