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
                'Integrate real-time dashboards to track inventory and forecast revenue using linear regression',
                'Design full-stack tracking solution with Figma wireframes and user flow diagrams'
            ]
        },
        {
            'company': 'Wentworth Institute of Technology',
            'location': 'Boston, MA',
            'position': 'Product Manager – Learning Management System (LMS) Initiative',
            'period': 'Sep 2024 – Dec 2024',
            'highlights': [
                'Drove product strategy by conducting market research (150+ surveys, 25+ stakeholder interviews)',
                'Led vendor evaluation of 3 LMS platforms via scoring matrix (12 criteria including usability, scalability, and integrations)',
                'Streamlined project communication via Trello and developed automated Power BI reporting from user analytics'
            ]
        },
        {
            'company': 'Vestmark, Inc.',
            'location': 'Wakefield, MA',
            'position': 'Technical Support Engineer Co-op',
            'period': 'Jan 2024 – May 2024',
            'highlights': [
                'Acted as a client-facing point of contact for 20+ financial institutions to support portfolio management workflows and triage issues.',
                'Coordinated with Engineering and Operations teams to prioritize and resolve 130+ issues',
                'Implemented SQL logging and standardized documentation, enhancing traceability and root-cause analysis.'
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
    
    # Featured projects (shown by default)
    featured_projects = [
        {
            'title': 'Inventory Management System',
            'technologies': ['JavaScript', 'HTML', 'CSS', 'PHP', 'PostgreSQL', 'Figma'],
            'period': 'May 2025 – Present',
            'description': '-	Lead a 2-person cross-functional team using Agile workflows and Git version control to digitalize pen & paper inventory system, addressing manual tracking inefficiencies that generated 2 additional client prospects within first quarter.',
            'highlights': [
                'Integrate real-time dashboards to track inventory and forecast revenue using linear regression, reducing daily decision-making time from 3 to 2 hours and uncovering $3K in potential cost savings.',
                'Design full-stack tracking solution with Figma wireframes and user flow diagrams, automating 5 core inventory processes and achieving 99% stock accuracy (up from 60% manual accuracy).'
            ],
            'image': 'laptop-code.jpg',
            'github_url': 'https://github.com/hoangv1atwit/inventory-tracking-system',
            'demo_url': 'https://mywentworth-my.sharepoint.com/:p:/g/personal/hoangv1_wit_edu/EeE3TAIaz69BtcMelT6mUDQBj8n3lJYAhnZ-E3BDi2GSrQ?e=cLLXYH',
            'status': 'In Development',
            'featured': True
        },
        {
            'title': 'Urban Renewal VR Experience',
            'technologies': ['Unity', 'Meta Quest VR', 'C#', 'Agile'],
            'period': 'Jan 2025 – April 2025',
            'description': '-	Launched VR product featuring 5 interactive environments and 15+ engagement elements, validated by 10+ beta testers to bridge history with immersive storytelling.',
            'highlights': [
                '-	Collaborated with the West End Museum and a 4-person development team to create immersive 3D visualizations of the neighborhood, earning 90%+ approval from 8 historical consultants via iterative feedback and quality assurance processes.'
            ],
            'image': 'vr-code.jpg',
            'github_url': 'https://github.com/vyhoang/urban-renewal-vr',
            'demo_url': '#',
            'status': 'Completed',
            'featured': True
        },
        {
            'title': 'Learning Management System Initiative',
            'technologies': ['Microsoft Excel', 'Microsoft Project', 'Trello', 'Power BI'],
            'period': 'Sep 2024 – Dec 2024',
            'description': 'Led vendor evaluation of 3 LMS platforms via scoring matrix (12 criteria including usability, scalability, and integrations), ensuring technical fit for stakeholder requirements.',
            'highlights': [
                'Drove product strategy by conducting market research (150+ surveys, 25+ stakeholder interviews), synthesizing insights into user stories and prioritizing backlog to align roadmap with user needs.',
                '-	Streamlined project communication via Trello and developed automated Power BI reporting from user analytics, accelerating stakeholder decision timelines by 20%.'
            ],
            'image': 'data-analysis.jpg',
            'github_url': 'https://github.com/vyhoang/lms-initiative',
            'demo_url': 'https://lms-analysis.vyhoang.dev',
            'status': 'Completed',
            'featured': True
        }
    ]
    
    # Additional projects (shown when "View All Projects" is clicked)
    additional_projects = [
        {
            'title': 'English Marble Solitaire',
            'technologies': ['Java', 'JavaScript', 'HTML5', 'CSS3', 'Bootstrap', 'MVC'],
            'period': 'Sep 2023 – Dec 2023',
            'description': 'Architected and translated Java-based English Marble Solitaire game from Model-View-Controller framework to interactive web application, demonstrating proficiency in both object-oriented Java programming and modern JavaScript.',
            'highlights': [
                'Implemented Model-View-Controller design pattern by porting Java classes into JavaScript modules',
                'Developed responsive web interface with advanced game mechanics including real-time move validation algorithms, hint system, and state management',
                'Successfully bridged backend Java logic with frontend technologies to create a fully functional browser-based game application'
            ],
            'image': 'game.jpg',
            'github_url': 'https://github.com/hoangv1atwit/EnglishMarbleSolitaire',
            'demo_url': 'https://marble-solitaire.vyhoang.dev',
            'status': 'Completed',
            'featured': False
        },
        {
            'title': 'Audience Engagement System',
            'technologies': ['JavaScript', 'Chart.js', 'HTML', 'CSS', 'Analytics', 'Agile'],
            'period': 'Jan 2024 – May 2024',
            'description': 'Integrated software that records daily audience engagement statistics from client\'s website and displays graphs based on readings like page views, session duration and geographic source over time.',
            'highlights': [
                'Implemented Agile development methodologies, managing 4 two-week sprints with a cross-functional team of 4 students, achieving 100% sprint completion rate',
                'Launched the finished system on time and obtained a client satisfaction score of 4.5/5 based on its ability to provide requested insights',
                'Built comprehensive analytics dashboard with real-time data visualization capabilities'
            ],
            'image': 'analytics.jpg',
            'github_url': 'https://github.com/vyhoang/audience-engagement-system',
            'demo_url': 'https://engagement-analytics.vyhoang.dev',
            'status': 'Completed',
            'featured': False
        },
        {
            'title': 'Portfolio Website',
            'technologies': ['Flask', 'Python', 'HTML', 'CSS', 'JavaScript', 'Bootstrap'],
            'period': 'Dec 2024 – Present',
            'description': 'Personal portfolio website built with Flask to showcase projects, experience, and technical skills with modern web technologies.',
            'highlights': [
                'Responsive design with modern UI/UX principles',
                'Dynamic content management with Flask templating',
                'Optimized performance and accessibility'
            ],
            'image': 'portfolio.jpg',
            'github_url': 'https://github.com/hoangv1atwit/portfolio-website',
            'demo_url': 'https://evelynhoangvy.space',
            'status': 'Completed',
            'featured': False
        }
    ]
    
    # Combine all projects for data passing
    all_projects = featured_projects + additional_projects
    
    # Technical skills
    technical_skills = {
        'Languages': ['Java', 'Python', 'SQL', 'C', 'HTML', 'CSS', 'JavaScript', 'PHP', 'Swift', 'Bash', 'PowerShell'],
        'Databases & Frameworks': ['AWS', 'JUnit', 'UIKit', 'PostgreSQL', 'MSSQL', 'Oracle', 'Linux'],
        'Tools': ['Git', 'Jira', 'Figma', 'SketchUp', 'Adobe', 'Trello', 'Power BI', 'Salesforce', 'Unity', 'Bloomberg Terminal']
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
        'location': 'Boston, MA',
        'phone': '857-234-5331',
        'email': 'hoangv1@wit.edu',
        'linkedin': 'linkedin.com/in/vybaohg'
    }
    
    return render_template('index.html', 
                         work_experiences=work_experiences,
                         featured_projects=featured_projects,
                         all_projects=all_projects,
                         technical_skills=technical_skills,
                         education=education,
                         contact_info=contact_info)
