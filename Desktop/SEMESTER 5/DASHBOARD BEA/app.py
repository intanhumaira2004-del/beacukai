import streamlit as st

st.set_page_config(
    page_title="Customs in Action — DJBC Aceh",
    page_icon="🛃",
    layout="wide"
)

# ===================== GLOBAL STYLE =====================
st.markdown("""
<style>
body {
    background-color: #f4f7fb;
}

.header-box {
    background: linear-gradient(135deg, #003a8f, #005bac);
    padding: 45px;
    border-radius: 22px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.2);
}

.header-title {
    font-size: 46px;
    font-weight: 900;
}

.header-subtitle {
    font-size: 20px;
    margin-top: 4px;
    opacity: 0.95;
}

.header-desc {
    max-width: 950px;
    margin: 20px auto 0;
    font-size: 15.5px;
    line-height: 1.8;
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #003a8f;
    margin-top: 35px;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    border-left: 6px solid #003a8f;
    transition: 0.3s;
}

.info-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

.icon {
    font-size: 34px;
}

.card-title {
    font-size: 18px;
    font-weight: 800;
    margin-top: 6px;
}

.card-text {
    font-size: 14.5px;
    margin-top: 6px;
    line-height: 1.7;
}

.highlight-box {
    background: #eaf1fb;
    border-left: 6px solid #005bac;
    padding: 22px;
    border-radius: 16px;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 18px;
}

.flow-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 16px;
    margin-top: 18px;
}

.flow-step {
    background: white;
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-weight: 700;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.badge {
    display: inline-block;
    background: #005bac;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    margin-right: 6px;
}

.footer {
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
    text-align: center;
    font-size: 13px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
st.sidebar.title("🛃 DJBC Aceh")
menu = st.sidebar.radio(
    "Navigasi Materi",
    [
        "🏠 Beranda",
        "📘 Konsep Dasar Kepabeanan",
        "🌍 Daerah Pabean & Wilayah Pengawasan",
        "📄 Pemberitahuan Pabean",
        "🏗️ TPS, TPB, & Penimbunan",
        "🚢 Impor & Ekspor",
        "💰 Pembayaran, Penagihan & Jaminan",
        "🚚 Pengangkutan & Pengawasan",
        "🛡️ Barang Tertentu & Penegakan Hukum",
        "ℹ️ Tentang Dashboard"
    ]
)

# ===================== BERANDA =====================
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="header-box">
        <div class="header-title">🛃 Customs in Action</div>
        <div class="header-subtitle">Infographic Dashboard — DJBC Aceh</div>
        <div class="header-desc">
        Dashboard ini menyajikan ringkasan visual interaktif berdasarkan materi resmi
        Undang-Undang Kepabeanan mengenai pengawasan lalu lintas barang,
        pemungutan bea masuk dan bea keluar, serta perlindungan masyarakat dan industri nasional,
        dengan fokus pada peran strategis Direktorat Jenderal Bea dan Cukai Wilayah Aceh.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Utama Kepabeanan")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📦 Lalu Lintas Barang", "Impor & Ekspor")
    col2.metric("💰 Penerimaan Negara", "Bea & Cukai")
    col3.metric("🛡️ Perlindungan Publik", "Barang Ilegal")
    col4.metric("🏭 Dukungan Industri", "Fasilitas Fiskal")

    st.success("📘 Dashboard ini bersifat **edukatif** dan disusun berdasarkan bahan ajar resmi kepabeanan.")

# ===================== KONSEP DASAR =====================
elif menu == "📘 Konsep Dasar Kepabeanan":
    st.markdown('<div class="section-title">📘 Konsep Dasar Kepabeanan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <b>📌 Kepabeanan adalah</b> segala sesuatu yang berhubungan dengan pengawasan atas lalu lintas barang
    yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar sesuai
    dengan ketentuan peraturan perundang-undangan yang berlaku.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">💰</div>
            <div class="card-title">Bea Masuk</div>
            <div class="card-text">
            Pungutan negara yang dikenakan terhadap barang yang diimpor ke dalam daerah pabean.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📤</div>
            <div class="card-title">Bea Keluar</div>
            <div class="card-text">
            Pungutan negara atas barang tertentu yang diekspor keluar daerah pabean.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">⚖️</div>
            <div class="card-title">Pengawasan Pabean</div>
            <div class="card-text">
            Serangkaian tindakan pengendalian terhadap lalu lintas barang agar sesuai dengan ketentuan hukum.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📑</div>
            <div class="card-title">Kewajiban Pabean</div>
            <div class="card-text">
            Kewajiban menyerahkan pemberitahuan pabean dan melunasi pungutan negara.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== DAERAH PABEAN =====================
elif menu == "🌍 Daerah Pabean & Wilayah Pengawasan":
    st.markdown('<div class="section-title">🌍 Daerah Pabean & Wilayah Pengawasan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <b>📌 Daerah Pabean</b> meliputi wilayah Republik Indonesia yang mencakup darat, perairan,
    dan ruang udara di atasnya, serta tempat-tempat tertentu di Zona Ekonomi Eksklusif (ZEE)
    dan landas kontinen yang diperlakukan sebagai daerah pabean.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🏞️</div>
            <div class="card-title">Wilayah Darat</div>
            <div class="card-text">
            Seluruh daratan Indonesia yang menjadi lokasi kegiatan kepabeanan dan pengawasan barang.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🌊</div>
            <div class="card-title">Perairan</div>
            <div class="card-text">
            Laut teritorial Indonesia termasuk pelabuhan dan perairan pedalaman.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">✈️</div>
            <div class="card-title">Ruang Udara</div>
            <div class="card-text">
            Ruang udara di atas wilayah Indonesia yang menjadi jalur lalu lintas barang.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🛢️</div>
            <div class="card-title">ZEE & Landas Kontinen</div>
            <div class="card-text">
            Tempat tertentu di luar laut teritorial yang digunakan untuk eksplorasi dan eksploitasi ekonomi.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== PEMBERITAHUAN PABEAN =====================
elif menu == "📄 Pemberitahuan Pabean":
    st.markdown('<div class="section-title">📄 Pemberitahuan Pabean</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <b>📌 Pemberitahuan Pabean</b> adalah pernyataan yang dibuat oleh orang dalam rangka
    melaksanakan kewajiban pabean dalam bentuk dan syarat yang ditetapkan dalam Undang-Undang Kepabeanan.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🖊️</div>
            <div class="card-title">Bentuk Pemberitahuan</div>
            <div class="card-text">
            Disampaikan dalam bentuk tulisan pada formulir atau data elektronik dan merupakan alat bukti yang sah.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">👤</div>
            <div class="card-title">Pihak yang Wajib Menyampaikan</div>
            <div class="card-text">
            Pengangkut, importir, eksportir, atau PPJK sebagai kuasa pemilik barang.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📥</div>
            <div class="card-title">Registrasi Kepabeanan</div>
            <div class="card-text">
            Setiap pihak yang memenuhi kewajiban pabean wajib registrasi untuk memperoleh identitas kepabeanan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🔁</div>
            <div class="card-title">Perubahan & Pembatalan</div>
            <div class="card-text">
            Dapat diajukan apabila terdapat kesalahan data atau kekhilafan nyata sesuai ketentuan.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== TPS TPB =====================
elif menu == "🏗️ TPS, TPB, & Penimbunan":
    st.markdown('<div class="section-title">🏗️ TPS, TPB, & Penimbunan Barang</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <b>📌 Tempat Penimbunan Sementara (TPS)</b> adalah bangunan atau lapangan di kawasan pabean
    untuk menimbun barang sementara menunggu pemuatan atau pengeluaran.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">📦</div>
            <div class="card-title">TPS</div>
            <div class="card-text">
            Digunakan untuk menimbun barang sementara setelah dibongkar dari sarana pengangkut.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🏭</div>
            <div class="card-title">TPB (Tempat Penimbunan Berikat)</div>
            <div class="card-text">
            Menimbun barang dengan fasilitas penangguhan bea masuk untuk diolah, dirakit, atau diekspor kembali.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🏢</div>
            <div class="card-title">TPP (Tempat Penimbunan Pabean)</div>
            <div class="card-text">
            Tempat yang disediakan pemerintah untuk menyimpan barang yang tidak dikuasai atau menjadi milik negara.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">♻️</div>
            <div class="card-title">Tujuan Penimbunan</div>
            <div class="card-text">
            Untuk diolah, dipamerkan, dijual, dilelang, didaur ulang, atau diekspor kembali.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== IMPOR EKSPOR =====================
elif menu == "🚢 Impor & Ekspor":
    st.markdown('<div class="section-title">🚢 Impor & Ekspor</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">📥</div>
            <div class="card-title">Barang Impor</div>
            <div class="card-text">
            Barang yang dimasukkan ke dalam daerah pabean diperlakukan sebagai barang impor dan terutang bea masuk.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📤</div>
            <div class="card-title">Barang Ekspor</div>
            <div class="card-text">
            Barang yang dikeluarkan dari daerah pabean dan dapat dikenakan bea keluar dalam hal tertentu.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔄 Alur Impor")
    st.markdown("""
    <div class="flow-grid">
        <div class="flow-step">📄 Pemberitahuan Impor Barang (PIB)</div>
        <div class="flow-step">🔍 Penelitian Dokumen</div>
        <div class="flow-step">📦 Pemeriksaan Fisik (Selektif)</div>
        <div class="flow-step">💰 Pembayaran Bea Masuk</div>
        <div class="flow-step">🚚 Pengeluaran Barang</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔄 Alur Ekspor")
    st.markdown("""
    <div class="flow-grid">
        <div class="flow-step">📄 Pemberitahuan Ekspor Barang (PEB)</div>
        <div class="flow-step">🔍 Penelitian Dokumen</div>
        <div class="flow-step">📦 Pemeriksaan Fisik (Tertentu)</div>
        <div class="flow-step">🚢 Pemuatan Barang</div>
        <div class="flow-step">🌍 Ke Luar Daerah Pabean</div>
    </div>
    """, unsafe_allow_html=True)

# ===================== PEMBAYARAN =====================
elif menu == "💰 Pembayaran, Penagihan & Jaminan":
    st.markdown('<div class="section-title">💰 Pembayaran, Penagihan & Jaminan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    Bea masuk, denda administrasi, dan bunga dibayar ke kas negara atau tempat pembayaran lain
    yang ditunjuk Menteri, paling lambat pada tanggal pendaftaran pemberitahuan pabean.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">💵</div>
            <div class="card-title">Pembayaran Bea Masuk</div>
            <div class="card-text">
            Dapat diberikan penundaan pembayaran atau pembayaran berkala tanpa dikenakan bunga.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">⏳</div>
            <div class="card-title">Penagihan Kekurangan</div>
            <div class="card-text">
            Kekurangan pembayaran wajib dilunasi paling lama 60 hari sejak tanggal penetapan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📈</div>
            <div class="card-title">Denda & Bunga</div>
            <div class="card-text">
            Keterlambatan dikenakan bunga 2% per bulan dengan batas waktu tertentu.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🛡️</div>
            <div class="card-title">Jaminan</div>
            <div class="card-text">
            Dapat berupa tunai, bank, perusahaan asuransi, atau bentuk lain yang ditetapkan.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== PENGANGKUTAN =====================
elif menu == "🚚 Pengangkutan & Pengawasan":
    st.markdown('<div class="section-title">🚚 Pengangkutan & Pengawasan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    Pengangkut wajib memberitahukan rencana kedatangan sarana pengangkut serta mencantumkan
    barang dalam manifes, baik untuk barang impor maupun ekspor.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🚢</div>
            <div class="card-title">Pemberitahuan RKSP</div>
            <div class="card-text">
            Pengangkut wajib menyampaikan rencana kedatangan sarana pengangkut sebelum tiba.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📜</div>
            <div class="card-title">Manifes Barang</div>
            <div class="card-text">
            Setiap barang wajib dicantumkan dalam manifes dan diberitahukan kepada Bea Cukai.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">⚠️</div>
            <div class="card-title">Keadaan Darurat</div>
            <div class="card-text">
            Dalam keadaan tertentu, barang dapat dibongkar terlebih dahulu dengan kewajiban pelaporan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🚨</div>
            <div class="card-title">Sanksi</div>
            <div class="card-text">
            Pelanggaran kewajiban pemberitahuan dikenakan denda administratif sesuai ketentuan.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== BARANG TERTENTU =====================
elif menu == "🛡️ Barang Tertentu & Penegakan Hukum":
    st.markdown('<div class="section-title">🛡️ Barang Tertentu & Penegakan Hukum</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    Barang tertentu adalah barang yang ditetapkan oleh instansi teknis terkait yang
    pengangkutannya di dalam daerah pabean diawasi oleh Direktorat Jenderal Bea dan Cukai.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">

        <div class="info-card">
            <div class="icon">🚫</div>
            <div class="card-title">Barang Berbahaya</div>
            <div class="card-text">
            Termasuk narkotika, senjata api, bahan peledak, dan zat berbahaya lainnya.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">🚬</div>
            <div class="card-title">Barang Kena Cukai Ilegal</div>
            <div class="card-text">
            Rokok dan minuman beralkohol tanpa pita cukai yang sah.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">⚖️</div>
            <div class="card-title">Penindakan</div>
            <div class="card-text">
            Bea Cukai berwenang melakukan penindakan, penyidikan, dan penegakan hukum kepabeanan.
            </div>
        </div>

        <div class="info-card">
            <div class="icon">📑</div>
            <div class="card-title">Pemeriksaan Kepabeanan</div>
            <div class="card-text">
            Meliputi pemeriksaan laporan keuangan, dokumen, serta sediaan barang.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ===================== TENTANG =====================
elif menu == "ℹ️ Tentang Dashboard":
    st.markdown('<div class="section-title">ℹ️ Tentang Dashboard</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
    <div class="card-text">
    Dashboard ini dikembangkan sebagai media edukasi visual berbasis materi resmi
    Undang-Undang Kepabeanan dan bahan ajar DJBC, khususnya untuk mendukung literasi
    kepabeanan masyarakat serta kegiatan akademik dan magang di lingkungan
    Direktorat Jenderal Bea dan Cukai Wilayah Aceh.
    <br><br>
    Teknologi: <b>Python — Streamlit</b>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
🛃 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh<br>
Customs in Action | Infographic Education Dashboard
</div>
""", unsafe_allow_html=True)
