ARG NODE_VERSION=20.17.0

FROM node:${NODE_VERSION}-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build --prod
##############################################
FROM nginx:alpine

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY --from=build /app/dist/angular-conduit /usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
