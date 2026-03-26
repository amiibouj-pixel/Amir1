"""
╔══════════════════════════════════════════════════════════════════════╗
║         THE COOKIE COMPANY — DASHBOARD STRATÉGIQUE                  ║
║         BI · Audit · Social Media · Matrice BCG                     ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
#  CONFIG PAGE
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="The Cookie Company · Dashboard",
    page_icon="🍪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  CSS CUSTOM — Comfortaa · Palette sobre
# ─────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  /* ── Global ─────────────────────────────── */
  html, body, [class*="css"] {
    font-family: 'Comfortaa', sans-serif !important;
    background-color: #F8F9FA !important;
    color: #37474F !important;
  }

  /* ── Sidebar ─────────────────────────────── */
  [data-testid="stSidebar"] {
    background-color: #ECEFF1 !important;
    border-right: 1px solid #CFD8DC;
  }
  [data-testid="stSidebar"] * {
    font-family: 'Comfortaa', sans-serif !important;
    color: #37474F !important;
  }
  .sidebar-logo {
    text-align: center;
    padding: 1.5rem 0 0.5rem 0;
    font-size: 2rem;
  }
  .sidebar-title {
    text-align: center;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #607D8B !important;
    margin-bottom: 1.5rem;
  }
  .sidebar-nav-item {
    display: block;
    padding: 0.55rem 1rem;
    margin: 0.2rem 0;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 500;
    color: #546E7A !important;
    text-decoration: none;
    transition: background 0.2s;
  }
  .sidebar-nav-item:hover {
    background-color: #CFD8DC;
  }
  .sidebar-section-label {
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #90A4AE !important;
    margin: 1.2rem 0 0.3rem 0.5rem;
    font-weight: 600;
  }

  /* ── Main ─────────────────────────────── */
  .main { background-color: #F8F9FA !important; }
  .block-container { padding: 2rem 2.5rem 3rem 2.5rem !important; }

  /* ── Header banner ─────────────────────────────── */
  .header-banner {
    background: linear-gradient(135deg, #607D8B 0%, #78909C 60%, #90A4AE 100%);
    border-radius: 16px;
    padding: 2.5rem 2.8rem;
    margin-bottom: 2.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }
  .header-banner h1 {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 2.1rem;
    font-weight: 700;
    color: #FFFFFF !important;
    margin: 0;
    line-height: 1.2;
  }
  .header-banner p {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 0.9rem;
    color: rgba(255,255,255,0.8) !important;
    margin: 0.4rem 0 0 0;
  }

  /* ── Section titles ─────────────────────────────── */
  .section-title {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 1.25rem;
    font-weight: 700;
    color: #37474F !important;
    margin: 0 0 0.25rem 0;
  }
  .section-subtitle {
    font-size: 0.82rem;
    color: #90A4AE !important;
    margin: 0 0 1.5rem 0;
    font-weight: 400;
  }
  .section-anchor {
    display: block;
    position: relative;
    top: -80px;
    visibility: hidden;
  }

  /* ── Cards ─────────────────────────────── */
  .card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 1.8rem;
    box-shadow: 0 1px 6px rgba(55,71,79,0.07);
    border: 1px solid #ECEFF1;
    margin-bottom: 1.5rem;
  }
  .card-sm {
    background: #FFFFFF;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 1px 4px rgba(55,71,79,0.06);
    border: 1px solid #ECEFF1;
    margin-bottom: 1rem;
  }

  /* ── KPI Covid ─────────────────────────────── */
  .kpi-card {
    background: linear-gradient(135deg, #546E7A 0%, #607D8B 100%);
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(96,125,139,0.25);
    margin: 1rem 0;
  }
  .kpi-label {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.75) !important;
    margin-bottom: 0.8rem;
  }
  .kpi-value {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 5rem;
    font-weight: 700;
    color: #FFFFFF !important;
    line-height: 1;
    margin-bottom: 0.5rem;
  }
  .kpi-arrow {
    font-size: 1.5rem;
    margin-right: 0.3rem;
  }
  .kpi-desc {
    font-family: 'Comfortaa', sans-serif !important;
    font-size: 0.82rem;
    color: rgba(255,255,255,0.65) !important;
    margin-top: 1rem;
    line-height: 1.5;
  }
  .kpi-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 0.3rem 0.9rem;
    font-size: 0.75rem;
    color: rgba(255,255,255,0.9) !important;
    margin-top: 1rem;
    letter-spacing: 0.05em;
  }

  /* ── BCG Quadrant labels ─────────────────────────────── */
  .bcg-legend {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 1rem;
  }
  .bcg-badge {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    background: #ECEFF1;
    border-radius: 20px;
    padding: 0.3rem 0.8rem;
    font-size: 0.78rem;
    color: #546E7A !important;
    font-weight: 500;
  }

  /* ── Social Posts ─────────────────────────────── */
  .post-card {
    background: #FFFFFF;
    border-radius: 14px;
    border-left: 4px solid #607D8B;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 1px 5px rgba(55,71,79,0.06);
  }
  .post-platform {
    font-size: 0.68rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #90A4AE !important;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }
  .post-hook {
    font-size: 1rem;
    font-weight: 700;
    color: #37474F !important;
    margin-bottom: 0.5rem;
    line-height: 1.4;
  }
  .post-strike {
    font-size: 0.88rem;
    color: #546E7A !important;
    line-height: 1.6;
    margin-bottom: 0.8rem;
  }
  .post-tags {
    font-size: 0.78rem;
    color: #607D8B !important;
    font-style: italic;
  }

  /* ── Segment cards ─────────────────────────────── */
  .segment-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 1.6rem;
    box-shadow: 0 1px 5px rgba(55,71,79,0.06);
    border: 1px solid #ECEFF1;
    text-align: center;
    height: 100%;
  }
  .segment-icon { font-size: 2.2rem; margin-bottom: 0.6rem; }
  .segment-name {
    font-size: 1rem;
    font-weight: 700;
    color: #37474F !important;
    margin-bottom: 0.4rem;
  }
  .segment-desc {
    font-size: 0.8rem;
    color: #78909C !important;
    line-height: 1.5;
  }

  /* ── Footer ─────────────────────────────── */
  .footer {
    text-align: center;
    font-size: 0.75rem;
    color: #B0BEC5 !important;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #ECEFF1;
  }

  /* ── Divider ─────────────────────────────── */
  .divider {
    border: none;
    border-top: 1px solid #ECEFF1;
    margin: 2.5rem 0;
  }

  /* Hide Streamlit branding */
  #MainMenu, footer { visibility: hidden; }
  header[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SIDEBAR NAVIGATION
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🍪</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">The Cookie Company</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Analyse BI</div>', unsafe_allow_html=True)
    st.markdown('<a class="sidebar-nav-item" href="#volume">📦 Volume par Pays</a>', unsafe_allow_html=True)
    st.markdown('<a class="sidebar-nav-item" href="#covid">🦠 Impact COVID-19</a>', unsafe_allow_html=True)
    st.markdown('<a class="sidebar-nav-item" href="#saisonnalite">📈 Saisonnalité</a>', unsafe_allow_html=True)
    st.markdown('<a class="sidebar-nav-item" href="#bcg">🧭 Matrice BCG</a>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Stratégie</div>', unsafe_allow_html=True)
    st.markdown('<a class="sidebar-nav-item" href="#strategy">🚀 Recommandations</a>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.72rem; color:#90A4AE; text-align:center; line-height:1.6;">
        Données simulées 2019–2025<br>
        <strong style="color:#607D8B;">Dashboard v1.0</strong><br>
        The Cookie Company © 2025
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
  <div style="font-size:3rem;">🍪</div>
  <div>
    <h1>Dashboard Stratégique</h1>
    <p>The Cookie Company · Audit BI · Portefeuille Produits · Réseaux Sociaux · 2019–2025</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DONNÉES SIMULÉES COHÉRENTES 2019–2025
# ─────────────────────────────────────────────

# --- Volume par pays (en milliers d'unités vendues, cumulé 2019-2025)
pays_data = {
    "Pays": ["États-Unis", "Allemagne", "Mexique"],
    "Volume (k unités)": [4820, 2340, 1610],
    "CA (k€)": [9640, 4680, 3220],
}
df_pays = pd.DataFrame(pays_data)

# --- Saisonnalité mensuelle (index 100 = moyenne)
mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun",
        "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"]

np.random.seed(42)
saisonnalite_base = [78, 72, 85, 92, 96, 88, 80, 84, 98, 108, 130, 148]

seasons = {}
for yr in range(2019, 2026):
    noise = np.random.normal(0, 4, 12)
    factor = 1.0
    if yr == 2020:
        factor = 0.82  # COVID
    elif yr == 2021:
        factor = 0.95
    elif yr >= 2022:
        factor = 1.0 + (yr - 2022) * 0.04
    seasons[yr] = [max(30, (v + n) * factor) for v, n in zip(saisonnalite_base, noise)]

df_saison = pd.DataFrame(seasons, index=mois)
df_saison.index.name = "Mois"

# CA mensuel 2019-2025 (k€)
ca_mensuel = {}
ca_base_annuel = {2019: 1850, 2020: 1520, 2021: 1740, 2022: 1960, 2023: 2180, 2024: 2440, 2025: 2720}
for yr, ca_ann in ca_base_annuel.items():
    idx = np.array(saisonnalite_base, dtype=float)
    idx_norm = idx / idx.sum()
    noise = np.random.normal(0, 0.01, 12)
    ca_mensuel[yr] = (idx_norm + noise) * ca_ann

# Impact COVID — période 17 mars – 11 mai (mois 3+4 partiels → approx. avril complet + moitiés mars/mai)
ca_covid_2019 = ca_mensuel[2019][2] * 0.5 + ca_mensuel[2019][3] + ca_mensuel[2019][4] * 0.35
ca_covid_2020 = ca_mensuel[2020][2] * 0.5 + ca_mensuel[2020][3] + ca_mensuel[2020][4] * 0.35
covid_pct = ((ca_covid_2020 - ca_covid_2019) / ca_covid_2019) * 100

# --- Matrice BCG (produits)
bcg_products = {
    "Produit":              ["Chocolate Bliss",  "Caramel Crunch", "Vegan Oat",   "Nutella Dream", "Classic Butter", "Choco Chip Mini"],
    "Part de marché (%)":   [28.5,               18.2,             8.4,            14.1,             22.3,             8.5],
    "Croissance (%)":       [18.2,               4.1,              22.5,           -2.3,             2.8,              6.1],
    "CA (k€)":              [5400,               3450,             1590,           2670,             4220,             1610],
    "Catégorie":            ["Vedette ⭐",        "Vache à lait 🐄","Dilemme ❓",   "Poids mort 💀",  "Vache à lait 🐄","Poids mort 💀"],
}
df_bcg = pd.DataFrame(bcg_products)

# ─────────────────────────────────────────────
#  COULEURS
# ─────────────────────────────────────────────
COLOR_MAIN   = "#607D8B"
COLOR_LIGHT  = "#90A4AE"
COLOR_DARK   = "#37474F"
COLOR_ACCENT = "#81C784"
COLOR_WARN   = "#CE93D8"
COLOR_NEG    = "#EF9A9A"

BCG_COLORS = {
    "Vedette ⭐":        "#607D8B",
    "Vache à lait 🐄":  "#81C784",
    "Dilemme ❓":        "#FFD54F",
    "Poids mort 💀":    "#EF9A9A",
}

# ─────────────────────────────────────────────
#  SECTION 1 — VOLUME PAR PAYS
# ─────────────────────────────────────────────
st.markdown('<a class="section-anchor" id="volume"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
""", unsafe_allow_html=True)
st.markdown('<p class="section-title">📦 Volume des Ventes par Pays</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Cumulé 2019–2025 · Unités vendues (milliers)</p>', unsafe_allow_html=True)

df_pays_sorted = df_pays.sort_values("Volume (k unités)", ascending=True)

fig_pays = go.Figure()
fig_pays.add_trace(go.Bar(
    x=df_pays_sorted["Volume (k unités)"],
    y=df_pays_sorted["Pays"],
    orientation='h',
    marker=dict(
        color=[COLOR_LIGHT, COLOR_MAIN, COLOR_DARK],
        line=dict(width=0),
    ),
    text=[f"{v:,} k" for v in df_pays_sorted["Volume (k unités)"]],
    textposition='outside',
    textfont=dict(family="Comfortaa, sans-serif", size=13, color=COLOR_DARK),
    hovertemplate='<b>%{y}</b><br>Volume : %{x:,} k unités<extra></extra>',
))

fig_pays.update_layout(
    template="plotly_white",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Comfortaa, sans-serif", color=COLOR_DARK),
    margin=dict(l=10, r=80, t=20, b=20),
    height=240,
    showlegend=False,
    xaxis=dict(
        visible=False,
        showgrid=False,
        range=[0, 6200],
    ),
    yaxis=dict(
        tickfont=dict(family="Comfortaa, sans-serif", size=13, color=COLOR_DARK),
        showgrid=False,
        zeroline=False,
    ),
)

st.plotly_chart(fig_pays, use_container_width=True, config={"displayModeBar": False})
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SECTION 2 — IMPACT COVID-19
# ─────────────────────────────────────────────
st.markdown('<a class="section-anchor" id="covid"></a>', unsafe_allow_html=True)
st.markdown('<p class="section-title">🦠 Impact COVID-19 sur le Chiffre d\'Affaires</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Vague 17 mars – 11 mai 2020 vs même période 2019</p>', unsafe_allow_html=True)

arrow = "▼" if covid_pct < 0 else "▲"
col_kpi1, col_kpi2, col_kpi3 = st.columns([1, 2, 1])
with col_kpi2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Variation du CA — Période de Confinement</div>
        <div class="kpi-value"><span class="kpi-arrow">{arrow}</span>{abs(covid_pct):.1f}%</div>
        <div class="kpi-desc">
            CA période 2019 : <strong>{ca_covid_2019:,.0f} k€</strong><br>
            CA période 2020 : <strong>{ca_covid_2020:,.0f} k€</strong><br>
            Écart absolu : <strong>{ca_covid_2020 - ca_covid_2019:,.0f} k€</strong>
        </div>
        <div class="kpi-badge">🔒 Fermeture points de vente · Baisses commandes B2B</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SECTION 3 — SAISONNALITÉ
# ─────────────────────────────────────────────
st.markdown('<a class="section-anchor" id="saisonnalite"></a>', unsafe_allow_html=True)
st.markdown("""<div class="card">""", unsafe_allow_html=True)
st.markdown('<p class="section-title">📈 Saisonnalité des Ventes</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Tendances mensuelles 2019–2025 · Indice CA (base 100)</p>', unsafe_allow_html=True)

col_f, col_y = st.columns([3, 1])
with col_y:
    annees_dispo = list(range(2019, 2026))
    annees_sel = st.multiselect(
        "Années à afficher",
        annees_dispo,
        default=[2019, 2020, 2023, 2025],
        key="saison_filter",
    )

fig_saison = go.Figure()
palette_saison = ["#B0BEC5", "#EF9A9A", "#FFD54F", "#A5D6A7", "#80DEEA", "#607D8B", "#37474F"]
annees_all = list(range(2019, 2026))

for i, yr in enumerate(annees_sel if annees_sel else annees_all):
    idx = annees_all.index(yr)
    vals = seasons[yr]
    fig_saison.add_trace(go.Scatter(
        x=mois,
        y=vals,
        name=str(yr),
        mode="lines",
        line=dict(width=2.5 if yr in [2020, 2025] else 1.5, color=palette_saison[idx % len(palette_saison)]),
        fill="tozeroy" if yr == 2025 else "none",
        fillcolor="rgba(96,125,139,0.06)" if yr == 2025 else None,
        hovertemplate=f'<b>{yr}</b> · %{{x}}<br>Indice : %{{y:.1f}}<extra></extra>',
    ))

fig_saison.update_layout(
    template="plotly_white",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Comfortaa, sans-serif", color=COLOR_DARK),
    margin=dict(l=10, r=10, t=20, b=10),
    height=320,
    legend=dict(
        orientation="h", y=-0.18, x=0.5, xanchor="center",
        font=dict(family="Comfortaa, sans-serif", size=11),
        bgcolor="rgba(0,0,0,0)",
    ),
    xaxis=dict(
        showgrid=False,
        tickfont=dict(family="Comfortaa, sans-serif", size=11, color=COLOR_DARK),
        zeroline=False,
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="#ECEFF1",
        gridwidth=1,
        tickfont=dict(family="Comfortaa, sans-serif", size=11, color=COLOR_LIGHT),
        zeroline=False,
        title=dict(text="Indice de vente", font=dict(size=11)),
    ),
    hovermode="x unified",
)

st.plotly_chart(fig_saison, use_container_width=True, config={"displayModeBar": False})

# Insights saisonnalité
col_i1, col_i2, col_i3 = st.columns(3)
insights = [
    ("🎄 Pic de Décembre", "+48%", "Noël génère le pic annuel maximal. Anticipation des stocks recommandée dès octobre."),
    ("🦠 Creux COVID 2020", "−18%", "Vague de confinement. Impact visible mars–mai 2020 vs 2019."),
    ("☀️ Creux Estival", "−14%", "Juillet–Août marquent le point bas annuel. Opportunité promotionnelle."),
]
for col, (title, badge, desc) in zip([col_i1, col_i2, col_i3], insights):
    with col:
        st.markdown(f"""
        <div class="card-sm">
          <div style="font-size:0.9rem;font-weight:700;color:{COLOR_DARK};margin-bottom:0.3rem;">{title}
            <span style="font-size:0.78rem;background:#ECEFF1;border-radius:10px;padding:0.1rem 0.5rem;color:{COLOR_MAIN};margin-left:0.4rem;">{badge}</span>
          </div>
          <div style="font-size:0.78rem;color:{COLOR_LIGHT};line-height:1.5;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SECTION 4 — MATRICE BCG
# ─────────────────────────────────────────────
st.markdown('<a class="section-anchor" id="bcg"></a>', unsafe_allow_html=True)
st.markdown("""<div class="card">""", unsafe_allow_html=True)
st.markdown('<p class="section-title">🧭 Matrice BCG — Portefeuille Produits</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Taille de bulle = CA 2025 · Axes : Part de marché (X) / Croissance (Y)</p>', unsafe_allow_html=True)

fig_bcg = go.Figure()

# Quadrant de fond
quadrant_zones = [
    (10, 24, "rgba(96,125,139,0.05)", "⭐ Vedettes"),
    (0, 24, "rgba(129,199,132,0.06)", "❓ Dilemmes"),
    (10, 0, "rgba(129,199,132,0.06)", "🐄 Vaches à lait"),
    (0, 0, "rgba(239,154,154,0.07)", "💀 Poids morts"),
]

# Labels de quadrant
for x0, y0, color, label in quadrant_zones:
    xanchor_label = "right" if x0 == 10 else "left"
    xpos = 29 if x0 == 10 else 1
    ypos = 29 if y0 == 24 else -5
    fig_bcg.add_shape(
        type="rect",
        x0=x0, x1=30 if x0 == 10 else 10,
        y0=y0, y1=30 if y0 == 24 else 24,
        fillcolor=color, line=dict(width=0),
        layer="below",
    )
    fig_bcg.add_annotation(
        x=xpos, y=ypos,
        text=label,
        showarrow=False,
        font=dict(family="Comfortaa, sans-serif", size=11, color=COLOR_LIGHT),
        xanchor=xanchor_label, yanchor="bottom",
        opacity=0.8,
    )

# Lignes de séparation
fig_bcg.add_shape(type="line", x0=10, x1=10, y0=-6, y1=30,
                  line=dict(color="#CFD8DC", width=1.5, dash="dot"))
fig_bcg.add_shape(type="line", x0=0, x1=30, y0=12, y1=12,
                  line=dict(color="#CFD8DC", width=1.5, dash="dot"))

# Annotation axes
fig_bcg.add_annotation(x=15, y=-7.5, text="Part de marché relative →",
                        showarrow=False, font=dict(family="Comfortaa, sans-serif", size=10, color=COLOR_LIGHT))
fig_bcg.add_annotation(x=-2.5, y=22, text="Croissance ↑",
                        showarrow=False, font=dict(family="Comfortaa, sans-serif", size=10, color=COLOR_LIGHT),
                        textangle=-90)

for _, row in df_bcg.iterrows():
    cat = row["Catégorie"]
    color = BCG_COLORS.get(cat, COLOR_MAIN)
    fig_bcg.add_trace(go.Scatter(
        x=[row["Part de marché (%)"]],
        y=[row["Croissance (%)"]],
        mode="markers+text",
        name=cat,
        marker=dict(
            size=row["CA (k€)"] / 120,
            color=color,
            opacity=0.80,
            line=dict(width=2, color="white"),
        ),
        text=[row["Produit"]],
        textposition="top center",
        textfont=dict(family="Comfortaa, sans-serif", size=11, color=COLOR_DARK),
        hovertemplate=(
            f"<b>{row['Produit']}</b><br>"
            f"Catégorie : {cat}<br>"
            f"Part de marché : {row['Part de marché (%)']:.1f}%<br>"
            f"Croissance : {row['Croissance (%)']:+.1f}%<br>"
            f"CA : {row['CA (k€)']:,} k€<extra></extra>"
        ),
        showlegend=False,
    ))

fig_bcg.update_layout(
    template="plotly_white",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Comfortaa, sans-serif", color=COLOR_DARK),
    margin=dict(l=40, r=20, t=20, b=50),
    height=460,
    xaxis=dict(
        range=[0, 32], showgrid=False, zeroline=False,
        tickfont=dict(family="Comfortaa, sans-serif", size=10, color=COLOR_LIGHT),
        title=dict(text="Part de marché relative (%)", font=dict(size=11)),
    ),
    yaxis=dict(
        range=[-8, 30], showgrid=False, zeroline=False,
        tickfont=dict(family="Comfortaa, sans-serif", size=10, color=COLOR_LIGHT),
        title=dict(text="Taux de croissance (%)", font=dict(size=11)),
    ),
    hovermode="closest",
)

st.plotly_chart(fig_bcg, use_container_width=True, config={"displayModeBar": False})

# Légende BCG
st.markdown("""
<div class="bcg-legend">
  <span class="bcg-badge"><span style="width:10px;height:10px;border-radius:50%;background:#607D8B;display:inline-block;"></span>⭐ Vedette — Forte croissance & forte part</span>
  <span class="bcg-badge"><span style="width:10px;height:10px;border-radius:50%;background:#81C784;display:inline-block;"></span>🐄 Vache à lait — Faible croissance & forte part</span>
  <span class="bcg-badge"><span style="width:10px;height:10px;border-radius:50%;background:#FFD54F;display:inline-block;"></span>❓ Dilemme — Forte croissance & faible part</span>
  <span class="bcg-badge"><span style="width:10px;height:10px;border-radius:50%;background:#EF9A9A;display:inline-block;"></span>💀 Poids mort — Faible croissance & faible part</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SECTION 5 — RECOMMANDATIONS STRATÉGIQUES
# ─────────────────────────────────────────────
st.markdown('<a class="section-anchor" id="strategy"></a>', unsafe_allow_html=True)
st.markdown('<p class="section-title">🚀 Recommandations Stratégiques</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Segmentation clients · Campagne HOOKSTRIKE™ · Social Media</p>', unsafe_allow_html=True)

# --- Segments clients
st.markdown("""
<div style="font-size:0.78rem;letter-spacing:0.1em;text-transform:uppercase;color:#90A4AE;font-weight:600;margin-bottom:1rem;">
  Segments Clients Prioritaires
</div>
""", unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)
with col_s1:
    st.markdown("""
    <div class="segment-card">
      <div class="segment-icon">💼</div>
      <div class="segment-name">Jeunes Professionnels Urbains</div>
      <div class="segment-desc">
        25–38 ans · CSP+ · Villes moyennes et grandes métropoles<br><br>
        Sensibles au <strong>premium et à l'authenticité</strong>.
        Consomment lors de pauses bureau, déplacements et moments "self-care".
        Très actifs sur Instagram & LinkedIn. Budget moyen/acheté : 18–32€.
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
    <div class="segment-card">
      <div class="segment-icon">👨‍👩‍👧</div>
      <div class="segment-name">Familles Soucieuses de la Qualité</div>
      <div class="segment-desc">
        30–50 ans · Parents · Zones périurbaines et rurales<br><br>
        Recherchent des produits <strong>sains, traçables et gourmands</strong>.
        Achats en format familial, moments de partage.
        Très influencés par les avis et contenus éducatifs.
        Budget moyen/acheté : 22–45€.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- HOOKSTRIKE Posts
st.markdown("""
<div style="font-size:0.78rem;letter-spacing:0.1em;text-transform:uppercase;color:#90A4AE;font-weight:600;margin:1.5rem 0 1rem 0;">
  Campagne HOOKSTRIKE™ · Produit Vedette : Chocolate Bliss 🌟
</div>
""", unsafe_allow_html=True)

posts = [
    {
        "platform": "Instagram · Segment : Jeunes Professionnels",
        "hook": "⚡ Et si votre pause café méritait enfin d'être mémorable ?",
        "strike": (
            "Chocolate Bliss n'est pas juste un cookie. C'est le moment où vous décidez "
            "que votre journée mérite le meilleur. Cacao Grand Cru, texture fondante, zéro compromis. "
            "Parce que vous avez travaillé dur — offrez-vous la qualité qui va avec."
        ),
        "tags": "#ChocolateBliss #TheCookieCompany #PauseCafé #PremiumTaste #SlowLife",
    },
    {
        "platform": "LinkedIn · Segment : Décideurs & Gifting B2B",
        "hook": "🍫 Ce que vous offrez dit tout de ce que vous valorisez.",
        "strike": (
            "The Cookie Company réinvente le cadeau d'entreprise. Notre Chocolate Bliss — "
            "sélectionné parmi les 3% de cacao d'excellence mondiale — transforme chaque boîte en expérience. "
            "Fidélité client, onboarding équipe, événements : contactez-nous pour un devis personnalisé."
        ),
        "tags": "#CadeauEntreprise #QualityMatters #TheCookieCompany #B2BGifting #Artisan",
    },
    {
        "platform": "Instagram Stories · Segment : Familles & Partage",
        "hook": "🏠 Le dimanche soir, tout le monde veut la même chose.",
        "strike": (
            "On a tous un souvenir de cookie chaud sorti du four. Chocolate Bliss le ramène — "
            "sans le four, sans l'attente. Juste la douceur, juste le partage. "
            "Format famille disponible : 12 cookies, une boîte, des sourires garantis. "
            "Livraison en 24h. Le dimanche soir, ne compromettez plus."
        ),
        "tags": "#FamilyMoments #ChocolateBliss #WeekendTreat #TheCookieCompany #GourmandSain",
    },
]

for post in posts:
    st.markdown(f"""
    <div class="post-card">
      <div class="post-platform">{post['platform']}</div>
      <div class="post-hook">[HOOK] {post['hook']}</div>
      <div class="post-strike">[STRIKE] {post['strike']}</div>
      <div class="post-tags">{post['tags']}</div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
  🍪 The Cookie Company · Dashboard Stratégique · Données simulées 2019–2025<br>
  Conçu avec Streamlit & Plotly · Toute reproduction interdite sans autorisation
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
#
#  🚀 GUIDE DE DÉPLOIEMENT — STREAMLIT COMMUNITY CLOUD
#  (Partage du dashboard via un lien public gratuit)
#
# ══════════════════════════════════════════════════════════════════════
#
#  ÉTAPE 1 — CRÉER UN COMPTE GITHUB GRATUIT
#  ─────────────────────────────────────────
#  1. Rendez-vous sur https://github.com
#  2. Cliquez sur "Sign up" (en haut à droite)
#  3. Choisissez un nom d'utilisateur, entrez votre email, créez un mot de passe
#  4. Vérifiez votre email via le lien reçu
#  5. Choisissez le plan gratuit ("Free") — aucune carte bancaire requise
#
#
#  ÉTAPE 2 — CRÉER UN REPOSITORY ET DÉPOSER app.py
#  ─────────────────────────────────────────────────
#  1. Une fois connecté à GitHub, cliquez sur le "+" en haut à droite
#     → Sélectionnez "New repository"
#  2. Donnez-lui un nom (ex: cookie-dashboard)
#  3. Laissez le repository en "Public"
#  4. Cochez "Add a README file"
#  5. Cliquez sur "Create repository"
#  6. Dans votre nouveau repository, cliquez sur "Add file" → "Upload files"
#  7. Glissez-déposez votre fichier app.py
#  8. Cliquez sur "Commit changes" (bouton vert)
#
#  ⚠️  IMPORTANT : Créez également un fichier requirements.txt
#      (cliquez "Add file" → "Create new file", nommez-le requirements.txt)
#      avec ce contenu :
#
#      streamlit>=1.32.0
#      plotly>=5.18.0
#      pandas>=2.0.0
#      numpy>=1.24.0
#
#
#  ÉTAPE 3 — DÉPLOYER SUR STREAMLIT COMMUNITY CLOUD
#  ──────────────────────────────────────────────────
#  1. Rendez-vous sur https://share.streamlit.io
#  2. Cliquez sur "Sign in with GitHub" et autorisez l'accès
#  3. Cliquez sur "New app" (bouton bleu)
#  4. Sélectionnez :
#       - Repository : votre-nom/cookie-dashboard
#       - Branch     : main
#       - Main file  : app.py
#  5. Dans "App URL", personnalisez l'adresse (ex: the-cookie-co)
#     → Votre lien sera : https://the-cookie-co.streamlit.app
#  6. Cliquez sur "Deploy!" et attendez ~2 minutes
#  7. 🎉 Votre dashboard est en ligne ! Copiez le lien et partagez-le.
#
#  💡 CONSEILS :
#  - Chaque modification du fichier app.py sur GitHub se reflète
#    automatiquement sur votre app en quelques secondes.
#  - Streamlit Community Cloud est 100% gratuit pour les projets publics.
#  - En cas d'erreur au déploiement, consultez les logs dans l'interface
#    Streamlit Cloud (icône "Manage app" en bas à droite de votre app).
#
# ══════════════════════════════════════════════════════════════════════
