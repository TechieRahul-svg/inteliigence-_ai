import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="
        background: rgba(17,24,39,0.5);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.25);
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.16,1,0.3,1);
    ">
        <!-- Gradient header strip -->
        <div style="
            height: 4px;
            background: linear-gradient(90deg, #7C3AED, #06B6D4);
        "></div>

        <div style="padding: 20px 24px;">
            <!-- Subject name -->
            <h3 style="
                margin: 0 0 8px 0;
                color: #F9FAFB;
                font-size: 1.25rem;
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-weight: 700;
                letter-spacing: -0.02em;
            ">{name}</h3>

            <!-- Code & Section -->
            <div style="
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 16px;
            ">
                <span style="
                    background: rgba(124,58,237,0.12);
                    color: #A78BFA;
                    padding: 4px 12px;
                    border-radius: 6px;
                    font-weight: 600;
                    font-family: 'JetBrains Mono', monospace;
                    font-size: 0.8rem;
                    letter-spacing: 0.03em;
                    border: 1px solid rgba(124,58,237,0.2);
                ">{code}</span>
                <span style="
                    color: #6B7280;
                    font-size: 0.85rem;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                ">Section {section}</span>
            </div>
    """

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap;">'
        for icon, label, value in stats:
            html += f"""
            <div style="
                background: rgba(31,41,55,0.6);
                border: 1px solid rgba(255,255,255,0.06);
                padding: 8px 14px;
                border-radius: 10px;
                font-size: 0.8rem;
                font-family: 'Plus Jakarta Sans', sans-serif;
                display: flex;
                align-items: center;
                gap: 6px;
            ">
                <span style="font-size: 1rem;">{icon}</span>
                <span style="color: #9CA3AF; font-weight: 400;">{label}</span>
                <span style="color: #F9FAFB; font-weight: 700;">{value}</span>
            </div>
            """
        html += "</div>"

    html += "</div></div>"

    st.html(html)

    if footer_callback:
        footer_callback()
