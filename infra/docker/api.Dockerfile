FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY packages/sdk-py /app/packages/sdk-py
RUN pip install --no-cache-dir fastapi uvicorn && pip install -e /app/packages/sdk-py
COPY . /app
ENV PORT=8000 API_MODULE=api.main:app
EXPOSE 8000
CMD ["sh","-c","uvicorn ${API_MODULE} --host 0.0.0.0 --port ${PORT}"]
