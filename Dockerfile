FROM python:3.11.1

ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p  app/school
ADD requirements.txt app/
ADD entrypoint.sh app
ADD . app/school

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod u+x /app/entrypoint.sh
ENTRYPOINT /app/entrypoint.sh $WORKERS $FLASK_APP
