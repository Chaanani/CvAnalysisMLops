
ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}


WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "./main.py"]