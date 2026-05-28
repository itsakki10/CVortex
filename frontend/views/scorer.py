from typing import Optional

import requests
import streamlit as st

from frontend.services import api_client
from frontend.components.dashboard import display_results_dashboard


def _read_jd(jd_file, jd_text: str) -> str:
    """
    Convert uploaded/pasted JD into plain text.
    """

    if jd_text:
        return jd_text.strip()

    if jd_file is None:
        return ""

    if jd_file.name.lower().endswith(".txt"):
        return jd_file.getvalue().decode(
            "utf-8",
            errors="ignore"
        )

    st.warning(
        "Job description uploads currently support only .txt files."
    )

    return ""


def _show_backend_error(exc: Exception) -> None:

    if isinstance(exc, requests.ConnectionError):

        st.error(
            "Could not connect to backend.\n\n"
            "Make sure FastAPI is running on port 8000."
        )

    elif isinstance(exc, requests.Timeout):

        st.error(
            "Backend response timed out.\n\n"
            "Try again or check server logs."
        )

    elif isinstance(exc, requests.HTTPError) and exc.response is not None:

        try:
            detail = exc.response.json().get(
                "detail",
                exc.response.text
            )

        except ValueError:
            detail = exc.response.text

        st.error(
            f"Backend Error {exc.response.status_code}: {detail}"
        )

    else:

        st.error(f"Unexpected Error: {exc}")


def _summary_text(analysis: dict) -> str:

    score = analysis.get(
        "ATS_score",
        analysis.get("ats_score", 0)
    )

    lines = [
        f"CVortex ATS Score: {score:.0f}/100",
        ""
    ]

    if analysis.get("strengths"):

        lines.append("STRENGTHS:")

        lines.extend(
            f"- {s}"
            for s in analysis["strengths"]
        )

        lines.append("")

    if analysis.get("critical_issues"):

        lines.append("CRITICAL ISSUES:")

        lines.extend(
            f"- {s}"
            for s in analysis["critical_issues"]
        )

        lines.append("")

    if analysis.get("suggestions"):

        lines.append("SUGGESTIONS:")

        lines.extend(
            f"- {s}"
            for s in analysis["suggestions"]
        )

    return "\n".join(lines)


def _render_upload_area(analysis_mode: str):

    left, right = st.columns(2)

    # =====================================================
    # RESUME UPLOAD
    # =====================================================

    with left:

        st.markdown(
            """
            <div class="upload-card">

            <div class="upload-header">
                    📄 Upload Resume
            </div>

            <p class="upload-subtext">
                    Upload PDF, DOC, or DOCX resume files.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        resume_file = st.file_uploader(
            "Choose Resume",
            type=["pdf", "doc", "docx"],
            key="resume_upload",
            label_visibility="collapsed"
        )

        if resume_file:

            st.success(
                f"✅ {resume_file.name}"
            )

    # =====================================================
    # JD SECTION
    # =====================================================

    jd_file: Optional[object] = None
    jd_text = ""

    with right:

        st.markdown(
            """
            <div class="upload-card">

            <div class="upload-header">
                    📋 Job Description
            </div>

            <p class="upload-subtext">
                    Compare your resume with a target role.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if analysis_mode == "Job Description Comparison":

            jd_method = st.radio(
                "Input Method",
                [
                    "Paste Text",
                    "Upload .txt File"
                ],
                horizontal=True,
                key="jd_input_method"
            )

            if jd_method == "Upload .txt File":

                jd_file = st.file_uploader(
                    "Upload JD",
                    type=["txt"],
                    key="jd_upload",
                    label_visibility="collapsed"
                )

                if jd_file:

                    st.success(
                        f"✅ {jd_file.name}"
                    )

            else:

                jd_text = st.text_area(
                    "Paste Job Description",
                    height=220,
                    placeholder="Paste the job description here...",
                    key="jd_text",
                    label_visibility="collapsed"
                )

        else:

            st.info(
                "Enable Job Description Comparison mode for ATS matching."
            )

    return resume_file, jd_file, jd_text


def _render_export_buttons(analysis: dict) -> None:

    st.markdown(
        """
        <h3 class="section-title">
            📥 Export Results
        </h3>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    # =====================================================
    # PDF EXPORT
    # =====================================================

    with c1:

        if st.button(
            "📑 Generate PDF Report",
            use_container_width=True,
            type="primary"
        ):

            try:

                with st.spinner(
                    "Generating PDF Report..."
                ):

                    pdf_bytes = api_client.generate_pdf(
                        analysis,
                        access_token=st.session_state[
                            "access_token"
                        ],
                    )

                st.session_state[
                    "scorer_pdf_bytes"
                ] = pdf_bytes

            except requests.RequestException as exc:

                _show_backend_error(exc)

        if "scorer_pdf_bytes" in st.session_state:

            st.download_button(
                "⬇️ Download PDF",
                data=st.session_state[
                    "scorer_pdf_bytes"
                ],
                file_name="cvortex_ats_report.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_pdf"
            )

    # =====================================================
    # TXT EXPORT
    # =====================================================

    with c2:

        st.download_button(
            "📄 Download Summary",
            data=_summary_text(analysis),
            file_name="cvortex_summary.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_summary"
        )


def render() -> None:

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <div class="scorer-hero">

        <div class="hero-badge">
                ⚡ AI-Powered Resume Intelligence
        </div>

        <h1 class="hero-title">
                CVortex ATS Resume Scorer
        </h1>

        <p class="hero-subtitle">
                Analyze your resume using advanced AI-driven
                ATS scoring, keyword matching, semantic analysis,
                and optimization recommendations.
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
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.markdown("---")

        st.markdown("## 📊 Analysis Options")

        st.info(
            "**General ATS Score**\n\n"
            "Resume-only ATS evaluation.\n\n"
            "**JD Comparison**\n\n"
            "Match resume against job descriptions."
        )

    # =====================================================
    # ANALYSIS MODE
    # =====================================================

    st.markdown(
        """
        <h3 class="section-title">
            Choose Analysis Mode
        </h3>
        """,
        unsafe_allow_html=True
    )

    analysis_mode = st.radio(
        "Analysis Mode",
        [
            "General ATS Score",
            "Job Description Comparison"
        ],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # UPLOAD AREA
    # =====================================================

    resume_file, jd_file, jd_text = _render_upload_area(
        analysis_mode
    )

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # EMPTY STATE
    # =====================================================

    if not resume_file:

        st.info(
            "👆 Upload your resume to begin AI analysis."
        )

        if st.session_state.get("scorer_analysis"):

            display_results_dashboard(
                st.session_state[
                    "scorer_analysis"
                ]
            )

        return

    # =====================================================
    # AUTH CHECK
    # =====================================================

    access_token = st.session_state.get(
        "access_token"
    )

    if not access_token:

        st.warning(
            "⚠️ Please sign in from the sidebar first."
        )

        return

    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    _, mid, _ = st.columns([1, 2, 1])

    with mid:

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
            type="primary"
        )

    # =====================================================
    # PREVIOUS RESULT
    # =====================================================

    if not analyze:

        if st.session_state.get("scorer_analysis"):

            display_results_dashboard(
                st.session_state[
                    "scorer_analysis"
                ]
            )

            _render_export_buttons(
                st.session_state[
                    "scorer_analysis"
                ]
            )

        return

    # =====================================================
    # RESET SESSION CACHE
    # =====================================================

    st.session_state.pop(
        "scorer_pdf_bytes",
        None
    )

    st.session_state.pop(
        "scorer_analysis",
        None
    )

    # =====================================================
    # JD EXTRACTION
    # =====================================================

    job_description = ""

    if analysis_mode == "Job Description Comparison":

        job_description = _read_jd(
            jd_file,
            jd_text
        )

    # =====================================================
    # ANALYSIS
    # =====================================================

    try:

        with st.spinner(
            "Analyzing Resume using CVortex AI..."
        ):

            analysis = api_client.analyze_resume(
                resume_file=resume_file,
                access_token=access_token,
                job_description=job_description,
            )

    except requests.RequestException as exc:

        _show_backend_error(exc)

        return

    # =====================================================
    # STORE RESULTS
    # =====================================================

    st.session_state[
        "scorer_analysis"
    ] = analysis

    st.success(
        "✅ CVortex Analysis Complete!"
    )

    # =====================================================
    # DASHBOARD
    # =====================================================

    display_results_dashboard(analysis)

    # =====================================================
    # EXPORTS
    # =====================================================

    _render_export_buttons(analysis)