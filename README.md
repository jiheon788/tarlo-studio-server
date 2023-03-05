# Tarlo Studio - server

## Getting Started

Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000). You will see the automatic interactive [API documentation](http://127.0.0.1:8000/docs)

#### Fill out `.env`

```
KAKAOBRAIN_HOST_URL=${kakaobrain host url}
KAKAO_REST_API_KEY=${your kakao rest api key}
```

#### Install

```
pip install -r requirements.txt
```

#### Start

```
uvicorn main:app --reload
```
