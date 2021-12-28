FROM python:3.8.6

WORKDIR /app
COPY . /app

RUN pip install  --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/
EXPOSE 8000

CMD ["daphne", "aoi.asgi:application"]