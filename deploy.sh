#!/bin/bash

# Personal Website Deployment Script
# This script helps deploy the website to GitHub Pages

echo "🚀 Personal Website Deployment Script"
echo "======================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Initializing git..."
    git init
    echo "✅ Git initialized"
fi

# Check if there are any changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "⚠️  No changes detected to commit"
else
    echo "📝 Changes detected. Adding files..."
    git add .
    
    # Get commit message from user or use default
    read -p "Enter commit message (or press Enter for default): " commit_message
    if [ -z "$commit_message" ]; then
        commit_message="Update personal website - $(date '+%Y-%m-%d %H:%M:%S')"
    fi
    
    git commit -m "$commit_message"
    echo "✅ Changes committed"
fi

# Check if remote origin exists
if ! git remote | grep -q "origin"; then
    echo "🔗 No remote origin found. Please add your GitHub repository URL:"
    read -p "Enter GitHub repository URL (e.g., https://github.com/username/personal_site.git): " repo_url
    git remote add origin "$repo_url"
    echo "✅ Remote origin added"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
if git push -u origin main; then
    echo "✅ Successfully pushed to GitHub!"
else
    echo "❌ Failed to push to GitHub. Please check your repository settings."
    exit 1
fi

echo ""
echo "🎉 Deployment Complete!"
echo "======================================="
echo "Your website should be available at:"
echo "https://$(git remote get-url origin | sed 's/.*github\.com[:/]\(.*\)\.git/\1/' | sed 's/\//.github.io\//')/"
echo ""
echo "📋 Next Steps:"
echo "1. Go to your GitHub repository"
echo "2. Click on 'Settings' tab"
echo "3. Scroll to 'Pages' section"
echo "4. Select 'Deploy from a branch'"
echo "5. Choose 'main' branch and '/ (root)' folder"
echo "6. Click 'Save'"
echo ""
echo "⏱️  It may take a few minutes for your site to become available."
echo "🖼️  Don't forget to add your images to the assets/ directory!"

# List missing assets
echo ""
echo "📋 Missing Assets Checklist:"
echo "============================="
echo "Profile Images:"
echo "  - assets/profile.jpg"
echo "  - assets/profile-small.jpg"
echo ""
echo "Project Images (assets/projects/):"
echo "  - investment-analyzer.jpg"
echo "  - portfolio-tracker.jpg"
echo "  - automation-suite.jpg"
echo "  - market-dashboard.jpg"
echo ""
echo "Blog Images (assets/blog/):"
echo "  - ai-automation-future.jpg"
echo "  - building-scalable-apis.jpg"
echo "  - machine-learning-finance.jpg"
echo "  - blockchain-investment.jpg"
echo "  - react-performance.jpg"
echo "  - ai-ethics.jpg"
echo ""
echo "Book Covers (assets/books/):"
echo "  - intelligent-investor.jpg"
echo "  - life-3-0.jpg"
echo "  - zero-to-one.jpg"
echo ""
echo "Other:"
echo "  - assets/favicon.ico"
echo "  - assets/resume.pdf"
