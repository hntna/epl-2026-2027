import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_style = """<style>
:root{
  /* Typography */
  --font-ui: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-display: 'Inter', system-ui, sans-serif;
  --font-head: 'Inter', system-ui, sans-serif;

  /* ═══ VIBRANT, YOUTHFUL & PROFESSIONAL (Light Mode) ═══ */
  --bg:#F8FAFC; /* Slate 50 */
  --bg-elevated:#FFFFFF;
  --surface:#FFFFFF;
  --surface2:#F1F5F9; /* Slate 100 */
  --surface3:#E2E8F0; /* Slate 200 */
  --border:#E2E8F0; /* Slate 200 */
  --border-accent:#CBD5E1; /* Slate 300 */

  /* Vibrant Accents */
  --primary:#4F46E5; /* Indigo 600 */
  --primary-dim:#EEF2FF; /* Indigo 50 */
  --primary-text:#4338CA; /* Indigo 700 */

  --gold:#F59E0B;
  --gold-dim:#FEF3C7;
  --green:#10B981;
  --green-dim:#D1FAE5;
  --red:#F43F5E; /* Rose 500 */
  --red-dim:#FFE4E6;
  --orange:#F97316;
  --orange-dim:#FFEDD5;
  --cyan:#06B6D4;
  --cyan-dim:#CFFAFE;
  --blue:#3B82F6;
  --blue-dim:#DBEAFE;

  --text:#0F172A; /* Slate 900 */
  --text2:#475569; /* Slate 600 */
  --muted:#94A3B8; /* Slate 400 */

  --header-h:64px;
  --topbar-h:56px;
  --bottomnav-h:70px;
  
  --shadow-sm:0 1px 2px 0 rgba(0,0,0,0.05);
  --shadow:0 4px 12px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.03);
  --shadow-lg:0 12px 24px rgba(79, 70, 229, 0.1), 0 4px 8px rgba(0,0,0,0.05);
  --shadow-colored:0 10px 20px rgba(79, 70, 229, 0.25);
  
  --radius:16px;--radius-sm:10px;--radius-xs:6px;
  --modal-bg:rgba(15,23,42,0.6);

  color-scheme:light;
}

body.dark-mode{
  /* ═══ VIBRANT, YOUTHFUL & PROFESSIONAL (Dark Mode) ═══ */
  --bg:#0F172A; /* Slate 900 */
  --bg-elevated:#1E293B; /* Slate 800 */
  --surface:#1E293B; /* Slate 800 */
  --surface2:#334155; /* Slate 700 */
  --surface3:#475569; /* Slate 600 */
  --border:#334155; 
  --border-accent:#475569;

  --primary:#6366F1; /* Indigo 500 */
  --primary-dim:rgba(99,102,241,0.15);
  --primary-text:#818CF8; /* Indigo 400 */

  --gold:#FBBF24;--gold-dim:rgba(251,191,36,0.15);
  --green:#34D399;--green-dim:rgba(52,211,153,0.15);
  --red:#FB7185;--red-dim:rgba(251,113,133,0.15);
  --orange:#FB923C;--orange-dim:rgba(251,146,60,0.15);
  --cyan:#22D3EE;--cyan-dim:rgba(34,211,238,0.15);
  --blue:#60A5FA;--blue-dim:rgba(96,165,250,0.15);

  --text:#F8FAFC; /* Slate 50 */
  --text2:#CBD5E1; /* Slate 300 */
  --muted:#94A3B8; /* Slate 400 */
  
  --shadow:0 4px 16px rgba(0,0,0,0.4);
  --shadow-lg:0 12px 24px rgba(0,0,0,0.5);
  --shadow-colored:0 8px 20px rgba(99,102,241,0.25);
  --modal-bg:rgba(0,0,0,0.7);

  color-scheme:dark;
}

*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}

body{
  background:var(--bg);color:var(--text);font-family:var(--font-ui);
  min-height:100vh;min-height:100dvh;overflow-x:hidden;
  font-size:14px;line-height:1.5;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  -webkit-tap-highlight-color:transparent;
}

/* Beautiful youthful gradient bar */
body::before{
  content:'';position:fixed;top:0;left:0;right:0;height:4px;
  background:linear-gradient(90deg, #3B82F6, #8B5CF6, #EC4899, #F43F5E, #F59E0B);
  z-index:9999;
}

::selection{background:var(--primary-dim);color:var(--primary-text)}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:var(--muted)}

button{font-family:inherit;-webkit-tap-highlight-color:transparent}
:focus-visible{outline:2px solid var(--primary);outline-offset:2px;border-radius:6px}

/* KEYFRAMES */
@keyframes fadeSlideUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes overlayIn{from{opacity:0}to{opacity:1}}
@keyframes modalIn{from{opacity:0;transform:translateY(20px) scale(0.98)}to{opacity:1;transform:none}}

/* HEADER */
#sidebarOverlay{display:none;position:fixed;inset:0;background:var(--modal-bg);z-index:90;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}

#sidebar{
  position:fixed;top:0;left:0;right:0;
  width:100%;height:var(--header-h);
  background:rgba(255, 255, 255, 0.85);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border-bottom:1px solid var(--border);
  display:flex;flex-direction:row;align-items:center;
  z-index:100;
  box-shadow:var(--shadow-sm);
}
body.dark-mode #sidebar {
  background:rgba(30, 41, 59, 0.85);
}

.sidebar-logo{padding:0 24px;flex-shrink:0;display:flex;align-items:center;height:100%}
.logo-row{display:flex;align-items:center;gap:12px}
.logo-icon{
  width:32px;height:32px;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  font-size:18px;
  background:linear-gradient(135deg, #4F46E5, #EC4899);
  color:#fff;border-radius:10px;
  box-shadow:0 4px 10px rgba(236, 72, 153, 0.3);
}
.logo-text .lt{
  font-family:var(--font-head);font-weight:800;
  font-size:16px;letter-spacing:-0.5px;color:var(--text);
  line-height:1;
}
.logo-text .ls{display:none}

.sidebar-nav{
  flex:1;display:flex;flex-direction:row;align-items:center;
  justify-content:flex-start;gap:8px;
  padding:0 16px;height:100%;
  overflow-x:auto;scrollbar-width:none;
}
.sidebar-nav::-webkit-scrollbar{display:none}
.nav-label{display:none}

.nav-item{
  display:flex;align-items:center;gap:6px;
  padding:8px 16px;margin:0;
  background:transparent;border:none;border-radius:99px;
  color:var(--text2);
  font-size:14px;font-weight:600;cursor:pointer;
  position:relative;white-space:nowrap;flex-shrink:0;
  transition:all .2s ease;
}
.nav-item:hover{background:var(--surface2);color:var(--text)}
.nav-item.active{
  background:linear-gradient(135deg, var(--primary), #8B5CF6);
  color:#fff;
  box-shadow:var(--shadow-colored);
}
.nav-icon{display:none}

.nav-badge{
  margin-left:4px;min-width:20px;height:20px;padding:0 6px;
  display:inline-flex;align-items:center;justify-content:center;
  background:var(--surface3);border-radius:99px;
  font-size:11px;font-weight:700;color:var(--text);
}
.nav-item.active .nav-badge{background:rgba(255,255,255,0.2);color:#fff}
.admin-nav-lock{margin-left:4px;font-size:11px;opacity:0.5}
.nav-badge + .admin-nav-lock{margin-left:4px}
.sidebar-footer{display:none}

/* MAIN & TOPBAR */
#main{
  margin-left:0!important;
  min-height:100vh;display:flex;flex-direction:column;position:relative;z-index:1;
  padding-top:var(--header-h);
}

#topbar{
  height:var(--topbar-h);
  display:flex;align-items:center;gap:14px;
  padding:0 24px;
  position:sticky;top:var(--header-h);z-index:80;
  background:rgba(248, 250, 252, 0.85); /* Matches light bg */
  backdrop-filter:blur(8px);
}
body.dark-mode #topbar {
  background:rgba(15, 23, 42, 0.85);
}

.hamburger{display:none!important}
.breadcrumb{display:none}

.topbar-right{margin-left:auto;display:flex;align-items:center;gap:12px;flex-shrink:0}

.member-identity-bar{
  display:flex;align-items:center;gap:12px;
  background:var(--surface);border:1px solid var(--border);
  padding:4px 4px 4px 12px;border-radius:99px;
  box-shadow:var(--shadow-sm);
}
.member-identity-name{font-size:13px;font-weight:600;color:var(--text);max-width:150px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.member-switch-btn{
  background:linear-gradient(135deg, var(--primary), #8B5CF6);color:#fff;
  border:none;padding:6px 14px;border-radius:99px;
  font-size:13px;font-weight:600;cursor:pointer;transition:transform .2s;white-space:nowrap;
  box-shadow:var(--shadow-colored);
}
.member-switch-btn:active{transform:scale(.95)}

.admin-badge{font-size:12px;font-weight:700;padding:6px 12px;border-radius:99px;white-space:nowrap}
.admin-badge.is-admin{background:linear-gradient(135deg, #EC4899, #F43F5E);color:#fff;border:none;box-shadow:0 4px 10px rgba(236,72,153,0.3)}
.admin-badge.is-guest{display:none}

.admin-btn{
  background:var(--surface);border:1px solid var(--border);
  color:var(--text);padding:6px 14px;border-radius:99px;
  font-size:13px;font-weight:600;cursor:pointer;transition:all .2s;white-space:nowrap;
  box-shadow:var(--shadow-sm);
}
.admin-btn:hover{background:var(--surface2); border-color:var(--primary-dim);}
.admin-btn:active{transform:scale(.96)}

.theme-btn{
  width:32px;height:32px;border-radius:99px;flex-shrink:0;
  background:var(--surface);border:1px solid var(--border);
  color:var(--text);font-size:14px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;transition:all .2s;
  box-shadow:var(--shadow-sm);
}
.theme-btn:hover{background:var(--primary-dim);color:var(--primary);transform:rotate(15deg);border-color:var(--primary-dim);}

/* HERO BANNER */
.hero-banner{
  padding:32px 24px 16px;
  text-align:center;
}
.hero-content{display:inline-flex;flex-direction:column;align-items:center}
.hero-trophy{display:none}
.hero-info{min-width:0}
.hero-title{
  font-family:var(--font-head);font-weight:800;
  font-size:36px;letter-spacing:-1.5px;
  line-height:1.1;color:var(--text);margin-bottom:8px;
}
.hero-title span{
  background:linear-gradient(135deg, var(--primary), #EC4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-sub{
  font-size:15px;font-weight:500;color:var(--text2);
}
.hero-decoration{display:none}

/* CONTENT */
#content{flex:1;padding:0 24px 48px;max-width:1000px;width:100%;margin:0 auto;z-index:2;min-width:0}
footer{
  text-align:center;padding:32px 20px;font-size:13px;color:var(--muted);
  border-top:1px solid var(--border);font-weight:500;
}

.tab-pane{display:none;animation:fadeSlideUp .3s ease}
.tab-pane.active{display:block}

/* Section Header */
.section-header{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin:0 0 20px}
.section-title{
  font-family:var(--font-head);font-weight:700;
  font-size:20px;letter-spacing:-0.5px;color:var(--text);
  display:flex;align-items:center;gap:12px;
}
.section-icon{display:none}

/* STAT CARDS */
.stats-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:16px;margin-bottom:32px;
}
.stat-card{
  display:flex;flex-direction:column;gap:6px;
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);padding:20px;
  box-shadow:var(--shadow-sm);
  transition:all .3s ease;
  position: relative;
  overflow: hidden;
}
.stat-card::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: transparent; transition: background 0.3s;
}
.stat-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg)}
.stat-card:hover::after { background: linear-gradient(90deg, var(--primary), var(--cyan)); }

.stat-card>div:last-child{min-width:0}
.stat-icon{display:none}
.s-label{font-size:12px;font-weight:700;color:var(--text2);text-transform:uppercase;letter-spacing:0.5px}
.s-value{font-family:var(--font-display);font-size:32px;font-weight:800;line-height:1;color:var(--text);letter-spacing:-1px}
.s-sub{display:none}

/* TABLES */
.table-wrap{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);overflow-x:auto;-webkit-overflow-scrolling:touch;
  box-shadow:var(--shadow-sm);
}
table{width:100%;border-collapse:collapse;min-width:520px}
thead th{
  text-align:left;padding:14px 20px;
  font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;
  color:var(--text2);border-bottom:1px solid var(--border);
  background:var(--surface2);white-space:nowrap;
}
tbody td{padding:14px 20px;font-size:13px;border-bottom:1px solid var(--border);vertical-align:middle;white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:var(--surface2)}

#rankBody tr:nth-child(1) td{background:var(--gold-dim)}
#rankBody tr:nth-child(2) td{background:var(--surface2)}
#rankBody tr:nth-child(3) td{background:var(--orange-dim)}

.rank{font-family:var(--font-display);font-size:16px;font-weight:800;color:var(--text2)}
.name-cell{font-weight:700;color:var(--text)}
.name-avatar{display:flex;align-items:center;gap:10px}

.avatar{
  width:32px;height:32px;border-radius:50%;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:800;color:#fff;
  background:linear-gradient(135deg, var(--primary), #EC4899);
  box-shadow:var(--shadow-sm);
}

.pill{
  display:inline-flex;align-items:center;justify-content:center;
  width:26px;height:26px;border-radius:6px;
  font-size:12px;font-weight:700;
}
.pill-win{background:var(--green-dim);color:var(--green)}
.pill-loss{background:var(--red-dim);color:var(--red)}
.pill-draw{background:var(--gold-dim);color:var(--gold)}
.pill-neu{background:var(--surface3);color:var(--text2)}

.amount{font-family:var(--font-display);font-weight:800;font-size:14px;letter-spacing:-0.5px}

.empty-state{text-align:center;padding:48px 24px;color:var(--text2);font-size:14px;font-weight:600;background:var(--surface);border:1px dashed var(--border-accent);border-radius:var(--radius)}
.empty-state .ei{font-size:32px;margin:0 auto 12px;opacity:0.5;}

/* TAGS */
.tag{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:6px;white-space:nowrap}
.tag-stage{background:var(--primary-dim);color:var(--primary-text)}
.tag-date{background:transparent;color:var(--text2);padding:0}
.tag-handicap{background:var(--cyan-dim);color:var(--cyan)}
.tag-bet{background:var(--gold-dim);color:var(--gold)}
.tag-done{background:var(--green-dim);color:var(--green)}
.tag-open{background:var(--surface2);color:var(--text)}
.tag-locked{background:var(--red-dim);color:var(--red)}

/* MATCH CARDS */
.match-item{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);padding:24px;margin-bottom:24px;
  box-shadow:var(--shadow);
  transition:all .3s ease;
  min-width:0;
  position: relative;
  overflow: hidden;
}
.match-item::after {
  content: ''; position: absolute; top: 0; left: 0; width: 4px; bottom: 0;
  background: transparent; transition: background 0.3s;
}
.match-item:hover{box-shadow:var(--shadow-lg); border-color:var(--primary-dim);}
.match-item:hover::after{background: var(--primary);}
.match-item.is-locked{opacity:0.9;background:var(--surface2)}

.match-top{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.match-no{font-family:var(--font-display);font-size:12px;font-weight:800;color:var(--primary-text);background:var(--primary-dim);padding:4px 8px;border-radius:6px;flex-shrink:0}
.match-meta{display:flex;align-items:center;gap:10px;flex-wrap:wrap;flex:1;min-width:0}
.match-actions-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-left:auto}

/* Teams & Score */
.match-teams-row{
  display:flex;align-items:center;justify-content:space-between;
  gap:16px;margin-bottom:20px;
}
.match-team-box{display:flex;align-items:center;gap:12px;flex:1;min-width:0}
.match-team-box.right-side{flex-direction:row-reverse;text-align:right}
.mteam-flag{font-size:28px;line-height:1; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));}
.mteam-name{font-size:18px;font-weight:800;color:var(--text);max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:normal;line-height:1.2;word-break:break-word}

.vs-center{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:linear-gradient(135deg, var(--surface2), var(--surface3));border-radius:12px;
  padding:10px 16px;min-width:80px;flex-shrink:0;
  box-shadow: inset 0 2px 4px rgba(255,255,255,0.5);
}
body.dark-mode .vs-center { box-shadow: inset 0 2px 4px rgba(0,0,0,0.5); }
.vs-txt{font-size:11px;font-weight:800;color:var(--text2);text-transform:uppercase}
.vs-score{font-family:var(--font-display);font-size:32px;font-weight:900;line-height:1;color:var(--text);letter-spacing:-1px}
.vs-handicap{font-size:12px;font-weight:700;color:var(--text2);margin-top:4px;white-space:nowrap}

/* Prediction Panel */
.pred-panel{background:var(--bg);border-radius:var(--radius-sm);padding:20px;margin-top:16px;border:1px solid var(--border)}
.pred-panel-header{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:16px}
.pred-panel-title{font-size:12px;font-weight:800;color:var(--text2);text-transform:uppercase;letter-spacing:0.5px}
.pred-count-item{font-weight:700}
.pred-locked-bar{background:var(--red-dim);color:var(--red);padding:4px 12px;border-radius:6px;font-weight:700;font-size:12px}

.pred-rows{display:flex;flex-direction:column;gap:10px}
.pred-member-row{display:grid;grid-template-columns:140px minmax(0,1fr) auto;align-items:center;gap:16px;background:var(--surface);border-radius:8px;padding:10px 14px;border:1px solid var(--border);box-shadow:0 1px 2px rgba(0,0,0,0.02)}
.pred-member-row.is-mine{border:2px solid var(--primary);box-shadow:0 0 0 2px var(--primary-dim)}
.pred-member-row.is-confirmed{opacity:1}
.pred-member-row.is-other{opacity:0.6}
.pred-member-row.is-locked-row{opacity:0.8;background:var(--surface2)}

.pred-member-name{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:700;color:var(--text);min-width:0;overflow:hidden}
.me-tag{background:var(--primary);color:#fff;font-size:10px;font-weight:800;padding:2px 6px;border-radius:4px;flex-shrink:0}

/* Prediction Buttons (Ticket Style) */
.pred-btns{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,0.8fr) minmax(0,1fr);gap:8px;min-width:0}
.pred-btns.pred-btns-2{grid-template-columns:1fr 1fr}
.pbet{
  border:1px solid var(--border-accent);background:var(--surface);color:var(--text2);
  font-size:13px;font-weight:700;padding:10px 6px;border-radius:8px;
  cursor:pointer;transition:all .2s;
  white-space:normal; word-break:break-word; line-height:1.2; min-width:0;
  text-align:center; display:flex; align-items:center; justify-content:center;
}
.pbet:hover{background:var(--surface2);color:var(--text);border-color:var(--border-accent)}
.pbet:active{transform:scale(.97)}
.pbet.sel-win{background:var(--green);color:#fff;border-color:var(--green);box-shadow:0 4px 12px rgba(16,185,129,0.4)}
.pbet.sel-draw{background:var(--gold);color:#fff;border-color:var(--gold);box-shadow:0 4px 12px rgba(245,158,11,0.4)}
.pbet.sel-loss{background:var(--red);color:#fff;border-color:var(--red);box-shadow:0 4px 12px rgba(244,63,94,0.4)} /* Using rose-red */

.is-other .pbet,.is-locked-row .pbet,.is-confirmed .pbet{pointer-events:none}

.pred-confirm{display:flex;align-items:center;gap:8px;justify-content:flex-end;flex-wrap:wrap}
.pc-btn{border:none;border-radius:6px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;transition:transform .2s;white-space:nowrap}
.pc-btn:active{transform:scale(.95)}
.pc-confirm{background:linear-gradient(135deg, var(--primary), #8B5CF6);color:#fff;box-shadow:var(--shadow-colored)}
.pc-unlock{background:var(--surface);color:var(--text);border:1px solid var(--border)}
.pc-badge{font-size:12px;font-weight:700;padding:6px 12px;border-radius:6px;white-space:nowrap}
.pc-done{background:var(--surface3);color:var(--text)}
.pc-pending{background:var(--surface);color:var(--text);border:1px solid var(--border)}
.pc-picked{background:var(--primary-dim);color:var(--primary-text)}
.pc-none{background:transparent;color:var(--muted)}
.pc-hint{font-size:11px;color:var(--text2);white-space:nowrap;font-weight:600;}

.btn-sm{border:none;background:var(--surface);border:1px solid var(--border);color:var(--text);font-size:12px;font-weight:700;padding:6px 12px;border-radius:6px;cursor:pointer;transition:all .2s;white-space:nowrap}
.btn-sm:active{transform:scale(.95)}
.btn-edit:hover{background:var(--primary-dim);color:var(--primary);border-color:var(--primary-dim)}
.btn-del:hover{background:var(--red-dim);color:var(--red);border-color:var(--red-dim)}
.btn-orange{background:var(--surface);color:var(--orange);border-color:var(--border)}
.btn-orange:hover{background:var(--orange-dim);border-color:var(--orange-dim)}
.btn-lock,.btn-unlock{border:none;border-radius:6px;padding:6px 12px;font-size:12px;font-weight:700;cursor:pointer;transition:transform .2s;white-space:nowrap}
.btn-lock{background:var(--red-dim);color:var(--red)}
.btn-unlock{background:var(--green-dim);color:var(--green)}
.btn-lock:active,.btn-unlock:active{transform:scale(.95)}

/* RESULTS TAB */
.filter-tabs{display:flex;gap:8px;margin-bottom:24px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:4px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.filter-tabs::-webkit-scrollbar{display:none}
.filter-tab{flex:1;border:none;background:transparent;color:var(--text2);font-size:13px;font-weight:700;padding:8px 16px;border-radius:6px;cursor:pointer;white-space:nowrap;transition:all .2s}
.filter-tab:hover{color:var(--text)}
.filter-tab.active{background:var(--surface);color:var(--primary-text);box-shadow:0 2px 4px rgba(0,0,0,0.05);font-weight:800}

.result-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);margin-bottom:24px;overflow:hidden;box-shadow:var(--shadow-sm);transition:all .3s ease;}
.result-card:hover{box-shadow:var(--shadow)}
.result-card.done{border:1px solid var(--green); box-shadow:0 4px 12px rgba(16,185,129,0.1)}
.result-card-header{display:flex;align-items:flex-start;gap:12px;padding:20px 24px;background:var(--surface2);border-bottom:1px solid var(--border)}
.result-card-body{padding:24px}

.score-entry-row{display:flex;align-items:center;justify-content:center;gap:24px;margin-bottom:24px}
.score-team{display:flex;flex-direction:column;align-items:center;gap:12px;text-align:center;min-width:0;flex:1}
.score-team-name{font-size:15px;font-weight:700;color:var(--text);max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:normal;line-height:1.2;word-break:break-word}
.score-input-box{display:flex;flex-direction:column;align-items:center}
.score-vs-divider{font-family:var(--font-display);font-size:24px;color:var(--text2);font-weight:800;margin:0 16px}
.score-input-big{width:64px;height:64px;background:var(--surface2);border:1px solid var(--border);border-radius:12px;color:var(--text);font-family:var(--font-display);font-size:32px;font-weight:800;text-align:center;outline:none;transition:all .2s;-moz-appearance:textfield;appearance:textfield;}
.score-input-big::-webkit-outer-spin-button,.score-input-big::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
.score-input-big:focus{border-color:var(--primary);background:var(--surface);box-shadow:0 0 0 3px var(--primary-dim)}
.score-input-big.s-win{color:var(--green);border-color:var(--green);box-shadow:0 0 0 3px var(--green-dim)}
.score-input-big.s-loss{color:var(--red);border-color:var(--red);box-shadow:0 0 0 3px var(--red-dim)}

.result-preview-bar{padding:12px 16px;border-radius:8px;background:var(--surface2);font-size:13px;font-weight:700;color:var(--text);text-align:center;margin-bottom:24px;border:1px solid var(--border)}
.result-preview-bar.rp-home{color:var(--green);background:var(--green-dim);border-color:var(--green-dim)}
.result-preview-bar.rp-away{color:var(--red);background:var(--red-dim);border-color:var(--red-dim)}
.result-preview-bar.rp-draw{color:var(--gold);background:var(--gold-dim);border-color:var(--gold-dim)}

.result-save-row{display:flex;align-items:center;justify-content:flex-end;gap:12px;flex-wrap:wrap}
.btn-clear-result{background:var(--surface);color:var(--red);border:1px solid var(--border);font-size:12px;font-weight:700;padding:8px 16px;border-radius:6px;cursor:pointer;transition:background .2s}
.btn-clear-result:hover{background:var(--red-dim);border-color:var(--red-dim)}

.member-result-grid{display:flex;flex-direction:column;gap:8px}
.member-result-row{display:grid;grid-template-columns:minmax(120px,140px) 1fr auto auto;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:10px 14px;}
.member-result-row.mrr-correct{border-left:4px solid var(--green)}
.member-result-row.mrr-wrong{border-left:4px solid var(--red)}
.mrr-name{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:700;color:var(--text);min-width:0;overflow:hidden}
.mrr-pick{font-size:11px;font-weight:700;padding:4px 8px;border-radius:4px;white-space:nowrap;justify-self:start;background:var(--surface2)}
.mrr-pick-win{color:var(--green);background:var(--green-dim)}
.mrr-pick-draw{color:var(--gold);background:var(--gold-dim)}
.mrr-pick-loss{color:var(--red);background:var(--red-dim)}
.mrr-pick-none{color:var(--muted);background:var(--surface3)}
.mrr-verdict{font-size:11px;font-weight:700;white-space:nowrap}
.mrr-verdict-correct{color:var(--green)}
.mrr-verdict-wrong{color:var(--red)}
.mrr-penalty{font-family:var(--font-display);font-size:15px;font-weight:800;color:var(--red);text-align:right;white-space:nowrap}

/* FORM */
.form-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:24px;box-shadow:var(--shadow-sm)}
.form-section-label{font-family:var(--font-head);font-weight:800;font-size:14px;color:var(--text);margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid var(--border)}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px}
.form-row-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-bottom:20px}
.form-group{display:flex;flex-direction:column;gap:6px;min-width:0}
.form-group label{font-size:12px;font-weight:700;color:var(--text2)}
.form-group select,.form-group input[type="date"],.form-group input[type="time"]{width:100%;background:var(--surface2);border:1px solid var(--border);color:var(--text);padding:12px 14px;border-radius:8px;font-family:var(--font-ui);font-size:14px;font-weight:600;outline:none;transition:all .2s;min-height:44px}
.form-group select:focus,.form-group input:focus{border-color:var(--primary);background:var(--surface);box-shadow:0 0 0 3px var(--primary-dim)}
.form-group select{appearance:none;-webkit-appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%234B5563' stroke-width='2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px}
body.dark-mode .form-group select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23D1D5DB' stroke-width='2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")}

.bet-control{display:flex;align-items:center;gap:16px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:6px;width:max-content;max-width:100%}
.bet-btn{width:36px;height:36px;border-radius:6px;flex-shrink:0;border:1px solid var(--border);background:var(--surface);color:var(--text);font-size:20px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s;box-shadow:0 1px 2px rgba(0,0,0,0.05)}
.bet-btn:hover{background:var(--surface2);border-color:var(--border-accent)}
.bet-btn:active{transform:scale(.92)}
.bet-val{font-family:var(--font-display);font-size:20px;font-weight:800;color:var(--text);min-width:100px;text-align:center;letter-spacing:-0.5px}

/* NHÀ CÁI */
.banker-bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:8px 12px;border-radius:8px;background:var(--surface2);border:1px solid var(--border);margin-bottom:12px}
.bb-label{font-size:11px;font-weight:800;letter-spacing:.5px;color:var(--text2);text-transform:uppercase;white-space:nowrap}
.banker-select{background:var(--surface);border:1px solid var(--border-accent);color:var(--text);padding:6px 10px;border-radius:6px;font-size:12px;font-weight:700;outline:none;min-width:150px;cursor:pointer}
.banker-name{font-size:13px;font-weight:800;color:var(--text)}
.banker-name.none{color:var(--muted);font-weight:600;font-style:italic}
.banker-warn{font-size:11px;color:var(--orange);font-weight:700}
.banker-tag{font-size:9px;font-weight:800;background:linear-gradient(135deg, var(--primary), #EC4899);color:#fff;padding:2px 6px;border-radius:4px;margin-left:4px;white-space:nowrap;display:inline-block;box-shadow:0 2px 4px rgba(236,72,153,0.3)}
.pred-member-row.is-banker{background:var(--surface2);border-color:var(--border)}
.banker-row-note{margin-left:auto;font-size:11px;font-weight:600;color:var(--text2);font-style:italic;white-space:nowrap}
.member-result-row.mrr-banker{background:var(--surface2);border-color:var(--border)}

/* BUTTONS */
.btn{border:none;border-radius:8px;padding:12px 24px;font-size:13px;font-weight:700;cursor:pointer;transition:transform .2s;min-height:44px;white-space:nowrap}
.btn:active{transform:scale(.96)}
.btn-primary{background:linear-gradient(135deg, var(--primary), #8B5CF6);color:#fff;box-shadow:var(--shadow-colored)}

/* MODALS */
.modal-overlay{display:none;position:fixed;inset:0;z-index:200;background:var(--modal-bg);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:24px}
.modal-overlay.open{display:flex;animation:overlayIn .2s ease}

.modal{background:var(--bg-elevated);border:1px solid var(--border);border-radius:16px;padding:24px;width:100%;max-width:400px;box-shadow:var(--shadow-lg);animation:modalIn .2s ease;max-height:90vh;max-height:90dvh;overflow-y:auto}

.modal-title{font-family:var(--font-head);font-weight:800;font-size:20px;letter-spacing:-0.5px;color:var(--text);margin-bottom:6px;text-align:center}
.modal-sub{font-size:13px;color:var(--text2);margin-bottom:20px;font-weight:600;text-align:center}
.modal-btns{display:flex;flex-direction:column;gap:10px;margin-top:20px}
.btn-full{width:100%;border:none;border-radius:8px;padding:12px;font-size:14px;font-weight:700;cursor:pointer;transition:transform .2s;min-height:44px}
.btn-full:active{transform:scale(.97)}
.btn-cancel{background:var(--surface2);color:var(--text);border:1px solid var(--border)}
.btn-confirm{background:linear-gradient(135deg, var(--primary), #8B5CF6);color:#fff;box-shadow:var(--shadow-colored)}
.btn-confirm-red{background:linear-gradient(135deg, var(--red), #E11D48);color:#fff;box-shadow:0 4px 10px rgba(225,29,72,0.3)}

.modal input{min-height:44px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:10px 14px;color:var(--text);font-family:var(--font-ui);font-size:14px;width:100%;outline:none;transition:all .2s;margin-bottom:12px}
.modal input:focus{border-color:var(--primary);background:var(--surface);box-shadow:0 0 0 3px var(--primary-dim)}

/* TOAST */
.toast{position:fixed;top:32px;left:50%;z-index:300;display:flex;align-items:center;justify-content:center;background:var(--text);border-radius:8px;padding:12px 20px;font-size:13px;font-weight:700;color:var(--bg);box-shadow:var(--shadow-lg);opacity:0;transform:translate(-50%,-20px) scale(0.9);pointer-events:none;transition:all .3s ease;max-width:min(90vw,400px)}
.toast.show{opacity:1;transform:translate(-50%,0) scale(1)}
.toast-bar{display:none}

/* RESPONSIVE */
@media(max-width:900px){
  .pred-member-row{grid-template-columns:1fr;gap:12px}
  .pred-confirm{justify-content:flex-start}
  .member-result-row{display:flex;flex-wrap:wrap;align-items:center;row-gap:8px}
  .mrr-name{flex:1 1 100%}.mrr-penalty{margin-left:auto}
  .match-teams-row{flex-direction:column;gap:12px}
  .match-team-box{width:100%;justify-content:center}
  .match-team-box.right-side{flex-direction:row}
  .score-entry-row{flex-direction:column;gap:12px}
  .score-vs-divider{transform:rotate(90deg);margin:4px 0}
}

@media(max-width:768px){
  /* Clean Premium Bottom Tab Bar */
  #sidebar{
    top:auto;left:0;right:0;bottom:0;
    width:100%;height:calc(var(--bottomnav-h) + env(safe-area-inset-bottom,0px));
    flex-direction:row;border-bottom:none;border-top:1px solid var(--border);
    background:rgba(255,255,255,0.85);
    backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
    box-shadow:0 -4px 16px rgba(0,0,0,0.05);
  }
  body.dark-mode #sidebar{background:rgba(30,41,59,0.85)}
  .sidebar-logo{display:none}

  .sidebar-nav{
    flex:1;display:flex;flex-direction:row;align-items:stretch;justify-content:space-around;
    padding:4px 4px calc(4px + env(safe-area-inset-bottom,0px));overflow:visible;
  }
  .nav-item{
    flex:1;flex-direction:column;justify-content:center;align-items:center;
    gap:4px;margin:0;padding:4px 2px;font-size:0;
    border-radius:10px;color:var(--muted);max-width:80px;background:transparent!important;
  }
  .nav-item.active{color:var(--primary)}
  .nav-icon{display:block;font-size:22px;line-height:1}
  
  #nav-rank .nav-icon{font-size:0;} #nav-rank .nav-icon::after{content:'🏆';font-size:22px}
  #nav-matches .nav-icon{font-size:0;} #nav-matches .nav-icon::after{content:'⚽';font-size:22px}
  #nav-results .nav-icon{font-size:0;} #nav-results .nav-icon::after{content:'📊';font-size:22px}
  #nav-add .nav-icon{font-size:0;} #nav-add .nav-icon::after{content:'➕';font-size:22px}
  #nav-members .nav-icon{font-size:0;} #nav-members .nav-icon::after{content:'👥';font-size:22px}

  .nav-item::after{content:'';font-size:10px;font-weight:700;letter-spacing:0;margin-top:2px}
  #nav-rank::after{content:'BXH'}
  #nav-matches::after{content:'Trận đấu'}
  #nav-results::after{content:'Kết quả'}
  #nav-add::after{content:'Thêm'}
  #nav-members::after{content:'T.viên'}

  .nav-badge{position:absolute;top:4px;right:50%;margin:0;transform:translateX(10px);min-width:16px;height:16px;padding:0 4px;font-size:9px;background:linear-gradient(135deg, var(--red), #E11D48);color:#fff;border:none;box-shadow:none}
  .nav-item.active .nav-badge{background:linear-gradient(135deg, var(--red), #E11D48);color:#fff}
  .admin-nav-lock{position:absolute;top:4px;left:50%;margin:0;transform:translateX(-24px);font-size:10px}

  #main{margin-left:0!important;padding-top:0}
  #content{padding:0 16px calc(var(--bottomnav-h) + env(safe-area-inset-bottom,0px) + 24px)}

  #topbar{height:56px;padding:0 16px;gap:8px;position:sticky;top:0;background:rgba(248, 250, 252, 0.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}
  body.dark-mode #topbar{background:rgba(30,41,59,0.85)}
  
  .member-identity-name{max-width:80px;font-size:12px}
  .member-identity-bar{padding:4px 4px 4px 10px;gap:6px;background:transparent;border:none;box-shadow:none}
  .member-switch-btn{padding:6px 10px;font-size:11px;box-shadow:none}
  .admin-badge{display:none}
  .admin-btn{padding:6px 10px;font-size:11px;background:var(--surface2);border:none;box-shadow:none}
  .theme-btn{width:28px;height:28px;font-size:14px;background:var(--surface2);border:none;box-shadow:none}

  .hero-banner{padding:24px 0 12px;margin:0 16px 16px}
  .hero-title{font-size:28px}
  .hero-sub{font-size:13px}

  .toast{top:auto;bottom:calc(var(--bottomnav-h) + env(safe-area-inset-bottom,0px) + 24px);transform:translate(-50%,20px) scale(0.9)}

  .modal-overlay{padding:0;align-items:flex-end}
  .modal{max-width:100%!important;border-radius:20px 20px 0 0;border:none;padding:24px 20px calc(24px + env(safe-area-inset-bottom,0px));animation:sheetIn .3s ease}
  @keyframes sheetIn{from{transform:translateY(100%)}to{transform:none}}

  .section-title{font-size:18px}
  .stats-grid{grid-template-columns:1fr 1fr;gap:12px}
  .stat-card{padding:16px;gap:4px}
  .s-label{font-size:11px}
  .s-value{font-size:24px}

  .match-item{padding:16px;margin-bottom:16px;border-radius:16px}
  .match-top{flex-direction:row;align-items:flex-start;gap:8px; flex-wrap: wrap;}
  .match-actions-row { 
    margin-left: auto !important; 
    flex-wrap: nowrap !important; 
    gap: 6px !important; 
    width: 100% !important;
    justify-content: flex-end !important;
    margin-top: 4px !important;
  }
  .match-teams-row{gap:8px; flex-direction:row;}
  .mteam-flag{font-size:24px}
  .mteam-name{font-size:15px}
  .vs-score{font-size:24px}
  .vs-center{min-width: 60px; padding: 6px;}

  .pbet{font-size:12px;padding:10px 4px}
  .pred-btns{gap:6px}

  .result-card-header{padding:14px 16px}
  .result-card-body{padding:16px}
  .score-input-big{width:56px;height:56px;font-size:28px;border-radius:12px}
  .form-card{padding:20px 16px}
  .filter-tab{font-size:12px;padding:8px 12px}

  table{min-width:0}
  thead th,tbody td{padding:10px 12px;font-size:13px}

  .match-team-box{flex-direction: row;}
  .match-team-box.right-side{flex-direction: row-reverse;}
  
  .score-entry-row { flex-direction: row !important; gap: 8px !important; }
  .score-input-big { width: 44px !important; height: 44px !important; font-size: 20px !important; }
  .score-team-name { font-size: 13px !important; }
  .score-vs-divider { transform: none !important; font-size: 16px !important; margin: 0 4px !important; }
  
  .pred-member-row { grid-template-columns: 80px minmax(0,1fr) auto !important; gap: 6px !important; padding: 8px !important; }
  .member-result-row { grid-template-columns: 80px minmax(0,1fr) auto auto !important; gap: 6px !important; padding: 8px !important; }
  .pred-member-name, .mrr-name { font-size: 12px !important; gap: 4px !important; }
  
  #tab-members th:nth-child(3), #tab-members td:nth-child(3),
  #tab-members th:nth-child(4), #tab-members td:nth-child(4),
  #tab-members th:nth-child(5), #tab-members td:nth-child(5) {
      display: none !important;
  }
}
@media(max-width:560px){
  .form-row{grid-template-columns:1fr}
  #tab-rank th:nth-child(5),#tab-rank td:nth-child(5){display:none}
  .banker-bar .banker-select{flex:1 1 100%;min-width:0;font-size:14px}
}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:0.01ms!important;animation-iteration-count:1!important;transition-duration:0.01ms!important}
}
</style>"""

content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("CSS patched with vibrant colors successfully")
