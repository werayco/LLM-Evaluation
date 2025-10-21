FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r order-requirements.txt
CMD ["uvicorn", "fastapp:service", "--host","0.0.0.0", "--port", "8000"]