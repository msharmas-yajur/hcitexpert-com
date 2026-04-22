#!/usr/bin/env node
import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const PORT = 4000;

const FONTS = `<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">`;

function parseFrontMatter(raw) {
  if (!raw.startsWith('---')) return { meta: {}, body: raw };
  const end = raw.indexOf('\n---', 3);
  if (end === -1) return { meta: {}, body: raw };
  const yaml = raw.slice(3, end).trim();
  const body = raw.slice(end + 4).trim();
  const meta = {};
  let currentKey = null;
  for (const line of yaml.split('\n')) {
    if (line.startsWith('  - ')) {
      if (currentKey) meta[currentKey] = (meta[currentKey] ? meta[currentKey] + ',' : '') + line.slice(4).trim();
      continue;
    }
    const colon = line.indexOf(':');
    if (colon === -1) continue;
    currentKey = line.slice(0, colon).trim();
    const val = line.slice(colon + 1).trim().replace(/^["']|["']$/g, '');
    meta[currentKey] = val;
  }
  return { meta, body };
}

const LOGO_SVG = fs.existsSync(path.join(ROOT, 'assets/images/logo.png'))
  ? fs.readFileSync(path.join(ROOT, 'assets/images/logo.png'), 'utf8')
  : '';

function shell(title, content) {
  return `<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>${FONTS}
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<link rel="shortcut icon" type="image/png" href="/assets/images/favicon.png">
<link rel="stylesheet" href="/assets/css/main.css">
</head><body>
<header class="site-header">
  <div class="header-inner">
    <a class="site-logo" href="/">
      <img src="/assets/images/logo.png" alt="HCITExperts" height="32">
    </a>
    <nav class="header-nav">
      <a href="/">Blog</a>
      <a href="#" class="btn-subscribe">Subscribe</a>
    </nav>
  </div>
</header>
<main>${content}</main>
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-left">
      <img src="/assets/images/logo-full.png" alt="HCITExperts" height="60">
      <p>Healthcare IT insights by Yajur Healthcare since 2013.</p>
    </div>
  </div>
  <div class="footer-copy"><p>&copy; 2026 HCITExperts &middot; Local Preview</p></div>
</footer>
</body></html>`;
}

function getPosts() {
  const dir = path.join(ROOT, '_posts');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.md'))
    .map(f => {
      const raw = fs.readFileSync(path.join(dir, f), 'utf8');
      const { meta, body } = parseFrontMatter(raw);
      const m = f.match(/^(\d{4}-\d{2}-\d{2})-(.+)\.md$/);
      const slug = m ? `${m[1]}/${m[2]}` : f.replace('.md', '');
      return { slug, meta, body };
    })
    .sort((a, b) => (b.meta.date || '').localeCompare(a.meta.date || ''));
}

function avatar(name) {
  return (name || 'T')[0].toUpperCase();
}

function rt(body) {
  return Math.max(1, Math.ceil(body.replace(/<[^>]+>/g, '').split(/\s+/).length / 200));
}

function thumb(body) {
  const m = body.match(/src="(https?:\/\/[^"]+\.(png|jpg|jpeg|webp|gif)[^"]*)"/i);
  return m ? m[1] : null;
}

function cardHtml(post, large = false) {
  const img = thumb(post.body);
  const cat = post.meta.categories ? post.meta.categories.split(',')[0].trim() : 'Healthcare IT';
  const author = post.meta.author || 'Team HCITExperts';
  const date = (post.meta.date || '').slice(0, 10);
  const mins = rt(post.body);
  const titleSize = large ? '1.1rem' : '1rem';

  return `<article class="post-card">
    <div class="card-body">
      <div class="card-top-meta">
        <span>${date}</span>
        <span class="meta-sep">&middot;</span>
        <span class="card-cat">${cat}</span>
        <span class="meta-sep">&middot;</span>
        <span>${mins} min read</span>
      </div>
      <a href="/post/${post.slug}" class="card-title-link">
        <h2 class="card-title" style="font-size:${titleSize}">${decodeEntities(post.meta.title)}</h2>
      </a>
    </div>
  </article>`;
}

function decodeEntities(str) {
  return (str || '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#039;/g, "'");
}

function homeHtml(posts) {
  const featured = posts.find(p => p.meta.featured === 'true') || posts[0];
  const rest = posts.filter(p => p !== featured).slice(0, 20);
  const img = featured ? thumb(featured.body) : null;
  const cat = featured?.meta.categories ? featured.meta.categories.split(',')[0].trim() : 'Healthcare IT';
  const author = featured?.meta.author || 'Team HCITExperts';
  const mins = featured ? rt(featured.body) : 0;

  const heroSection = featured ? `
<section class="hero">
  <div class="hero-inner">
    <p class="hero-tag">Featured</p>
    <a href="/post/${featured.slug}" class="hero-link">
      <div class="hero-body">
        <span class="cat-badge">${cat}</span>
        <h1 class="hero-title">${decodeEntities(featured.meta.title)}</h1>
        <div class="post-meta">
          <span class="meta-avatar">${avatar(author)}</span>
          <span class="meta-author">${author}</span>
          <span class="meta-sep">&middot;</span>
          <span>${(featured.meta.date || '').slice(0,10)}</span>
          <span class="meta-sep">&middot;</span>
          <span>${mins} min read</span>
        </div>
      </div>
    </a>
  </div>
</section>` : '';

  const grid = rest.map(p => cardHtml(p, true)).join('');

  return shell('HCITExperts — Healthcare IT Blog', `
${heroSection}
<section class="posts-section">
  <div class="posts-inner">
    <div class="posts-grid">${grid}</div>
    <p style="text-align:center;margin-top:2rem;font-size:.85rem;color:#999">${posts.length} total posts &mdash; local preview shows 20</p>
  </div>
</section>`);
}

function postHtml(post) {
  const author = post.meta.author || 'Team HCITExperts';
  const cat = post.meta.categories ? post.meta.categories.split(',')[0].trim() : '';
  const mins = rt(post.body);

  return shell(decodeEntities(post.meta.title) || 'Post', `
<div class="progress-bar" id="progressBar"></div>
<article class="post-article">
  <div class="post-container">
    <header class="post-header">
      ${cat ? `<div class="post-cats"><span class="cat-badge">${cat}</span></div>` : ''}
      <h1 class="post-title">${decodeEntities(post.meta.title)}</h1>
      <div class="post-byline">
        <span class="meta-avatar">${avatar(author)}</span>
        <div class="byline-info">
          <span class="meta-author">${author}</span>
          <div class="byline-sub">
            <span>${(post.meta.date || '').slice(0,10)}</span>
            <span class="meta-sep">&middot;</span>
            <span>${mins} min read</span>
          </div>
        </div>
      </div>
    </header>
    <div class="post-body">${post.body}</div>
    <div style="margin-top:2rem;padding-top:1rem;border-top:1px solid #e6e6e6">
      <a href="/" style="font-size:.85rem;font-weight:600;color:#1a8917">&larr; Back to Blog</a>
    </div>
  </div>
</article>
<script>
  window.addEventListener('scroll',function(){
    var b=document.getElementById('progressBar'),p=document.querySelector('.post-body');
    if(!b||!p)return;
    b.style.width=Math.min(100,Math.max(0,(window.scrollY-p.offsetTop)/p.offsetHeight*100))+'%';
  });
</script>`);
}

const server = http.createServer((req, res) => {
  const pathname = new URL(req.url, `http://localhost:${PORT}`).pathname;

  if (pathname.startsWith('/assets/')) {
    const f = path.join(ROOT, pathname);
    if (fs.existsSync(f) && fs.statSync(f).isFile()) {
      const ext = path.extname(f);
      const types = { '.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.ico':'image/x-icon' };
      res.writeHead(200, { 'Content-Type': types[ext] || 'application/octet-stream' });
      res.end(fs.readFileSync(f));
    } else { res.writeHead(404); res.end(); }
    return;
  }

  const posts = getPosts();

  // home
  if (pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(homeHtml(posts));
    return;
  }

  if (pathname.startsWith('/post/')) {
    const slug = pathname.replace('/post/', '').replace(/\/$/, '');
    const post = posts.find(p => p.slug === slug || p.slug.endsWith('/' + slug.split('/').slice(1).join('/')));
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(post ? postHtml(post) : shell('Not Found', '<div style="padding:4rem 2rem;max-width:680px;margin:0 auto"><h1 style="font-size:2rem;margin-bottom:1rem">Post not found</h1><a href="/" style="color:#1a8917">&larr; Home</a></div>'));
    return;
  }

  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end(homeHtml(posts));
});

server.listen(PORT, () => {
  const posts = getPosts();
  console.log(`\n  HCITExperts local preview`);
  console.log(`  → http://localhost:${PORT}`);
  console.log(`  ${posts.length} posts loaded\n`);
});
