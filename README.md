## AI Agents System

### Description
A modular system of AI agents where each agent performs a specific task, orchestrated by a Manager Agent that analyzes user inputs and selects the most appropriate agent(s).

### How to Run
1. Clone the repo
2. Run: `docker build -t ai-agents .`
3. Then: `docker run -p 8000:8000 ai-agents`

### Endpoints
- `POST /process`: Accepts input text and optionally document directory path. Returns selected agent outputs with justification.

### Example Request
```json
{
  "input_text": "summarize this article and extract keywords",
  "documents_path": "./docs"
}
