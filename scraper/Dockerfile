FROM python:3
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install selenium
# RUN apt-get update
# RUN apt-get install -y chromium-driver

COPY . .
CMD ["python", "./scraper.py"]