import streamlit as st
import analytics

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Enterprise Insight AI",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("📊 Enterprise Insight AI")
st.markdown("### AI Powered Business Intelligence Platform")

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📊 Dashboard Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All", 2011, 2012, 2013, 2014]
)

selected_market = st.sidebar.selectbox(
    "Select Market",
    ["All", "APAC", "EU", "US", "LATAM", "EMEA", "Africa", "Canada"]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Enterprise Insight AI
    
    Version 1.0
    
    Developed using:
    - Python
    - SQLite
    - Streamlit
    - Plotly
    """
)

# ==========================================
# LOAD KPIs
# ==========================================

total_sales = analytics.total_sales().iloc[0]["total_sales"]
total_profit = analytics.total_profit().iloc[0]["total_profit"]
total_orders = analytics.total_orders().iloc[0]["total_orders"]
total_customers = analytics.total_customers().iloc[0]["customers"]

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.0f}")

with col3:
    st.metric("📦 Total Orders", f"{total_orders:,}")

with col4:
    st.metric("👥 Customers", f"{total_customers:,}")

import plotly.express as px
import analytics

st.divider()

st.subheader("📈 Monthly Sales Trend")

monthly = analytics.monthly_sales()

fig = px.line(
    monthly,
    x="month",
    y="total_sales",
    markers=True,
    title="Monthly Sales"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.subheader("🌍 Sales by Region")

region = analytics.sales_by_region()

fig = px.bar(
    region,
    x="region",
    y="total_sales",
    color="total_sales",
    title="Regional Sales"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.subheader("📦 Sales by Category")

category = analytics.sales_by_category()

fig = px.pie(
    category,
    names="category",
    values="total_sales",
    hole=0.45
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.subheader("🏆 Top 10 Countries")

country = analytics.sales_by_country()

fig = px.bar(
    country,
    x="country",
    y="total_sales",
    color="total_sales"
)

st.plotly_chart(fig, use_container_width=True)


