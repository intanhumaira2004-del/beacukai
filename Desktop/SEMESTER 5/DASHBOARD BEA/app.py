import streamlit as st

st.set_page_config(
    page_title="Customs in Action | DJBC Aceh",
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
    padding: 55px 45px;
    border-radius: 30px;
    color: white;
    box-shadow: 0 14px 40px rgba(0,0,0,0.25);
}

.hero-title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    margin-bottom: 5px;
}

.hero-subtitle {
    text-align: center;
    font-size: 22px;
    opacity: 0.95;
    margin-bottom: 25px;
}

.hero-tagline {
    text-align: center;
    font-size: 16px;
    max-width: 1000px;
    margin: auto;
    line-height: 1.9;
    margin-bottom: 35px;
}

.badge-row {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 35px;
}

.badge {
    background: rgba(255,255,255,0.2);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

.section-title {
    font-size: 28px;
    font-weight: 900;
    margin: 45px 0 25px;
    border-left: 8px solid #f9b233;
    padding-left: 16px;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
}

.info-card {
    background: rgba(255,255,255,0.18);
    border-radius: 24px;
    padding: 26px 24px;
    text-align: center;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.15);
}

.info-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

.info-title {
    font-weight: 900;
    font-size: 17px;
    margin-bottom: 8px;
}

.info-text {
    font-size: 14.5px;
    line-height: 1.7;
}

.highlight-box {
    background: rgba(255,255,255,0.2);
    border-radius: 26px;
    padding: 28px;
    line-height: 1.85;
    font-size: 15.5px;
}

.timeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 18px;
    margin-top: 10px;
}

.timeline-step {
    background: rgba(255,255,255,0.22);
    padding: 18px;
    border-radius: 20px;
    text-align: center;
    font-weight: 700;
    font-size: 14.5px;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 22px;
}

.stat-box {
    background: rgba(255,255,255,0.22);
    border-radius: 22px;
    padding: 22px;
    text-align: center;
}

.stat-number {
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 6px;
}

.stat-label {
    font-size: 13px;
    opacity: 0.95;
}

.footer {
    margin-top: 65px;
    padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,0.35);
    text-align: center;
    font-size: 14px;
    opacity: 0.9;
}
</style>

<div class="wrapper">

<div class="hero-title">🛃 Customs in Action</div>
<div class="hero-subtitle">Menjaga Perbatasan, Menggerakkan Ekonomi</div>

<div class="hero-tagline">
Infographic dashboard ini menyajikan gambaran komprehensif mengenai peran strategis
Direktorat Jenderal Bea dan Cukai (DJBC) Wilayah Aceh dalam menjaga kedaulatan ekonomi,
memfasilitasi perdagangan, serta melindungi masyarakat dari peredaran barang ilegal
dan berbahaya.
</div>

<div class="badge-row">
    <div class="badge">📦 Kepabeanan</div>
    <div class="badge">🏷️ Cukai</div>
    <div class="badge">🛡️ Pengawasan</div>
    <div class="badge">🚢 Ekspor–Impor</div>
    <div class="badge">💰 Penerimaan Negara</div>
    <div class="badge">🏭 Fasilitas Fiskal</div>
</div>

<div class="section-title">📘 Apa Itu Kepabeanan & Cukai?</div>

<div class="highlight-box">
<b>🔹 Kepabeanan adalah</b> seluruh kegiatan yang berkaitan dengan pengawasan atas lalu lintas
barang yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar
sesuai dengan ketentuan peraturan perundang-undangan yang berlaku.
<br><br>
<b>🔹 Cukai adalah</b> pungutan negara yang dikenakan terhadap barang tertentu yang mempunyai
sifat atau karakteristik tertentu, seperti hasil tembakau, minuman mengandung etil alkohol,
dan produk lain yang pengendaliannya perlu dilakukan oleh negara.
</div>

<div class="section-title">🏛️ Empat Pilar Strategis Bea Cukai</div>

<div class="info-grid">

<div class="info-card">
<div class="info-icon">💰</div>
<div class="info-title">Revenue Collector</div>
<div class="info-text">
Menghimpun penerimaan negara dari bea masuk, bea keluar, dan cukai sebagai sumber
pembiayaan pembangunan nasional.
</div>
</div>

<div class="info-card">
<div class="info-icon">🛡️</div>
<div class="info-title">Community Protector</div>
<div class="info-text">
Melindungi masyarakat dari peredaran narkotika, barang berbahaya, senjata ilegal,
serta praktik penyelundupan lintas batas.
</div>
</div>

<div class="info-card">
<div class="info-icon">🚢</div>
<div class="info-title">Trade Facilitator</div>
<div class="info-text">
Memfasilitasi arus ekspor dan impor melalui pelayanan kepabeanan yang cepat,
transparan, berbasis teknologi, dan berorientasi pada kemudahan berusaha.
</div>
</div>

<div class="info-card">
<div class="info-icon">🏭</div>
<div class="info-title">Industrial Assistance</div>
<div class="info-text">
Mendukung pertumbuhan industri nasional melalui fasilitas fiskal seperti kawasan
berikat, KITE, dan insentif kepabeanan lainnya.
</div>
</div>

</div>

<div class="section-title">🔄 Alur Proses Kepabeanan (Impor & Ekspor)</div>

<div class="timeline">
    <div class="timeline-step">📄 Penyampaian Dokumen Pabean</div>
    <div class="timeline-step">🔎 Analisis Risiko & Pemeriksaan</div>
    <div class="timeline-step">📦 Pemeriksaan Fisik Barang</div>
    <div class="timeline-step">💰 Pembayaran Bea & Cukai</div>
    <div class="timeline-step">🚚 Persetujuan & Pengeluaran Barang</div>
</div>

<div class="section-title">⚙️ Tugas Pokok dan Fungsi DJBC</div>

<div class="info-grid">

<div class="info-card">
<div class="info-icon">📊</div>
<div class="info-title">Pengawasan Perbatasan</div>
<div class="info-text">
Mengawasi lalu lintas barang di pelabuhan laut, bandara, dan perbatasan untuk
mencegah masuknya barang ilegal dan berbahaya.
</div>
</div>

<div class="info-card">
<div class="info-icon">⚖️</div>
<div class="info-title">Penegakan Hukum</div>
<div class="info-text">
Melakukan penindakan, penyidikan, dan penegakan hukum terhadap pelanggaran
di bidang kepabeanan dan cukai.
</div>
</div>

<div class="info-card">
<div class="info-icon">🤝</div>
<div class="info-title">Pelayanan Publik</div>
<div class="info-text">
Memberikan pelayanan prima kepada pengguna jasa kepabeanan melalui sistem
digital dan pendekatan berbasis risiko.
</div>
</div>

<div class="info-card">
<div class="info-icon">🏢</div>
<div class="info-title">Fasilitasi Industri</div>
<div class="info-text">
Memberikan fasilitas fiskal untuk meningkatkan daya saing industri nasional,
ekspor, dan investasi.
</div>
</div>

</div>

<div class="section-title">🌏 Peran Strategis DJBC Wilayah Aceh</div>

<div class="highlight-box">
Wilayah Aceh memiliki posisi strategis sebagai pintu gerbang perdagangan di wilayah
barat Indonesia. DJBC Aceh berperan penting dalam menjaga keamanan perbatasan laut,
mengawasi arus barang lintas negara, mendorong ekspor komoditas unggulan daerah,
serta melindungi masyarakat dari peredaran narkotika dan barang ilegal.
</div>

<div class="section-title">🎯 Dampak Positif Kehadiran Bea Cukai</div>

<div class="stat-grid">
    <div class="stat-box">
        <div class="stat-number">💰</div>
        <div class="stat-label">Peningkatan penerimaan negara</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">🛡️</div>
        <div class="stat-label">Perlindungan masyarakat & generasi muda</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">🚢</div>
        <div class="stat-label">Kelancaran arus perdagangan nasional</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">🏭</div>
        <div class="stat-label">Pertumbuhan industri & UMKM ekspor</div>
    </div>
</div>

<div class="footer">
© 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
<br>Customs in Action | Infographic Education Dashboard
</div>

</div>
""", unsafe_allow_html=True)
