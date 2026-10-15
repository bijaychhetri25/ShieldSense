

import sys
import re
import html
from pathlib import Path
from datetime import datetime

import streamlit as st

# ==========================================
# PROJECT SETUP
# ==========================================

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="ShieldSense | Scam Protection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# LOAD EXISTING DETECTION MODELS
# ==========================================

try:
    from model_evaluation.rules_baseline import classify_message
    RULES_ERROR = None
except Exception as exc:
    classify_message = None
    RULES_ERROR = str(exc)

try:
    from model_evaluation.ml_predictor import predict_message
    ML_ERROR = None
except Exception as exc:
    predict_message = None
    ML_ERROR = str(exc)

# ==========================================
# SESSION STATE
# ==========================================

if "scan_history" not in st.session_state:
    st.session_state.scan_history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
:root {
    color-scheme: dark;
}

.stApp {
    background:
        radial-gradient(
            ellipse at 85% 0%,
            rgba(91, 68, 185, 0.22),
            transparent 42%
        ),
        radial-gradient(
            ellipse at 5% 30%,
            rgba(0, 150, 210, 0.12),
            transparent 45%
        ),
        #080e20;
    color: #f1f5ff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

[data-testid="stSidebar"] {
    background: #101a32;
    border-right: 1px solid #263654;
}

[data-testid="stSidebar"] * {
    color: #f1f5ff;
}

h1, h2, h3 {
    color: #f5f8ff !important;
}

p, label {
    color: #d7e2f5;
}

.hero {
    padding: 30px;
    border: 1px solid #30486c;
    border-radius: 22px;
    background: linear-gradient(
        115deg,
        #13294d 0%,
        #182347 55%,
        #31205c 100%
    );
    margin-bottom: 22px;
}

.hero-title {
    font-size: clamp(2rem, 4vw, 3.1rem);
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 10px;
    line-height: 1.2;
}

.hero-subtitle {
    color: #d5e5ff;
    font-size: 1.05rem;
    max-width: 680px;
    line-height: 1.7;
}

.eyebrow {
    color: #9edcff;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.panel {
    background: #121e37;
    border: 1px solid #2c405e;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.panel-title {
    font-size: 1.2rem;
    font-weight: 750;
    color: #f4f8ff;
    margin-bottom: 10px;
}

.panel-copy {
    color: #b9cbe5;
    line-height: 1.6;
}

.stat-card {
    padding: 22px;
    background: #13213c;
    border: 1px solid #2a4264;
    border-radius: 17px;
    margin-bottom: 14px;
}

.stat-number {
    color: #ffffff;
    font-size: 2rem;
    font-weight: 800;
}

.stat-label {
    color: #b7c9e4;
    font-size: 0.9rem;
    margin-top: 5px;
}

.risk-card {
    padding: 25px;
    border-radius: 18px;
    margin-top: 16px;
    margin-bottom: 20px;
}

.risk-green {
    background: #102d29;
    border: 2px solid #35d5a0;
}

.risk-amber {
    background: #392b17;
    border: 2px solid #f4b84b;
}

.risk-red {
    background: #391c29;
    border: 2px solid #ff697d;
}

.risk-heading {
    font-size: 1.5rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}

.risk-description {
    color: #f1f5ff;
    line-height: 1.7;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        100deg,
        #2774f5,
        #7850e8
    );
    color: white;
    border: none;
    border-radius: 11px;
    font-weight: 700;
    min-height: 48px;
}

.stButton > button {
    border-radius: 11px;
    min-height: 42px;
}

.stTextArea textarea {
    background: #121d34 !important;
    color: #ffffff !important;
    border: 1px solid #4b6487 !important;
    border-radius: 12px !important;
}

.stTextArea textarea:focus {
    border: 2px solid #7dbdff !important;
}

[data-testid="stMetric"] {
    background: #14223d;
    border: 1px solid #304667;
    padding: 18px;
    border-radius: 14px;
}

[data-testid="stMetricValue"] {
    color: #ffffff;
}

a {
    color: #9fd8ff !important;
}

*:focus-visible {
    outline: 3px solid #91d5ff !important;
    outline-offset: 3px;
}

@media (max-width: 700px) {
    .hero {
        padding: 20px;
    }

    .stat-card {
        padding: 16px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# RESULT NORMALISATION
# ==========================================

def risk_from_value(value):
    """
    Convert common model labels into Green, Amber or Red.
    Return None when the format is unknown.
    """
    if value is None:
        return None

    if isinstance(value, bool):
        return "Red" if value else "Green"

    if isinstance(value, (int, float)):
        if value == 0:
            return "Green"
        if value == 1:
            return "Red"
        return None

    text = str(value).strip().lower()

    green = {
        "green", "low", "low risk", "safe",
        "legitimate", "ham", "benign", "normal",
        "not scam", "not spam"
    }

    amber = {
        "amber", "yellow", "medium",
        "medium risk", "moderate",
        "suspicious", "review", "uncertain"
    }

    red = {
        "red", "high", "high risk",
        "scam", "spam", "fraud",
        "fraudulent", "phishing", "malicious"
    }

    if text in green:
        return "Green"

    if text in amber:
        return "Amber"

    if text in red:
        return "Red"

    return None


def normalise_result(raw):
    """
    Support common outputs from existing project models:
    - string: "High", "Scam", "Green"
    - integer: 0 or 1
    - dict: {"risk": "High", "reason": "..."}
    - tuple: ("High", "Explanation")
    """

    label = None
    explanation = None

    if isinstance(raw, dict):
        for key in (
            "risk", "risk_level", "risk_category",
            "category", "label", "prediction",
            "classification", "result", "status"
        ):
            if key in raw:
                candidate = risk_from_value(raw[key])
                if candidate:
                    label = candidate
                    break

        for key in (
            "reason", "explanation",
            "details", "message"
        ):
            if key in raw and raw[key]:
                explanation = str(raw[key])
                break

    elif isinstance(raw, (tuple, list)):
        for item in raw:
            candidate = risk_from_value(item)
            if candidate:
                label = candidate
                break

        for item in raw:
            if isinstance(item, str) and (
                risk_from_value(item) is None
            ):
                explanation = item
                break

    else:
        label = risk_from_value(raw)

    if label is None:
        raise ValueError(
            "The detection model returned an unrecognised "
            f"result format: {str(raw)[:250]}"
        )

    return label, explanation


# ==========================================
# SCAM INDICATORS
# ==========================================

def find_indicators(message):
    """
    Explain visible message patterns.
    These do not override the model prediction.
    """

    patterns = {
        "Urgency or pressure": (
            r"\b(urgent|immediately|act now|"
            r"within 24 hours|final warning)\b"
        ),
        "Account verification request": (
            r"\b(verify your account|confirm your "
            r"identity|account suspended)\b"
        ),
        "Financial information request": (
            r"\b(bank details|credit card|"
            r"payment details|card number)\b"
        ),
        "Password or security-code request": (
            r"\b(password|one.time password|"
            r"otp|security code)\b"
        ),
        "Suspicious reward language": (
            r"\b(you have won|claim your prize|"
            r"free gift|congratulations winner)\b"
        ),
        "Link included": (
            r"https?://[^\s]+|www\.[^\s]+"
        ),
    }

    found = []

    for name, pattern in patterns.items():
        if re.search(pattern, message, re.IGNORECASE):
            found.append(name)

    return found


# ==========================================
# RUN EXISTING MODEL
# ==========================================

def run_detection(message, model_choice):

    if model_choice == "Rules-Based Baseline":
        if classify_message is None:
            raise RuntimeError(
                "Rules-based model unavailable: "
                + str(RULES_ERROR)
            )

        raw = classify_message(message)

    else:
        if predict_message is None:
            raise RuntimeError(
                "Machine-learning model unavailable: "
                + str(ML_ERROR)
            )

        raw = predict_message(message)

    risk, explanation = normalise_result(raw)

    return {
        "risk": risk,
        "explanation": explanation,
        "model": model_choice,
        "indicators": find_indicators(message),
        "time": datetime.now().strftime("%H:%M:%S"),
    }


# ==========================================
# RISK DISPLAY
# ==========================================

def show_result(result):

    risk = result["risk"]

    config = {
        "Green": {
            "icon": "🟢",
            "class": "risk-green",
            "heading": "LOW RISK",
            "description": (
                "The selected model classified this "
                "message as lower risk. This does not "
                "guarantee the message is safe."
            ),
        },
        "Amber": {
            "icon": "🟡",
            "class": "risk-amber",
            "heading": "MEDIUM RISK",
            "description": (
                "The message may require further "
                "verification. Avoid clicking links "
                "until the sender is confirmed."
            ),
        },
        "Red": {
            "icon": "🔴",
            "class": "risk-red",
            "heading": "HIGH RISK",
            "description": (
                "The selected model flagged this "
                "message as high risk. Do not share "
                "passwords, financial information "
                "or verification codes."
            ),
        },
    }

    item = config[risk]

    st.markdown(
        f"""
        <div class="risk-card {item['class']}">
            <div class="risk-heading">
                {item['icon']} {item['heading']}
            </div>
            <div class="risk-description">
                {item['description']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Classification: "
        + risk
        + " | Detection model: "
        + result["model"]
    )

    if result["explanation"]:
        st.info(
            "Model explanation: "
            + result["explanation"]
        )

    st.markdown("#### 🔎 Message indicators")

    if result["indicators"]:
        for indicator in result["indicators"]:
            st.write("• " + indicator)
    else:
        st.write(
            "No predefined warning phrases were "
            "detected by the interface's indicator "
            "checker."
        )

    st.caption(
        "Indicators are explanatory only. "
        "They are not the model's prediction "
        "or a guarantee of safety."
    )

    st.markdown("#### 🛡️ Recommended next steps")

    if risk == "Red":
        st.warning(
            "Do not respond to suspicious requests. "
            "Contact the organisation using its "
            "official website or a trusted number."
        )
    elif risk == "Amber":
        st.warning(
            "Verify the sender independently before "
            "following links or sharing information."
        )
    else:
        st.success(
            "No high-risk classification was returned "
            "by the selected model. Continue to use "
            "caution with unknown senders."
        )


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## 🛡️ ShieldSense")
    st.caption("SCAM DETECTION PLATFORM")

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select dashboard page",
        [
            "🔍 Message Scanner",
            "📊 Scan History",
            "♿ Accessibility",
            "ℹ️ About ShieldSense",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    st.markdown("### System Status")

    if classify_message is not None:
        st.success("Rules engine loaded")
    else:
        st.error("Rules engine unavailable")

    if predict_message is not None:
        st.success("ML predictor imported")
    else:
        st.error("ML predictor unavailable")

    st.caption(
        "ML model files are checked when a "
        "prediction is requested."
    )

    st.divider()

    st.caption(
        "ShieldSense | Educational prototype"
    )


# ==========================================
# MAIN DASHBOARD
# ==========================================

if page == "🔍 Message Scanner":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">
            INTELLIGENT MESSAGE SCREENING
        </div>
        <div class="hero-title">
            🛡️ ShieldSense
        </div>
        <div class="hero-subtitle">
            Stay alert. Spot suspicious messages.
            Use rules-based or machine-learning
            detection to screen potential scams.
        </div>
    </div>
    """, unsafe_allow_html=True)

    history = st.session_state.scan_history

    total = len(history)

    high = sum(
        item["risk"] == "Red"
        for item in history
    )

    medium = sum(
        item["risk"] == "Amber"
        for item in history
    )

    low = sum(
        item["risk"] == "Green"
        for item in history
    )

    a, b, c, d = st.columns(4)

    with a:
        st.metric("Total Scans", total)

    with b:
        st.metric("🔴 High Risk", high)

    with c:
        st.metric("🟡 Medium Risk", medium)

    with d:
        st.metric("🟢 Low Risk", low)

    st.markdown("## 🔍 Scam Message Scanner")

    st.markdown(
        "Paste an SMS, email or chat message "
        "below to analyse its potential scam risk."
    )

    message = st.text_area(
        "Message to analyse",
        placeholder=(
            "Example: URGENT! Your account will "
            "be suspended. Click the link to "
            "verify your identity."
        ),
        height=180,
        max_chars=5000,
        help=(
            "Avoid entering passwords, banking "
            "details or other sensitive information."
        ),
    )

    model_choice = st.radio(
        "Choose detection method",
        [
            "Rules-Based Baseline",
            "Machine Learning",
        ],
        horizontal=True,
    )

    st.caption(
        "Only the selected model determines "
        "the risk classification."
    )

    scan_clicked = st.button(
        "🛡️ Analyse Message",
        type="primary",
        use_container_width=True,
    )

    if scan_clicked:

        if not message.strip():
            st.warning(
                "Please enter a message "
                "before starting the scan."
            )

        else:
            try:
                with st.spinner(
                    "Analysing message..."
                ):
                    result = run_detection(
                        message.strip(),
                        model_choice,
                    )

                st.session_state.last_result = result

                # Store limited history without
                # retaining raw message contents.
                st.session_state.scan_history.append({
                    "time": result["time"],
                    "risk": result["risk"],
                    "model": result["model"],
                })

            except Exception as exc:
                st.session_state.last_result = None

                st.error(
                    "The scan could not be completed."
                )

                st.code(str(exc))

                st.info(
                    "Check the model function and "
                    "the format it returns."
                )

    if st.session_state.last_result:
        st.markdown("## 📋 Analysis Result")

        show_result(
            st.session_state.last_result
        )

    st.divider()

    st.markdown("### 🔐 Security Reminder")

    st.info(
        "ShieldSense is a prototype. "
        "Predictions can be incorrect. "
        "Always verify suspicious messages "
        "through official communication channels."
    )


# ==========================================
# SCAN HISTORY
# ==========================================

elif page == "📊 Scan History":

    st.title("📊 Scan History")

    st.write(
        "Review classifications made during "
        "your current browser session."
    )

    history = st.session_state.scan_history

    if not history:
        st.info(
            "No scans recorded yet. "
            "Go to Message Scanner to begin."
        )

    else:
        st.dataframe(
            list(reversed(history)),
            use_container_width=True,
            hide_index=True,
        )

        total = len(history)

        red_count = sum(
            item["risk"] == "Red"
            for item in history
        )

        amber_count = sum(
            item["risk"] == "Amber"
            for item in history
        )

        green_count = sum(
            item["risk"] == "Green"
            for item in history
        )

        a, b, c = st.columns(3)

        a.metric("High Risk", red_count)
        b.metric("Medium Risk", amber_count)
        c.metric("Low Risk", green_count)

        if st.button(
            "🗑️ Clear Scan History",
            use_container_width=True,
        ):
            st.session_state.scan_history = []
            st.session_state.last_result = None
            st.rerun()

    st.caption(
        "History is stored in Streamlit session "
        "state, not in a permanent database."
    )


# ==========================================
# ACCESSIBILITY PAGE
# ==========================================

elif page == "♿ Accessibility":

    st.title("♿ Accessibility & Inclusive Design")

    st.write(
        "ShieldSense aims to provide an "
        "accessible experience for users "
        "with different needs."
    )

    st.markdown("### Accessible Design Features")

    st.markdown("""
    - Clear headings and labelled input fields.
    - Keyboard-friendly Streamlit controls.
    - Visible focus outlines.
    - Text labels alongside risk colours.
    - High-contrast dark dashboard styling.
    - Explanations and recommended actions.
    - Responsive layout for smaller screens.
    - No reliance on colour alone.
    """)

    st.markdown("### Understanding Risk Levels")

    st.success(
        "🟢 GREEN — Lower-risk classification"
    )

    st.warning(
        "🟡 AMBER — Medium-risk classification"
    )

    st.error(
        "🔴 RED — High-risk classification"
    )

    st.markdown("### WCAG 2.2 AA")

    st.info(
        "This interface includes accessibility "
        "design measures, but WCAG 2.2 AA "
        "conformance must be verified through "
        "manual and automated testing."
    )


# ==========================================
# ABOUT PAGE
# ==========================================

elif page == "ℹ️ About ShieldSense":

    st.title("ℹ️ About ShieldSense")

    st.markdown("""
    ShieldSense is an accessible scam-message
    screening application developed as an
    educational software project.

    ### Project Objectives

    - Identify potentially suspicious messages.
    - Provide understandable risk classifications.
    - Support rules-based and ML predictions.
    - Explain common scam indicators.
    - Promote safe digital communication.
    - Support accessible interface design.

    ### Technologies

    - Python
    - Streamlit
    - Scikit-learn (machine learning)
    - Rules-based detection
    - HTML/CSS styling

    ### Important Limitations

    ShieldSense is not a guaranteed scam detector.
    A low-risk result does not prove that a message
    is genuine. Model performance must be measured
    against an appropriate test dataset.
    """)

    st.markdown("### Privacy")

    st.write(
        "The interface does not intentionally "
        "store message text in its scan-history "
        "records. Review model code and "
        "application hosting before making "
        "any broader privacy guarantees."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "🛡️ ShieldSense | Accessible Scam Screening "
    "| Educational Prototype"
)

# ---------------------------------
# Message scan history
# ---------------------------------

st.divider()
st.header("📋 Message Scan History")

st.write(
    "Review messages checked during your current session."
)

history = st.session_state.scan_history

if history:

    st.metric(
        "Total Messages Checked",
        len(history)
    )

    low_count = sum(
        1 for item in history
        if item["risk"] == "LOW"
    )

    medium_count = sum(
        1 for item in history
        if item["risk"] == "MEDIUM"
    )

    high_count = sum(
        1 for item in history
        if item["risk"] == "HIGH"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🟢 Low", low_count)

    with col2:
        st.metric("🟠 Medium", medium_count)

    with col3:
        st.metric("🔴 High", high_count)

    for index, record in enumerate(
        reversed(history),
        start=1
    ):

        record_risk = record["risk"]

        if record_risk == "LOW":
            risk_icon = "🟢"
        elif record_risk == "MEDIUM":
            risk_icon = "🟠"
        else:
            risk_icon = "🔴"

        with st.expander(
            f"Scan {index} — "
            f"{risk_icon} {record_risk} RISK"
        ):

            st.write(
                "**Date and Time:**",
                record["time"]
            )

            st.write(
                "**Message:**",
                record["message"]
            )

            st.write(
                "**Detection Model:**",
                record["model"]
            )

            st.write(
                "**Risk Level:**",
                record["risk"]
            )

    # ---------------------------------
    # Clear history
    # ---------------------------------

    if st.button(
        "🗑️ Clear Scan History",
        use_container_width=True
    ):

        st.session_state.scan_history = []
        st.session_state.latest_result = None

        st.rerun()

else:

    st.info(
        "No messages have been checked in this session."
    )


# ---------------------------------
# Accessibility information
# ---------------------------------

st.divider()
st.subheader("♿ Accessibility Features")

st.write(
    "ShieldSense uses labelled input fields, "
    "text-based risk descriptions and colour-coded "
    "results to make information easier to understand."
)

st.info(
    "Risk categories are communicated using both "
    "colour and text, so users do not need to "
    "rely on colour alone."
)

st.caption(
    "WCAG 2.2 AA compliance has not yet been verified. "
    "Keyboard navigation, screen-reader support, "
    "focus behaviour and contrast must be tested."
)


# ---------------------------------
# Privacy notice
# ---------------------------------

st.divider()
st.subheader("🔒 Privacy Notice")

st.write(
    "Message history is kept in the current "
    "Streamlit session and is not automatically "
    "saved to a database by this interface."
)

st.write(
    "Avoid entering sensitive personal information. "
    "Message processing and logging behaviour also "
    "depend on the connected detection models "
    "and deployment environment."
)


# ---------------------------------
# Footer
# ---------------------------------

st.divider()

st.markdown(
    "### About ShieldSense"
)

st.write(
    "ShieldSense is an educational prototype "
    "designed to support scam awareness through "
    "accessible message screening."
)

st.markdown(
    '<p class="footer">'
    '🛡️ ShieldSense | ITEC320 Industry Placement Project'
    '</p>',
    unsafe_allow_html=True
)
