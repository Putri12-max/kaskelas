import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Portal Kas Kelas Sains Data 1A",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DATA MAHASISWA & KAS KELAS SAINS DATA 1A
# ---------------------------------------------------------
months = ["September", "November", "Desember", "Januari", "Februari"]

@st.cache_data
def load_initial_data():
    data = {
        "No": list(range(1, 26)),
        "Nama": [
            "Yoga Prasetya", "Narendra Putra Apriyanto", "Ahmad Jihad Maulana", "Zaenatun Nisa", "Salwa Fakhirah",
            "Qismika Agny Azzalfa", "Viona Dwi Susilowati", "Raihan Ahsan Syarif", "Nisfa Nur Rohmah", "Angga (Viangga)",
            "Muhimatul Mahmudah", "Putri Titha Navidya", "Sabda Pratama", "Agung Wibowo", "Ardian Ardiyansah",
            "Arina Manasikana", "Sri Mulyotari", "Wafa Maulana Kamal", "Ahmad Ibham Yumna", "Khaylaisya Maudy",
            "Talitha Yumna Reswara", "Ahmad Fauzi Santoso", "Gilang Ramadan Werfete", "Chadijah Sofia Maturbongs", "Maxi Alfred Busira"
        ],
        "NIM": [
            "73020260001", "73020260002", "73020260003", "73020260004", "73020260005",
            "73020260006", "73020260007", "73020260008", "73020260009", "73020260010",
            "73020260011", "73020260012", "73020260013", "73020260014", "73020260015",
            "73020260016", "73020260017", "73020260018", "73020260019", "73020260020",
            "73020260021", "73020260022", "73020260051", "73020260046", "73020260045"
        ],
        "September": ["Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum"],
        "November": ["Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas"],
        "Desember": ["Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas"],
        "Januari": ["Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum"],
        "Februari": ["Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Belum", "Lunas", "Lunas", "Lunas", "Belum", "Lunas", "Lunas"]
    }
    return pd.DataFrame(data)

# State Management
if 'df_kas' not in st.session_state:
    st.session_state.df_kas = load_initial_data()

df = st.session_state.df_kas

# ---------------------------------------------------------
# SIDEBAR / NAVIGASI
# ---------------------------------------------------------
st.sidebar.title("Portal Kas Sains Data 1A")
st.sidebar.markdown("UIN Salatiga | Transparansi & Manajemen Kas")

login_mode = st.sidebar.radio(
    "Pilih Akses Portal:",
    ["👤 Cek Personal", "📊 Cek Kas Kelas", "🔑 Portal Bendahara"]
)

# ---------------------------------------------------------
# 1. OPSI: CEK PERSONAL
# ---------------------------------------------------------
if login_mode == "👤 Cek Personal":
    st.title("👤 Portal Kas Personal Mahasiswa")
    st.markdown("Cek status pembayaran kas bulanan, akumulasi XP, lencana keaktifan, dan peringkat Anda.")

    selected_name = st.selectbox(
        "Pilih / Cari Nama Mahasiswa:",
        df["Nama"].tolist(),
        index=11  # Default nama Putri Titha Navidya
    )

    user_data = df[df["Nama"] == selected_name].iloc[0]

    # Hitung jumlah lunas & XP
    lunas_count = sum([1 for m in months if user_data[m] == "Lunas"])
    total_months = len(months)
    persen_lunas = (lunas_count / total_months) * 100
    xp = lunas_count * 250 + 100
    
    if lunas_count == 5:
        badge_kuning = "🟨 Lencana Kuning: Sempurna (5/5 Bulan)"
        badge_biru = "🟦 Lencana Biru: Terdisiplin (Level Tinggi)"
        badge
