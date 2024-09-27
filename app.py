import os
import streamlit as st
from google.generativeai import configure, GenerativeModel
import base64



# Set your API key as an environment variable
os.environ['GENAI_API_KEY'] = 'AIzaSyDzeATPLWRenJGapH8wOCtKEs_QFf6FPR0'  # Replace with your actual API key

# Configure the SDK with the API key
api_key = os.getenv('GENAI_API_KEY')
configure(api_key=api_key)

# Define generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model
model = GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[]
)
knowledge_base = {
    "name": "Anurag Srivatsav",
    "contact": {
        "phone": "9581403857",
        "email": "anuragsrivatsav4@gmail.com",
        "linkedin": "https://linkedin.com/in/anuragsrivatsav",
        "github": "https://github.com/anurag-srivatsav",
    },
    "education": {
        "university": "KL University Hyderabad",
        "degree": "B.Tech in Artificial Intelligence and Data Science",
        "GPA": "8.36/10",
        "graduation_date": "July 2025",
    },
    "experience": [
        {
            "role": "Amazon ML Summer School-Participant",
            "organization": "Amazon ML Summer School",
            "duration": "September 2023 - October 2023",
            "details": [
                "Engaged with 10 advanced machine learning models and techniques.",
                "Collaborated with 5 ML scientists.",
            ],
        },
        {
            "role": "Google Cloud Ready Facilitator",
            "organization": "Google",
            "duration": "February 2022 - Present",
            "details": [
                "Explored Google Cloud Platform applications.",
                "Contributed to 70% of cloud platform endeavors.",
                "Completed weekly and monthly Google Cloud skill boost challenges.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Task Manager Application with MongoDB",
            "duration": "February 2023 - March 2023",
            "technologies": ["Python", "MongoDB", "Flask"],
            "details": [
                "Developed a web app for task management.",
                "Integrated features like task addition, completion tracking, and secure user authentication.",
            ],
            "link": "https://github.com/anurag-srivatsav/MongoDb-UserManagement",
            "View live site":"https://mongousermanagement.streamlit.app/",
        },
        {
            "name": "AI Voice Clone",
            "duration": "December 2023 - February 2024",
            "technologies": ["Python", "Google's Generative AI", "LangChain", "PlayHT"],
            "details": [
                "Implemented an AI voice clone application.",
                "Engineered a customizable voice clone using advanced NLP techniques.",
            ],
            "link": "https://github.com/anurag-srivatsav/EchoClone-AI",
            "View live site":"https://echoclone-ai.streamlit.app/",
        },
        {
            "name": "TEXT to HTML converter",
            "duration": "February 2023 - April 2023",
            "technologies": ["Django"],
            "details": [
                "Designed and implemented a TEXT to HTML converter using Django framework.",
                "Implemented functionality to convert text input into HTML format.",
                "Integrated user-friendly interface for easy input and output interaction."
            ],
            "link": "https://github.com/anurag-srivatsav/Text2Html",
            "View live site":"https://anuragportfoli04.netlify.app/",
        },
        {
            "name": "Image Classification (Cat vs. Dog)",
            "duration": "March 2023 - May 2023",
            "technologies": ["Python", "TensorFlow", "Keras"],
            "details": [
                "Developed a deep learning model to classify images of cats and dogs.",
                "Preprocessed a dataset of cat and dog images for training and validation.",
                "Implemented data augmentation techniques to improve model generalization.",
                "Evaluated model performance using metrics like accuracy and loss."
            ],
            "link": "https://github.com/anurag-srivatsav/image-classification",
            "View live site":"https://anuragportfoli04.netlify.app/",
        },
        {
            "name": "My Portfolio Website",
            "duration": "May 2024",
            "technologies": ["JavaScript", "HTML", "CSS"],
            "details": [
            "Designed and developed a personal portfolio website showcasing my education, skills, projects, and certifications.",
            "Implemented responsive web design techniques to ensure compatibility across various devices and screen sizes.",
            "Integrated interactive sections for dynamic project displays, including links to GitHub repositories and live demos.",
            "Utilized JavaScript for smooth navigation and animations, enhancing user experience."
            ],
            "link": "https://github.com/anurag-srivatsav/MyPortfolio",
            "View live site":"https://anuragportfoli04.netlify.app/",
}
    ],
    "skills": {
        "languages": [ "Python", "Java", "R", "C"],
        "frameworks": ["Django", "React.js", "Node.js", "TensorFlow"],
        "databases": ["MySQL", "MongoDB", "Oracle"],
        "web": ["HTML", "CSS", "JavaScript", "Tableau", "Power BI"],
        "Cloud": ["Google Cloud", "Azure", "AWS"],
        "DS & AI": ["TensorFlow", "Machine Learning", "Artificial Intelligence"],
        "Other": ["Git", "Jupyter Notebook", "Docker"]
    },
    "certifications": [
        {
            "name": "Google Cloud Data Analytics Certificate",
            "link": "https://www.credly.com/badges/97a889b4-6069-4118-9b29-3f7de7a3cc23"
        },
        {
            "name": "Google TensorFlow Developer Certificate",
            "link": "https://www.credential.net/d81c83e2-673f-475f-a6dc-bf5ffafc81b7#gs.ak34mm"
        },
        {
            "name": "Oracle Cloud Infrastructure 2024 Generative AI Certified Professional",
            "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B3BBAE0554318278F137B99606886BC7FC"
        },
        {
            "name": "Microsoft Certified: Azure AI Fundamentals",
            "link": "https://learn.microsoft.com/en-us/users/anuragsrivatsav-6772/credentials/b42af8fa0151a887?ref=https%3A%2F%2Fwww.linkedin.com%2F"
        },
        {
            "name": "Advanced Automation Certification",
            "link": "https://certificates.automationanywhere.com/a02047c5-a380-4ebb-a15e-44da8fd0a097"
        },
        {
            "name": "Oracle Cloud Infrastructure 2023 Certified Architect Associate",
            "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B33C5B29DDB470072B0A3CDB447E72BBE0"
        },
        {
            "name": "Google AI Essentials",
            "link": "https://www.credly.com/badges/2e2258c6-8d4b-4be0-ba97-8dfaea5f5116"
        },
        {
            "name": "CS50’s Introduction to Programming with Python",
            "link": "https://certificates.cs50.io/c54c3ae3-1816-42b1-b3db-316da4b49055.pdf"
        },
        {
            "name": "NoSQL - MongoDB",
            "link": "https://courses.etrain.skillsnetwork.site/certificates/8a07367606c641cfa29e468a11de8179"
        }
    ]
}

# Function to check the knowledge base for answers
def check_knowledge_base(question, user_name):
    question = question.lower()

    name_keywords = ["name", "who are you", "what is your name", "tell me your name"]
    contact_keywords = ["contact", "email", "phone", "reach you","how can I reach you","contact details","phone number","email address","linkedin profile","github profile"]
    education_keywords = ["education", "study", "schooling", "university", "college","where did you study","your schooling","educational background","college details","clg","academic background","educational qualifications"]
    experience_keywords = ["experience", "work", "job", "role", "position","previous work","jobs you've had","your role","work experience","positions held"]
    projects_keywords = ["projects", "project", "work","show me your projects","what projects have you worked on","details of your projects","your work examples"]
    skills_keywords = ["skills", "abilities", "proficiencies","what are your skills","your abilities","proficiency areas","what can you do"]
    certifications_keywords = ["certifications", "certificates", "credentials","what certifications do you have","your certificates","credentials you hold","certification details"]
    about_me_keywords = ["about yourself", "about me","about you", "u", "about", "tell me about yourself","who are you","introduce yourself","personal details"]
    resume_keywords=["Resume",'cv',"show me your resume", "show me your CV"]

    if any(keyword in question for keyword in name_keywords):
        return f"My name is Anurag Srivastav Thammera."
    elif any(keyword in question for keyword in contact_keywords):
        return f"You can reach me through mail: {knowledge_base['contact']['email']} \n\n phn No. : {knowledge_base['contact']['phone']}  \n\n Linkedin: {knowledge_base['contact']['linkedin']}  \n\n Github: {knowledge_base['contact']['github']}"
    elif any(keyword in question for keyword in education_keywords):
        return f"I am currently pursuing a Bachelor of Technology in Artificial Intelligence and Data Science at KL University in Hyderabad, maintaining a GPA of 8.36 out of 10, with an expected graduation date in July 2025."
    elif any(keyword in question for keyword in experience_keywords):
        experience = knowledge_base["experience"]
        return "\n".join([f"I worked as a {exp['role']} at {exp['organization']} from {exp['duration']}.\n\n" for exp in experience])
    elif any(keyword in question for keyword in projects_keywords):
        projects = knowledge_base["projects"]
        response = ""
        for proj in projects:
            response += f"\n\n Project :  {proj['name']} - Duration: {proj['duration']} - Technologies: {', '.join(proj['technologies'])}. \n\n Link: {proj['link']}\n\n  live site: {proj['View live site']}"
        return response
    elif any(keyword in question for keyword in skills_keywords):
        return f"My skills include: \n\n Languages: {', '.join(knowledge_base['skills']['languages'])}\n\n Frameworks: {', '.join(knowledge_base['skills']['frameworks'])}\n\n Databases: {', '.join(knowledge_base['skills']['databases'])}\n\n Web: {', '.join(knowledge_base['skills']['web'])}\n\n cloud: {', '.join(knowledge_base['skills']['Cloud'])}\n\n DS & AI: {', '.join(knowledge_base['skills']['DS & AI'])}, {', '.join(knowledge_base['skills']['Other'])}."
    elif any(keyword in question for keyword in certifications_keywords):
        certifications = knowledge_base["certifications"]
        response = ""
        for cert in certifications:
            response += f"\n\nCertification name : {cert['name']}.\n\n Link: {cert['link']}\n\n"
        return response
    elif any(keyword in question for keyword in about_me_keywords):
        return f"My name is Anurag Srivastav. \n\n Final year BTech student specializing in Artificial Intelligence and Data Science at {knowledge_base['education']['university']}, with a strong academic background and practical experience in machine learning, deep learning, and statistical modeling.\n\n Seeking opportunities to apply analytical skills and contribute to innovative projects in AI-driven solutions. \n\n I have experience in  {', '.join([exp['role'] for exp in knowledge_base['experience']])}. \n\n My projects include {', '.join([proj['name'] for proj in knowledge_base['projects']])}. \n\n I have skills in {', '.join(knowledge_base['skills']['languages'])}, {', '.join(knowledge_base['skills']['frameworks'])}, {', '.join(knowledge_base['skills']['databases'])}, and {', '.join(knowledge_base['skills']['web'])}. I am interested in AI and data science-related jobs."
    elif any(keyword in question for keyword in resume_keywords):
        st.write("You can download the resume by clicking the button below:")
        
        pdf_file_path = "AnuragSrivastav_Resume.pdf"  # Update this with your actual file path
        with open(pdf_file_path, "rb") as pdf_file:
            st.download_button(label="Download Resume", data=pdf_file, file_name="Anurag_Srivastav_Resume.pdf", mime="application/pdf")
        st.write("Here's a preview of my resume:")
        

        # Optionally, use an iframe to embed the PDF directly in the page
        st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_file_path, "rb").read()).decode()}" width="700" height="900" type="application/pdf"></iframe>', unsafe_allow_html=True)
        return None
        
        
        
        
    

    else:
        return None
    
# Streamlit app

st.title('Questions about me? Shoot—I\'m here with all the answers!')



# Sidebar with description
st.sidebar.header("About the App:")

st.sidebar.write("""
This is an interactive AI profile bot. \n
Ask any questions about Anurag Srivatsav, and the bot will provide answers based on the preloaded knowledge base or generate responses using AI.
""")

st.sidebar.header("Choose a topic you wanna ask:")

st.sidebar.markdown(""" Name,  Education,   Contact, Experience
                 Skills,  Projects,  About me, Resume or CV """)


    



st.sidebar.image('https://res.cloudinary.com/dvlgixtg8/image/upload/v1721021639/chatbot.png', use_column_width=True)

# URL to redirect to
url = 'https://anuragportfoli04.netlify.app/'  # Replace with your desired URL

# Adding a button to redirect to another URL
if st.sidebar.button('Back to Portfolio'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)



url = 'https://echoclone-ai.streamlit.app/'  # Replace with your desired URL

st.markdown(
    """
    <style>
    .styled-text {
        font-size: 18px; /* Change font size */
        color: skyblue; /* Change text color */
        font-weight: bold; /* Make the text bold */
        
        margin-bottom: 20px; /* Add space below */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use markdown to display the styled text in the sidebar
st.sidebar.markdown('<p class="styled-text">Wanna explore my Unique Voice Assistant? Check it out now!</p>', unsafe_allow_html=True)
# Adding a button to redirect to another URL
if st.sidebar.button('EchoClone AI🎧'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)


    
# Initialize session state

# Initialize session state for chat history and user name
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

# Function to interact with the generative model
@st.cache_resource
def start_chat():
    chat_session = model.start_chat(history=[])
    return chat_session

# Main interaction loop
chat_session = start_chat()

# User name input only if not already entered
if not st.session_state['user_name']:
    st.session_state['user_name'] = st.text_input('Enter your name here to enhance your interaction before posing your query: 📝🧑‍💼', '')

if st.session_state['user_name']:
    st.write(f"Hello, {st.session_state['user_name']}! Ask me anything.")
    user_input = st.text_input('Now, go ahead and enter your query: 🔍', '')

    if st.button('Send'):
        if user_input:
            # Display loading spinner while waiting for the bot's response
            with st.spinner('Nani is typing...'):
                time.sleep(2)  # Simulate delay for response

                # Check the knowledge base first (replace with actual function if needed)
                kb_response = check_knowledge_base(user_input, st.session_state['user_name'])
                if kb_response:
                    bot_response = kb_response
                else:
                    # Prefix user input with their name
                    user_message = f"{st.session_state['user_name']}: {user_input}"
                    response = chat_session.send_message(user_message)
                    bot_response = response.text

            # Update chat history
            st.session_state['chat_history'].append((f"{st.session_state['user_name']}", user_input))
            st.session_state['chat_history'].append(('Nani', bot_response))

            # Display user message and bot response
            conversation = f"{st.session_state['user_name']}: {user_input}\n\nNani: {bot_response}"
            st.markdown(conversation, unsafe_allow_html=True)

    # Display chat history
    st.write('')
    st.subheader("Chat History:")
    st.markdown("""
<hr style="border-top: 3px solid #bbb;"> 
""", unsafe_allow_html=True)
    for idx, (role, text) in enumerate(st.session_state['chat_history']):
        st.write(f"{role}: {text}")
        if idx % 2 == 1:
            st.write("---")  # Add a line to differentiate entries


    

# Markdown with HTML for footer
st.markdown("""
<br><br>
<div style="text-align:center;">
    <p>&copy; 2024 Anurag Srivatsav. All rights reserved.</p>
    <p>Meet Nani: Your AI-Driven Profile Assistant 🤖🧠</p>
    <p>Connect with me on LinkedIn: <a href="https://linkedin.com/in/anuragsrivatsav" target="_blank">Anurag Srivatsav</a></p>
</div>
""", unsafe_allow_html=True)
