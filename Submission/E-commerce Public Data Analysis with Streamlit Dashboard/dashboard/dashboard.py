import streamlit as st
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import altair as alt

st.set_page_config(page_title="Dashboard E-Commerce", page_icon="📊", layout="wide")

# ========== INISIALISASI SESSION ==========
if "user_name" not in st.session_state:
    st.session_state.user_name = None  
if "show_form" not in st.session_state:
    st.session_state.show_form = False  
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False  

# ========== FORM AWAL (LANDING PAGE) ==========
if not st.session_state.user_name:
    placeholder = st.empty()

    with placeholder.container():
        header = Image.open('dashboard/assets/image/header.png')
        st.image(header)
        st.title("E-Commerce Performance Tracker: :blue[Best-Selling Products & Seller Efficiency]")
        st.write("Username Dicoding: @shendyeff")

        col1, col2, col3 = st.columns([1, 0.5, 1])  
        with col2:
            if st.button("🚀 Go to Dashboard", use_container_width=True):
                st.session_state.show_form = True  
                st.rerun()

    st.markdown("<style>[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

# ========== POP-UP INPUT NAMA ==========
if st.session_state.show_form and not st.session_state.user_name:
    @st.dialog("🎉 Selamat Datang!")
    def get_name():
        st.write("Silakan masukkan nama kamu terlebih dahulu!")
        name = st.text_input("Nama Anda", key="user_name_input")

        if st.button("Masuk"):
            if name.strip():
                st.session_state.user_name = name.strip()
                st.session_state.welcome_shown = False  
                st.rerun()
            else:
                st.warning("Silakan isi nama terlebih dahulu!")

    get_name()

# ========== DASHBOARD CONTENT ==========
if st.session_state.user_name:
    st.title(f"📊 Dashboard Analytics")
    st.header(f"Halo {st.session_state.user_name}! Welcome to Dashboard! 🚀")

    if not st.session_state.welcome_shown:
        st.toast(f"Selamat datang, {st.session_state.user_name}! 🎉")
        time.sleep(0.5)
        st.toast("Semoga harimu menyenangkan! ☀️")
        time.sleep(0.5)
        st.toast("Ayo jelajahi dashboard ini!", icon="🚀")
        st.session_state.welcome_shown = True  

    @st.cache_data
    def load_data():
        df = pd.read_csv("dashboard/main_data_cleaned.csv")  
        df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
        df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"], errors='coerce')
        return df

    df = load_data()

    # ========== SIDEBAR: NAVIGASI ==========
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Navigasi", ["📊 Overview", "📈 Exploratory Data Analysis", "🛍️ RFM Analysis", "⚙️ Settings"])
    
    # ========== HALAMAN OVERVIEW ==========
    if page == "📊 Overview":
        st.subheader("📊 Ringkasan Penjualan")

        # **FILTER TANGGAL ADA DI SINI (BUKAN SIDEBAR LAGI)**
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Tanggal Awal", df["order_purchase_timestamp"].min(), key="start_date")
        with col2:
            end_date = st.date_input("Tanggal Akhir", df["order_purchase_timestamp"].max(), key="end_date")

        filtered_df = df[(df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) & 
                         (df["order_purchase_timestamp"] <= pd.to_datetime(end_date))]

        if "order_delivered_customer_date" in filtered_df.columns:
            filtered_df["delivery_time"] = (filtered_df["order_delivered_customer_date"] - 
                                            filtered_df["order_purchase_timestamp"]).dt.days
        else:
            filtered_df["delivery_time"] = None

        # ========== METRIC CARDS ==========
        col1, col2, col3 = st.columns(3, gap="small")

        with col1:
            total_orders = filtered_df["order_id"].nunique()  
            st.info('📦 Total Penjualan')
            st.metric(label="Total Orders", value=f"{total_orders:,}")

        with col2:
            total_revenue = filtered_df["payment_value"].sum()
            st.info('💰 Total Revenue')
            st.metric(label="Revenue (BRL)", value=f"R$ {total_revenue:,.0f}")

        with col3:
            avg_delivery_time = filtered_df["delivery_time"].mean() if not filtered_df["delivery_time"].isna().all() else None
            st.info('🚚 Rata-rata Waktu Pengiriman')
            st.metric(label="Avg Delivery (Days)", value=f"{avg_delivery_time:.1f} Hari" if avg_delivery_time else "N/A")

        # ========== CHART: TOP 5 KATEGORI PRODUK ==========
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("🏆 Top 5 Kategori Produk dengan Penjualan Tertinggi"):
                if "product_category_name" in filtered_df.columns:
                    top_categories = filtered_df["product_category_name"].value_counts().head(5)

                    fig, ax = plt.subplots(figsize=(6, 4))
                    top_categories.sort_values().plot(kind="barh", color="#1f77b4", ax=ax)
                    ax.set_xlabel("Jumlah Penjualan")
                    ax.set_ylabel("Kategori Produk")
                    ax.set_title("Top 5 Kategori Produk")
                    st.pyplot(fig)
                else:
                    st.warning("⚠️ Data kategori produk tidak tersedia.")

        # ========== CHART: TOP 5 SELLER PENGIRIMAN TERCEPAT ==========
        with col2:
            with st.expander("⚡ Top 5 Seller dengan Pengiriman Tercepat"):
                if "delivery_time" in filtered_df.columns and "seller_id" in filtered_df.columns:
                    top_sellers = filtered_df.groupby("seller_id")["delivery_time"].mean().nsmallest(5)

                    fig, ax = plt.subplots(figsize=(6, 4.8))
                    top_sellers.sort_values().plot(kind="barh", color="#ff7f0e", ax=ax)
                    ax.set_xlabel("Rata-rata Waktu Pengiriman (Hari)")
                    ax.set_ylabel("Seller ID")
                    ax.set_title("Top 5 Seller dengan Pengiriman Tercepat")
                    st.pyplot(fig)
                else:
                    st.warning("⚠️ Data seller atau waktu pengiriman tidak tersedia.")


        # ========== LINE CHART: TREND PENJUALAN ==========
        with st.expander("📈 Tren Penjualan per Bulan"):
            filtered_df["order_month"] = filtered_df["order_purchase_timestamp"].dt.to_period("M")
            sales_trend = filtered_df.groupby("order_month")["order_id"].count()

            fig, ax = plt.subplots(figsize=(10, 5))
            sales_trend.plot(kind="line", marker="o", color="#2ca02c", ax=ax)
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah Penjualan")
            ax.set_title("Tren Penjualan per Bulan")
            ax.grid()
            st.pyplot(fig)
    
    # ========== Exploratory Data Analysis ==========  
    elif page == "📈 Exploratory Data Analysis":
        st.subheader("📊 Exploratory Data Analysis (EDA)")

        # ========== 1. Statistik Deskriptif ==========
        with st.expander("Statistik Deskriptif"):
            numeric_columns = df.select_dtypes(include=[np.number]).columns
            descriptive_stats = df[numeric_columns].describe()
            st.dataframe(descriptive_stats)

        # ========== 2. Distribusi Penjualan & Revenue ==========
        with st.expander("Distribusi Penjualan & Revenue"):
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            sns.histplot(df['order_item_id'], bins=30, kde=True, color='skyblue', ax=axes[0])
            axes[0].set_title('Distribusi Jumlah Transaksi')
            axes[0].set_xlabel('Jumlah Transaksi')

            sns.histplot(df['payment_value'], bins=30, kde=True, color='salmon', ax=axes[1])
            axes[1].set_title('Distribusi Revenue')
            axes[1].set_xlabel('Revenue (BRL)')

            plt.tight_layout()
            st.pyplot(fig)

        # ========== 3. Heatmap Korelasi ==========
        with st.expander("Heatmap Korelasi Antar Fitur Numerik"):
            numeric_data = df.select_dtypes(include=['number'])
            correlation_matrix = numeric_data.corr()

            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, ax=ax)
            ax.set_title("Heatmap Korelasi Antar Fitur Numerik", fontsize=14)
            st.pyplot(fig)

        # ========== 4. Distribusi Kategori ==========
        with st.expander("Distribusi Data Kategori"):
            fig, axes = plt.subplots(2, 2, figsize=(14, 10))

            top_categories = df['product_category_name'].value_counts().head(10)
            sns.barplot(x=top_categories.values, y=top_categories.index, hue=top_categories.index, palette="Blues_r", legend=False, ax=axes[0, 0])
            axes[0, 0].set_title("Top 10 Kategori Produk Terlaris")

            payment_methods = df['payment_type'].value_counts()
            sns.barplot(x=payment_methods.index, y=payment_methods.values, hue=payment_methods.index, palette="Purples_r", legend=False, ax=axes[0, 1])
            axes[0, 1].set_title("Distribusi Metode Pembayaran")

            order_status = df['order_status'].value_counts()
            sns.barplot(x=order_status.index, y=order_status.values, hue=order_status.index, palette="Oranges_r", legend=False, ax=axes[1, 0])
            axes[1, 0].set_title("Distribusi Status Pesanan")

            review_scores = df['review_score'].value_counts().sort_index()
            sns.barplot(x=review_scores.index, y=review_scores.values, hue=review_scores.index, palette="Greens_r", legend=False, ax=axes[1, 1])
            axes[1, 1].set_title("Distribusi Skor Ulasan")

            plt.tight_layout()
            st.pyplot(fig)


    elif page == "🛍️ RFM Analysis":
        st.subheader("🛍️ RFM Analysis")
        
        # Filter Tanggal di dalam menu RFM
        st.subheader("Pilih Rentang Tanggal untuk Analisis RFM")

        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Tanggal Awal", df["order_purchase_timestamp"].min(), key="start_date")
        with col2:
            end_date = st.date_input("Tanggal Akhir", df["order_purchase_timestamp"].max(), key="end_date")

        # Validasi Tanggal
        if start_date > end_date:
            st.warning("Tanggal mulai tidak boleh lebih besar dari tanggal akhir!")

        # Filter data berdasarkan rentang tanggal
        filtered_df = df[(df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) & 
                        (df['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

        if filtered_df.empty:
            st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")
        else:
            # Menghitung RFM jika belum dihitung
            reference_date = filtered_df['order_purchase_timestamp'].max()
            rfm = filtered_df.groupby('customer_unique_id').agg({
                'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,  # Recency
                'order_id': 'count',
                'payment_value': 'sum'
            }).reset_index()

            rfm.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']

            # Menampilkan distribusi Recency, Frequency, dan Monetary
            st.subheader("Distribusi Recency, Frequency, dan Monetary")

            # Expander untuk Recency
            with st.expander("Distribusi Recency"):
                recency_chart = alt.Chart(rfm).mark_bar().encode(
                    x=alt.X('Recency', bin=alt.Bin(maxbins=30), title='Recency (Hari sejak transaksi terakhir)'),
                    y='count()',
                    color=alt.Color('Recency', scale=alt.Scale(scheme='blues')),
                    tooltip=['Recency', 'count()']
                ).properties(title='Distribusi Recency')
                st.altair_chart(recency_chart, use_container_width=True)

            # Expander untuk Frequency
            with st.expander("Distribusi Frequency"):
                frequency_chart = alt.Chart(rfm).mark_bar().encode(
                    x=alt.X('Frequency', bin=alt.Bin(maxbins=30), title='Frequency (Jumlah Transaksi)'),
                    y='count()',
                    color=alt.Color('Frequency', scale=alt.Scale(scheme='greens')),
                    tooltip=['Frequency', 'count()']
                ).properties(title='Distribusi Frequency')
                st.altair_chart(frequency_chart, use_container_width=True)

            # Expander untuk Monetary
            with st.expander("Distribusi Monetary"):
                monetary_chart = alt.Chart(rfm).mark_bar().encode(
                    x=alt.X('Monetary', bin=alt.Bin(maxbins=30), title='Monetary (Total Pengeluaran dalam BRL)'),
                    y='count()',
                    color=alt.Color('Monetary', scale=alt.Scale(scheme='oranges')),
                    tooltip=['Monetary', 'count()']
                ).properties(title='Distribusi Monetary')
                st.altair_chart(monetary_chart, use_container_width=True)

            # Visualisasi Top 5 Pelanggan Paling Aktif (Recency Rendah) dan Lama Tidak Bertransaksi (Recency Tinggi)
            top_recency = rfm.nsmallest(5, 'Recency')
            worst_recency = rfm.nlargest(5, 'Recency')

            st.subheader("Top 5 Pelanggan Berdasarkan Recency")

            # Expander untuk Top 5 Pelanggan Paling Aktif
            with st.expander("Top 5 Pelanggan Paling Aktif (Recency Rendah)"):
                active_customers_chart = alt.Chart(top_recency).mark_bar().encode(
                    y=alt.Y('customer_unique_id', sort='-x', title='Customer ID'),
                    x='Recency',
                    color=alt.Color('Recency', scale=alt.Scale(scheme='blues')),
                    tooltip=['customer_unique_id', 'Recency']
                ).properties(title='Top 5 Pelanggan Paling Aktif (Recency Rendah)')
                st.altair_chart(active_customers_chart, use_container_width=True)

            # Expander untuk Top 5 Pelanggan Lama Tidak Bertransaksi
            with st.expander("Top 5 Pelanggan Lama Tidak Bertransaksi (Recency Tinggi)"):
                inactive_customers_chart = alt.Chart(worst_recency).mark_bar().encode(
                    y=alt.Y('customer_unique_id', sort='-x', title='Customer ID'),
                    x='Recency',
                    color=alt.Color('Recency', scale=alt.Scale(scheme='reds')),
                    tooltip=['customer_unique_id', 'Recency']
                ).properties(title='Top 5 Pelanggan Lama Tidak Bertransaksi (Recency Tinggi)')
                st.altair_chart(inactive_customers_chart, use_container_width=True)

            # Expander untuk Top 5 Pelanggan Paling Sering Bertransaksi
            with st.expander("Top 5 Pelanggan Paling Sering Bertransaksi"):
                top_frequency = rfm.nlargest(5, 'Frequency')
                frequency_customers_chart = alt.Chart(top_frequency).mark_bar().encode(
                    y=alt.Y('customer_unique_id', sort='-x', title='Customer ID'),
                    x='Frequency',
                    color=alt.Color('Frequency', scale=alt.Scale(scheme='greens')),
                    tooltip=['customer_unique_id', 'Frequency']
                ).properties(title='Top 5 Pelanggan Paling Sering Bertransaksi')
                st.altair_chart(frequency_customers_chart, use_container_width=True)

            # Expander untuk Top 5 Pelanggan dengan Pengeluaran Tertinggi
            with st.expander("Top 5 Pelanggan dengan Pengeluaran Tertinggi"):
                top_monetary = rfm.nlargest(5, 'Monetary')
                monetary_customers_chart = alt.Chart(top_monetary).mark_bar().encode(
                    y=alt.Y('customer_unique_id', sort='-x', title='Customer ID'),
                    x='Monetary',
                    color=alt.Color('Monetary', scale=alt.Scale(scheme='oranges')),
                    tooltip=['customer_unique_id', 'Monetary']
                ).properties(title='Top 5 Pelanggan dengan Pengeluaran Tertinggi')
                st.altair_chart(monetary_customers_chart, use_container_width=True)




        
        

    
    elif page == "⚙️ Settings":
        st.subheader("⚙️ Pengaturan")

        # Tema (Light/Dark)
        st.write("### Pilih Tema")
        theme = st.radio("Pilih Tema", ("Terang", "Gelap"))
        if theme == "Gelap":
            st.session_state.theme = "dark"
            st.markdown(
                """
                <style>
                    .css-18e3th9 {
                        background-color: #121212;
                        color: white;
                    }
                    .css-18e3th9 .stButton>button {
                        background-color: #333;
                        color: white;
                    }
                </style>
                """, unsafe_allow_html=True)
        else:
            st.session_state.theme = "light"
            st.markdown(
                """
                <style>
                    .css-18e3th9 {
                        background-color: #FFFFFF;
                        color: black;
                    }
                    .css-18e3th9 .stButton>button {
                        background-color: #f0f0f0;
                        color: black;
                    }
                </style>
                """, unsafe_allow_html=True)
        
        # Pilih Bahasa
        st.write("### Pilih Bahasa")
        language = st.selectbox("Pilih Bahasa untuk Tampilan", ["Indonesia", "English"])
        st.session_state.language = language

        if language == "Indonesia":
            st.write("Bahasa Indonesia dipilih")
        else:
            st.write("English is selected")
        
        # Format Tanggal
        st.write("### Pilih Format Tanggal")
        date_format = st.selectbox("Pilih Format Tanggal", ["YYYY-MM-DD", "DD-MM-YYYY", "MM-DD-YYYY"])
        st.session_state.date_format = date_format
        st.write(f"Format tanggal yang dipilih: {date_format}")

        # Notifikasi
        st.write("### Pengaturan Notifikasi")
        notification = st.checkbox("Aktifkan Notifikasi", value=True)
        st.session_state.notifications = notification
        if notification:
            st.write("Notifikasi diaktifkan!")
        else:
            st.write("Notifikasi dimatikan.")

        # Logout Button
        st.write("### Logout")
        if st.button("Logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]  
            st.rerun()

        # Feedback Pengguna
        st.write("### Feedback Pengguna")
        feedback = st.text_area("Tulis umpan balik atau saran di sini:")
        if feedback:
            st.write("Terima kasih atas umpan balik Anda!")

