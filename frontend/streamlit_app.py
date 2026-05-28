import sys
from pathlib import Path

import streamlit as st

# =====================================================
# PATH SETUP
# =====================================================

ROOT_DIR = Path(__file__).parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="CVortex",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SESSION STATE DEFAULTS
# =====================================================

SESSION_DEFAULTS = {
    "access_token": None,
    "refresh_token": None,
    "user_id": None,
    "user_email": None,
    "auth_error": None,
    "auth_info": None,
    "current_view": "landing",
}

for key, value in SESSION_DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value

# =====================================================
# LOAD CSS
# =====================================================

def load_css():

    css_path = (
        Path(__file__).parent
        / "assets"
        / "styles.css"
    )

    try:

        with open(css_path, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            "styles.css not found."
        )

load_css()

# =====================================================
# OAUTH HANDLER
# =====================================================

if (
    not st.session_state.access_token
    and "code" in st.query_params
):

    from frontend.services import supabase_client

    result = supabase_client.exchange_code_for_session(
        st.query_params["code"]
    )

    st.query_params.clear()

    if "error" in result:

        st.session_state.auth_error = (
            f"Google sign-in failed: {result['error']}"
        )

    else:

        st.session_state.access_token = result[
            "access_token"
        ]

        st.session_state.refresh_token = result[
            "refresh_token"
        ]

        st.session_state.user_id = result[
            "user_id"
        ]

        st.session_state.user_email = result[
            "email"
        ]

        st.rerun()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    # =============================================
    # BRANDING
    # =============================================

    st.markdown(
        """
        <div class="sidebar-brand">

        <div class="sidebar-logo">
                🚀
        </div>

        <div class="sidebar-title">
                CVortex
        </div>

        <div class="sidebar-subtitle">
                AI Resume Intelligence
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =============================================
    # NAVIGATION
    # =============================================

    st.markdown(
        """
        <div class="sidebar-section-title">
            Navigation
        </div>
        """,
        unsafe_allow_html=True
    )

    NAV_ITEMS = [
        ("🏠 Home", "landing"),
        ("🎯 ATS Scorer", "scorer"),
        ("📊 History", "history"),
        ("📚 Resources", "resources"),
    ]

    for label, view in NAV_ITEMS:

        if st.button(
            label,
            use_container_width=True,
            key=f"nav_{view}"
        ):

            st.session_state.current_view = view

            st.rerun()

    st.markdown("---")

    # =============================================
    # ACCOUNT SECTION
    # =============================================

    st.markdown(
        """
        <div class="sidebar-section-title">
            Account
        </div>
        """,
        unsafe_allow_html=True
    )

    from frontend.services import supabase_client

    # =============================================
    # AUTH MESSAGES
    # =============================================

    if st.session_state.auth_error:

        st.error(
            st.session_state.auth_error
        )

        st.session_state.auth_error = None

    if st.session_state.auth_info:

        st.info(
            st.session_state.auth_info
        )

        st.session_state.auth_info = None

    # =============================================
    # SIGNED IN
    # =============================================

    if st.session_state.access_token:

        st.markdown(
            f"""
            <div class="user-profile-card">

            <div class="user-avatar">
                    👤
            </div>

            <div class="user-email">
                    {st.session_state.user_email}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "🚪 Sign Out",
            use_container_width=True
        ):

            supabase_client.sign_out()

            for k in [
                "access_token",
                "refresh_token",
                "user_id",
                "user_email",
            ]:

                st.session_state[k] = None

            st.rerun()

    # =============================================
    # SIGNED OUT
    # =============================================

    else:

        signin_tab, signup_tab = st.tabs(
            [
                "Sign In",
                "Sign Up"
            ]
        )

        # =========================================
        # SIGN IN
        # =========================================

        with signin_tab:

            with st.form(
                "signin_form",
                clear_on_submit=False
            ):

                email = st.text_input(
                    "Email",
                    key="signin_email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    key="signin_pw"
                )

                submitted = st.form_submit_button(
                    "Sign In",
                    use_container_width=True
                )

            if submitted:

                result = (
                    supabase_client
                    .sign_in_with_password(
                        email,
                        password
                    )
                )

                if "error" in result:

                    st.session_state.auth_error = (
                        result["error"]
                    )

                else:

                    st.session_state.access_token = (
                        result["access_token"]
                    )

                    st.session_state.refresh_token = (
                        result["refresh_token"]
                    )

                    st.session_state.user_id = (
                        result["user_id"]
                    )

                    st.session_state.user_email = (
                        result["email"]
                    )

                st.rerun()

        # =========================================
        # SIGN UP
        # =========================================

        with signup_tab:

            with st.form(
                "signup_form",
                clear_on_submit=False
            ):

                email_up = st.text_input(
                    "Email",
                    key="signup_email"
                )

                password_up = st.text_input(
                    "Password (min 6 chars)",
                    type="password",
                    key="signup_pw"
                )

                submitted_up = (
                    st.form_submit_button(
                        "Create Account",
                        use_container_width=True
                    )
                )

            if submitted_up:

                result = (
                    supabase_client
                    .sign_up_with_password(
                        email_up,
                        password_up
                    )
                )

                if "error" in result:

                    st.session_state.auth_error = (
                        result["error"]
                    )

                elif result.get(
                    "pending_confirmation"
                ):

                    st.session_state.auth_info = (
                        f"Check your inbox — "
                        f"confirmation email sent "
                        f"to {result['email']}."
                    )

                else:

                    st.session_state.access_token = (
                        result["access_token"]
                    )

                    st.session_state.refresh_token = (
                        result["refresh_token"]
                    )

                    st.session_state.user_id = (
                        result["user_id"]
                    )

                    st.session_state.user_email = (
                        result["email"]
                    )

                st.rerun()

        st.markdown(
            """
            <div class="oauth-divider">
                or continue with
            </div>
            """,
            unsafe_allow_html=True
        )

        oauth = (
            supabase_client
            .google_oauth_url()
        )

        if "error" in oauth:

            st.caption(
                f"Google OAuth unavailable: "
                f"{oauth['error']}"
            )

        else:

            st.link_button(
                "🔐 Continue with Google",
                url=oauth["url"],
                use_container_width=True
            )

# =====================================================
# ROUTING
# =====================================================

current_view = st.session_state.current_view

if current_view == "landing":

    from frontend.views import landing

    landing.render()

elif current_view == "scorer":

    from frontend.views import scorer

    scorer.render()

elif current_view == "history":

    from frontend.views import history

    history.render()

elif current_view == "resources":

    from frontend.views import resources

    resources.render()