# =========================================
# FILE: app.py
# =========================================

import streamlit as st
import os

import zipfile
import shutil

from agent_main import run_agents

from core.workspace_manager import (
    reset_workspace
)

st.set_page_config(
    page_title="AI WhatsApp Automation",
    layout="wide"
)

st.title(
    "🤖 AI WhatsApp Order Automation"
)

# ----------------------------------------
# UPLOAD CHAT
# ----------------------------------------

uploaded_zip = st.file_uploader(
    "Upload WhatsApp Export ZIP",
    type=["zip"]
)

# ----------------------------------------
# PROCESS BUTTON
# ----------------------------------------

if st.button("🚀 Process Orders"):

    # ----------------------------------------
    # RESET WORKSPACE
    # ----------------------------------------

    reset_workspace()

    # ----------------------------------------
    # SAVE ZIP FILE
    # ----------------------------------------

    zip_path = ("data/whatsapp_export/export.zip")

    with open(zip_path, "wb") as f:

        f.write(uploaded_zip.getbuffer())

    # ----------------------------------------
    # UNZIP FILES
    # ----------------------------------------

    with zipfile.ZipFile(
        zip_path,
        "r"
    ) as zip_ref:

        zip_ref.extractall("data/whatsapp_export")

    st.success("✅ ZIP extracted")

    # ----------------------------------------
    # RUN AGENT WORKFLOW
    # ----------------------------------------

    with st.spinner("🤖 AI Agent processing..."):

        result = run_agents()

    st.success("✅ Workflow completed")

    st.write(result)

    # ----------------------------------------
    # DOWNLOAD FILES
    # ----------------------------------------

    if os.path.exists("output/orders.xlsx"):

        st.download_button(
            "📥 Download Orders",

            open(
                "output/orders.xlsx",
                "rb"
            ),

            file_name="orders.xlsx"
        )

    if os.path.exists("output/report.xlsx"):

        st.download_button(
            "📥 Download Report",

            open(
                "output/report.xlsx",
                "rb"
            ),

            file_name="report.xlsx"
        )