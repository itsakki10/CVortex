import streamlit as st


def render():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <div class="resources-hero">

        <div class="hero-badge">
                📚 ATS Career Intelligence
        </div>

        <h1 class="hero-title">
                CVortex Resume Resources
        </h1>

        <p class="hero-subtitle">
                Learn how modern Applicant Tracking Systems work
                and discover proven strategies to improve your
                resume visibility and interview chances.
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
    # ATS TIPS
    # =====================================================

    st.markdown(
        """
        <h2 class="section-title">
            🎯 ATS Optimization Tips
        </h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # =====================================================
    # DO'S
    # =====================================================

    with col1:

        st.markdown(
            """
            <div class="resource-card">

            <div class="resource-icon">
                    ✅
            </div>

            <h3>
                    ATS Resume Best Practices
            </h3>

            <ul class="resource-list">

            <li>Use standard section headings</li>

            <li>Match keywords from job descriptions</li>

            <li>Use clean ATS-friendly formatting</li>

            <li>List technical and soft skills clearly</li>

            <li>Quantify achievements with numbers</li>

            <li>Use professional fonts</li>

            <li>Save resumes as PDF or DOCX</li>

            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # DON'TS
    # =====================================================

    with col2:

        st.markdown(
            """
            <div class="resource-card">

            <div class="resource-icon">
                    ❌
            </div>

            <h3>
                    Common ATS Mistakes
            </h3>

            <ul class="resource-list">

            <li>Avoid tables and text boxes</li>

            <li>Do not hide text in headers/footers</li>

            <li>Avoid graphics and images</li>

            <li>Do not use fancy fonts</li>

            <li>Avoid multi-column layouts</li>

            <li>Do not keyword stuff unnaturally</li>

            <li>Avoid unexplained abbreviations</li>

            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # INDUSTRY KEYWORDS
    # =====================================================

    st.markdown(
        """
        <h2 class="section-title">
            🔑 ATS Keywords by Industry
        </h2>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "💻 Tech",
            "💼 Business",
            "🎨 Creative"
        ]
    )

    # =====================================================
    # TECH TAB
    # =====================================================

    with tab1:

        st.markdown(
            """
            <div class="industry-card">

            <h3>
                    Software Development & Engineering
            </h3>

            <div class="keyword-grid">

            <span class="keyword-pill">Python</span>

            <span class="keyword-pill">Java</span>

            <span class="keyword-pill">JavaScript</span>

            <span class="keyword-pill">React</span>

            <span class="keyword-pill">Django</span>

            <span class="keyword-pill">Docker</span>

            <span class="keyword-pill">Kubernetes</span>

            <span class="keyword-pill">CI/CD</span>

            <span class="keyword-pill">Agile</span>

            <span class="keyword-pill">Git</span>

            <span class="keyword-pill">REST APIs</span>

            <span class="keyword-pill">Cloud Computing</span>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # BUSINESS TAB
    # =====================================================

    with tab2:

        st.markdown(
            """
            <div class="industry-card">

            <h3>
                    Business & Management
            </h3>

            <div class="keyword-grid">

            <span class="keyword-pill">Project Management</span>

            <span class="keyword-pill">Leadership</span>

            <span class="keyword-pill">Strategic Planning</span>

            <span class="keyword-pill">Budget Management</span>

            <span class="keyword-pill">Stakeholder Engagement</span>

            <span class="keyword-pill">Business Analysis</span>

            <span class="keyword-pill">CRM</span>

            <span class="keyword-pill">Negotiation</span>

            <span class="keyword-pill">Operations</span>

            <span class="keyword-pill">Analytics</span>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # CREATIVE TAB
    # =====================================================

    with tab3:

        st.markdown(
            """
            <div class="industry-card">

            <h3>
                    Creative & Design
            </h3>

            <div class="keyword-grid">

            <span class="keyword-pill">UI/UX Design</span>

            <span class="keyword-pill">Adobe XD</span>

            <span class="keyword-pill">Figma</span>

            <span class="keyword-pill">Wireframing</span>

            <span class="keyword-pill">Prototyping</span>

            <span class="keyword-pill">Brand Identity</span>

            <span class="keyword-pill">Visual Design</span>

            <span class="keyword-pill">Creative Strategy</span>

            <span class="keyword-pill">Typography</span>

            <span class="keyword-pill">Motion Graphics</span>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # RESUME TEMPLATE SECTION
    # =====================================================

    st.markdown(
        """
        <h2 class="section-title">
            📄 ATS-Friendly Resume Templates
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="template-coming-soon">

        <div class="template-icon">
                🚀
        </div>

        <h3>
                Premium CVortex Templates Coming Soon
        </h3>

        <p>
                Download ATS-optimized resume templates
                designed for modern hiring systems and
                recruiter readability.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # =====================================================
    # FINAL INFO
    # =====================================================

    st.success(
        """
💡 Pro Tip

Tailor your resume for every job application.
Matching relevant ATS keywords significantly improves
shortlisting chances.
        """
    )