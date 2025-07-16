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
    
    # Featured projects (shown by default)
    featured_projects = [
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
            'github_url': 'https://github.com/hoangv1atwit/inventory-tracking-system',
            'demo_url': 'https://inventory-demo.vyhoang.dev',
            'status': 'In Development',
            'featured': True
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
            'status': 'Completed',
            'featured': True
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
        'Databases & Frameworks': ['AWS', 'JUnit', 'UIKit', 'MySQL', 'MSSQL', 'Oracle', 'Linux'],
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
        'location': 'Brighton, MA',
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
