from flask import render_template
from app import app

@app.route('/')
def index():
    """Main portfolio page"""
    # Work experiences data from resume
    work_experiences = [
        {
            'company': 'Amal\'s Boutique',
            'location': 'Boston, MA',
            'position': 'Software Engineer – Inventory Management System',
            'period': 'May 2025 – Present',
            'highlights': [
                'Lead a two-person team using Agile workflow and Git for version control',
                'Integrate dynamic dashboards with real-time data visualizations, improving 15% faster decision-making',
                'Design full-stack tracking solution eliminating 40+ manual hours monthly with 99% stock accuracy'
            ]
        },
        {
            'company': 'Wentworth Institute of Technology',
            'location': 'Boston, MA',
            'position': 'Product Manager – Learning Management System (LMS) Initiative',
            'period': 'Sep 2024 – Dec 2024',
            'highlights': [
                'Conducted market research via surveys, interviews, and user personas',
                'Scoped MVP requirements and evaluated three LMS platforms using vendor scorecard',
                'Streamlined project communication through Trello workflows and Power BI reports'
            ]
        },
        {
            'company': 'Vestmark, Inc.',
            'location': 'Wakefield, MA',
            'position': 'Technical Support Engineer Co-op',
            'period': 'Jan 2024 – May 2024',
            'highlights': [
                'Handled inbound support inquiries ensuring accurate reproducible descriptions',
                'Refined SQL documentation resulting in 45% decrease in average resolution time',
                'Collaborated with cross-functional teams to track issues and bugs'
            ]
        },
        {
            'company': 'Success Studio Wentworth Institute of Technology',
            'location': 'Boston, MA',
            'position': 'Academic Peer Tutor',
            'period': 'Oct 2023 – Dec 2024',
            'highlights': [
                'Supported student success in computing and management courses',
                'Provided 1-on-1 tutoring and skill-based workshops',
                'Helped troubleshoot software assignments in Python, SQL, and Java'
            ]
        }
    ]
    
    # Projects data
    projects = [
        {
            'title': 'Inventory Management System',
            'technologies': ['JavaScript', 'HTML', 'CSS', 'PHP', 'MySQL', 'Figma'],
            'period': 'May 2025 – Present',
            'description': 'Led a two-person team using Agile workflow and Git for version control, partnering with a local business owner to build their custom solution while discussing implementation with a second prospective client.',
            'highlights': [
                'Integrate dynamic dashboards with real-time data visualizations, improving 15% faster decision-making and reducing excess inventory costs by 20% through predictive analytics.',
                'Design full-stack tracking solution with Figma wireframes and user flow diagrams, eliminating 40+ manual hours monthly and achieving 99% stock accuracy via automated reconciliation and supplier integration.'
            ],
            'image': 'laptop-code.jpg',
            'github_url': 'https://github.com/vyhoang/inventory-management-system',
            'demo_url': 'https://inventory-demo.vyhoang.dev',
            'status': 'In Development'
        },
        {
            'title': 'Urban Renewal VR Experience',
            'technologies': ['Unity', 'Meta Quest VR', 'C#', 'Agile'],
            'period': 'Jan 2025 – April 2025',
            'description': 'Conducted archival research using over 10 primary sources, oral histories, and museum documents to create an authentic experience. Demonstrated technical proficiency by incorporating 5 interactive VR environments and 10+ interactive elements that bridge historical documentation with immersive digital storytelling.',
            'highlights': [
                'Collaborated with the West End Museum and a team of four students, maintaining a 90% above approval rating from historical consultants.'
            ],
            'image': 'vr-code.jpg',
            'github_url': 'https://github.com/vyhoang/urban-renewal-vr',
            'demo_url': '#',
            'status': 'Completed'
        },
        {
            'title': 'Learning Management System Initiative',
            'technologies': ['Microsoft Excel', 'Microsoft Project', 'Trello', 'Power BI'],
            'period': 'Sep 2024 – Dec 2024',
            'description': 'Conducted market research via surveys, interviews, and user personas to define pain points and draft prioritized user stories across student and faculty workflows.',
            'highlights': [
                'Scoped MVP requirements and evaluated three LMS platforms using a vendor scorecard, balancing usability, integration, and scalability for key stakeholders.',
                'Streamlined project communication and deliverable tracking through Trello workflows, translated survey responses and user analytics into comprehensive Power BI reports, and performed cost-benefit analysis in Excel to justify platform selection.'
            ],
            'image': 'data-analysis.jpg',
            'github_url': 'https://github.com/vyhoang/lms-initiative',
            'demo_url': 'https://lms-analysis.vyhoang.dev',
            'status': 'Completed'
        }
    ]
    
    # Technical skills
    technical_skills = {
        'Languages': ['Java', 'Python', 'SQL', 'C', 'HTML', 'CSS', 'JavaScript', 'PHP', 'Swift', 'Bash', 'PowerShell'],
        'Databases & Frameworks': ['AWS', 'JUnit', 'UIKit', 'MySQL', 'MSSQL', 'Oracle', 'Linux'],
        'Tools': ['Git', 'Jira', 'Figma', 'SketchUp', 'Adobe', 'Trello', 'Power BI', 'Salesforce', 'Unity']
    }
    
    # Education
    education = {
        'institution': 'Wentworth Institute of Technology',
        'location': 'Boston, MA',
        'degree': 'Bachelor of Science in Computer Information Systems',
        'minor': 'Computer Science',
        'graduation': 'Expected Graduation: Dec 2025',
        'coursework': ['Security Principles', 'Operating Systems', 'Systems Analysis and Design', 'Statistics', 'Algorithms', 'Economics']
    }
    
    # Contact info
    contact_info = {
        'name': 'Vy (Evelyn) Hoang',
        'location': 'Brighton, MA',
        'phone': '857-234-5331',
        'email': 'hoangv1@wit.edu',
        'linkedin': 'linkedin.com/in/vybaohg'
    }
    
    return render_template('index.html', 
                         work_experiences=work_experiences,
                         projects=projects,
                         technical_skills=technical_skills,
                         education=education,
                         contact_info=contact_info)