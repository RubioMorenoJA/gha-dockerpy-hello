FROM python:3.11-slim
# COPY saludo.py /saludo.py
# CMD ["python", "/saludo.py"]
COPY dice-throwing.py /dice-throwing.py
CMD ["python", "/dice-throwing.py"]