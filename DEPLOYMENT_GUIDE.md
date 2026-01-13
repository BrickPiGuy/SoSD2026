# GitHub Pages Setup Guide

## Quick Start

Your SoSD 2026 website is ready to be deployed to GitHub Pages. Follow these steps:

### Step 1: Verify Local Setup (Optional)

Before pushing to GitHub, test the website locally:

```bash
cd /workspaces/SoSD2026
python -m http.server 8000
```

Then visit: `http://localhost:8000`

### Step 2: Commit Changes

Stage all files for commit:

```bash
git add .
git commit -m "Initial SoSD 2026 website with GitHub Pages deployment"
```

### Step 3: Push to GitHub

Push all changes to the main branch:

```bash
git push origin main
```

### Step 4: Configure GitHub Pages

1. Go to your repository on GitHub.com
2. Click **Settings** (top navigation)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - The workflow `.github/workflows/deploy.yml` will handle deployment automatically
5. Click **Save**

### Step 5: Monitor Deployment

1. Go to the **Actions** tab in your repository
2. You should see a workflow run named "Deploy GitHub Pages"
3. Wait for it to complete (usually < 1 minute)
4. Check the Status Checks for deployment confirmation

### Step 6: Access Your Site

Once deployment completes, your site will be available at:

```
https://BrickPiGuy.github.io/SoSD2026/
```

(Replace `BrickPiGuy` with your actual GitHub username if applicable)

---

## Troubleshooting

### Site Not Appearing

**Problem**: After setup, site shows 404 or doesn't load

**Solutions**:
1. Check Actions tab - ensure deployment workflow succeeded
2. Wait 1-2 minutes after successful deployment (GitHub CDN cache)
3. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
4. Clear browser cache
5. Verify Pages settings show "Deployed successfully"

### Workflow Not Running

**Problem**: Actions tab shows no deploy workflow

**Solutions**:
1. Verify `.github/workflows/deploy.yml` exists in your repository
2. Ensure file is properly formatted YAML (check indentation)
3. Check branch name is exactly `main` (case-sensitive)
4. Go to Settings → Pages and select "GitHub Actions"

### CSS or Images Not Loading

**Problem**: Site loads but styling looks broken

**Solutions**:
1. Check browser console for 404 errors
2. Verify file names match exactly (case-sensitive on Linux)
3. Ensure relative paths are correct in HTML files
4. Check `.gitignore` isn't excluding CSS files

### Custom Domain

To use a custom domain:

1. Go to Settings → Pages
2. Under "Custom domain", enter your domain
3. Add DNS records as GitHub instructs
4. GitHub will create a `CNAME` file automatically

---

## What's Included

✅ **index.html** - Landing page with overview  
✅ **about.html** - Research initiative details  
✅ **trends.html** - Technology trends analysis  
✅ **resources.html** - Learning resources and tools  
✅ **styles.css** - Professional responsive styling  
✅ **deploy.yml** - Automatic GitHub Pages deployment  
✅ **README.md** - Project documentation  
✅ **.gitignore** - Git configuration  

---

## Local Development

### Live Server Option (VS Code)

1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"
4. Browser opens automatically with live reload

### Python HTTP Server

```bash
# Python 3
python -m http.server 8000

# Then visit http://localhost:8000
```

### Node HTTP Server (if installed)

```bash
npx http-server
```

---

## Making Updates

After your site is live:

1. **Edit Files Locally**: Make changes to `.html` or `.css` files
2. **Test Locally**: Run local server and verify changes
3. **Commit**: `git add .` then `git commit -m "Update message"`
4. **Push**: `git push origin main`
5. **Automatic Deploy**: GitHub Actions workflow deploys automatically
6. **Site Updates**: Changes live within 1-2 minutes

No rebuild or additional steps needed - it's automatic!

---

## Performance Notes

- **Total Size**: ~100KB (HTML + CSS)
- **Load Time**: < 1 second
- **No External Dependencies**: All CSS is self-contained
- **Mobile Optimized**: Responsive design works on all devices
- **Accessible**: WCAG compliant markup

---

## Next Steps

1. Commit and push to GitHub
2. Configure GitHub Pages (Settings → Pages → GitHub Actions)
3. Monitor deployment in Actions tab
4. Visit your live site URL
5. Share with ECPI University community!

---

For more details, see:
- `README.md` - Full project documentation
- `STRUCTURE.md` - Content and file organization
- `.github/workflows/deploy.yml` - Deployment configuration

**Happy deploying! 🚀**
