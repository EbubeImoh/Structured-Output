from google.adk.agents import Agent
from pydantic import BaseModel, Field

# === Define Outpyt Schema ===
class EmailContent(BaseModel):
    subject: str = Field(
        description='The subject line of the email. Should be concise and relevant to the content.'
    )
    body: str = Field(
        description='The main content of the email. Should be well formatted with proper greeting, paragraph, and signature.'
    )

# === Define Email Generator Agent ===
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='email_agent',
    instruction="""
        You are an email generator assistant.
        Your task is to generate a well-structured email based on the user's provided content. 
        Ensure that the email has a clear subject line and a well-formatted body with appropriate greetings and signatures.
        
        GUIDLINES:
        - Create an appropriate subject lline that summarizes the email content.
        - Write a well structured email body that includes:
            1. A professional greeting
            2. A clear and concise message body
            3. A polite closing statement
            4. A signature with the sender's name
        - Suggest relevant attachements if applicable (empty list if none needed)
        - Ensure the email is professional and suitable for business communication.
        - Keep emails concise and to the point, avoiding unnecessary jargon or complexity.

        IMPORTANT: Your response MUST be valid JSON that matches this schema:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper formatting including greeting, message, closing, and signature."
        }

        DO NOT include any explanation or additional text outside of the JSON response.
        """,
    description="Generate professional emails with structured subject and body.",
    output_schema=EmailContent,
    output_key="email",
)
