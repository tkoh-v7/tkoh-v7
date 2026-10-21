# TKOH V7 — static creator and project hub

A five-page static website, with JSON-driven projects and series, plus a scheduled YouTube uploads feed. No framework, paid hosting or browser-side API keys required.

## Publish to GitHub Pages

1. Create a **public** GitHub repository named `tkoh-v7` (public is needed for GitHub Pages on GitHub Free).
2. Upload **the contents of this folder** to the repository root, including the hidden `.github` folder. Do not upload the zip as one file.
3. Repository → **Settings → Pages → Build and deployment**: choose **Deploy from a branch**, branch `main`, folder `/(root)`; save. If your default branch is different, select it.
4. Before using a custom domain, verify the site works at `https://YOUR-USERNAME.github.io/tkoh-v7/`. **Important:** this build uses root-relative paths and is designed for the final custom domain. For testing on the repository URL, use a temporary apex or subdomain instead, or replace `/` references with the repository base path before testing. The intended production host is `tkoh-v7.com`.
5. In repository Settings → Pages → Custom domain, enter `tkoh-v7.com`. GitHub may create a `CNAME` file; if it does, commit/preserve it. If not, add a root `CNAME` file containing `tkoh-v7.com`.
6. At Cloudflare DNS add GitHub Pages apex A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (DNS only / grey cloud initially). Optionally add `www` CNAME to `YOUR-USERNAME.github.io`, also DNS only. Remove conflicting A/AAAA records. Verify current GitHub documentation before changing DNS.
7. Enable **Enforce HTTPS** in GitHub Pages once certificate provisioning completes. Configure `www` redirects in GitHub Pages/Cloudflare as desired; the canonical hostname in this build is the apex.
8. Set repository **Settings → Secrets and variables → Actions → Variables**: `YOUTUBE_CHANNEL_ID` = your actual channel ID beginning `UC` (24 characters total). Go to **Actions → Refresh YouTube uploads → Run workflow**. The feed refreshes every six hours; scheduled runs can be delayed.
9. Edit `data/projects.json`, `data/series.json`, and `contact/index.html` to add verified links. The site intentionally does not invent destinations. Add real social URLs and an optional support link only when you have chosen them.
10. Test all five pages, mobile navigation, cards, social preview, HTTPS and YouTube refresh after deployment.

## Notes

- Until `YOUTUBE_CHANNEL_ID` is configured and the workflow succeeds, videos show a friendly empty state. The site still deploys normally.
- Project and series URLs are intentionally blank placeholders. The UI displays "Link coming soon" rather than a dead link.
- The public YouTube Atom feed typically returns only recent uploads, not the full channel history.
- YouTube thumbnails are loaded directly from YouTube; visitors' browsers contact YouTube's image domain.
- This is a fan-made website, not affiliated with Jagex.
- If branch protection blocks the automated commit, grant the workflow appropriate write permissions or switch to a PR-based workflow. Repository Settings → Actions → General → Workflow permissions should allow read/write for this workflow where permitted.
- Root-relative paths require deployment at a domain root, such as `tkoh-v7.com`, not a GitHub Pages repository subpath.
- GitHub Pages does not offer arbitrary custom HTTP response headers. If advanced CSP/security headers are needed, plan a deliberate Cloudflare proxy/Worker deployment and test before enabling.
