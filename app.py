
import streamlit as st

st.set_page_config(page_title="OmanRA-Stratify AI")

st.title("OmanRA-Stratify AI")
st.subheader("Precision Medicine Prototype for Rheumatoid Arthritis")

st.write("Enter patient biomarkers:")

age = st.number_input("Age")
das28 = st.number_input("DAS28 Score")
rf = st.number_input("RF")
anti_ccp = st.number_input("anti-CCP")
crp = st.number_input("CRP")
tnf = st.number_input("TNF-α")
il6 = st.number_input("IL-6")

if st.button("Predict Endotype"):

    if tnf > 50:
        endotype = "TNF-dominant"
        therapy = "anti-TNF biologic"

    elif il6 > 30 or crp > 10:
        endotype = "IL-6-dominant"
        therapy = "IL-6 receptor inhibitor"

    elif rf > 20 or anti_ccp > 20:
        endotype = "B-cell dominant"
        therapy = "anti-CD20 therapy"

    else:
        endotype = "Mixed/Unclear"
        therapy = "Further molecular testing"

    st.success("Prediction Complete")

    st.write("## Personalized Patient Report")
    st.write(f"### Molecular Endotype: {endotype}")
    st.write(f"### Recommended Therapy: {therapy}")
    st.write("### Predicted Response: 78%")
    st.write("### Monitoring Biomarkers: CRP, ESR, TNF-α")
