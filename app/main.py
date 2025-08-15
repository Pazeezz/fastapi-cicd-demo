# app/main.py  (only the /ui route below needs replacing)
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
import os

app = FastAPI()
GIT_SHA = os.getenv("GIT_SHA", "dev")

@app.get("/")
def root():
    return {"message": "Hello, SLIIT students !"}

@app.get("/greet")
def greet(name: str | None = None):
    return {"message": f"Hello, {name or 'SLIIT students'}!"}

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)

@app.get("/version")
def version():
    return {"version": GIT_SHA}

@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>CI/CD Demo • SLIIT</title>
  <style>
    :root {{
      --bg1:#0f172a; --bg2:#111827; --card:#0b1220cc; --ink:#e5e7eb; --muted:#9ca3af;
      --brand:#2563eb; --brand-2:#22d3ee; --ring:#60a5fa; --chip:#0b1220; --border:#1f2937;
    }}
    * {{ box-sizing:border-box }}
    html,body {{ height:100% }}
    body {{
      margin:0; color:var(--ink); font:16px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
      background: radial-gradient(1200px 800px at 20% 10%, #1e293b, transparent 60%),
                  radial-gradient(900px 700px at 120% 0%, #0ea5e9, transparent 55%),
                  linear-gradient(180deg, var(--bg1), var(--bg2));
      overflow-x:hidden;
    }}
    /* subtle animated glow band */
    .glow {{
      position:fixed; inset:-20vh -20vw auto -20vw; height:40vh; filter:blur(60px); opacity:.35;
      background:linear-gradient(90deg, var(--brand), var(--brand-2), var(--brand));
      background-size:200% 100%; animation:move 9s ease-in-out infinite;
      pointer-events:none;
    }}
    @keyframes move {{ 0%{{transform:translateX(-20%)}} 50%{{transform:translateX(20%)}} 100%{{transform:translateX(-20%)}} }}

    .wrap {{
      min-height:100dvh; display:grid; place-items:center; padding:48px 16px;
    }}
    .card {{
      width:min(860px, 92vw); padding:32px; border-radius:20px;
      background:var(--card); border:1px solid var(--border);
      box-shadow:0 20px 70px rgba(0,0,0,.45), 0 0 0 1px rgba(255,255,255,.03) inset;
      backdrop-filter: blur(12px);
      transform:translateY(0); transition: transform .25s ease;
    }}
    .card:hover {{ transform:translateY(-2px) }}
    .head {{ display:flex; gap:10px; align-items:center; margin-bottom:6px }}
    .logo {{
      width:36px; height:36px; border-radius:10px; display:grid; place-items:center;
      background:linear-gradient(135deg, var(--brand), var(--brand-2));
      box-shadow:0 6px 20px rgba(34,211,238,.25);
      font-weight:800;
    }}
    h1 {{ margin:0; font-size:26px; letter-spacing:.2px }}
    p.lead {{ margin:6px 0 18px; color:var(--muted) }}

    .row {{ display:flex; gap:10px; margin-top:6px }}
    input {{
      flex:1; padding:12px 14px; border-radius:12px; border:1px solid var(--border);
      background:#0b1220; color:var(--ink); outline:none;
      transition:border-color .15s, box-shadow .15s;
    }}
    input:focus {{ border-color:var(--ring); box-shadow:0 0 0 4px rgba(96,165,250,.18) }}
    button {{
      padding:12px 16px; border-radius:12px; border:0; color:white; background:var(--brand);
      cursor:pointer; font-weight:600; letter-spacing:.2px; transition: transform .06s ease, opacity .2s ease;
      box-shadow:0 10px 24px rgba(37,99,235,.35);
    }}
    button:active {{ transform:translateY(1px) }}
    .bar {{ height:3px; background:linear-gradient(90deg,var(--brand),var(--brand-2)); width:0; border-radius:3px; margin:10px 0 4px; transition:width .28s ease }}

    .msg {{ font-size:22px; font-weight:700; margin:10px 0 2px }}
    .chips {{ display:flex; gap:10px; flex-wrap:wrap; margin-top:10px; opacity:.95 }}
    .chip {{ background:var(--chip); border:1px solid var(--border); padding:6px 10px; border-radius:999px; font-size:12px }}
    .link {{ text-decoration:none; color:var(--ink) }}
    .foot {{ margin-top:16px; color:var(--muted); font-size:13px }}
    code {{ background:#0b1220; padding:2px 6px; border-radius:8px; border:1px solid var(--border) }}

    /* tiny confetti for first greet */
    .confetti {{ position:fixed; inset:0; pointer-events:none }}
    .dot {{ position:absolute; width:6px; height:6px; border-radius:50%; opacity:0; }}
  </style>
</head>
<body>
  <div class="glow"></div>
  <canvas class="confetti" id="confetti"></canvas>

  <div class="wrap">
    <div class="card">
      <div class="head">
        <div class="logo">🚀</div>
        <div>
          <h1>CI/CD Demo • SLIIT</h1>
          <p class="lead">FastAPI + Docker + GitHub Actions + Cloud Deploy</p>
        </div>
      </div>

      <div class="row">
        <input id="name" placeholder="Try your name… (optional)" />
        <button id="btn" title="Call the API">Greet</button>
      </div>

      <div class="bar" id="bar"></div>
      <div class="msg" id="msg">Hello, SLIIT students!</div>

      <div class="chips">
        <span class="chip" id="lat">Latency: — ms</span>
        <span class="chip">Version: <span id="ver">{GIT_SHA[:7]}</span></span>
        <a class="chip link" href="/docs" target="_blank">Open API Docs</a>
        <span class="chip">API: <code>/greet?name=…</code></span>
      </div>

      <div class="foot">
        Learning outcomes: CLI vs Docker run • CI tests on push • Build & tag image • Auto deploy (CD) • Show running version.
      </div>
    </div>
  </div>

  <script>
    const bar = document.getElementById('bar');
    const msg = document.getElementById('msg');
    const lat = document.getElementById('lat');
    const nameInput = document.getElementById('name');
    const btn = document.getElementById('btn');

    async function load(name) {{
      bar.style.width = '35%';
      const t0 = performance.now();
      const res = await fetch('/greet' + (name ? '?name=' + encodeURIComponent(name) : ''));
      const data = await res.json();
      const t1 = performance.now();
      msg.textContent = data.message;
      lat.textContent = 'Latency: ' + Math.max(0, Math.round(t1 - t0)) + ' ms';
      bar.style.width = '100%'; setTimeout(()=>bar.style.width='0%', 260);
      sparkles();
    }}

    btn.addEventListener('click', () => load(nameInput.value.trim()));
    nameInput.addEventListener('keydown', (e) => {{ if (e.key === 'Enter') btn.click(); }});

    // Show server version from API (in case not baked)
    fetch('/version').then(r=>r.json()).then(v=>{{
      const el = document.getElementById('ver');
      if (el) el.textContent = (v.version || '').slice(0,7) || el.textContent;
    }}).catch(()=>{{}});

    // tiny confetti
    const cvs = document.getElementById('confetti'), ctx = cvs.getContext('2d');
    function resize() {{ cvs.width = innerWidth; cvs.height = innerHeight; }}
    addEventListener('resize', resize); resize();
    function sparkles() {{
      const dots = Array.from({{length: 26}}, () => ({{
        x: Math.random()*cvs.width, y: Math.random()*cvs.height*0.15 + cvs.height*0.35,
        vx: (Math.random()-.5)*2.2, vy: (Math.random()*-2.8)-1.2,
        a: 1, c: ['#22d3ee','#60a5fa','#93c5fd','#e879f9','#34d399'][Math.floor(Math.random()*5)]
      }}));
      let t=0;
      const id = setInterval(()=>{{
        ctx.clearRect(0,0,cvs.width,cvs.height);
        dots.forEach(d=>{{
          d.x+=d.vx; d.y+=d.vy; d.vy+=0.05; d.a-=0.02;
          ctx.globalAlpha=Math.max(0,d.a); ctx.fillStyle=d.c; ctx.fillRect(d.x,d.y,4,4);
        }});
        if ((t+=1)>60) {{ clearInterval(id); ctx.clearRect(0,0,cvs.width,cvs.height); }}
    }}, 16);
    }}
  </script>
</body>
</html>
"""
