"""
Tejas More — Portfolio / Dynamic Resume Site
A small Flask app that renders the CV from structured Python data.
Edit the CV_DATA dict below to update site content without touching HTML.
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

# ---------------------------------------------------------------------------
# EDIT ME: All resume content lives here. Update this dict to change the site.
# ---------------------------------------------------------------------------
CV_DATA = {
    "name": "Tejas More",
    "title": "Project Coordinator | AI-Assisted Operations & Project Management",
    "location": "Pune / Mumbai, India",
    "email": "tejas2more@email.com",
    "phone": "+91 98765 43210",
    "resume_file": "resume/Tejas_More_Resume.pdf",
    "profile_image": "img/profile.webp",

    # 👉 Replace this with your real Google Form link (see README "Configuration").
    "contact_form_url": "https://forms.gle/REPLACE-WITH-YOUR-GOOGLE-FORM-ID",

    "summary": (
        "High-performing Operations & Project Coordination professional with 2+ years managing "
        "day-to-day operational workflows, cross-functional project execution, and system bottleneck "
        "resolution. Proven record applying generative AI tools (ChatGPT, Claude, Gemini), prompt "
        "engineering, and CLI-based automation to eliminate repetitive tasks and build standardized "
        "operating procedures (SOPs). Strong in stakeholder coordination, KPI tracking, risk and "
        "compliance monitoring, and data-driven decision support — positioned for Project Manager / "
        "Project Coordinator roles requiring both technical fluency and delivery discipline."
    ),

    "pipeline": [
        {"label": "Input", "icon": "input"},
        {"label": "AI Automate", "icon": "bot"},
        {"label": "SOP & Process", "icon": "gear"},
        {"label": "KPI Monitor", "icon": "chart"},
        {"label": "Delivery", "icon": "check"},
    ],

    "skill_groups": [
        {
            "title": "AI & Automation",
            "icon": "bot",
            "skills": ["ChatGPT", "Claude", "Gemini", "Prompt Engineering", "AI Agents",
                      "CLI-Based Automation Workflows", "Operational Task Automation", "n8n"],
        },
        {
            "title": "Project Management",
            "icon": "target",
            "skills": ["Project Planning & Execution", "Risk & Issue Management",
                      "Resource Planning & Allocation", "Change Management"],
        },
        {
            "title": "Systems & Tools",
            "icon": "layers",
            "skills": ["ERP Systems", "Issue Tracking & Support Ticketing", "Google Workspace",
                      "Microsoft Office (Excel, Word, PowerPoint)"],
        },
        {
            "title": "PM Tools",
            "icon": "grid",
            "skills": ["Microsoft Project", "Jira"],
        },
        {
            "title": "Productivity & Analytics",
            "icon": "chart",
            "skills": ["Microsoft Excel (Advanced)", "Microsoft PowerPoint", "Power BI"],
        },
        {
            "title": "Data & Reporting",
            "icon": "database",
            "skills": ["Operational Data Analysis", "Trial Balance & Closing Account Reconciliation",
                      "KPI Dashboards & Reporting"],
        },
        {
            "title": "Process & Documentation",
            "icon": "doc",
            "skills": ["SOP & Documentation Creation", "Process Optimization",
                      "Workflow Automation", "Bottleneck Identification"],
        },
    ],

    "pm_skillset": [
        {
            "title": "Delivery & Planning",
            "desc": "Task and timeline tracking, milestone monitoring, process optimization, workflow redesign.",
        },
        {
            "title": "Stakeholder Management",
            "desc": "Cross-departmental coordination, stakeholder communication, executive reporting.",
        },
        {
            "title": "Risk & Compliance",
            "desc": "Risk and compliance tracking, change management, SOP governance.",
        },
        {
            "title": "Performance Monitoring",
            "desc": "KPI monitoring, bottleneck identification, data-driven decision support.",
        },
    ],

    "experience": [
        {
            "company": "Enfuse Solutions",
            "location": "Mumbai, India",
            "roles": [
                {"title": "Associate Project Coordinator", "period": "Sept 2025 – July 2026"},
                {"title": "Operations Associate", "period": "Mar 2024 – Sept 2025"},
            ],
            "highlights": [
                "Supervised and coordinated daily activities of cross-functional teams to achieve operational targets.",
                "Streamlined day-to-day operational workflows by authoring AI-assisted SOPs and deploying prompt engineering and CLI tools to automate routine data handling, reporting, and daily tracking tasks.",
                "Monitored core operational KPIs, identified system bugs and workflow delays, and collaborated with cross-functional teams to resolve operational bottlenecks rapidly.",
                "Executed in-depth analysis of operational data — including complex trial balance and closing account reconciliations — delivering actionable insights to support leadership decision-making.",
                "Coordinated daily operations and communications across departments, managing task execution across team members to maintain high operational accuracy and efficiency.",
                "Coordinated and delivered end-to-end ERP system training and SOPs for primary stakeholders, ensuring seamless digital adoption.",
                "Guided and supported team members by resolving operational issues and providing process-related assistance.",
                "Routinely tested and integrated emerging LLM tools (ChatGPT, Claude, Gemini) and CLI scripts into daily operational workflows, reducing manual task processing time by up to 30%.",
                "Managed day-to-day communication with clients, ensuring timely resolution of operational issues and service requests.",
                "Built and maintained strong client relationships by providing professional support and regular project updates.",
                "Maintained team attendance, work schedules, and performance records while ensuring compliance with company policies.",
            ],
        },
    ],

    "education": [
        {"degree": "Master of Computer Applications (MCA)",
         "detail": "Specialization in Artificial Intelligence & Machine Learning, 2025"},
        {"degree": "Bachelor of Computer Applications (BCA)",
         "detail": "Shivaji University"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", cv=CV_DATA)


@app.route("/healthz")
def healthz():
    # Simple health check endpoint for Render / uptime monitors.
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
