FROM python:3.11-slim
COPY saludo.py /saludo.py
CMD ["python", "/saludo.py"]