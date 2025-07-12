# Stage 1: Build Environment
FROM node:20 AS builder

WORKDIR /app

# Copy package.json and yarn.lock
COPY package.json ./

# Install dependencies
RUN yarn install

# Copy the rest of the application source code
COPY . .

# Build the React application
RUN yarn build

# Stage 2: Production Environment
FROM node:20 AS runner

WORKDIR /app

# Install serve globally
RUN yarn global add serve

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Copy the built application from the builder stage
COPY --from=builder /app/dist ./build
COPY --from=builder /app/package.json ./package.json 
COPY --from=builder /app/yarn.lock ./yarn.lock 

# Expose the port your React app will run on
EXPOSE 3000

# Command to start the application
CMD ["serve", "-s", "build"]