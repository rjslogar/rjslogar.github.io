# Agent-Era Architecture Portfolio — deploy guide

Static site: no build step, no dependencies. Everything in this folder deploys as-is.

## 1. Replace placeholders (5 minutes)
Find-and-replace across ALL files (your editor, or `grep -rl YOUR_NAME . | xargs sed -i 's/YOUR_NAME/Jane Doe/g'` style):
- `YOUR_NAME` — your name (appears in pages, JSON-LD, llms.txt, and [NAME] in the three briefs/*.md footers)
- `[NAME]`, `[SITE]`, `[LINKEDIN]` — in briefs/*.md footers
- `YOUR_EMAIL` — contact email
- `YOUR_LINKEDIN` — LinkedIn slug (the part after linkedin.com/in/)
- `YOUR_DOMAIN` — your final domain (or username.github.io)

## 2. Create the repo and push
Option A — web UI (no git):
1. github.com → New repository → name it `username.github.io` (site lives at that URL) or any name (site lives at username.github.io/reponame). Public.
2. "uploading an existing file" link → drag this whole folder's contents in → Commit.

Option B — git / Claude Code:
    git init && git add -A && git commit -m "portfolio"
    git branch -M main
    git remote add origin https://github.com/USERNAME/REPO.git
    git push -u origin main

## 3. Enable Pages
Repo → Settings → Pages → Source: "Deploy from a branch" → Branch: main, folder: / (root) → Save.
Live in ~1 minute at the URL shown.

## 4. Custom domain (recommended, ~$12/yr)
1. Buy the domain (Cloudflare Registrar or Namecheap).
2. Repo → Settings → Pages → Custom domain → enter it → Save (this creates a CNAME file).
3. At your DNS provider add: CNAME record, host `www` → `USERNAME.github.io`; plus four A records on the apex (@) → 185.199.108.153 / .109. / .110. / .111.153.
4. Back in Pages settings, tick "Enforce HTTPS" once the certificate is issued (can take an hour).

## 5. Analytics (optional, 10 minutes)
1. Free account at goatcounter.com → pick a code.
2. Uncomment the analytics <script> in index.html and copy it into about.html and the three briefs/*.html pages, setting your code.

## 6. Verify
- Every page loads; nav works; each brief page's "machine-readable twin" link serves the .md.
- /llms.txt loads.
- Paste the site URL into LinkedIn: Contact info → Website, plus one Featured item per brief URL.
