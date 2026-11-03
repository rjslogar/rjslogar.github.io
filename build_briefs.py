import markdown, re, html

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — RJSlogar</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Public+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{title}",
  "author": {{"@type": "Person", "name": "RJSlogar"}},
  "description": "{desc}",
  "encodingFormat": "text/html",
  "sameAs": "https://rjslogar.github.io/{twin_path}"
}}
</script>
<!-- Analytics: uncomment after setup, same snippet as index.html -->
</head>
<body>
<header class="site">
  <div class="shell">
    <a class="wordmark" href="{root}index.html">RJSlogar · Agent-Era Architecture</a>
    <nav aria-label="Site">
      <a href="{root}index.html">Briefs</a>
      <a href="{root}about.html">About</a>
      <a href="{root}llms.txt">llms.txt</a>
    </nav>
  </div>
</header>
<main class="shell">
<div class="sibling">Governed siblings: you are reading the human serialization of this brief. Agents should prefer the <a href="{twin}">machine-readable twin</a>.</div>
<article>
<p class="eyebrow">{eyebrow}</p>
{body}
</article>
</main>
<footer class="site">
  <div class="shell">
    <span>© 2026 RJSlogar · <a href="mailto:rjslogar@gmail.com">rjslogar@gmail.com</a> · <a href="https://www.linkedin.com/in/mba-ma-richs/">LinkedIn</a></span>
    <span>This site ships governed siblings: every brief has a <a href="{root}llms.txt">machine-readable twin</a>.</span>
  </div>
</footer>
</body>
</html>
"""

BRIEFS = [
    ("content-governance", "01 · What enters the agent",
     "Governed content delivery to AI agents and humans — per-field release control bound to the moments of agent cognition."),
    ("two-cohort", "02 · What the agent is told",
     "Customer intelligence simplified for efficient agent processing, with one audit record, written at injection time, as the source of the causal training data."),
    ("post-inference", "03 · What leaves the agent",
     "Comprehensibility scoring for AI-generated text and code, enabling propagation containment in multi-agent systems."),
]

# Supporting pages: (markdown source, html output, eyebrow, description)
PAGES = [
    ("briefs/business-health-score-demo/SUMMARY.md", "briefs/business-health-score-demo/summary.html",
     "02 · Demonstration summary",
     "Results from a working demonstration of the two-cohort, one-metric approach: one business health score, and what agent actions add to it."),
]
# On web pages, links to a supporting page's markdown twin point to its html page instead
HTML_LINKS = {"business-health-score-demo/SUMMARY.md": "business-health-score-demo/summary.html"}

def build(md_path, html_path, eyebrow, desc, root):
    src = open(md_path, encoding="utf-8").read()
    title = re.search(r"^# (.+)$", src, re.M).group(1)
    body = markdown.markdown(src, extensions=["smarty", "tables"])
    for md_link, html_link in HTML_LINKS.items():
        body = body.replace(f'href="{md_link}"', f'href="{html_link}"')
    twin = md_path.rsplit("/", 1)[1]
    page = TEMPLATE.format(title=html.escape(title), desc=html.escape(desc), root=root, twin=twin,
                           twin_path=md_path, eyebrow=eyebrow, body=body)
    open(html_path, "w", encoding="utf-8").write(page)
    print(f"built {html_path} ({len(page)} bytes)")

for slug, eyebrow, desc in BRIEFS:
    build(f"briefs/{slug}.md", f"briefs/{slug}.html", eyebrow, desc, "../")
for md_path, html_path, eyebrow, desc in PAGES:
    build(md_path, html_path, eyebrow, desc, "../" * (html_path.count("/")))
