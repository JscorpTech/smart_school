#!/bin/bash
set -e

echo "Starting deployment..."

make deploy-prod

echo "Deployment complete!"
