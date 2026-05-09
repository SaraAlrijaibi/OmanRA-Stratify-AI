import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="OmanRA-Stratify AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 OmanRA-Stratify AI")
st.subheader("AI Prototype for Rheumatoid Arthritis Endotyping and Personalized Therapy")

st.info("This is an academic prototype. It is not a diagnostic medical tool.")

col1, col2 = st.columns(2)

with col1:
    st.header("Patient Clinical Data")
    age = st.number_input("Age", min_value=0, max_value=100, value=45)
    das28 = st.number_input("DAS28 Score", min_value=0.0, max_value=10.0, value=5.6)
    symptoms = st.selectbox("Symptoms severity", ["Mild", "Moderate", "Severe"])

with col2:
    st.header("Laboratory Biomarkers")
    rf = st.number_input("RF", value=60.0)
    anti_ccp = st.number_input("anti-CCP", value=70.0)
    esr = st.number_input("ESR", value=35.0)
    crp = st.number_input("CRP", value=15.0)

st.header("Cytokines / Protein Markers")

c1, c2, c3, c4 = st.columns(4)

with c1:
    tnf = st.number_input("TNF-α", value=80.0)
with c2:
    il6 = st.number_input("IL-6", value=20.0)
with c3:
    il17 = st.number_input("IL-17", value=10.0)
with c4:
    gmcsf = st.number_input("GM-CSF", value=8.0)

if st.button("Generate AI Patient Report"):

    if tnf > 50:
        endotype = "TNF-dominant"
        therapy = "Anti-TNF biologic"
        response = "82%"
        biomarkers = "TNF-α, DAS28, CRP"

    elif il6 > 30 or crp > 10:
        endotype = "IL-6-dominant"
        therapy = "IL-6 receptor inhibitor"
        response = "78%"
        biomarkers = "IL-6, CRP, ESR"

    elif rf > 20 or anti_ccp > 20:
        endotype = "B-cell dominant"
        therapy = "Anti-CD20 therapy"
        response = "75%"
        biomarkers = "RF, anti-CCP, B-cell markers"

    elif il17 > 25 or gmcsf > 20:
        endotype = "JAK/IFN-high"
        therapy = "JAK inhibitor"
        response = "73%"
        biomarkers = "IL-17, GM-CSF, IFN-related markers"

    else:
        endotype = "Mixed / unclear endotype"
        therapy = "Further molecular testing recommended"
        response = "Not determined"
        biomarkers = "CRP, ESR, cytokine panel"

    risk_score = "High" if das28 >= 5.1 or crp > 10 else "Moderate"

    st.success("AI Report Generated Successfully")

    st.markdown("## Personalized Patient Report")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("RA Risk Score", risk_score)

    with r2:
        st.metric("Molecular Endotype", endotype)

    with r3:
        st.metric("Predicted Response", response)

    st.markdown("### Recommended Therapy")
    st.write(therapy)

    st.markdown("### Monitoring Biomarkers")
    st.write(biomarkers)

    st.markdown("### Clinical Interpretation")
    st.write(
        f"The patient shows a {endotype} profile. "
        f"Based on the entered biomarkers, the suggested personalized treatment is {therapy}. "
        f"Monitoring should focus on {biomarkers}."
    )

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef7ff 0%, #f8f3ff 45%, #ffffff 100%);
}

h1 {
    color: #12355B;
    text-align: center;
    font-size: 46px !important;
    font-weight: 800;
}

h2, h3 {
    color: #246A73;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

.stButton>button {
    background: linear-gradient(90deg, #246A73, #6A4C93);
    color: white;
    border-radius: 14px;
    height: 52px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1D4F57, #563A78);
    color: white;
}

[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #e6e6f0;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
}

.stNumberInput, .stSelectbox {
    background-color: white;
    border-radius: 12px;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

logo = Image.open("SQU-LOGO.png")

col1, col2 = st.columns([1,5])

with col1:
    st.image(logo, width=120)

with col2:
    st.title("🧬 OmanRA-Stratify AI")
    st.subheader("AI Prototype for Rheumatoid Arthritis Endotyping and Personalized Therapy")

