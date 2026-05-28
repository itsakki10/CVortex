import requests
import streamlit as st

from frontend.services import api_client


def _show_backend_error(exc: Exception) -> None:

    if isinstance(exc, requests.ConnectionError):

        st.error(
            "Could not connect to backend.\n\n"
            "Make sure FastAPI is running on port 8000."
        )

    elif isinstance(exc, requests.HTTPError) and exc.response is not None:

        st.error(
            f"Backend Error {exc.response.status_code}: "
            f"{exc.response.text}"
        )

    else:

        st.error(f"Unexpected Error: {exc}")


def render() -> None:

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <div class="history-hero">

        <div class="hero-badge">
                📊 Resume Intelligence Archive
        </div>

        <h1 class="hero-title">
                CVortex Analysis History
        </h1>

        <p class="hero-subtitle">
                View previous ATS resume analyses,
                track improvements, compare scores,
                and manage your optimization history.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # AUTH CHECK
    # =====================================================

    access_token = st.session_state.get(
        "access_token"
    )

    if not access_token:

        st.warning(
            "⚠️ Sign in from the sidebar to access analysis history."
        )

        return

    # =====================================================
    # FETCH HISTORY
    # =====================================================

    try:

        with st.spinner(
            "Loading analysis history..."
        ):

            history = api_client.get_history(
                access_token
            )

    except requests.RequestException as exc:

        _show_backend_error(exc)

        return

    # =====================================================
    # EMPTY STATE
    # =====================================================

    if not history:

        st.markdown(
            """
            <div class="empty-history-card">

            <div class="empty-history-icon">
                    📂
            </div>

            <h2>
                    No Resume Analyses Yet
            </h2>

            <p>
                    Start analyzing resumes using CVortex AI
                    to build your ATS optimization history.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        _, mid, _ = st.columns([1, 2, 1])

        with mid:

            if st.button(
                "🎯 Go to ATS Scorer",
                use_container_width=True,
                type="primary"
            ):

                st.session_state.current_view = "scorer"

                st.rerun()

        return

    # =====================================================
    # TOTAL ANALYSES
    # =====================================================

    st.markdown(
        f"""
        <div class="history-stats-card">

        <div class="history-stat-number">
                {len(history)}
        </div>

        <div class="history-stat-label">
                Total Resume Analyses
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # HISTORY LOOP
    # =====================================================

    for idx, entry in enumerate(history):

        filename = entry.get(
            "filename",
            "resume"
        )

        ats_score = float(
            entry.get("ats_score", 0)
        )

        created_at = entry.get(
            "created_at",
            ""
        )

        analysis = entry.get(
            "analysis_result",
            {}
        ) or {}

        component_scores = analysis.get(
            "component_scores",
            {}
        ) or {}

        jd_comparison = (
            analysis.get("jd_comparison")
            or analysis.get("jd_match_analysis")
        )

        # =================================================
        # EXPANDER
        # =================================================

        with st.expander(
            f"📄 {filename} • ATS Score {ats_score:.0f}/100"
        ):

            # =============================================
            # TOP METRICS
            # =============================================

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "Overall Score",
                    f"{ats_score:.0f}/100"
                )

                st.metric(
                    "Formatting",
                    f"{component_scores.get('formatting', 0):.0f}/20"
                )

            with c2:

                st.metric(
                    "Keywords",
                    f"{component_scores.get('keywords', 0):.0f}/25"
                )

                st.metric(
                    "Content",
                    f"{component_scores.get('content', 0):.0f}/25"
                )

            with c3:

                st.metric(
                    "Skill Validation",
                    f"{component_scores.get('skill_validation', 0):.0f}/15"
                )

                st.metric(
                    "ATS Compatibility",
                    f"{component_scores.get('ats_compatibility', 0):.0f}/15"
                )

            st.markdown(
                '<div class="section-divider"></div>',
                unsafe_allow_html=True
            )

            # =============================================
            # JD MATCH
            # =============================================

            if jd_comparison:

                st.markdown(
                    f"""
                    <div class="jd-match-card">

                    <h3>
                            🎯 JD Match Score
                    </h3>

                    <div class="jd-match-number">
                            {jd_comparison.get('match_percentage', 0):.0f}%
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =============================================
            # CREATED DATE
            # =============================================

            st.markdown(
                f"""
                <div class="history-date">
                    🕒 Analysis Date: {created_at}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            # =============================================
            # DELETE BUTTON
            # =============================================

            entry_id = entry.get("id")

            if entry_id:

                if st.button(
                    "🗑️ Delete Analysis",
                    key=f"delete_{idx}",
                    use_container_width=True
                ):

                    try:

                        api_client.delete_history_entry(
                            str(entry_id),
                            access_token
                        )

                        st.success(
                            "Analysis deleted successfully."
                        )

                        st.rerun()

                    except requests.RequestException as exc:

                        _show_backend_error(exc)