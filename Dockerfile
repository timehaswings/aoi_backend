FROM python:3.8.6

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install  --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/
EXPOSE 8000

CMD ["daphne", "aoi.asgi:application"]
