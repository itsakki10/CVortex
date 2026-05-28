import streamlit as st


def render():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <div class="hero-container">

        <div class="hero-badge">
                ✨ AI-Powered ATS Optimization
        </div>

        <h1 class="hero-title">
                🎯 CVortex
        </h1>

        <h3 class="hero-heading">
                Optimize Your Resume for Applicant Tracking Systems
        </h3>

        <p class="hero-subtitle">
                Get instant feedback on your resume ATS compatibility
                using AI-powered semantic analysis and intelligent scoring.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # CTA BUTTON
    # =====================================================

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "🚀 Start Analyzing Your Resume",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.current_view = "scorer"
            st.rerun()

    st.write("")
    st.write("")

    # =====================================================
    # FEATURES TITLE
    # =====================================================

    st.markdown(
        """
        <h2 class="section-title">
            ✨ Key Features
        </h2>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    # CARD 1

    with col1:

        st.markdown(
            """
            <div class="feature-box">

            <div class="feature-icon">
                    📊
            </div>

            <h3>
                    Comprehensive Scoring
            </h3>

            <p>
                    Get detailed ATS scores across formatting,
                    keywords, content quality, and skill validation.
            </p>

            <ul class="feature-list">
                    <li>Formatting Analysis</li>
                    <li>Keyword Matching</li>
                    <li>Content Quality</li>
                    <li>ATS Compatibility</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    # CARD 2

    with col2:

        st.markdown(
            """
            <div class="feature-box">

            <div class="feature-icon">
                    🔍
            </div>

            <h3>
                    Skill Validation
            </h3>

            <p>
                    Verify whether your skills are truly reflected
                    in projects, achievements, and experience.
            </p>

            <div class="feature-highlight">
                    No more empty claims!
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # CARD 3

    with col3:

        st.markdown(
            """
            <div class="feature-box">

            <div class="feature-icon">
                    🔒
            </div>

            <h3>
                    Privacy First
            </h3>

            <p>
                    All analysis runs locally on your system.
                    Your resume data never leaves your machine.
            </p>

            <div class="feature-highlight">
                    100% Private & Secure
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # HOW IT WORKS
    # =====================================================

    st.markdown(
        """
        <h2 class="section-title">
            🚀 How It Works
        </h2>
        """,
        unsafe_allow_html=True
    )

    step1, step2, step3 = st.columns(3)

    # STEP 1

    with step1:

        st.markdown(
            """
            <div class="step-card">

            <div class="step-number">
                    1
            </div>

            <h4>
                    Upload Resume
            </h4>

            <p>
                    Upload PDF, DOC, or DOCX resumes instantly.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # STEP 2

    with step2:

        st.markdown(
            """
            <div class="step-card">

            <div class="step-number">
                    2
            </div>

            <h4>
                    AI Analysis
            </h4>

            <p>
                    Our AI models analyze ATS compatibility
                    and semantic relevance.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # STEP 3

    with step3:

        st.markdown(
            """
            <div class="step-card">

            <div class="step-number">
                    3
            </div>

            <h4>
                    Improve Resume
            </h4>

            <p>
                    Receive actionable recommendations
                    to improve shortlisting chances.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # SECURITY MESSAGE
    # =====================================================

    st.success(
        """
🔒 100% Private & Secure

All resume analysis is performed locally.
Your data never leaves your system.
        """
    )


    st.markdown(
    """
    <div class="custom-footer">

    <div class="footer-title">
            Built with ❤️ by Akash Mehra
    </div>

    <div class="footer-links">

    <a href="https://github.com/itsakki10" target="_blank">
                💻 GitHub
    </a>

    <a href="mailto:yourmail@gmail.com">
                📧 Email
    </a>

    <a href="https://linkedin.com" target="_blank">
                🔗 LinkedIn
    </a>

    </div>

    </div>
    """,
    unsafe_allow_html=True
)


        