from imports import *
from filter_chat import *

class HTML_report(BaseModel):
    Report_HTML: str

sources="Data was utilized forn the folowwing sources - Skills were utilized from -ESCO -Udacity -EMSI\n Jobs sources are Linkedin whereas courses are from UAE universities "

# Report Generation
report_agent_i = Agent(
    role="Report and Summary Generator",
    goal="Produce insightful, factually accurate, and well-structured HTML reports based on the response data provided.",
    backstory=(
        "You are a Data Analyst with expertise in analyzing complex data "
        "and delivering concise, detailed insights. Your reports should "
        "be professional, engaging, and ready for both online viewing and "
        "future conversion to PDF."
        "If `code = 1`, include images/visualizations in the report using the provided path; "
        "if `code = 0`, focus solely on textual analysis and exclude any visual references."
    ),
    allow_delegation=False,
    max_iter=3,
    verbose=True
)

# Task Definition
report_writer_i = Task(
    description=(
        "Your task is to analyze the data in {response} and generate a professional HTML report. "
        "The report should be well-structured and formatted without unnecessary characters like \\n. "
        "Follow these steps:"
        "<ol>"
        "<li>Analyze the data in {response} to extract key insights.</li>"
        "<li>Structure the report into logical sections with proper headings and subheadings.</li>"
        "<li>Create a summary data table (using <code>&lt;table&gt;</code> in HTML) to present key points effectively.</li>"
        "<li>For `code = 1`, include visualizations or images using the provided <code>{path}</code>, "
        "adding them under a section titled 'Data Visualizations.' Avoid if `code = 0`.</li>"
        "<li>Proofread for grammatical accuracy, logical flow, and factual consistency.</li>"
        "<li>Add a section titled 'Sources' to cite references in <code>{sources}</code>.</li>"
        "</ol>"
        "The output must be a professional HTML document, fully formatted and ready for display. "
        "Avoid inserting \\n or other raw text newline markers."
        "Ensure the JSON output is properly formatted and can be parsed directly."
    ),
    expected_output=(
        "The final output must be a fully-structured HTML report with:"
        "<ul>"
        "<li>Markdown-style tables converted into clean HTML tables (<code>&lt;table&gt;</code>).</li>"
        "<li>Visualizations or images (if applicable) seamlessly integrated under a section titled 'Data Visualizations.' with Image source</li>"
        "<li>Clear, actionable insights and logical sections without redundant content.</li>"
        "<li>Output should strickly follow the JSON schema provided 'Report_HTML: html code'.</li>"
        "<li>HTML optimized  to be display on a front-end application only.</li>"
        "</ul>"
    ),
    output_json=HTML_report,
    agent=report_agent_i
)
# SEQUETINAL GENERATOR------------------------

# Create a crew and add the task
analysis_crew_i = Crew(
    agents=[report_agent_i],
    tasks=[report_writer_i],
)

#-----------------------------

# Report Generation
report_agent_x = Agent(
    role="Report and Summary Generator",
    goal="Produce insightful, factually accurate, and well-structured HTML reports based on the response data provided.",
    backstory=(
        "You are a Data Analyst with expertise in analyzing complex data "
        "and delivering concise, detailed insights. Your reports should "
        "be professional, engaging, and ready for both online viewing and "
        "future conversion to PDF."
        "focus solely on textual analysis and exclude any visual references."
    ),
    allow_delegation=False,
    max_iter=3,
    verbose=True
)

# Task Definition
report_writer_x = Task(
    description=(
        "Your task is to analyze the data in {response} and generate a professional HTML report. "
        "The report should be well-structured and formatted without unnecessary characters like \\n. "
        "Follow these steps:"
        "<ol>"
        "<li>Analyze the data in {response} to extract key insights.</li>"
        "<li>Structure the report into logical sections with proper headings and subheadings.</li>"
        "<li>Create a summary data table (using <code>&lt;table&gt;</code> in HTML) to present key points effectively.</li>"
        "<li>Proofread for grammatical accuracy, logical flow, and factual consistency.</li>"
        "<li>Add a section titled 'Sources' to cite references in <code>{sources}</code>.</li>"
        "</ol>"
        "The output must be a professional HTML document, fully formatted and ready for display. "
        "Avoid inserting \\n or other raw text newline markers."
        "Ensure the JSON output is properly formatted and can be parsed directly."
    ),
    expected_output=(
        "The final output must be a fully-structured HTML report with:"
        "<ul>"
        "<li>Markdown-style tables converted into clean HTML tables (<code>&lt;table&gt;</code>).</li>"
        "<li>Clear, actionable insights and logical sections without redundant content.</li>"
        "<li>Output should strickly follow the JSON schema provided 'Report_HTML: html code'.</li>"
        "<li>HTML optimized  to be display on a front-end application only.</li>"
        "</ul>"
    ),
    output_json=HTML_report,
    agent=report_agent_x
)




analysis_crew_x = Crew(
    agents=[report_agent_x],
    tasks=[report_writer_x]
)
