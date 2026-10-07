import sys
from pathlib import Path

import streamlit as st

# Add ShieldSense project root to Python path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model_evaluation.rules_baseline import classify_message


# ---------------------------------
# ShieldSense Interface
# ---------------------------------

st.set_page_config(
    page_title="ShieldSense",
    page_icon="🛡️",
    layout="centered"
)


st.title("🛡️ ShieldSense")
st.subheader("Accessible Scam-Message Screening")

st.write(
    "Enter an SMS or chat message below to check its potential scam risk."
)


# ---------------------------------
# Message input
# ---------------------------------

message = st.text_area(
    "Enter your message",
    placeholder="Paste or type a message here...",
    height=160
)


# ---------------------------------
# Check message
# ---------------------------------

if st.button("Check Message", type="primary"):

    if not message.strip():
        st.warning("Please enter a message before checking.")
    else:

        result = classify_message(message)

        risk = result["risk"]
        score = result["score"]
        reasons = result["reasons"]


        # ---------------------------------
        # Risk display
        # ---------------------------------

        if risk == "LOW":
            st.success("🟢 LOW RISK")

        elif risk == "MEDIUM":
            st.warning("🟠 MEDIUM RISK")

        else:
            st.error("🔴 HIGH RISK")


        st.write(f"**Risk level:** {risk}")
        st.write(f"**Risk score:** {score}")


        # ---------------------------------
        # Explanation
        # ---------------------------------

        st.markdown("### Why was this result given?")

        if reasons:
            for reason in reasons:
                st.write(f"• {reason}")
        else:
            st.write("• No scam indicators were detected.")


        # ---------------------------------
        # QA information
        # ---------------------------------

        with st.expander("Technical result"):
            st.json(result)