import streamlit as st

st.set_page_config(page_title="DJBC Aceh | Customs in Action", page_icon="🛃", layout="wide")

# ===================== STYLE =====================
st.markdown("""
<style>
body { background: #f4f7fb; }

.hero {
    background: linear-gradient(135deg, #002d72, #005bac);
    padding: 60px 40px;
    border-radius: 28px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
}

.hero-title { font-size: 52px; font-weight: 900; }
.hero-subtitle { font-size: 20px; margin-top: 8px; opacity: 0.95; }
.hero-desc { max-width: 800px; margin: 20px auto 0; font-size: 16px; line-height: 1.8; }

.section-title {
    font-size: 30px;
    font-weight: 900;
    color: #002d72;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 24px 22px;
    border-radius: 20px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
    border-top: 6px solid #005bac;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 38px rgba(0,0,0,0.12);
}

.card-icon { font-size: 38px; margin-bottom: 10px; }
.card-title { font-weight: 800; font-size: 17px; margin-bottom: 6px; }
.card-text { font-size: 14.5px; line-height: 1.7; color: #444; }

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 24px;
}

.highlight {
    background: #eef4ff;
    padding: 26px;
    border-radius: 20px;
    font-size: 15.5px;
    line-height: 1.9;
    margin-bottom: 30px;
}

.timeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
}

.timeline-step {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    font-weight: 700;
    box-shadow: 0 10px 24px rgba(0,0,0,0.08);
    border-bottom: 5px solid #005bac;
}

.stat {
    background: linear-gradient(135deg, #002d72, #005bac);
    color: white;
    padding: 26px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 14px 32px rgba(0,0,0,0.22);
}

.stat-icon { font-size: 34px; margin-bottom: 6px; }
.stat-label { font-size: 14px; opacity: 0.95; }

.footer {
    text-align: center;
    font-size: 13px;
    color: gray;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
st.sidebar.title("🛃 DJBC Aceh")
menu = st.sidebar.radio(
    "Navigasi",
    [
        "🏠 Beranda",
        "📘 Kepabeanan & Cukai",
        "🏛️ Pilar Bea Cukai",
        "🔄 Alur Impor–Ekspor",
        "⚙️ Tugas & Fungsi",
        "🌏 DJBC Aceh",
        "🎯 Dampak",
        "ℹ️ Tentang"
    ]
)

# ===================== BERANDA =====================
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="hero">
        <div class="hero-title">🛃 Customs in Action</div>
        <div class="hero-subtitle">DJBC Wilayah Aceh</div>
        <div class="hero-desc">
        Infografis ini yang menyajikan peran strategis Bea dan Cukai
        dalam menjaga perbatasan, mengamankan penerimaan negara, memfasilitasi perdagangan,
        serta melindungi masyarakat dari peredaran barang ilegal dan berbahaya.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎯 Tujuan Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="card"><div class="card-icon">📘</div><div class="card-title">Edukasi Publik</div><div class="card-text">Memberikan pemahaman kepabeanan dan cukai kepada masyarakat.</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card"><div class="card-icon">🛡️</div><div class="card-title">Proteksi Negara</div><div class="card-text">Mencegah masuknya barang ilegal dan berbahaya lintas negara.</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card"><div class="card-icon">🚢</div><div class="card-title">Fasilitasi Perdagangan</div><div class="card-text">Mempercepat arus ekspor–impor untuk pertumbuhan ekonomi.</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="card"><div class="card-icon">🏭</div><div class="card-title">Dukungan Industri</div><div class="card-text">Memberikan fasilitas fiskal bagi industri dan UMKM.</div></div>""", unsafe_allow_html=True)

# ===================== KEPA BEANAN =====================
elif menu == "📘 Kepabeanan & Cukai":
    st.markdown("## 📘 Kepabeanan & Cukai")

    st.markdown("""
    <div class="highlight">
    <b>🔹 Kepabeanan adalah</b> seluruh kegiatan yang berkaitan dengan pengawasan atas lalu lintas
    barang yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar
    sesuai dengan ketentuan peraturan perundang-undangan yang berlaku.
    <br><br>
    <b>🔹 Cukai adalah</b> pungutan negara yang dikenakan terhadap barang tertentu yang memiliki
    sifat atau karakteristik tertentu, seperti hasil tembakau dan minuman beralkohol.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="card"><div class="card-icon">💰</div><div class="card-title">Bea Masuk</div><div class="card-text">Pungutan negara atas barang impor.</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card"><div class="card-icon">📤</div><div class="card-title">Bea Keluar</div><div class="card-text">Pungutan atas ekspor barang tertentu.</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card"><div class="card-icon">⚖️</div><div class="card-title">Pengawasan</div><div class="card-text">Kontrol lalu lintas barang lintas negara.</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="card"><div class="card-icon">📑</div><div class="card-title">Kewajiban Pabean</div><div class="card-text">Pelaporan dan pembayaran kewajiban.</div></div>""", unsafe_allow_html=True)

# ===================== PILAR =====================
elif menu == "🏛️ Pilar Bea Cukai":
    st.markdown("## 🏛️ Empat Pilar Bea Cukai")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="card"><div class="card-icon">💰</div><div class="card-title">Revenue Collector</div><div class="card-text">Menghimpun penerimaan negara.</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card"><div class="card-icon">🛡️</div><div class="card-title">Community Protector</div><div class="card-text">Melindungi masyarakat dari barang ilegal.</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card"><div class="card-icon">🚢</div><div class="card-title">Trade Facilitator</div><div class="card-text">Memfasilitasi ekspor–impor.</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="card"><div class="card-icon">🏭</div><div class="card-title">Industrial Assistance</div><div class="card-text">Mendukung industri nasional.</div></div>""", unsafe_allow_html=True)

# ===================== ALUR =====================
elif menu == "🔄 Alur Impor–Ekspor":
    st.markdown("## 🔄 Alur Proses Kepabeanan")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""<div class="timeline-step">📄 Dokumen Pabean</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="timeline-step">🔎 Analisis Risiko</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="timeline-step">📦 Pemeriksaan</div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="timeline-step">💰 Pembayaran</div>""", unsafe_allow_html=True)
    with col5:
        st.markdown("""<div class="timeline-step">🚚 Pengeluaran</div>""", unsafe_allow_html=True)

# ===================== TUGAS =====================
elif menu == "⚙️ Tugas & Fungsi":
    st.markdown("## ⚙️ Tugas Pokok dan Fungsi DJBC")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="card"><div class="card-icon">📊</div><div class="card-title">Pengawasan</div><div class="card-text">Mengawasi lalu lintas barang lintas negara.</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card"><div class="card-icon">⚖️</div><div class="card-title">Penegakan Hukum</div><div class="card-text">Menindak pelanggaran kepabeanan.</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card"><div class="card-icon">🤝</div><div class="card-title">Pelayanan Publik</div><div class="card-text">Memberikan pelayanan prima.</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="card"><div class="card-icon">🏢</div><div class="card-title">Fasilitasi Industri</div><div class="card-text">Mendukung industri nasional.</div></div>""", unsafe_allow_html=True)

# ===================== DJBC ACEH =====================
elif menu == "🌏 DJBC Aceh":
    st.markdown("## 🌏 Peran Strategis DJBC Wilayah Aceh")

    st.markdown("""
    <div class="highlight">
    Aceh merupakan wilayah strategis di jalur perdagangan barat Indonesia. DJBC Aceh berperan dalam
    menjaga keamanan perbatasan laut, mengawasi arus barang lintas negara, mendorong ekspor komoditas
    unggulan daerah, serta melindungi masyarakat dari peredaran narkotika dan barang ilegal.
    </div>
    """, unsafe_allow_html=True)

# ===================== DAMPAK =====================
elif menu == "🎯 Dampak":
    st.markdown("## 🎯 Dampak Positif Kehadiran Bea Cukai")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<div class="stat"><div class="stat-icon">💰</div><div class="stat-label">Penerimaan Negara</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="stat"><div class="stat-icon">🛡️</div><div class="stat-label">Perlindungan Masyarakat</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="stat"><div class="stat-icon">🚢</div><div class="stat-label">Kelancaran Perdagangan</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<div class="stat"><div class="stat-icon">🏭</div><div class="stat-label">Pertumbuhan Industri</div></div>""", unsafe_allow_html=True)

# ===================== TENTANG =====================
elif menu == "ℹ️ Tentang":
    st.markdown("## ℹ️ Tentang Dashboard")

    st.markdown("""
    <div class="highlight">
    Dashboard ini dikembangkan sebagai media edukasi kepabeanan berbasis materi resmi DJBC
    untuk mendukung literasi masyarakat serta kegiatan akademik dan magang di lingkungan
    Direktorat Jenderal Bea dan Cukai Wilayah Aceh.
    <br><br>
    Teknologi: <b>Python & Streamlit</b>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
© 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
<br>Customs in Action | Infographic Dashboard
</div>
""", unsafe_allow_html=True)
