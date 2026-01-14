import streamlit as st

st.set_page_config(
    page_title="Bea Cukai in Action | DJBC Aceh",
    page_icon="🛃",
    layout="wide"
)

st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .container {
        background: linear-gradient(135deg, #003a8f, #005bac);
        padding: 50px 35px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 8px 28px rgba(0,0,0,0.25);
    }
    .title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        margin-bottom: 25px;
        opacity: 0.95;
    }
    .desc {
        text-align: center;
        font-size: 17px;
        max-width: 1000px;
        margin: auto;
        line-height: 1.8;
        margin-bottom: 40px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin: 35px 0 20px;
        border-left: 6px solid #f9b233;
        padding-left: 14px;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 20px;
    }

    .card {
        background: rgba(255,255,255,0.15);
        padding: 22px;
        border-radius: 18px;
        backdrop-filter: blur(6px);
    }

    .flow {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 15px;
        text-align: center;
    }

    .step {
        background: rgba(255,255,255,0.18);
        padding: 18px;
        border-radius: 16px;
        font-weight: 600;
    }

    .footer {
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.3);
        text-align: center;
        font-size: 14px;
        opacity: 0.9;
    }
    </style>

    <div class="container">
        <div class="title">🛃 Bea Cukai in Action</div>
        <div class="subtitle">Interactive Customs Dashboard — DJBC Aceh</div>

        <div class="desc">
            Dashboard ini dirancang sebagai media informatif dan edukatif
            untuk menggambarkan peran strategis Direktorat Jenderal Bea dan Cukai
            (DJBC) Wilayah Aceh dalam pengawasan, pelayanan, dan penegakan hukum
            di bidang kepabeanan dan cukai. Aplikasi ini mendukung pemahaman
            mahasiswa dan masyarakat terhadap fungsi Bea Cukai sebagai penjaga
            lalu lintas barang dan pelindung kepentingan nasional.
        </div>

        <div class="section-title">🏛️ Peran Strategis Bea Cukai</div>
        <div class="grid">
            <div class="card">
                💰 <b>Revenue Collector</b>
                <ul>
                    <li>Bea Masuk & Bea Keluar</li>
                    <li>Cukai hasil tembakau & MMEA</li>
                    <li>Penerimaan negara</li>
                </ul>
            </div>
            <div class="card">
                🛡️ <b>Community Protector</b>
                <ul>
                    <li>Pencegahan penyelundupan</li>
                    <li>Pengawasan narkotika</li>
                    <li>Barang berbahaya</li>
                </ul>
            </div>
            <div class="card">
                🚢 <b>Trade Facilitator</b>
                <ul>
                    <li>Kelancaran ekspor-impor</li>
                    <li>Pelayanan kepabeanan</li>
                    <li>Dukungan UMKM ekspor</li>
                </ul>
            </div>
            <div class="card">
                🏭 <b>Industrial Assistance</b>
                <ul>
                    <li>Fasilitas fiskal</li>
                    <li>Kawasan berikat</li>
                    <li>Dukungan industri</li>
                </ul>
            </div>
        </div>

        <div class="section-title">🔄 Alur Impor & Ekspor</div>
        <div class="flow">
            <div class="step">📄 Pemberitahuan Pabean</div>
            <div class="step">📦 Pemeriksaan Dokumen</div>
            <div class="step">🔍 Pemeriksaan Fisik</div>
            <div class="step">💰 Pembayaran Bea & Cukai</div>
            <div class="step">🚚 Pengeluaran Barang</div>
        </div>

        <div class="section-title">⚙️ Tugas Utama DJBC</div>
        <div class="card">
            <ul>
                <li>Mengawasi lalu lintas barang masuk dan keluar daerah pabean</li>
                <li>Memungut penerimaan negara dari sektor kepabeanan dan cukai</li>
                <li>Melaksanakan penegakan hukum kepabeanan dan cukai</li>
                <li>Memberikan pelayanan dan fasilitas kepabeanan</li>
                <li>Mendukung kebijakan fiskal dan perdagangan nasional</li>
            </ul>
        </div>

        <div class="footer">
            © 2026 Direktorat Jenderal Bea dan Cukai — Wilayah Aceh  
            <br>
            Dashboard Edukasi & Visualisasi Kepabeanan
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
