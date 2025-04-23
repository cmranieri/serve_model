# ML Model API Starter

Um projeto simples usando FastAPI para servir um modelo de aprendizado de máquina.

## Getting Started

1. Instalar dependências:

```
bash
pip install -r requirements.txt
```

2. Rodar a API:

```
uvicorn app:app --reload
```

3. Abrir o Swagger no browser:

```
http://127.0.0.1:8000/docs
```

4. Testar o /predict usando o arquivo uma entrada contida em arquivo json:

```
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d @input_example.json
```
