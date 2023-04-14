# Dockerfile

FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/todo
COPY requirements.txt start-server.sh /opt/app/todo/
COPY . /opt/app/todo/
WORKDIR /opt/app/todo
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN chown -R www-data:www-data /opt/app

# superuser

ENV DJANGO_SUPERUSER_USERNAME carra
ENV DJANGO_SUPERUSER_PASSWORD hello$

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/todo/start-server.sh"]