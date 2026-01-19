import streamlit as st

st.set_page_config(
    page_title="Customs in Action — DJBC Aceh",
    page_icon="🛃",
    layout="wide"
)

# ===================== STYLE =====================
st.markdown("""
<style>
body {
    background-color: #f4f7fb;
}
.block {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
    border-left: 6px solid #003a8f;
    margin-bottom: 20px;
}
.title {
    font-size: 36px;
    font-weight: 900;
    color: #003a8f;
}
.subtitle {
    font-size: 18px;
    color: #555;
}
.section {
    font-size: 26px;
    font-weight: 800;
    color: #003a8f;
    margin-top: 30px;
}
.flow {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 15px;
}
.step {
    background: #eaf1fb;
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-weight: 700;
}
.footer {
    text-align: center;
    margin-top: 40px;
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
        "📘 Konsep Kepabeanan",
        "🌍 Daerah Pabean",
        "📄 Pemberitahuan Pabean",
        "🏗️ TPS & TPB",
        "🚢 Impor & Ekspor",
        "💰 Pembayaran & Jaminan",
        "🚚 Pengangkutan",
        "🛡️ Barang Tertentu",
        "ℹ️ Tentang"
    ]
)

# ===================== BERANDA =====================
if menu == "🏠 Beranda":
    st.markdown('<div class="title">🛃 Customs in Action</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Infographic Dashboard — DJBC Aceh</div>', unsafe_allow_html=True)

    st.success("Dashboard edukasi kepabeanan berbasis materi resmi DJBC Wilayah Aceh")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📦 Lalu Lintas Barang", "Impor & Ekspor")
    col2.metric("💰 Penerimaan Negara", "Bea & Cukai")
    col3.metric("🛡️ Perlindungan Publik", "Barang Ilegal")
    col4.metric("🏭 Dukungan Industri", "Fasilitas Fiskal")

    st.markdown("""
    <div class="block">
    <b>Kepabeanan adalah</b> segala sesuatu yang berhubungan dengan pengawasan atas lalu lintas
    barang yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar
    untuk melindungi masyarakat, industri nasional, dan penerimaan negara.
    </div>
    """, unsafe_allow_html=True)

# ===================== KONSEP =====================
elif menu == "📘 Konsep Kepabeanan":
    st.markdown('<div class="section">📘 Konsep Dasar Kepabeanan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <b>Kepabeanan adalah</b> segala sesuatu yang berhubungan dengan pengawasan atas lalu lintas barang
    yang masuk atau keluar daerah pabean serta pemungutan bea masuk dan bea keluar berdasarkan
    peraturan perundang-undangan yang berlaku.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">💰 <b>Bea Masuk</b><br>Pungutan negara atas barang yang diimpor ke dalam daerah pabean.</div>
    <div class="block">📤 <b>Bea Keluar</b><br>Pungutan negara atas barang tertentu yang diekspor keluar daerah pabean.</div>
    <div class="block">⚖️ <b>Pengawasan Pabean</b><br>Pengendalian atas lalu lintas barang agar sesuai ketentuan hukum.</div>
    <div class="block">📑 <b>Kewajiban Pabean</b><br>Kewajiban menyampaikan pemberitahuan pabean dan melunasi pungutan negara.</div>
    """, unsafe_allow_html=True)

# ===================== DAERAH PABEAN =====================
elif menu == "🌍 Daerah Pabean":
    st.markdown('<div class="section">🌍 Daerah Pabean & Wilayah Pengawasan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <b>Daerah Pabean</b> meliputi wilayah darat, perairan, dan ruang udara Indonesia, termasuk
    tempat tertentu di Zona Ekonomi Eksklusif dan landas kontinen yang diperlakukan sebagai
    daerah pabean.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">🏞️ <b>Darat</b><br>Seluruh daratan Indonesia sebagai wilayah pengawasan kepabeanan.</div>
    <div class="block">🌊 <b>Perairan</b><br>Laut teritorial dan perairan pedalaman Indonesia.</div>
    <div class="block">✈️ <b>Ruang Udara</b><br>Ruang udara di atas wilayah Indonesia.</div>
    <div class="block">🛢️ <b>ZEE & Landas Kontinen</b><br>Wilayah ekonomi khusus yang diperlakukan sebagai daerah pabean.</div>
    """, unsafe_allow_html=True)

# ===================== PEMBERITAHUAN =====================
elif menu == "📄 Pemberitahuan Pabean":
    st.markdown('<div class="section">📄 Pemberitahuan Pabean</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <b>Pemberitahuan Pabean</b> adalah pernyataan yang dibuat oleh orang untuk melaksanakan
    kewajiban pabean dalam bentuk dan syarat yang ditetapkan oleh undang-undang.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">🖊️ <b>Bentuk</b><br>Ditulis di formulir atau disampaikan secara elektronik.</div>
    <div class="block">👤 <b>Pihak</b><br>Pengangkut, importir, eksportir, atau PPJK.</div>
    <div class="block">📥 <b>Registrasi</b><br>Setiap pihak wajib memiliki identitas kepabeanan.</div>
    <div class="block">🔁 <b>Perubahan</b><br>Dapat diajukan jika terdapat kekeliruan data.</div>
    """, unsafe_allow_html=True)

# ===================== TPS TPB =====================
elif menu == "🏗️ TPS & TPB":
    st.markdown('<div class="section">🏗️ TPS, TPB & Penimbunan Barang</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <b>Tempat Penimbunan Sementara (TPS)</b> adalah bangunan atau lapangan di kawasan pabean
    untuk menimbun barang sementara setelah dibongkar dari sarana pengangkut.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">📦 <b>TPS</b><br>Penimbunan sementara sebelum pengeluaran barang.</div>
    <div class="block">🏭 <b>TPB</b><br>Penimbunan berikat dengan fasilitas penangguhan bea masuk.</div>
    <div class="block">🏢 <b>TPP</b><br>Tempat penimbunan pabean milik pemerintah.</div>
    <div class="block">♻️ <b>Tujuan</b><br>Diolah, dirakit, dipamerkan, diekspor kembali.</div>
    """, unsafe_allow_html=True)

# ===================== IMPOR EKSPOR =====================
elif menu == "🚢 Impor & Ekspor":
    st.markdown('<div class="section">🚢 Impor & Ekspor</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">📥 <b>Barang Impor</b><br>Barang yang dimasukkan ke dalam daerah pabean.</div>
    <div class="block">📤 <b>Barang Ekspor</b><br>Barang yang dikeluarkan dari daerah pabean.</div>
    """, unsafe_allow_html=True)

    st.subheader("🔄 Alur Impor")
    st.markdown("""
    <div class="flow">
        <div class="step">📄 PIB</div>
        <div class="step">🔍 Penelitian Dokumen</div>
        <div class="step">📦 Pemeriksaan Fisik</div>
        <div class="step">💰 Pembayaran</div>
        <div class="step">🚚 Pengeluaran Barang</div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🔄 Alur Ekspor")
    st.markdown("""
    <div class="flow">
        <div class="step">📄 PEB</div>
        <div class="step">🔍 Penelitian Dokumen</div>
        <div class="step">📦 Pemeriksaan</div>
        <div class="step">🚢 Pemuatan</div>
        <div class="step">🌍 Ekspor</div>
    </div>
    """, unsafe_allow_html=True)

# ===================== PEMBAYARAN =====================
elif menu == "💰 Pembayaran & Jaminan":
    st.markdown('<div class="section">💰 Pembayaran, Penagihan & Jaminan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    Bea masuk, denda administrasi, dan bunga dibayar ke kas negara atau tempat pembayaran
    yang ditunjuk Menteri pada saat pendaftaran pemberitahuan pabean.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">💵 <b>Pembayaran</b><br>Dapat diberikan penundaan atau pembayaran berkala.</div>
    <div class="block">⏳ <b>Penagihan</b><br>Kekurangan pembayaran wajib dilunasi paling lama 60 hari.</div>
    <div class="block">📈 <b>Denda & Bunga</b><br>Dikenakan atas keterlambatan pembayaran.</div>
    <div class="block">🛡️ <b>Jaminan</b><br>Dapat berupa tunai, bank, atau asuransi.</div>
    """, unsafe_allow_html=True)

# ===================== PENGANGKUTAN =====================
elif menu == "🚚 Pengangkutan":
    st.markdown('<div class="section">🚚 Pengangkutan & Pengawasan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    Pengangkut wajib memberitahukan rencana kedatangan sarana pengangkut dan mencantumkan
    barang dalam manifes kepada Bea dan Cukai.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">🚢 <b>RKSP</b><br>Pemberitahuan rencana kedatangan sarana pengangkut.</div>
    <div class="block">📜 <b>Manifes</b><br>Daftar barang yang diangkut.</div>
    <div class="block">⚠️ <b>Keadaan Darurat</b><br>Barang dapat dibongkar dengan kewajiban pelaporan.</div>
    <div class="block">🚨 <b>Sanksi</b><br>Pelanggaran dikenakan denda administratif.</div>
    """, unsafe_allow_html=True)

# ===================== BARANG TERTENTU =====================
elif menu == "🛡️ Barang Tertentu":
    st.markdown('<div class="section">🛡️ Barang Tertentu & Penindakan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    Barang tertentu adalah barang yang pengangkutannya di dalam daerah pabean diawasi
    oleh Direktorat Jenderal Bea dan Cukai karena sifat, jenis, atau dampaknya.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">🚫 <b>Barang Berbahaya</b><br>Narkotika, senjata api, bahan peledak.</div>
    <div class="block">🚬 <b>Barang Kena Cukai Ilegal</b><br>Rokok & MMEA tanpa pita cukai.</div>
    <div class="block">⚖️ <b>Penindakan</b><br>Penegakan hukum kepabeanan.</div>
    <div class="block">📑 <b>Pemeriksaan</b><br>Pemeriksaan dokumen dan barang.</div>
    """, unsafe_allow_html=True)

# ===================== TENTANG =====================
elif menu == "ℹ️ Tentang":
    st.markdown('<div class="section">ℹ️ Tentang Dashboard</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    Dashboard ini dibuat sebagai media edukasi kepabeanan berbasis materi resmi DJBC
    untuk mendukung literasi masyarakat dan kegiatan akademik, khususnya di wilayah Aceh.
    <br><br>
    Teknologi: <b>Python — Streamlit</b>
    </div>
    """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
🛃 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh<br>
Customs in Action | Infographic Dashboard
</div>
""", unsafe_allow_html=True)
