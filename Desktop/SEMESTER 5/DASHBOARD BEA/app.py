import streamlit as st

st.set_page_config(
    page_title="DJBC Aceh | Customs in Action",
    page_icon="🛃",
    layout="wide"
)

# ===================== STYLE =====================
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #f3f7fc, #e9f0fb);
}

.main-card {
    background: white;
    padding: 40px;
    border-radius: 26px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.08);
    margin-bottom: 35px;
}

.hero {
    background: linear-gradient(135deg, #002d72, #005bac);
    border-radius: 28px;
    padding: 70px 50px;
    color: white;
    text-align: center;
    box-shadow: 0 25px 60px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 56px;
    font-weight: 900;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 22px;
    opacity: 0.95;
}

.hero-desc {
    max-width: 850px;
    margin: 24px auto 0;
    font-size: 16.5px;
    line-height: 1.9;
}

.badge-row {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 28px;
}

.badge {
    background: rgba(255,255,255,0.18);
    padding: 9px 18px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
}

.section-title {
    font-size: 30px;
    font-weight: 900;
    color: #002d72;
    margin: 15px 0 28px;
}

.section-subtitle {
    font-size: 15.5px;
    color: #555;
    margin-bottom: 25px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
}

.card {
    background: #f8fbff;
    padding: 26px 22px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    transition: 0.3s;
    border-top: 6px solid #005bac;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.12);
}

.card-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 6px;
}

.card-text {
    font-size: 14.5px;
    line-height: 1.7;
    color: #444;
}

.highlight {
    background: linear-gradient(135deg, #edf4ff, #f8fbff);
    padding: 28px;
    border-radius: 22px;
    font-size: 15.5px;
    line-height: 1.9;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

.timeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
}

.timeline-step {
    background: white;
    padding: 20px 18px;
    border-radius: 20px;
    text-align: center;
    font-weight: 700;
    box-shadow: 0 10px 26px rgba(0,0,0,0.08);
    border-bottom: 5px solid #005bac;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 26px;
}

.stat {
    background: linear-gradient(135deg, #002d72, #005bac);
    color: white;
    padding: 28px;
    border-radius: 24px;
    text-align: center;
    box-shadow: 0 14px 34px rgba(0,0,0,0.2);
}

.stat-icon {
    font-size: 34px;
    margin-bottom: 8px;
}

.stat-label {
    font-size: 14px;
    opacity: 0.95;
}

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
        Dashboard infografis interaktif ini menyajikan peran strategis Bea dan Cukai
        dalam menjaga perbatasan, mengamankan penerimaan negara, memfasilitasi perdagangan,
        serta melindungi masyarakat dari peredaran barang ilegal dan berbahaya.
        </div>

        <div class="badge-row">
            <div class="badge">📦 Kepabeanan</div>
            <div class="badge">🏷️ Cukai</div>
            <div class="badge">🛡️ Pengawasan</div>
            <div class="badge">🚢 Ekspor–Impor</div>
            <div class="badge">💰 Penerimaan Negara</div>
            <div class="badge">🏭 Fasilitas Fiskal</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="main-card">
        <div class="section-title">🎯 Tujuan Dashboard</div>
        <div class="section-subtitle">
        Media edukasi visual untuk memahami peran DJBC Aceh dalam sistem perdagangan internasional
        dan pengamanan wilayah perbatasan Indonesia.
        </div>

        <div class="grid">
            <div class="card">
                <div class="card-icon">📘</div>
                <div class="card-title">Edukasi Publik</div>
                <div class="card-text">
                Menyampaikan informasi kepabeanan dan cukai secara mudah, ringkas, dan visual.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🛡️</div>
                <div class="card-title">Proteksi Negara</div>
                <div class="card-text">
                Melindungi masyarakat dari masuknya barang berbahaya dan ilegal lintas batas.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🚢</div>
                <div class="card-title">Fasilitasi Perdagangan</div>
                <div class="card-text">
                Mempercepat arus ekspor–impor demi pertumbuhan ekonomi nasional dan daerah.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🏭</div>
                <div class="card-title">Dukungan Industri</div>
                <div class="card-text">
                Memberikan fasilitas fiskal bagi industri dan UMKM ekspor.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== KEPA BEANAN =====================
elif menu == "📘 Kepabeanan & Cukai":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">📘 Kepabeanan & Cukai</div>
        <div class="section-subtitle">Konsep dasar yang menjadi fondasi tugas DJBC</div>

        <div class="highlight">
        <b>🔹 Kepabeanan adalah</b> seluruh kegiatan yang berkaitan dengan pengawasan atas lalu lintas
        barang yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar
        sesuai ketentuan peraturan perundang-undangan yang berlaku.
        <br><br>
        <b>🔹 Cukai adalah</b> pungutan negara yang dikenakan terhadap barang tertentu yang memiliki
        sifat atau karakteristik tertentu, seperti hasil tembakau dan minuman beralkohol.
        </div>

        <br>

        <div class="grid">
            <div class="card">
                <div class="card-icon">💰</div>
                <div class="card-title">Bea Masuk</div>
                <div class="card-text">
                Pungutan negara atas barang impor ke dalam daerah pabean.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">📤</div>
                <div class="card-title">Bea Keluar</div>
                <div class="card-text">
                Pungutan negara atas barang tertentu yang diekspor keluar daerah pabean.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">⚖️</div>
                <div class="card-title">Pengawasan</div>
                <div class="card-text">
                Pengendalian lalu lintas barang agar sesuai hukum dan regulasi.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">📑</div>
                <div class="card-title">Kewajiban Pabean</div>
                <div class="card-text">
                Kewajiban menyampaikan pemberitahuan dan melunasi pungutan.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== PILAR =====================
elif menu == "🏛️ Pilar Bea Cukai":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">🏛️ Empat Pilar Strategis Bea Cukai</div>
        <div class="section-subtitle">Peran utama DJBC dalam sistem ekonomi nasional</div>

        <div class="grid">

            <div class="card">
                <div class="card-icon">💰</div>
                <div class="card-title">Revenue Collector</div>
                <div class="card-text">
                Menghimpun penerimaan negara dari bea masuk, bea keluar, dan cukai.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🛡️</div>
                <div class="card-title">Community Protector</div>
                <div class="card-text">
                Melindungi masyarakat dari narkotika, barang ilegal, dan berbahaya.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🚢</div>
                <div class="card-title">Trade Facilitator</div>
                <div class="card-text">
                Memfasilitasi ekspor–impor melalui pelayanan cepat dan transparan.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🏭</div>
                <div class="card-title">Industrial Assistance</div>
                <div class="card-text">
                Mendukung industri nasional melalui fasilitas fiskal.
                </div>
            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== ALUR =====================
elif menu == "🔄 Alur Impor–Ekspor":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">🔄 Alur Proses Kepabeanan</div>
        <div class="section-subtitle">Tahapan utama dalam proses impor dan ekspor</div>

        <div class="timeline">
            <div class="timeline-step">📄 Penyampaian Dokumen Pabean</div>
            <div class="timeline-step">🔎 Analisis Risiko</div>
            <div class="timeline-step">📦 Pemeriksaan Barang</div>
            <div class="timeline-step">💰 Pembayaran Bea & Cukai</div>
            <div class="timeline-step">🚚 Persetujuan Pengeluaran</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== TUGAS =====================
elif menu == "⚙️ Tugas & Fungsi":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">⚙️ Tugas Pokok dan Fungsi DJBC</div>
        <div class="section-subtitle">Ruang lingkup kerja Direktorat Jenderal Bea dan Cukai</div>

        <div class="grid">

            <div class="card">
                <div class="card-icon">📊</div>
                <div class="card-title">Pengawasan Perbatasan</div>
                <div class="card-text">
                Mengawasi lalu lintas barang di pelabuhan, bandara, dan perbatasan.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">⚖️</div>
                <div class="card-title">Penegakan Hukum</div>
                <div class="card-text">
                Melakukan penindakan dan penyidikan atas pelanggaran kepabeanan.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🤝</div>
                <div class="card-title">Pelayanan Publik</div>
                <div class="card-text">
                Memberikan pelayanan prima berbasis sistem digital.
                </div>
            </div>

            <div class="card">
                <div class="card-icon">🏢</div>
                <div class="card-title">Fasilitasi Industri</div>
                <div class="card-text">
                Memberikan insentif fiskal untuk meningkatkan daya saing industri.
                </div>
            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== DJBC ACEH =====================
elif menu == "🌏 DJBC Aceh":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">🌏 Peran Strategis DJBC Wilayah Aceh</div>
        <div class="section-subtitle">Posisi Aceh sebagai pintu gerbang perdagangan barat Indonesia</div>

        <div class="highlight">
        Wilayah Aceh memiliki posisi strategis sebagai jalur perdagangan internasional wilayah barat Indonesia.
        DJBC Aceh berperan dalam menjaga keamanan perbatasan laut, mengawasi arus barang lintas negara,
        mendorong ekspor komoditas unggulan daerah, serta melindungi masyarakat dari peredaran narkotika
        dan barang ilegal.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== DAMPAK =====================
elif menu == "🎯 Dampak":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">🎯 Dampak Positif Kehadiran Bea Cukai</div>
        <div class="section-subtitle">Kontribusi nyata terhadap negara dan masyarakat</div>

        <div class="stat-grid">
            <div class="stat">
                <div class="stat-icon">💰</div>
                <div class="stat-label">Peningkatan penerimaan negara</div>
            </div>
            <div class="stat">
                <div class="stat-icon">🛡️</div>
                <div class="stat-label">Perlindungan masyarakat & generasi muda</div>
            </div>
            <div class="stat">
                <div class="stat-icon">🚢</div>
                <div class="stat-label">Kelancaran arus perdagangan nasional</div>
            </div>
            <div class="stat">
                <div class="stat-icon">🏭</div>
                <div class="stat-label">Pertumbuhan industri & UMKM ekspor</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== TENTANG =====================
elif menu == "ℹ️ Tentang":
    st.markdown("""
    <div class="main-card">
        <div class="section-title">ℹ️ Tentang Dashboard</div>
        <div class="section-subtitle">Profil singkat aplikasi dan tujuan pengembangan</div>

        <div class="highlight">
        Dashboard ini dikembangkan sebagai media edukasi kepabeanan berbasis materi resmi DJBC
        untuk mendukung literasi masyarakat serta kegiatan akademik dan magang di lingkungan
        Direktorat Jenderal Bea dan Cukai Wilayah Aceh.
        <br><br>
        Teknologi yang digunakan: <b>Python & Streamlit</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
© 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
<br>Customs in Action | Infographic Dashboard
</div>
""", unsafe_allow_html=True)
