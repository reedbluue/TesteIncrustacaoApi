FROM alpine:latest
RUN apk add nodejs npm

WORKDIR /app

COPY . .

RUN npm install && npm run build

CMD npx vite --host --port 3000

EXPOSE 3000