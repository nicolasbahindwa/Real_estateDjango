ARG NODE_VERSION=18-alpine

FROM node:${NODE_VERSION} as node

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json .

RUN npm install

COPY . ${APP_HOME}

CMD ["npm", "start"]