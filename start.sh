#!/usr/bin/env bash
set -e

echo "==> Building JupyterHub image..."
docker build -t jupyterhub-hub:latest -f hub.Dockerfile .

echo "==> Building notebook image (this takes a few minutes the first time)..."
docker build -t ml-notebook:latest -f notebook.Dockerfile .

echo "==> Starting Ray + JupyterHub..."
docker compose up -d

echo ""
echo "Done."
echo "  JupyterHub  → http://localhost:8000"
echo "  Ray dashboard → http://localhost:8265"
echo ""
echo "First login:"
echo "  1. Go to http://localhost:8000"
echo "  2. Sign in as 'john' (you'll be prompted to set your password on first login)"
echo "  3. To add a user: Admin panel → Add Users"
