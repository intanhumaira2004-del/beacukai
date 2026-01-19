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
    box-shadow: 0 12px 35px rgba(0,0,0,0.25);
}

.hero-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    margin-bottom: 8px;
}

.hero-subtitle {
    text-align: center;
    font-size: 22px;
    opacity: 0.95;
    margin-bottom: 30px;
}

.hero-desc {
    text-align: center;
    max-width: 1000px;
    margin: auto;
    font-size: 17px;
    line-height: 1.9;
    margin-bottom: 45px;
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
    padding: 24px 22px;
    text-align: center;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.15);
}

.info-icon {
    font-size: 38px;
    margin-bottom: 10px;
}

.info-title {
    font-weight: 800;
    font-size: 17px;
    margin-bottom: 8px;
}

.info-text {
    font-size: 14.5px;
    line-height: 1.6;
}

.flow-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 18px;
    text-align: center;
}

.flow-step {
    background: rgba(255,255,255,0.2);
    padding: 18px;
    border-radius: 18px;
    font-weight: 700;
    font-size: 15px;
}

.highlight-box {
    background: rgba(255,255,255,0.18);
    border-radius: 22px;
    padding: 25px;
    line-height: 1.8;
    font-size: 15px;
}

.footer {
    margin-top: 55px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.35);
    text-align: center;
    font-size: 14px;
    opacity: 0.9;
}
</style>

<div class="wrapper">

<div class="hero-title">🛃 Bea Cukai in Action</div>
<div class="hero-subtitle">Infographic Dashboard — DJBC Aceh</div>

<div class="hero-desc">
Dashboard ini menyajikan visualisasi infografis mengenai peran strategis
Direktorat Jenderal Bea dan Cukai (DJBC) Wilayah Aceh dalam mengawasi lalu lintas
barang, memungut penerimaan negara, serta melindungi masyarakat dan industri nasional.
</div>

<div class="section-title">🏛️ Empat Pilar Peran Bea Cukai</div>
<div class="infographic-grid">

    <div class="info-box">
        <div class="info-icon">💰</div>
        <div class="info-title">Revenue Collector</div>
        <div class="info-text">
            Menghimpun penerimaan negara dari bea masuk, bea keluar,
            dan cukai sebagai sumber pembiayaan pembangunan nasional.
        </div>
    </div>

    <div class="info-box">
        <div class="info-icon">🛡️</div>
        <div class="info-title">Community Protector</div>
        <div class="info-text">
            Melindungi masyarakat dari peredaran narkotika,
            barang berbahaya, dan praktik penyelundupan ilegal.
        </div>
    </div>

    <div class="info-box">
        <div class="info-icon">🚢</div>
        <div class="info-title">Trade Facilitator</div>
        <div class="info-text">
            Memfasilitasi arus ekspor dan impor melalui pelayanan
            kepabeanan yang cepat, transparan, dan akuntabel.
        </div>
    </div>

    <div class="info-box">
        <div class="info-icon">🏭</div>
        <div class="info-title">Industrial Assistance</div>
        <div class="info-text">
            Mendukung pertumbuhan industri nasional melalui fasilitas
            fiskal dan kawasan berikat untuk meningkatkan daya saing.
        </div>
    </div>

</div>

<div class="section-title">🔄 Alur Proses Kepabeanan</div>
<div class="flow-container">
    <div class="flow-step">📄 Pemberitahuan Pabean</div>
    <div class="flow-step">📦 Pemeriksaan Dokumen</div>
    <div class="flow-step">🔍 Pemeriksaan Fisik</div>
    <div class="flow-step">💰 Pembayaran Bea & Cukai</div>
    <div class="flow-step">🚚 Pengeluaran Barang</div>
</div>

<div class="section-title">⚙️ Tugas Pokok DJBC</div>
<div class="highlight-box">
✔️ Mengawasi lalu lintas barang di wilayah pabean<br>
✔️ Memungut bea masuk, bea keluar, dan cukai<br>
✔️ Melaksanakan penegakan hukum kepabeanan dan cukai<br>
✔️ Memberikan pelayanan serta fasilitas kepabeanan<br>
✔️ Mendukung kebijakan fiskal dan perdagangan nasional
</div>

<div class="footer">
© 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
<br>Dashboard Infografis Kepabeanan
</div>

</div>
""", unsafe_allow_html=True)
