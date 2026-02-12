import streamlit as st
import pandas as pd
from io import BytesIO

# Page Config
st.set_page_config(page_title="Plaza Operations Report", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Report')
    return output.getvalue()

st.sidebar.title("Navigation")
menu = [
    "Plaza Wise Details", 
    "Boom Arm Order & Requirements", 
    "Other Material Requirements", 
    "Internet Details", 
    "Biometric", 
    "NVR Details"
]
choice = st.sidebar.radio("Select Section", menu)

# --- 1. PLAZA WISE DETAILS ---
if choice == "Plaza Wise Details":
    st.header("🏢 Category Wise - Plaza Wise Details")
    with st.form("plaza_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            p_name = st.text_input("Plaza Name")
            t_date = st.date_input("Take Over Date")
            h_date = st.date_input("Hand Over Date")
        with c2:
            l_total = st.number_input("No of Lanes", min_value=0)
            l_work = st.number_input("No of Lanes Working", min_value=0)
            l_not = st.number_input("No of Lanes Not Working", min_value=0)
        with c3:
            hhmsi = st.text_input("No. of HHMSI Name")
            bank = st.text_input("Bank Name")
            contact = st.text_input("Contact Name")
            mobile = st.text_input("Mobile No.")
        
        st.subheader("SI Details")
        sc1, sc2 = st.columns(2)
        with sc1:
            si_mgr = st.text_area("SI Reporting Manager Contact Details")
        with sc2:
            si_name = st.text_input("SI Contact Name")
            si_mob = st.text_input("SI Mobile No.")
            
        if st.form_submit_button("Generate Plaza Excel"):
            df = pd.DataFrame([{
                "Plaza Name": p_name, "Take Over": t_date, "Hand Over": h_date,
                "Lanes": l_total, "Working": l_work, "Not Working": l_not,
                "HHMSI": hhmsi, "Bank": bank, "Contact": contact, "Mobile": mobile,
                "SI Manager": si_mgr, "SI Contact": si_name, "SI Mobile": si_mob
            }])
            st.download_button("Download Report", data=to_excel(df), file_name="Plaza_Details.xlsx")

# --- 2. BOOM ARM DETAILS ---
elif choice == "Boom Arm Order & Requirements":
    st.header("🏗️ Boom Arm Order and Requirement Details")
    # Data editor allows adding multiple rows at once
    df_template = pd.DataFrame(columns=[
        "Plaza Name", "Request By", "Address", "Quantity", "Size", 
        "UTR Amount", "Approved By", "LLR Number", "Received By", "Vendor Details", "Images Link"
    ])
    edited_df = st.data_editor(df_template, num_rows="dynamic")
    if st.button("Export Boom Arm Report"):
        st.download_button("Download Excel", data=to_excel(edited_df), file_name="Boom_Arm_Report.xlsx")

# --- 3. OTHER MATERIALS ---
elif choice == "Other Material Requirements":
    st.header("📦 Other Material Required Details")
    df_mat = pd.DataFrame(columns=[
        "Plaza Name", "Request By", "Material Name", "Address", "Quantity", 
        "Size", "UTR Amount", "Approved By", "LLR Number", "Received By", "Vendor Details"
    ])
    edited_mat = st.data_editor(df_mat, num_rows="dynamic")
    if st.button("Export Material Report"):
        st.download_button("Download Excel", data=to_excel(edited_mat), file_name="Material_Requirements.xlsx")

# --- 4. INTERNET DETAILS ---
elif choice == "Internet Details":
    st.header("🌐 Internet Details")
    st.info("Primary and Secondary connection details")
    df_net = pd.DataFrame(columns=[
        "Plaza Name", "Internet Supplied", "Internet Speed (P/S)", 
        "Bill Paid By", "Static IP (P/S)", "Date of Billing", 
        "Primary Bill (M/Q/H/Y)", "Secondary Bill (M/Q/H/Y)"
    ])
    edited_net = st.data_editor(df_net, num_rows="dynamic")
    if st.button("Export Internet Report"):
        st.download_button("Download Excel", data=to_excel(edited_net), file_name="Internet_Report.xlsx")

# --- 5. BIOMETRIC ---
elif choice == "Biometric":
    st.header("👤 Biometric Details")
    df_bio = pd.DataFrame(columns=[
        "Plaza Name", "Biometric Make", "Model", "Serial Number", 
        "Device IP", "Quantity", "Working", "Non-Working", "Connected with Server"
    ])
    edited_bio = st.data_editor(df_bio, num_rows="dynamic")
    if st.button("Export Biometric Report"):
        st.download_button("Download Excel", data=to_excel(edited_bio), file_name="Biometric_Report.xlsx")

# --- 6. NVR DETAILS ---
elif choice == "NVR Details":
    st.header("📹 NVR Details")
    df_nvr = pd.DataFrame(columns=[
        "Plaza Name", "NVR Make", "NVR Model", "NVR Channel", 
        "No of Days Backup", "NVR Storage", "Online Status", 
        "NVR Static IP", "Username", "Password", "Reason for Offline"
    ])
    edited_nvr = st.data_editor(df_nvr, num_rows="dynamic")
    if st.button("Export NVR Report"):
        st.download_button("Download Excel", data=to_excel(edited_nvr), file_name="NVR_Report.xlsx")