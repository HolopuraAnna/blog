FROM node:20-alpine

WORKDIR /app

RUN npm install -g @vue/cli

EXPOSE 8080

CMD ["sh", "-c", "vue create vue-app --default || true && cd vue-app && npm run serve"]
