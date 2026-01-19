import streamlit as st

st.set_page_config(
    page_title="Bea Cukai in Action | DJBC Aceh",
    page_icon="🛃",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #eef3f9;
}
.wrapper {
    background: linear-gradient(135deg, #003a8f, #005bac);
    padding: 50px 40px;
    border-radius: 28px;
    color: white;
}
.section-title {
    font-size: 26px;
    font-weight: 800;
    margin: 40px 0 20px;
    border-left: 7px solid #f9b233;
    padding-left: 15px;
}
.infographic-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 22px;
}
.info-box {
    background: rgba(255,255,255,0.18);
    border-radius: 22px;
    padding: 24px;
    text-align: center;
}
.info-icon {
    font-size: 38px;
}
.info-title {
    font-weight: 800;
    margin: 10px 0;
}
.highlight-box {
    background: rgba(255,255,255,0.18);
    border-radius: 22px;
    padding: 22px;
    font-size: 15.5px;
    line-height: 1.8;
}
.footer {
    margin-top: 50px;
    border-top: 1px solid rgba(255,255,255,0.3);
    padding-top: 20px;
    text-align: center;
    font-size: 14px;
}
</style>

<div class="wrapper">

<h1 style="text-align:center;">🛃 Bea Cukai in Action</h1>
<h3 style="text-align:center;">Infographic Dashboard — DJBC Aceh</h3>

<div class="highlight-box" style="margin-top:30px;">
<b>📌 Kepabeanan adalah</b> seluruh kegiatan yang berkaitan dengan pengawasan
atas lalu lintas barang yang masuk atau keluar daerah pabean serta pemungutan
bea masuk dan bea keluar sesuai dengan ketentuan peraturan perundang-undangan
yang berlaku.
</div>

<p style="text-align:center; max-width:900px; margin:30px auto;">
Dashboard ini menyajikan visualisasi infografis mengenai peran strategis
Direktorat Jenderal Bea dan Cukai (DJBC) Wilayah Aceh dalam mengawasi lalu lintas
barang, memungut penerimaan negara, serta melindungi masyarakat dan industri nasional.
</p>

<div class="section-title">🏛️ Empat Pilar Peran Bea Cukai</div>

<div class="infographic-grid">

<div class="info-box">
<div class="info-icon">💰</div>
<div class="info-title">Revenue Collector</div>
<p>Menghimpun penerimaan negara dari bea masuk, bea keluar, dan cukai.</p>
</div>

<div class="info-box">
<div class="info-icon">🛡️</div>
<div class="info-title">Community Protector</div>
<p>Melindungi masyarakat dari penyelundupan dan barang berbahaya.</p>
</div>

<div class="info-box">
<div class="info-icon">🚢</div>
<div class="info-title">Trade Facilitator</div>
<p>Memfasilitasi arus ekspor dan impor secara cepat dan transparan.</p>
</div>

<div class="info-box">
<div class="info-icon">🏭</div>
<div class="info-title">Industrial Assistance</div>
<p>Mendukung industri nasional melalui fasilitas fiskal.</p>
</div>

</div>

<div class="footer">
© 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
<br>Dashboard Edukasi Kepabeanan
</div>

</div>
""", unsafe_allow_html=True)
