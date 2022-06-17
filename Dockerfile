FROM node:latest
COPY . .
RUN npm install
ENV speed 1
ENV time 0
CMD node app.js ${speed} ${time}

