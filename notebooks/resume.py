from weasyprint import HTML
import base64

# Define the HTML content for the resume
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 15mm;
            background-color: #ffffff;
        }
        body {
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 10pt;
            line-height: 1.4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        h1 {
            font-size: 22pt;
            margin: 0;
            color: #2c3e50;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .contact-info {
            margin-top: 5px;
            font-size: 9pt;
            color: #555;
        }
        h2 {
            font-size: 13pt;
            color: #2c3e50;
            border-left: 4px solid #2c3e50;
            padding-left: 8px;
            margin-top: 18px;
            margin-bottom: 8px;
            text-transform: uppercase;
            background-color: #f8f9fa;
        }
        .summary {
            margin-bottom: 15px;
            text-align: justify;
        }
        .job-title {
            font-weight: bold;
            font-size: 11pt;
            display: flex;
            justify-content: space-between;
        }
        .company-name {
            color: #2980b9;
            font-weight: bold;
            font-style: italic;
        }
        .date-location {
            float: right;
            font-weight: normal;
            color: #666;
        }
        ul {
            margin-top: 5px;
            margin-bottom: 10px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 4px;
        }
        .skills-grid {
            display: table;
            width: 100%;
            margin-bottom: 10px;
        }
        .skill-category {
            display: table-row;
        }
        .skill-label {
            display: table-cell;
            font-weight: bold;
            width: 30%;
            padding: 3px 0;
        }
        .skill-values {
            display: table-cell;
            padding: 3px 0;
        }
        .education-item {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>ZAID AHMED ANSARI</h1>
        <div class="contact-info">
            Mumbai, Maharashtra, India | +91 9819343589 | ansarizaid110@gmail.com
        </div>
    </div>

    <div class="summary">
        Results-driven Senior Full Stack Developer with over 7 years of expertise in designing and deploying scalable enterprise solutions across fintech, ERP, and logistics domains. Proven track record in architecting payment gateways, loan origination systems, and community platforms serving thousands of users. Adept at leading full-cycle development from requirements gathering to production deployment, with extensive experience in blockchain and system performance optimization.
    </div>

    <h2>Core Competencies</h2>
    <div class="skills-grid">
        <div class="skill-category">
            <div class="skill-label">Backend:</div>
            <div class="skill-values">PHP (Laravel, CodeIgniter), Node.js, Python, FastAPI, MySQL</div>
        </div>
        <div class="skill-category">
            <div class="skill-label">Frontend:</div>
            <div class="skill-values">Angular, React, JavaScript (ES6+), jQuery, HTML5, CSS3, Bootstrap</div>
        </div>
        <div class="skill-category">
            <div class="skill-label">Cloud & DevOps:</div>
            <div class="skill-values">AWS (EC2, S3, RDS), Git, CI/CD Pipelines, System Architecture</div>
        </div>
        <div class="skill-category">
            <div class="skill-label">Specialized:</div>
            <div class="skill-values">Fintech, Blockchain (Ethereum), Google Document AI, RESTful APIs</div>
        </div>
    </div>

    <h2>Professional Experience</h2>

    <div class="job-title">
        <span>Senior Full Stack Developer</span>
        <span class="date-location">April 2022 – Present</span>
    </div>
    <div class="company-name">Creative Mantra, Mumbai</div>
    <ul>
        <li>Architected and developed an enterprise-grade Loan Origination System (LOS) from scratch, designing scalable database schemas to streamline financial operations.</li>
        <li>Integrated third-party KYC, Video PD, and digital signing APIs, reducing verification time by 60% while ensuring strict regulatory compliance.</li>
        <li>Built a logistics management system featuring real-time rating APIs and advanced mapping solutions for optimized delivery tracking and route planning.</li>
        <li>Led R&D for Google Document AI implementation and Ethereum blockchain for secure, immutable document storage.</li>
    </ul>

    <div class="job-title">
        <span>Full Stack Developer</span>
        <span class="date-location">Dec 2021 – April 2022</span>
    </div>
    <div class="company-name">HeyHub, Mumbai</div>
    <ul>
        <li>Developed robust RESTful APIs for a community software platform, enabling seamless backend-to-frontend integration.</li>
        <li>Integrated multiple third-party systems to enhance platform functionality and improve cross-platform user experience for web and mobile.</li>
    </ul>

    <div class="job-title">
        <span>Software Developer</span>
        <span class="date-location">July 2019 – Dec 2021</span>
    </div>
    <div class="company-name">Carnelian Payment Networks India Pvt Ltd (PayNet), Mumbai</div>
    <ul>
        <li>Led UAT and production integration of the PayNet gateway across India and the Gulf, onboarding UPI, IMPS, and international processors.</li>
        <li>Engineered a Society Management System for 1,000+ users, automating billing and real-time payment processing.</li>
        <li>Designed mobile application APIs for iOS and Android, ensuring 99.9% uptime and consistent data synchronization.</li>
        <li>Developed mPOS systems and coworking space management platforms for diverse enterprise clients.</li>
    </ul>

    <div class="job-title">
        <span>Web Developer</span>
        <span class="date-location">Dec 2018 – July 2019</span>
    </div>
    <div class="company-name">Exim India Multimedia Pvt Ltd, Mumbai</div>
    <ul>
        <li>Managed the full SDLC for multiple concurrent projects, collaborating with stakeholders to align technical frameworks with business goals.</li>
    </ul>

    <h2>Education</h2>
    <div class="education-item">
        <strong>Bachelor of Engineering, Information Technology</strong> | GPA: 5.63/10<br>
        Theem College of Engineering, Mumbai | 2016
    </div>
    <div class="education-item">
        <strong>Diploma, Computer Technology</strong> | 65%<br>
        S.V.P Polytechnic, Mumbai | 2013
    </div>

</body>
</html>
"""

# Generate PDF
with open("Zaid_Ahmed_Ansari_Resume.html", "w") as f:
    f.write(html_content)

HTML(string=html_content).write_pdf("Zaid_Ahmed_Ansari_Resume_v1.pdf")