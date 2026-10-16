
import streamlit as st
from model import analyze_inquiry

st.set_page_config(
    page_title="Cynbit AI Lead Intelligence",
    page_icon="🤖",
)

st.title("Cynbit AI Lead Intelligence")
st.write(
    "Analyze customer inquiries, identify service categories, "
    "and estimate lead priority."
)

message = st.text_area(
    "Enter a customer inquiry",
    placeholder=(
        "We urgently need an AI chatbot before our product "
        "launch next week."
    ),
)

if st.button("Analyze Inquiry"):
    if not message.strip():
        st.warning("Please enter a customer inquiry.")
    else:
        try:
            result = analyze_inquiry(message)

            st.subheader("Analysis Results")

            st.write("**Service category:**", result["category"])
            st.write(
                "**Model confidence:**",
                f'{result["confidence"]:.1%}',
            )

            st.subheader("Lead Priority")

            if result["priority"] == "High":
                st.error("High Priority")
            elif result["priority"] == "Medium":
                st.warning("Medium Priority")
            else:
                st.info("Low Priority")

            st.write("**Reason:**", result["priority_reason"])

            st.info(
                "Prototype notice: the classifier uses synthetic "
                "training examples. Priority is based on keyword "
                "rules. Both require validation before real-world use."
            )

            st.subheader("Suggested Next Steps")
            st.write("- Confirm the project requirements.")
            st.write("- Ask about budget and timeline.")
            st.write("- Arrange a discovery call if appropriate.")

            st.subheader("Draft Response")
            st.write(
                "Thank you for sharing your project requirements. "
                f"We understand you are looking for "
                f"{result['category'].lower()}. "
                "Could you share your goals, timeline, and budget?"
            )

        except ValueError as error:
            st.error(str(error))
