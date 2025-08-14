#!/bin/bash

# Simple deployment script for personal website
# This script adds, commits, and pushes changes to GitHub

echo "🚀 Deploying personal website..."

# Add all changes
git add .

# Check if there are any changes to commit
if git diff --staged --quiet; then
    echo "❌ No changes to commit"
    exit 0
fi

# Get commit message from user or use default
if [ -z "$1" ]; then
    COMMIT_MESSAGE="Update personal website"
else
    COMMIT_MESSAGE="$1"
fi

# Commit changes
git commit -m "$COMMIT_MESSAGE"

# Push to GitHub
git push origin main

echo "✅ Website deployed successfully!"
echo "🌐 View your site at: https://zwright8.github.io/personal_site/"
