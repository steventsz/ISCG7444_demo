# Readme
## Installation

```bash
pip install -r requirements.txt
```
```bash
python app.py
```
```bash
python pytest
```

## Docker
```bash
docker build -t flask-app .
docker run -p 5001:5001 flask-app
docker exec -it flask-app pytest
```

