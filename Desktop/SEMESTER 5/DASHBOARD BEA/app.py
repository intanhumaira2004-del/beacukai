import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Bea Cukai in Action — DJBC Aceh",
    page_icon="🛃",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}

.title-box {
    background: linear-gradient(135deg, #003A8F, #0050B3);
    padding: 40px;
    border-radius: 16px;
    color: white;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
}

.title-main {
    font-size: 44px;
    font-weight: 800;
}

.subtitle {
    font-size: 20px;
    opacity: 0.9;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #003A8F;
    margin-top: 30px;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.info-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #003A8F;
    transition: 0.3s;
}

.info-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
}

.icon {
    font-size: 34px;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 6px;
}

.card-text {
    font-size: 15px;
    margin-top: 6px;
    color: #333;
}

.flow-box {
    background: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-top: 6px solid #0050B3;
}

.footer {
    text-align: center;
    font-size: 13px;
    color: gray;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("🛃 DJBC Aceh")
menu = st.sidebar.radio("Navigasi Dashboard", [
    "🏠 Beranda",
    "📌 Peran & Fungsi Bea Cukai",
    "🚢 Alur Impor & Ekspor",
    "🏛️ Kepabeanan",
    "🛡️ Perlindungan Masyarakat",
    "📖 Edukasi Publik",
    "ℹ️ Tentang Dashboard"
])

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="title-box">
        <div class="title-main">🛃 Bea Cukai in Action</div>
        <div class="subtitle">Infographic Dashboard — DJBC Aceh</div>
        <p style="margin-top:14px;font-size:16px;">
        Menampilkan peran strategis Direktorat Jenderal Bea dan Cukai Wilayah Aceh dalam
        mengawasi perdagangan internasional, melindungi masyarakat, serta mendukung pembangunan nasional.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Utama DJBC Aceh")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌍 Perdagangan", "Ekspor–Impor", "Fasilitasi")
    col2.metric("💰 Penerimaan", "Bea & Cukai", "Optimalisasi")
    col3.metric("🛡️ Perlindungan", "Barang Ilegal", "Pencegahan")
    col4.metric("🏭 Industri", "Fasilitas Fiskal", "Penguatan")

    st.success("Dashboard ini bersifat **edukatif & informatif** untuk mendukung literasi kepabeanan masyarakat Aceh.")

# ================= PERAN & FUNGSI =================
elif menu == "📌 Peran & Fungsi Bea Cukai":
    st.markdown('<div class="section-title">📌 Empat Pilar Strategis Bea Cukai</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">💰</div>
            <div class="card-title">Revenue Collector</div>
            <div class="card-text">
            Menghimpun penerimaan negara dari bea masuk, bea keluar, dan cukai sebagai
            sumber pembiayaan APBN untuk pembangunan nasional.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🛡️</div>
            <div class="card-title">Community Protector</div>
            <div class="card-text">
            Melindungi masyarakat dari peredaran narkotika, senjata ilegal, barang berbahaya,
            serta praktik perdagangan ilegal lintas negara.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🚢</div>
            <div class="card-title">Trade Facilitator</div>
            <div class="card-text">
            Memfasilitasi arus barang ekspor dan impor melalui pelayanan kepabeanan yang cepat,
            transparan, dan berbasis teknologi informasi.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🏭</div>
            <div class="card-title">Industrial Assistance</div>
            <div class="card-text">
            Mendukung pertumbuhan industri nasional melalui fasilitas fiskal, kawasan berikat,
            dan insentif kepabeanan untuk meningkatkan daya saing ekspor.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ================= ALUR IMPOR EKSPOR =================
elif menu == "🚢 Alur Impor & Ekspor":
    st.markdown('<div class="section-title">🚢 Alur Proses Kepabeanan Ekspor & Impor</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="flow-box">
        <h4>📦 Alur Impor</h4>
        <ol>
            <li>Kedatangan barang ke pelabuhan/bandara</li>
            <li>Pengajuan PIB (Pemberitahuan Impor Barang)</li>
            <li>Pemeriksaan dokumen & fisik (jika diperlukan)</li>
            <li>Pembayaran bea masuk & pajak</li>
            <li>Barang keluar dari kawasan pabean</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="flow-box">
        <h4>🚢 Alur Ekspor</h4>
        <ol>
            <li>Eksportir menyiapkan barang</li>
            <li>Pengajuan PEB (Pemberitahuan Ekspor Barang)</li>
            <li>Pemeriksaan dokumen</li>
            <li>Pemuatan ke sarana pengangkut</li>
            <li>Barang diberangkatkan ke luar negeri</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    st.info("DJBC Aceh memastikan seluruh proses berjalan **aman, legal, dan efisien**.")

# ================= KEPA BEANAN =================
elif menu == "🏛️ Kepabeanan":
    st.markdown('<div class="section-title">🏛️ Apa Itu Kepabeanan?</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
    <div class="card-text">
    <b>Kepabeanan</b> adalah segala sesuatu yang berhubungan dengan pengawasan lalu lintas barang
    yang masuk atau keluar daerah pabean Indonesia serta pemungutan bea masuk dan bea keluar
    sesuai peraturan perundang-undangan.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">📚 Ruang Lingkup Kepabeanan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">📄</div>
            <div class="card-title">Dokumen Kepabeanan</div>
            <div class="card-text">
            Meliputi PIB, PEB, manifest, invoice, packing list, dan dokumen pendukung lainnya.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🔍</div>
            <div class="card-title">Pemeriksaan Barang</div>
            <div class="card-text">
            Pemeriksaan administratif dan fisik untuk memastikan kesesuaian barang dengan dokumen.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">💵</div>
            <div class="card-title">Pemungutan Bea</div>
            <div class="card-text">
            Pemungutan bea masuk, bea keluar, dan pungutan negara lainnya sesuai tarif dan ketentuan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">⚖️</div>
            <div class="card-title">Penegakan Hukum</div>
            <div class="card-text">
            Penindakan terhadap pelanggaran kepabeanan seperti penyelundupan dan pemalsuan dokumen.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ================= PERLINDUNGAN =================
elif menu == "🛡️ Perlindungan Masyarakat":
    st.markdown('<div class="section-title">🛡️ Peran Bea Cukai dalam Perlindungan Publik</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🚫</div>
            <div class="card-title">Narkotika & Psikotropika</div>
            <div class="card-text">
            Mencegah masuknya narkoba lintas negara demi menjaga generasi bangsa.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🔫</div>
            <div class="card-title">Senjata & Bahan Berbahaya</div>
            <div class="card-text">
            Menangkal penyelundupan senjata api, bahan peledak, dan zat berbahaya lainnya.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🧪</div>
            <div class="card-title">Barang Tidak Standar</div>
            <div class="card-text">
            Mengawasi barang impor yang tidak memenuhi standar keamanan dan kesehatan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🚭</div>
            <div class="card-title">Rokok & Minuman Ilegal</div>
            <div class="card-text">
            Memberantas peredaran rokok dan minuman mengandung etil alkohol tanpa pita cukai.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ================= EDUKASI =================
elif menu == "📖 Edukasi Publik":
    st.markdown('<div class="section-title">📖 Literasi Kepabeanan untuk Masyarakat</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🎓</div>
            <div class="card-title">Sosialisasi Kepabeanan</div>
            <div class="card-text">
            Edukasi kepada pelaku usaha dan masyarakat mengenai prosedur ekspor-impor yang benar.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🏫</div>
            <div class="card-title">Program Sekolah & Kampus</div>
            <div class="card-text">
            Pengenalan peran Bea Cukai melalui kunjungan edukatif dan kuliah umum.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📢</div>
            <div class="card-title">Kampanye Publik</div>
            <div class="card-text">
            Penyebaran informasi melalui media sosial, publikasi, dan kegiatan masyarakat.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🤝</div>
            <div class="card-title">Kemitraan UMKM</div>
            <div class="card-text">
            Pendampingan UMKM ekspor agar mampu bersaing di pasar global.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ================= TENTANG =================
elif menu == "ℹ️ Tentang Dashboard":
    st.markdown('<div class="section-title">ℹ️ Tentang Dashboard</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
    <div class="card-text">
    Dashboard ini dibuat sebagai media visualisasi edukatif mengenai peran strategis
    Direktorat Jenderal Bea dan Cukai Wilayah Aceh dalam menjaga kedaulatan ekonomi,
    meningkatkan penerimaan negara, serta melindungi masyarakat dari perdagangan ilegal.
    <br><br>
    Dikembangkan menggunakan <b>Streamlit</b> sebagai bagian dari pembelajaran visualisasi data dan sistem informasi publik.
    </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
🛃 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh<br>
Dashboard Edukasi Kepabeanan | 2026
</div>
""", unsafe_allow_html=True)
