# SoSD 2026 - Website Structure Reference

## File Organization

```
SoSD2026/
├── index.html              # Landing page with overview
├── about.html              # Research initiative details
├── trends.html             # 6 technology trend categories
├── resources.html          # Learning tools and platforms
├── styles.css              # Unified responsive styling
├── .github/
│   └── workflows/
│       └── deploy.yml      # Auto-deployment to GitHub Pages
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
└── README.md              # Main documentation
```

## Page Navigation Flow

```
┌─────────────────────────────────────────┐
│           Navigation Bar                │
│  Home | About | Trends | Resources      │
└─────────────────────────────────────────┘
              ↓
    ┌─────────┼─────────┐
    ↓         ↓         ↓
 index.html about.html trends.html → resources.html
```

## Content Breakdown

### index.html (Home)
- Hero section with call-to-action
- 4 Overview cards (Emerging Tech, Insights, Learning, Best Practices)
- 6 Key Highlights (Cloud, AI, Security, Low-code, Distributed Teams, Sustainability)
- CTA section linking to About and Trends pages

### about.html (About)
- Research Initiative overview
- 4 Research Objectives
- Methodology (6 data sources)
- 4 Audience types (Students, Educators, Professionals, Employers)
- About ECPI University section

### trends.html (Trends)
- 6 Major Trend Categories:
  1. Cloud & Infrastructure (3 trends)
  2. AI & ML (3 trends)
  3. Security & Privacy (3 trends)
  4. Languages & Frameworks (3 trends)
  5. Development Practices (3 trends)
  6. Sustainability & Ethics (3 trends)
- Total: 18 detailed trend cards with tags

### resources.html (Resources)
- 5 Resource Categories:
  1. Programming Languages (4 languages with framework links)
  2. Cloud & DevOps (4 platform categories)
  3. AI & Machine Learning (4 ML categories)
  4. Security & Testing (4 tool categories)
  5. Learning Platforms (4 platform types)
- 16+ external resource links
- Total: 20+ learning platform and tool references

## Styling System

### Color Scheme (CSS Variables)
```css
--primary-color: #1e3a8a     /* Dark blue (headers, navbar) */
--secondary-color: #3b82f6   /* Light blue (accents, buttons) */
--accent-color: #f59e0b      /* Amber (CTAs) */
--text-color: #1f2937        /* Dark gray (body text) */
--light-bg: #f9fafb          /* Light gray (card backgrounds) */
```

### Responsive Breakpoints
- Desktop: Full grid layouts (2-4 columns)
- Tablet: 2-column grids
- Mobile: Single column (stacked)

## Key Features

✓ Mobile-responsive design
✓ Sticky navigation bar
✓ Smooth transitions and hover effects
✓ Card-based content organization
✓ Tag system for trend categorization
✓ External resource links (target="_blank")
✓ Professional typography
✓ Accessible color contrast
✓ SEO-friendly meta tags

## GitHub Pages Deployment

### Automatic Workflow (.github/workflows/deploy.yml)
- Triggers on: Push to main branch
- Deploys from: Root directory (`.`)
- Uses: Official GitHub Pages action
- Status: Check Actions tab in GitHub

### Manual Setup Steps
1. Go to repository Settings
2. Navigate to Pages section
3. Select "GitHub Actions" as source
4. Site auto-deploys on each push to main

## URL Structure

Once deployed, the site will be accessible at:
```
https://{github-username}.github.io/SoSD2026/
```

Each page is directly accessible:
- https://{github-username}.github.io/SoSD2026/
- https://{github-username}.github.io/SoSD2026/about.html
- https://{github-username}.github.io/SoSD2026/trends.html
- https://{github-username}.github.io/SoSD2026/resources.html

## Content Statistics

- **Total Pages**: 4 (+ styles + workflows)
- **Cards/Sections**: 50+
- **External Links**: 50+
- **Images**: None (text-only, lightweight)
- **Lines of Code**: ~2,500 (HTML + CSS combined)
- **Load Time**: < 1 second (all files < 100KB)

## Customization Tips

### Change Accent Color
Edit `styles.css` - update `--accent-color` variable

### Add New Navigation Item
1. Add `<li><a href="page.html">Title</a></li>` to nav-links in all HTML files
2. Create new page with same nav structure
3. Set class="active" on current page link

### Update Content
Simply edit text in any `.html` file - no build process needed

### Add Icons
Consider using emoji for visual interest (already included in trend/highlight headings)

## Next Steps

1. **Verify Setup**: Test locally with `python -m http.server 8000`
2. **Push to GitHub**: Commit and push all files
3. **Enable Pages**: Go to repository Settings → Pages
4. **Check Deployment**: View Actions tab for deployment status
5. **Share URL**: Site will be live at GitHub Pages URL

---

For more information, see README.md
