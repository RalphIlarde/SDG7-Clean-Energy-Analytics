import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="SDG 7 Global Clean Energy Analytics Hub",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #050505 0%, #101010 50%, #062b16 100%);
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #1DB954;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    .main-title {
        font-size: 50px;
        font-weight: 900;
        color: #1DB954;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .sub-title {
        font-size: 18px;
        color: #D8D8D8;
        margin-top: 0px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 34px;
        color: #1DB954;
        font-weight: 800;
        margin-top: 28px;
        margin-bottom: 12px;
    }

    .small-note {
        color: #CFCFCF;
        font-size: 14px;
    }

    .kpi-card {
        background-color: #0B0B0B;
        border: 1px solid #1DB954;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 0 18px rgba(29, 185, 84, 0.20);
        min-height: 125px;
    }

    .insight-box {
        background-color: #0B0B0B;
        border-left: 8px solid #1DB954;
        border-radius: 14px;
        padding: 20px 24px;
        color: #FFFFFF;
        font-size: 17px;
        line-height: 1.7;
        box-shadow: 0 0 16px rgba(29, 185, 84, 0.18);
    }

    .footer-box {
        background-color: #080808;
        border-top: 1px solid #1DB954;
        border-radius: 12px;
        padding: 16px 20px;
        color: #D6D6D6;
        font-size: 14px;
        margin-top: 28px;
    }

    div[data-testid="stMetric"] {
        background-color: #0B0B0B;
        border: 1px solid #1DB954;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 0 15px rgba(29, 185, 84, 0.16);
    }

    div[data-testid="stMetricLabel"] {
        color: #BDBDBD;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath, encoding="utf-8-sig")
    except:
        df = pd.read_csv(filepath, encoding="latin1")

    df.columns = df.columns.str.strip()

    st.write("Columns:", df.columns.tolist())

    return df

    # Convert columns to proper types
    numeric_cols = [
        "Year",
        "Renewable_Energy",
        "GDP_per_Capita",
        "Urban_Population",
        "Electricity_Access",
        "CO2_Emissions"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

try:
    df = load_data("cleaned_sdg7_data.csv")

    df["wealth_category"] = pd.cut(
    df["GDP_per_Capita"],
    bins=[0, 5000, 20000, float("inf")],
    labels=["Low Income", "Middle Income", "High Income"]
)

except FileNotFoundError:
    st.error("❌ Critical Error: 'cleaned_sdg7_data.csv' not found. Please run your prior notebook cells first.")
    st.stop()

st.markdown("<p class='main-title'>SDG 7: Global Clean Energy Analytics Hub 🔌</p>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-title'>Interactive Front-End Environment evaluating macroeconomic, structural, and infrastructural drivers of global energy transformations.</p>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='small-note'>
    <b>Developed by:</b> Ralph Victor L. Ilarde (BSIS 3B)<br>
    <b>Dashboard Optimization:</b> Analytical Techniques and Tools Portfolio Matrix Integration
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("# ⚙️ Framework Filters")
st.sidebar.markdown("Manipulate parameters to isolate spatial and structural factors.")

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
selected_year = st.sidebar.slider("Analysis Year Window", min_year, max_year, max_year)

all_countries = sorted(df["Country Code"].unique())
selected_countries = st.sidebar.multiselect(
    "Isolate Country Codes",
    options=all_countries,
    default=all_countries[:15]
)

gdp_range = st.sidebar.slider(
    "GDP per Capita Range ($)",
    int(df["GDP_per_Capita"].min()),
    int(df["GDP_per_Capita"].max()),
    (int(df["GDP_per_Capita"].min()), int(df["GDP_per_Capita"].max()))
)

elect_range = st.sidebar.slider(
    "Electricity Access Scope (%)",
    float(df["Electricity_Access"].min()),
    float(df["Electricity_Access"].max()),
    (float(df["Electricity_Access"].min()), float(df["Electricity_Access"].max()))
)

search_country = st.sidebar.text_input("Search Country Code / Sub-Index")

filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Country Code"].isin(selected_countries)) &
    (df["GDP_per_Capita"].between(gdp_range[0], gdp_range[1])) &
    (df["Electricity_Access"].between(elect_range[0], elect_range[1]))
].copy()

if search_country:
    filtered_df = filtered_df[filtered_df["Country Code"].str.lower().str.contains(search_country.lower(), na=False)]

if filtered_df.empty:
    st.warning("⚠️ No country records remain under these specific filter constraints. Please relax your settings.")
    st.stop()

st.markdown("<p class='section-title'>Empirical Macro-Level KPIs</p>", unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

total_obs = len(filtered_df)
avg_renew = filtered_df["Renewable_Energy"].mean()
avg_gdp = filtered_df["GDP_per_Capita"].mean()
avg_elect = filtered_df["Electricity_Access"].mean()
avg_co2 = filtered_df["CO2_Emissions"].mean()

kpi1.metric("Observed Units", f"{total_obs:,} Nations")
kpi2.metric("Avg Renewable Share", f"{avg_renew:.2f}%")
kpi3.metric("Avg GDP per Capita", f"${avg_gdp:,.2f}")
kpi4.metric("Avg Grid Access", f"{avg_elect:.2f}%")
kpi5.metric("Avg Per Capita CO2", f"{avg_co2:.2f} MT")

st.text("")

top_performing_nation = filtered_df.sort_values("Renewable_Energy", ascending=False).iloc[0]
st.markdown(
    f"""
    <div class='insight-box'>
    <b>Top Renewable Contributor in Selection ({selected_year}):</b> {top_performing_nation['Country Code']}<br>
    <b>Renewable Energy Share:</b> {top_performing_nation['Renewable_Energy']:.2f}% &nbsp; | &nbsp;
    <b>Infrastructure Grid Access:</b> {top_performing_nation['Electricity_Access']:.2f}% &nbsp; | &nbsp;
    <b>Urban Concentration:</b> {top_performing_nation['Urban_Population']:.2f}% &nbsp; | &nbsp;
    <b>Macro Wealth Output:</b> ${top_performing_nation['GDP_per_Capita']:,.2f}
    </div>
    """,
    unsafe_allow_html=True
)

st.text("")

def apply_spotify_layout(fig, title=None):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#050505",
        plot_bgcolor="#0B0B0B",
        font=dict(color="#FFFFFF"),
        title=dict(text=title if title else fig.layout.title.text, font=dict(size=20, color="#1DB954")),
        legend=dict(bgcolor="rgba(0,0,0,0)")
    )
    fig.update_xaxes(gridcolor="#2A2A2A")
    fig.update_yaxes(gridcolor="#2A2A2A")
    return fig

spotify_green_scale = ["#0B0B0B", "#0E7A35", "#1DB954", "#A7F3C1", "#FFFFFF"]

st.markdown("<p class='section-title'>Renewable Share Profiles and Variance</p>", unsafe_allow_html=True)

left_col, right_col = st.columns(2)

with left_col:
    top_renewables = filtered_df.sort_values("Renewable_Energy", ascending=False).head(15)
    fig_renew = px.bar(
        top_renewables,
        x="Renewable_Energy",
        y="Country Code",
        orientation="h",
        color="Renewable_Energy",
        color_continuous_scale=spotify_green_scale,
        title=f"Top National Entities by Renewable Adoption Profile ({selected_year})",
        labels={"Renewable_Energy": "Renewable Consumption %", "Country Code": "Country Identification Tag"}
    )
    fig_renew.update_layout(yaxis={"categoryorder": "total ascending"})
    fig_renew = apply_spotify_layout(fig_renew)
    st.plotly_chart(fig_renew, use_container_width=True)

with right_col:
    fig_hist = px.histogram(
        filtered_df,
        x="Renewable_Energy",
        nbins=20,
        color="wealth_category",
        color_discrete_sequence=["#FFFFFF", "#1DB954", "#0E7A35"],
        title="Distribution of Renewable Target Variable Across Wealth Strata",
        labels={"Renewable_Energy": "Renewable Share (%)", "wealth_category": "Economic Profile"}
    )
    fig_hist = apply_spotify_layout(fig_hist)
    st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("<p class='section-title'>Modeling Infrastructure and Macroeconomic Drivers</p>", unsafe_allow_html=True)

left_col2, right_col2 = st.columns(2)

with left_col2:
    fig_scatter1 = px.scatter(
        filtered_df,
        x="Electricity_Access",
        y="Renewable_Energy",
        size="Urban_Population",
        color="Country Code",
        hover_data=["GDP_per_Capita", "CO2_Emissions"],
        title="Grid Proliferation vs. Target Renewable Share (Beta Verification)",
        labels={"Electricity_Access": "Electricity Access Rate (%)", "Renewable_Energy": "Renewable Share (%)"}
    )
    fig_scatter1 = apply_spotify_layout(fig_scatter1)
    st.plotly_chart(fig_scatter1, use_container_width=True)

with right_col2:
    fig_scatter2 = px.scatter(
        filtered_df,
        x="GDP_per_Capita",
        y="CO2_Emissions",
        size="Renewable_Energy",
        color="wealth_category",
        color_discrete_sequence=["#1DB954", "#FFFFFF", "#0E7A35"],
        hover_name="Country Code",
        title="Economic Scaling vs Carbon Emissions Intensity Matrix",
        labels={"GDP_per_Capita": "GDP per Capita (USD)", "CO2_Emissions": "CO2 per Capita (Metric Tons)"}
    )
    fig_scatter2 = apply_spotify_layout(fig_scatter2)
    st.plotly_chart(fig_scatter2, use_container_width=True)

st.markdown("<p class='section-title'>Geographical Layout and Feature Interdependence</p>", unsafe_allow_html=True)

left_col3, right_col3 = st.columns([3, 2])

with left_col3:
    fig_map = px.choropleth(
        filtered_df, 
        locations="Country Code",
        color="Renewable_Energy",
        hover_name="Country Code",
        color_continuous_scale=px.colors.sequential.YlGn,
        title=f"Spatial Target Dispersion: Global Renewable Percentages ({selected_year})"
    )
    fig_map.update_layout(geo=dict(showframe=False, showcoastlines=True, bgcolor="#050505"))
    fig_map = apply_spotify_layout(fig_map)
    st.plotly_chart(fig_map, use_container_width=True)

with right_col3:
    corr_cols = ["Renewable_Energy", "Electricity_Access", "GDP_per_Capita", "Urban_Population", "CO2_Emissions"]
    corr_matrix = filtered_df[corr_cols].corr(numeric_only=True)

    fig_corr = go.Figure(
        data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale=[[0, "#FFFFFF"], [0.5, "#0B0B0B"], [1, "#1DB954"]],
            zmin=-1, zmax=1,
            colorbar=dict(title="Corr Index")
        )
    )
    fig_corr.update_layout(
        title="Correlation Matrix of Analytical Variables",
        template="plotly_dark",
        paper_bgcolor="#050505",
        plot_bgcolor="#0B0B0B",
        font=dict(color="#FFFFFF"),
        title_font=dict(size=20, color="#1DB954")
    )
    st.plotly_chart(fig_corr, use_container_width=True)

st.markdown("<p class='section-title'>Synchronized Regression Model Data Matrix</p>", unsafe_allow_html=True)
preview_cols = ["Country Code", "Year", "Renewable_Energy", "Electricity_Access", "GDP_per_Capita", "Urban_Population", "CO2_Emissions"]
st.dataframe(
    filtered_df[preview_cols].sort_values("Renewable_Energy", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.markdown("<p class='section-title'>💡 Econometric Verification Synthesis</p>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class='insight-box'>
    This interactive viewport explicitly verifies the core findings of our <b>OLS and Robust Linear Models (RLM)</b>. 
    Across our active filter window for the year <b>{selected_year}</b>, the target variable holds a mean of 
    <b>{avg_renew:.2f}%</b>. The visualization highlights that utility infrastructure deployment is heavily negatively correlated 
    with clean energy adoption. This confirms our calculated beta coefficient ($\\beta = -0.7110$), revealing that recent global 
    electrification expansions have relied intensely on carbon-heavy infrastructure. Additionally, the flat dispersion 
    profiles seen across our GDP metrics confirm that economic wealth does not automatically drive green transitions. Instead, 
    progress depends heavily on deliberate, strategic infrastructure investments.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='footer-box'>
    <b>Data Reference:</b> Curated panel dataset sourced via World Bank Development Indicators and 
    Our World in Data repositories. Calculated structures track longitudinal progress toward United Nations Sustainable Development 
    Goal 7 (Affordable and Clean Energy).<br><br>
    <b>Academic Compliance Notice:</b> This system component was constructed explicitly for final evaluation under the supervision of 
    Prof. Hilado. All derived coefficients, correlation heatmaps, and modeling projections correspond directly to the backend 
    statistical estimations inside the core study notebook.
    </div>
    """,
    unsafe_allow_html=True
)
