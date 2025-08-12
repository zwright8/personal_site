# Personal Website - Zach Wright

A modern, responsive personal portfolio website showcasing software engineering skills, investment thoughts, and professional experience.

## 🚀 Features

- **Responsive Design**: Optimized for all devices and screen sizes
- **Interactive Animations**: Particle effects, smooth transitions, and hover states
- **Dynamic Blog**: Searchable and categorizable blog posts
- **Investment Thoughts**: Dedicated section for investment analysis and insights
- **Reading List**: Current books and reading progress
- **Project Portfolio**: Filterable project showcase
- **Contact Form**: Interactive contact form with validation
- **SEO Optimized**: Meta tags, structured data, and search engine friendly

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Animations**: CSS Keyframes, Intersection Observer API
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter, JetBrains Mono)

## 📁 Project Structure

```
personal_site/
├── index.html              # Main landing page
├── blog.html               # Blog listing page
├── css/
│   ├── styles.css          # Main stylesheet
│   └── animations.css      # Animation definitions
├── js/
│   ├── main.js            # Main JavaScript functionality
│   └── particles.js       # Particle animation system
├── blog/
│   └── ai-automation-future-work.html  # Sample blog post
├── assets/
│   ├── projects/          # Project images
│   ├── blog/              # Blog post images
│   └── books/             # Book cover images
├── robots.txt             # Search engine robots file
├── sitemap.xml            # XML sitemap
└── README.md              # This file
```

## 🖼️ Required Assets

To complete the website setup, add the following images to their respective directories:

### Profile Images
- `assets/profile.jpg` - Main profile image (800x800px recommended)
- `assets/profile-small.jpg` - Small profile image for blog posts (200x200px)

### Project Images (assets/projects/)
- `investment-analyzer.jpg` - AI Investment Analyzer project
- `portfolio-tracker.jpg` - Portfolio Tracker project
- `automation-suite.jpg` - Business Automation Suite project
- `market-dashboard.jpg` - Real-time Market Dashboard project

### Blog Images (assets/blog/)
- `ai-automation-future.jpg` - AI and automation blog post header
- `building-scalable-apis.jpg` - API development blog post header
- `machine-learning-finance.jpg` - ML in finance blog post header
- `blockchain-investment.jpg` - Blockchain investment blog post header
- `react-performance.jpg` - React performance blog post header
- `ai-ethics.jpg` - AI ethics blog post header

### Book Cover Images (assets/books/)
- `intelligent-investor.jpg` - The Intelligent Investor book cover
- `life-3-0.jpg` - Life 3.0 book cover
- `zero-to-one.jpg` - Zero to One book cover

### Other Assets
- `assets/favicon.ico` - Website favicon
- `assets/resume.pdf` - Downloadable resume/CV

## 🚀 Deployment to GitHub Pages

Follow these steps to deploy your website to GitHub Pages:

### 1. Push to GitHub Repository

```bash
# Add all files
git add .

# Commit changes
git commit -m "Complete personal website with all features"

# Push to main branch
git push origin main
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on "Settings" tab
3. Scroll down to "Pages" section in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Select "main" branch and "/ (root)" folder
6. Click "Save"

### 3. Access Your Website

Your website will be available at: `https://zwright8.github.io/personal_site/`

*Note: It may take a few minutes for the site to become available after enabling GitHub Pages.*

### 4. Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to your repository root with your domain name
2. Configure your domain's DNS settings to point to GitHub Pages
3. Update the domain in your repository settings

## 🔧 Customization

### Update Personal Information

1. **Contact Information**: Update email and social media links in `index.html` and other pages
2. **About Section**: Modify the about me content in the main page
3. **Experience**: Update the timeline with your work experience
4. **Projects**: Replace project information with your own projects
5. **Skills**: Update the skills section with your technologies

### Add New Blog Posts

1. Create a new HTML file in the `blog/` directory
2. Follow the structure of the sample blog post
3. Add the new post to `blog.html` in the blog posts grid
4. Update the sitemap.xml with the new post URL

### Modify Styling

- **Colors**: Update CSS variables in `:root` selector in `styles.css`
- **Fonts**: Change Google Fonts imports and font-family declarations
- **Layout**: Modify grid and flexbox layouts as needed
- **Animations**: Customize animations in `animations.css`

## 📱 Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ⚠️ Internet Explorer (limited support)

## ⚡ Performance Features

- Lazy loading for images
- Optimized animations with `will-change` property
- Efficient scroll event handling with throttling
- Minimal external dependencies
- Compressed and minified assets (recommended for production)

## 🔒 SEO Features

- Semantic HTML structure
- Meta tags for social media sharing
- Structured data markup
- XML sitemap
- Robots.txt configuration
- Alt tags for all images
- Descriptive page titles and descriptions

## 📈 Analytics Setup (Optional)

To add Google Analytics:

1. Create a Google Analytics account
2. Get your tracking ID
3. Add the tracking code to all HTML pages in the `<head>` section

## 🤝 Contributing

This is a personal website template. Feel free to fork and customize for your own use!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you have questions about customizing this template:

- Create an issue on GitHub
- Check the documentation in code comments
- Review the CSS and JavaScript for customization examples

---

**Built with ❤️ by Zach Wright**