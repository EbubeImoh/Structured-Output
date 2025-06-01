# Google ADK Structured Output Tester

A project demonstrating and testing various structured output capabilities within Google's Agent Development Kit (ADK). This agent showcases how to receive structured data from a Gemini model.

📝 **Description**

The `adk-structured-output-tester` project serves as a practical guide and testbed for implementing structured outputs with Google ADK. It illustrates how to configure an agent to interact with a Gemini model (e.g., `gemini-1.5-flash-latest`) and receive responses in predefined formats such as JSON, custom Python objects (using Pydantic models or dataclasses), lists, and more.

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

adk-structured-output-tester/ ├── structured_output_tester/ │ ├── init.py # Makes the module importable │ ├── agent.py # Core agent logic, defines interaction paths for each output type │ ├── structured_outputs.py # Defines Pydantic models or dataclasses for custom outputs │ └── prompts.py # Contains prompt templates for eliciting structured data └── README.md

plaintext

*   `structured_output_tester/__init__.py`: Makes the `structured_output_tester` directory a Python package.
*   `structured_output_tester/agent.py`: Contains the main agent definition, including its methods for handling user input and generating responses with different structured output types.
*   `structured_output_tester/structured_outputs.py`: Defines the Python classes (e.g., Pydantic models or dataclasses) that represent the structure of the expected outputs from the LLM.
*   `structured_output_tester/prompts.py`: Stores the prompt templates used to instruct the LLM to generate data in the desired structured formats.

⚙️ **Requirements**

*   Python 3.9+
*   `google-adk`
*   `pydantic` (if using Pydantic models for structured outputs, often a good choice)

🚀 **Setup and Installation**

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd adk-structured-output-tester
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
    adk run structured_output_tester
    ```

**Example Interaction:**

The agent might guide you through different structured output demonstrations.

You: Hello Agent: Welcome to the Structured Output Demonstrator! I can show you how the LLM responds with different data structures. What would you like to see? 1. User Profile (JSON output) 2. Product Information (Custom Object output) 3. List of Tags (List of strings output) Please enter a number or describe what you want.

You: 1 Agent: Great! I'll ask the LLM for a sample user profile in JSON format. ... Agent: Here's the user profile as JSON: json { "userId": "user123", "username": "alex_g", "email": "alex.g@example.com", "preferences": { "theme": "dark", "notifications": true } }

You: Show me product information Agent: Okay, I'll request product information structured as a custom object. ... Agent: Here's the product information: Product(name='Wireless Headphones', price=99.99, currency='USD', in_stock=True, features=['Bluetooth 5.0', 'Noise Cancelling', '20-hour battery'])

You: Can you give me a list of tags for "adventure travel"? Agent: Sure, I'll get a list of relevant tags. ... Agent: Here are some tags for "adventure travel": ['hiking', 'exploration', 'mountaineering', 'safari', 'extreme sports', 'backpacking']

plaintext

📌 **Notes**

*   This project is designed to be a starting point and a reference for using structured outputs effectively with Google ADK.
*   Examine `agent.py` to see how different `OutputType`s are defined and used in agent methods.
*   Review `structured_outputs.py` for examples of how to define the schemas for your data (e.g., using Pydantic).
*   The quality of structured output heavily depends on the clarity and specificity of your prompts in `prompts.py`.
*   You can easily extend this project by adding more complex structured output types or more sophisticated prompting techniques.

🧠 **Author**

Ebube Imoh
*   GitHub: [Your GitHub Profile URL]
*   LinkedIn: [Your LinkedIn