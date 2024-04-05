#!/usr/bin/env bash

# Lauching API server

cd csv_uploader_backend
sudo docker-compose up -d --build

# Lauching React server

cd ../csv_uploader_frontend
sudo docker-compose up -d --build