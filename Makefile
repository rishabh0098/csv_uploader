# Makefile for CSV Uploader Docker operations

.PHONY: help build up down logs clean test

# Default target
help:
	@echo "CSV Uploader - Docker Commands"
	@echo "=============================="
	@echo "build     - Build the Docker image"
	@echo "up        - Start the application with docker-compose"
	@echo "down      - Stop the application"
	@echo "logs      - View application logs"
	@echo "clean     - Remove containers and images"
	@echo "test      - Run Docker setup test"
	@echo "dev       - Run in development mode (local Python)"

# Build the Docker image
build:
	docker-compose build

# Start the application
up:
	docker-compose up -d --build

# Stop the application
down:
	docker-compose down

# View logs
logs:
	docker-compose logs -f

# Clean up containers and images
clean:
	docker-compose down --rmi all --volumes --remove-orphans
	docker system prune -f

# Run Docker test
test:
	./test-docker.sh

# Run in development mode
dev:
	python app.py
