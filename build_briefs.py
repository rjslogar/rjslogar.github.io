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
<link rel="stylesheet" href="../style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{title}",
  "author": {{"@type": "Person", "name": "RJSlogar"}},
  "description": "{desc}",
  "encodingFormat": "text/html",
  "sameAs": "https://rjslogar.github.io/briefs/{slug}.md"
}}
</script>
<!-- Analytics: uncomment after setup, same snippet as index.html -->
</head>
<body>
<header class="site">
  <div class="shell">
    <a class="wordmark" href="../index.html">RJSlogar · Agent-Era Architecture</a>
    <nav aria-label="Site">
      <a href="../index.html">Briefs</a>
      <a href="../about.html">About</a>
      <a href="../llms.txt">llms.txt</a>
    </nav>
  </div>
</header>
<main class="shell">
<div class="sibling">Governed siblings: you are reading the human serialization of this brief. Agents should prefer the <a href="{slug}.md">machine-readable twin</a>.</div>
<article>
<p class="eyebrow">{eyebrow}</p>
{body}
</article>
</main>
<footer class="site">
  <div class="shell">
    <span>© 2026 RJSlogar · <a href="mailto:rjslogar@gmail.com">rjslogar@gmail.com</a> · <a href="https://www.linkedin.com/in/mba-ma-richs/">LinkedIn</a></span>
    <span>This site ships governed siblings: every brief has a <a href="../llms.txt">machine-readable twin</a>.</span>
  </div>
</footer>
</body>
</html>
"""

BRIEFS = [
    ("content-governance", "01 · What enters the agent",
     "Governed content delivery to AI agents and humans — per-field release control bound to the moments of agent cognition."),
    ("two-cohort", "02 · What the agent is told",
     "Customer intelligence simplified for efficient agent processing, with the audit record and causal training substrate as one structure."),
    ("post-inference", "03 · What leaves the agent",
     "Comprehensibility scoring for AI-generated text and code, enabling propagation containment in multi-agent systems."),
]

for slug, eyebrow, desc in BRIEFS:
    src = open(f"briefs/{slug}.md").read()
    title = re.search(r"^# (.+)$", src, re.M).group(1)
    body = markdown.markdown(src, extensions=["smarty"])
    page = TEMPLATE.format(title=html.escape(title), desc=html.escape(desc),
                           slug=slug, eyebrow=eyebrow, body=body)
    open(f"briefs/{slug}.html", "w").write(page)
    print(f"built briefs/{slug}.html ({len(page)} bytes)")
