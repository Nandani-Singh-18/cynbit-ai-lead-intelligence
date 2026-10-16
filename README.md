# Cynbit AI Lead Intelligence

An AI/ML proof of concept that classifies business inquiries, identifies priority levels, and suggests follow-up actions.

## Problem Statement

Technology service providers receive inquiries covering different services and urgency levels. Manually categorizing and reviewing each inquiry can lead to inconsistent triage. This prototype demonstrates how machine learning and rule-based automation can support that workflow.

## Features

- Text-based service-category classification.
- TF-IDF feature extraction and Logistic Regression.
- Rule-based High, Medium, and Low priority assignment.
- Urgency explanation and recommended next steps.
- Streamlit user interface.
- Automated tests using pytest.

## Technology Stack

- Python
- scikit-learn
- Streamlit
- pytest

## Service Categories

- Web Development
- Mobile App Development
- AI Automation
- Cloud and SaaS

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Nandani-Singh-18/cynbit-ai-lead-intelligence.git
cd cynbit-ai-lead-intelligence
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the tests

```bash
python -m pytest test_model.py -v
```

### 5. Start the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## Technical Approach

The prototype uses TF-IDF to convert text into numerical features and Logistic Regression to predict a service category. Separate keyword-based rules assign priority levels. The application then displays the results and suggests a next step.

The current response mechanism uses predefined templates. An LLM-based response generator is a potential future enhancement, not a current feature.

## Testing

The current test suite contains six tests covering two service categories, three priority levels, and empty inquiry handling.

## Limitations

- The training data is small and synthetic.
- Classification and priority rules require evaluation on representative real-world data.
- The prototype does not establish production CRM integration.
- The current version does not use a generative LLM.
- Production performance and business impact have not yet been measured.

## Future Improvements

- Evaluate the model using a representative labeled dataset.
- Add precision, recall, macro F1-score, and confusion-matrix analysis.
- Improve priority detection and support human correction.
- Explore optional LLM-assisted summarization.
- Evaluate authorized CRM integration and deployment.

## AI Opportunity Analysis

See [AI Opportunity Report](AI_Opportunity_Report.md) for the business opportunity comparison and use-case justification.

See [Technical Approach Report](Technical_Approach_Report.md) for architecture, model selection, data pipeline, evaluation, and execution planning.

## Public References

- https://www.cynbit.in/services
- https://www.cynbit.in/careers/ai-ml-engineer-intern

This project is an independent proof of concept developed for an AI/ML assessment. It is not represented as an existing internal Cynbit system.