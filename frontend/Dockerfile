# playwright fails to install on bookworm
FROM node:18.16-bullseye as development
ENV NODE_ENV=development
WORKDIR /home/node/aof
COPY package.json package-lock.json ./
RUN npm ci && npx playwright install --with-deps
HEALTHCHECK CMD curl -f http://localhost:5173 || exit 1
