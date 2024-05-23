FROM node:lts-alpine

WORKDIR /usr/src/app

COPY . .

RUN npm i

RUN npm install -g nodemon

EXPOSE 3000

CMD ["node", "src/index.js"]



