# Technical Approach Report — Cynbit AI Lead Intelligence

## 1. Project Overview

**Project:** AI Lead Intelligence and Qualification Assistant  
**Technology:** Python, scikit-learn, Streamlit, pandas (if used in the implementation), and pytest  
**Project Type:** AI/ML Proof of Concept (PoC)

The objective is to demonstrate how incoming business inquiries can be categorized and prioritized using natural language processing, machine learning, and transparent business rules.

The application accepts inquiry text and returns a predicted service category, priority level, urgency explanation, and recommended next step.

The current prototype is designed for demonstration and evaluation. It is not a production-ready lead management system.

## 2. System Architecture

The application consists of the following logical components:

1. **User Interface:** Streamlit accepts inquiry text and displays the results.
2. **Text Preprocessing and Feature Extraction:** TF-IDF converts the inquiry text into numerical features.
3. **Category Classification:** Logistic Regression predicts the most likely service category.
4. **Priority Assessment:** Keyword-based rules assign High, Medium, or Low priority.
5. **Explanation and Recommendation:** The application explains the priority decision and suggests a next action.
6. **Response Generation:** A predefined template provides the response; the current version does not use a generative LLM.
7. **Testing:** pytest checks category prediction, priority behavior, and empty input handling.

### Architecture Flow

User enters inquiry  
→ Streamlit interface  
→ Text processing and TF-IDF  
→ Logistic Regression category prediction  
→ Rule-based priority assessment  
→ Explanation and recommended next step  
→ Results displayed to the user

The category prediction and priority assignment are separate components. This makes the application easier to test and allows priority rules to be updated without redesigning the classifier.

## 3. Model Selection

### 3.1 TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** converts text into numerical features based on word importance within a document relative to the document collection.

TF-IDF is suitable for this PoC because it is lightweight, easy to implement, and works well as a baseline for text classification.

Advantages:
- Computationally inexpensive.
- Easy to combine with traditional machine-learning models.
- Does not require a GPU or paid API.
- Provides a useful baseline for short inquiry text.

Limitations:
- May not understand context, intent, or complex semantic relationships.
- Unseen wording and synonyms may reduce classification quality.
- Performance depends on training-data coverage.

### 3.2 Logistic Regression

Logistic Regression is a supervised classification algorithm that estimates class probabilities from input features.

It is selected because it is efficient, interpretable relative to many complex models, and suitable for a small text-classification baseline.

The classifier predicts one of the configured service categories:

- Web Development
- Mobile App Development
- AI Automation
- Cloud and SaaS

The model's predicted category is based on the patterns learned from its training examples. Because the current training dataset is small and synthetic, its predictions and confidence values should not be treated as validated business intelligence.

### 3.3 Rule-Based Priority Assessment

The prototype uses keyword-based rules to assign High, Medium, or Low priority.

This approach is transparent and easy to demonstrate. For example, configured urgency-related terms may trigger a higher priority, while other inquiries receive a lower or intermediate priority according to the implemented rules.

However, keyword matching can miss implied urgency or incorrectly interpret words in context. Priority rules should be reviewed against real, appropriately labeled examples before operational use.

### 3.4 Why Not Start With an LLM?

An LLM could support summarization, response drafting, and more context-aware inquiry interpretation. However, it may require API access, incur costs, introduce latency, and produce unsupported statements.

A TF-IDF and Logistic Regression baseline provides a simple, reproducible starting point without an external model dependency. An LLM can be evaluated as a future extension rather than being represented as an existing feature.

## 4. Data Pipeline

### Current Pipeline

1. Receive inquiry text through the Streamlit interface.
2. Validate the input and handle empty inquiries.
3. Pass the text through the configured TF-IDF feature extractor.
4. Use the trained Logistic Regression classifier to predict the service category.
5. Apply the implemented priority rules to the inquiry.
6. Generate the urgency explanation and recommended next step.
7. Display the results in the interface.

### Training Data

The current prototype uses a small synthetic dataset of example inquiries. Synthetic data is useful for developing and demonstrating a pipeline without exposing confidential customer information.

It is not sufficient to establish production-level performance or represent the full variety of real business inquiries.

### Future Production Pipeline

A production implementation would require an approved dataset of representative inquiries with verified service-category labels.

The data should be checked for:
- Missing or invalid text.
- Duplicate and inconsistent records.
- Incorrect category labels.
- Class imbalance.
- Personal or confidential information that should be removed or masked.

Training and test data should be separated before model evaluation. Any preprocessing or feature-learning steps must be fitted using training data only to prevent data leakage.

## 5. Prompt Engineering and Response Generation

### Current Implementation

The current prototype uses predefined response templates and rule-based recommendations. It does **not** currently send prompts to an LLM or generate responses using a generative AI model.

This distinction is important because the existing system is a machine-learning classification and rule-based automation PoC.

### Proposed Future LLM Extension

An LLM could be introduced to summarize inquiries or draft a suggested response after the category and priority have been determined.

A possible prompt template would be:

**Role:** You are an assistant helping a technology services team review business inquiries.

**Input fields:**
- Inquiry text
- Predicted service category
- Assigned priority
- Available company service information

**Instructions:**
1. Summarize the customer's requirement in plain language.
2. Identify the information that is missing.
3. Suggest a relevant next step.
4. Do not invent prices, delivery dates, service commitments, or company policies.
5. If the information is insufficient, recommend human review.
6. Return a structured response with a summary, missing information, and recommended action.

**Output format:** A structured object containing `summary`, `missing_information`, and `recommended_action`.

This is a proposed design for future work, not a feature currently implemented in the repository. If developed, it should be tested for factual accuracy, consistency, privacy, and resistance to misleading input.

## 6. Evaluation and Testing

The repository includes automated tests in `test_model.py`. The current test suite contains six passing tests covering:

- Web Development category prediction.
- AI Automation category prediction.
- High-priority detection.
- Medium-priority detection.
- Low-priority detection.
- Empty inquiry handling.

These tests validate selected functional behaviors. They do not establish that the model performs accurately on unseen real-world inquiries.

### Recommended Model Evaluation

For a larger labeled dataset, evaluate the classifier using:

- Accuracy.
- Per-class precision and recall.
- Macro F1-score.
- Confusion matrix.
- Error analysis of incorrectly classified inquiries.

The dataset should contain examples not used during model training. Evaluation should also include varied phrasing, spelling errors, short inquiries, ambiguous requests, and examples that do not clearly match any configured category.

### Recommended Priority Evaluation

Compare the rule-based priority output with priority labels reviewed by business stakeholders. Measure false-high and false-low assignments, especially for inquiries where urgency affects customer experience.

No accuracy percentage or business improvement should be reported until it has been measured on suitable evaluation data.

## 7. Execution Plan

### Phase 1 — Functional Prototype
- Implement the text-classification pipeline.
- Add priority rules and recommendations.
- Build the Streamlit interface.
- Add automated tests.

### Phase 2 — Model Validation
- Collect approved and representative labeled data.
- Split the dataset into training and evaluation sets.
- Measure classification metrics.
- Review and correct common errors.

### Phase 3 — Usability and Integration
- Gather feedback from potential users.
- Improve explanations and error handling.
- Add optional storage and authorized CRM integration.
- Maintain human review for important decisions.

### Phase 4 — Advanced AI Features
- Evaluate LLM-assisted summarization and response drafting.
- Add structured outputs and validation.
- Monitor hallucinations, privacy, latency, and costs.
- Compare the extended approach with the existing baseline.

## 8. Deployment and Reproducibility

The project is maintained in a GitHub repository. The repository should include the application code, model logic, tests, dependency list, and documentation.

### Local Setup

Run these commands from the project directory in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -v
streamlit run app.py
```

If PowerShell prevents virtual-environment activation, use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

Then install the requirements and run the tests and Streamlit application as shown above.

The required Python packages should be listed in `requirements.txt`. A public GitHub repository enables reviewers to inspect and run the project. A live demo should only be described as deployed after deployment has been completed and verified.

## 9. Limitations

The current PoC has several limitations:

1. The training dataset is small and synthetic.
2. Category predictions may not generalize to real customer inquiries.
3. Priority is determined using keyword rules rather than a trained urgency model.
4. The current response is template-based rather than LLM-generated.
5. No production CRM integration is established by the prototype.
6. Production accuracy, business impact, and response-time improvements have not been measured.

These limitations are expected for an initial proof of concept and define the next steps for further development.

## 10. Conclusion

The AI Lead Intelligence PoC demonstrates a practical baseline for classifying business inquiries and supporting initial triage. It combines TF-IDF, Logistic Regression, transparent priority rules, a Streamlit interface, and automated tests.

The next stage is to evaluate the model using representative labeled data, improve the priority logic, and consider optional LLM-based summarization or response drafting. Production deployment should follow only after suitable evaluation, privacy safeguards, and business validation.