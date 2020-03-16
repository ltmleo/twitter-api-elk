FROM leonardomontero/twitter-api-case:1.0.0

WORKDIR /app

COPY Main.py project.properties /app/
COPY ./src/ /app/src/

ENTRYPOINT [ "python", "/app/Main.py" ]