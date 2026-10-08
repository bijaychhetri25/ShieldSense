

import sys
from pathlib import Path

import streamlit as st

# Add ShieldSense project root to Python path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model_evaluation.rules_baseline import classify_message
from model_evaluation.ml_predictor import predict_message


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

st.caption(
    "Prototype screening tool. Results are not a guarantee "
    "that a message is safe or fraudulent."
)


# ---------------------------------
# Message input
# ---------------------------------

message = st.text_area(
    "Enter your message",
    placeholder="Paste or type a message here...",
    height=160
)

model_choice = st.radio(
    "Choose detection model",
    ["Rules-Based Baseline", "Machine Learning"],
    horizontal=True
)


# ---------------------------------
# Check message
# ---------------------------------

if st.button("Check Message", type="primary"):

    if not message.strip():
        st.warning("Please enter a message before checking.")

    else:
        if model_choice == "Machine Learning":
            result = predict_message(message)
        else:
            result = classify_message(message)

        risk = result["risk"]
        score = result.get("score")
        reasons = result.get("reasons", [])

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

        if model_choice == "Machine Learning":
            st.write(
                f"**Model confidence:** {result['confidence']:.2f}%"
            )
            st.caption(
                "Confidence is a model estimate, "
                "not a guarantee of accuracy."
            )
        else:
            st.write(f"**Risk score:** {score}")

        # ---------------------------------
        # Explanation
        # ---------------------------------

        st.markdown("### Why was this result given?")

        if model_choice == "Machine Learning":
            st.info(
                "This prediction uses patterns learned from "
                "the training messages. Detailed explanations "
                "are not yet available for this model."
            )

        elif reasons:
            for reason in reasons:
                st.write(f"• {reason}")

        else:
            st.write("• No rule-based scam indicators were detected.")

        # ---------------------------------
        # QA information
        # ---------------------------------

        with st.expander("Technical result"):
            st.json(result)
