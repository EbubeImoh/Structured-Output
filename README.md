# Google ADK Structured Output Tester

A project demonstrating and testing various structured output capabilities within Google's Agent Development Kit (ADK). This agent showcases how to receive structured data from a Gemini model.

📝 **Description**

The `Structured Output` project serves as a practical guide and testbed for implementing structured outputs with Google ADK. It illustrates how to configure an agent to interact with a Gemini model (e.g., `gemini-1.5-flash-latest`) and receive responses in predefined formats such as JSON, custom Python objects (using Pydantic models or dataclasses), lists, and more.

This project aims to:
*   Demonstrate how to define `OutputType` for your agent.
*   Provide clear examples of prompting strategies to elicit structured responses from the LLM.
*   Show how the ADK handles and parses these structured outputs.
*   Offer a base for developers to experiment with and validate their own structured output implementations.

✨ **Features**

*   **Multiple Output Type Demonstrations:** Includes examples for:
    *   JSON objects
    *   Custom Python classes (e.g., Pydantic models)
    *   Lists of items/strings
*   **Gemini-Powered:** Utilizes a configurable Gemini model (defaulting to `gemini-1.5-flash-latest`) for generating structured data.
*   **Clear Interaction Flows:** Designed with specific commands or conversational paths to trigger and display different structured output types.
*   **ADK Best Practices:** Showcases the integration of structured outputs within the `google.adk.agents.Agent` framework.
*   **Educational Tool:** Helps developers understand the nuances of prompting for and handling structured data from LLMs in an ADK environment.

📁 **Project Structure**

```
Structured Output/
├── email_agent/
│   ├── __init__.py              # Makes the module importable
│   ├── agent.py                 # Core agent logic, defines interaction paths for each output typ
│   └── .env                     # Defines environment variables
└── README.md
```

plaintext

*   `email_agent/__init__.py`: Makes the `Structured Output` directory a Python package.
*   `email_agent/agent.py`: Contains the main agent definition, including its methods for handling user input and generating responses with different structured output types.

⚙️ **Requirements**

*   Python 3.9+
*   `google-adk`
*   `pydantic` (if using Pydantic models for structured outputs, often a good choice)

🚀 **Setup and Installation**

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd Structured Output
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Create a `.env` file** in the root directory with your Google API Key:
    ```env
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

4.  **Install dependencies:**
    ```bash
    pip install google-adk pydantic
    ```

💬 **Usage**

1.  **Activate the virtual environment** (if not already active):
    ```bash
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

2.  **Run the agent using the ADK CLI:**
    ```bash
    adk run email_agent
    ```

📌 **Notes**

*   This project is designed to be a starting point and a reference for using structured outputs effectively with Google ADK.
*   Examine `agent.py` to see how different `OutputType`s are defined and used in agent methods
*   You can easily extend this project by adding more complex structured output types or more sophisticated prompting techniques.

🧠 **Author**

Ebube Imoh
*   GitHub: [https://github.com/EbubeImoh]
*   LinkedIn: [https://www.linkedin.com/in/ebubeimoh/]