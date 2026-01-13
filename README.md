# State of Software Development 2026

A comprehensive research initiative by ECPI University documenting the current state of the software development industry in 2026. This website showcases emerging technologies, industry trends, and best practices shaping modern software development.

## 🌐 Website

This project is hosted on GitHub Pages. The website includes:

- **Home Page** - Overview of 2026 development landscape with key highlights
- **About** - Research initiative details, methodology, and objectives
- **Trends** - In-depth analysis of emerging technologies and practices:
  - Cloud & Infrastructure (Kubernetes, Serverless, Edge Computing)
  - Artificial Intelligence & ML (AI-assisted development, LLMs, MLOps)
  - Security & Privacy (Zero-trust, Supply chain security, Privacy by design)
  - Languages & Frameworks (Rust, TypeScript, Framework consolidation)
  - Development Practices (Platform Engineering, Observability, Low-code)
  - Sustainability & Ethics (Green software, Ethical AI, Accessibility)
- **Resources** - Curated learning materials and tools:
  - Programming languages and frameworks
  - Cloud & DevOps platforms
  - AI & Machine Learning tools
  - Security & Testing frameworks
  - Learning platforms and communities

## 📁 Project Structure

```
.
├── index.html              # Home page
├── about.html              # About the research
├── trends.html             # Detailed trends analysis
├── resources.html          # Learning resources
├── styles.css              # Responsive styling
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Pages deployment workflow
├── LICENSE                 # MIT License
└── README.md              # This file
```

## 🚀 Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/BrickPiGuy/SoSD2026.git
cd SoSD2026
```

2. Open in a local web server (Python 3):
```bash
python -m http.server 8000
```

3. Visit `http://localhost:8000` in your browser

### View Online

The site is automatically deployed to GitHub Pages. Access it at:
```
https://brickpigy.github.io/SoSD2026/
```

(Note: Update the URL with your GitHub Pages URL once the site is deployed)

## ⚙️ GitHub Pages Setup

The repository is configured for automatic deployment to GitHub Pages:

1. **Workflow**: `.github/workflows/deploy.yml` automatically deploys changes pushed to `main`
2. **Settings**: GitHub Pages is configured to deploy from the root directory
3. **Custom Domain**: Optional - can be configured in GitHub Pages settings

### Enable GitHub Pages

1. Go to repository Settings → Pages
2. Under "Build and deployment", select:
   - **Source**: GitHub Actions
   - **Branch**: main (automatic)
3. The site will deploy automatically on each push to `main`

## 🎨 Features

- **Responsive Design**: Mobile-friendly layouts that work on all devices
- **Professional Styling**: Clean, modern design with intuitive navigation
- **Semantic HTML**: Properly structured content for accessibility
- **Performance**: Lightweight CSS with no external dependencies (except fonts)
- **Accessibility**: WCAG compliant design patterns

## 📊 Content Highlights

### Technology Categories Covered

**Infrastructure & Cloud**
- Kubernetes and container orchestration
- Serverless computing and FaaS
- Edge computing and distributed architectures

**Artificial Intelligence**
- AI-assisted development tools
- Large Language Models (LLMs)
- Machine Learning Operations (MLOps)

**Security**
- Zero-trust architecture
- Supply chain security
- Privacy-first development

**Modern Development**
- TypeScript and Rust adoption
- Platform engineering
- Low-code/no-code platforms

**Sustainability & Ethics**
- Green software development
- Ethical AI practices
- Web accessibility standards

## 🔧 Customization

### Modifying Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #1e3a8a;      /* Dark blue */
    --secondary-color: #3b82f6;    /* Light blue */
    --accent-color: #f59e0b;       /* Amber */
    --text-color: #1f2937;         /* Dark gray */
    --light-bg: #f9fafb;           /* Light gray */
}
```

### Adding New Pages

1. Create a new `.html` file in the root directory
2. Copy the navigation bar structure from an existing page
3. Link to it from the navbar in other pages

### Updating Content

All pages are static HTML files. Simply edit the content directly in any `.html` file and push to GitHub.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💼 About ECPI University

ECPI University is a career-focused institution dedicated to providing students with the skills and knowledge needed to succeed in technology and business fields. This research initiative reflects our commitment to understanding and communicating current trends in software development.

## 📧 Contact & Contributions

For questions or contributions to this research:
- Visit the [GitHub repository](https://github.com/BrickPiGuy/SoSD2026)
- Create an issue for suggestions or corrections
- Submit pull requests for content improvements

---

**Last Updated**: January 13, 2026

**Research Focus**: State of Software Development 2026 - Trends, Technologies, and Best Practices
# Trigger deployment
