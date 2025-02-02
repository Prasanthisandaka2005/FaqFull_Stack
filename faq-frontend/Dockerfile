# Use Node.js image to build the React app
FROM node:18 as build

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the files and build the project
COPY . ./
RUN npm run build

# Use Nginx to serve the built frontend
FROM nginx:alpine

# Copy built files into Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
