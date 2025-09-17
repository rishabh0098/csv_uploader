#!/bin/bash

# Test script for Docker setup
echo "Testing Docker setup for CSV Uploader..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    echo "Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Build the Docker image
echo "Building Docker image..."
if docker build -t csv-uploader .; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi

# Test running the container
echo "Testing container startup..."
if docker run --rm -d -p 5000:5000 --name csv-uploader-test csv-uploader; then
    echo "✅ Container started successfully"
    
    # Wait a moment for the app to start
    sleep 5
    
    # Test if the app is responding
    if curl -f http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Application is responding on http://localhost:5000"
    else
        echo "❌ Application is not responding"
    fi
    
    # Clean up
    docker stop csv-uploader-test
    echo "✅ Test container stopped and removed"
else
    echo "❌ Failed to start container"
    exit 1
fi

echo ""
echo "🎉 Docker setup test completed successfully!"
echo "You can now run: docker-compose up --build"
