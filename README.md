# django-react-todo
ToDo App developed with Django and React stack

## Development Environment

### Executing Backend

`cd` to `todobackend` directory and execute

```
docker build -t "todoapp" .
```

After building the app you can run it by executing

```
docker run --name todoapp -p 8020:8020 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=hello1 -e DJANGO_SUPERUSER_EMAIL=admin@example.com todoapp
```