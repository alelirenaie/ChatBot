# Import necessary libraries
import streamlit as st
from gradientai import Gradient

def main():
    # Streamlit title and description
    st.title("Interactive Food Drive Assistant")
    st.write("Ask a question about the Food Drive!")

    # Lists of sample queries and responses
    sample_queries = [
        "How does helping in the food drive benefit our community?",
        "Can I donate money instead of food items?",
        "How does the food drive support local farmers and businesses?",
        "What do volunteers do in the food drive event?",
        "Are there any events or activities during the food drive?",
        "How does the food drive handle dietary restrictions?",
        "Can people without transportation still help with the food drive?",
        "How can schools get involved in the food drive?"
        "Can you share tips for organizing a successful food drive event?"
        "Are there specific items that are in high demand for donations?",
        "How can we ensure that donated items reach those who need them the most?",
    ]

    sample_responses = [
        "Contributing to the food drive brings our community together and directly helps our neighbors in need. It's a chance to make a positive impact and show that we care.",
        "Definitely! Cash donations are welcome and allow us to buy what's needed in bulk. It's an easy way to support the cause and make sure everyone gets the help they need.",
        "We work with local farmers and businesses to get fresh, local produce. It's a win-win – supporting our community and providing a variety of healthy food for those who need it.",
        "Volunteers are the heart of the event. They help organize, spread the word, and ensure everything runs smoothly. Their time and effort make a big difference in making the food drive successful.",
        "Absolutely! We have collection drives, awareness campaigns, and gatherings to appreciate our volunteers. It's not just about donations; it's about coming together as a community.",
        "We accept a variety of food items to accommodate different diets. Also, monetary donations let us buy specific items, ensuring everyone, including those with dietary restrictions, gets the support they need.",
        "Of course! You can donate online or join in with local collection points. We want everyone to be able to participate and contribute, no matter their transportation situation.",
        "Schools can organize food drives, teach students about helping others, and encourage volunteering. It's a great way for students to make a positive impact and learn about giving back to their community."
        "Organizing a successful food drive involves strategic planning, engaging the community, and effective communication. Consider creating a central drop-off point, leveraging social media, and collaborating with local influencers to boost awareness."
        "Certainly! Items like canned goods, grains, and hygiene products are highly needed. These essentials help us provide a well-rounded support system for those facing food insecurity.",
        "Ensuring effective distribution is a priority. We work closely with local agencies and charities to identify and reach those in need, ensuring that donations reach the right hands at the right time.",
    ]

    with Gradient() as gradient:
        base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
        new_model_adapter = base_model.create_model_adapter(name="interactive_food_drive_model")

        user_input = st.text_input("Ask your question:")
        if user_input and user_input.lower() not in ['quit', 'exit']:
            sample_query = f"### Instruction: {user_input} \n\n### Response:"
            st.markdown(f"Asking: {sample_query}")

            # before fine-tuning
            completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
            st.markdown(f"Generated: {completion}")

        # Delete the model adapter after generating the response
        new_model_adapter.delete()

if __name__ == "__main__":
    main()
