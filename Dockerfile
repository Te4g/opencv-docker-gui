FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1 \
    libglib2.0-0 \
    libhdf5-dev \
    graphviz

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r src/requirements.txt

RUN apt-get autoremove -y && apt-get autoclean -y

ENV QT_X11_NO_MITSHM=1

ENTRYPOINT ["python", "/app/src/app.py"]