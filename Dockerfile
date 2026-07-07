FROM python:3.13.6-slim

WORKDIR /intern_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "intern_app.main:app", "--host", "0.0.0.0", "--port", "8000"]