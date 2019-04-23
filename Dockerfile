FROM alpine

EXPOSE 3031

WORKDIR /usr/src/app

RUN apk add --update --no-cache python python-dev py-setuptools py-pip linux-headers g++ gcc libxslt-dev

COPY . .

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--http", ":3031", \
               "--wsgi-file", "main.py", \
               "--master", \
               "--processes", "4", \
               "--threads", "2" ]
