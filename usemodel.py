# D:\Anuj\.venv\Scripts\activate
# cd .venv\Fine Tuning
# streamlit run usemodel.py 

import streamlit as st
import asyncio
import aiohttp
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
openai_api_key = os.getenv("API_KEY")

# Define the prohibited keywords and policies
prohibited_keywords = {
    "personal_attributes": [
        "race", "ethnicity", "religion", "age", "sexual orientation", "gender identity", "disability"
    ],
    "illegal_products": ["drugs", "firearms", "explosives", "weapons","gun", "tobacco"],
    "adult_content": ["nudity", "sexually suggestive", "explicit"],
    "misinformation": ["false", "fake", "misleading","gossip"],
    "profanity": ["curse","language","swear","expletive","obscenity","cuss","vulgarism","epithet"]
}

meta_policies = [
    "Personal Attributes",
    "Illegal Products",
    "Adult Content",
    "Misinformation",
    "Profanity"
]

def check_keywords(text: str, keywords: Dict[str, List[str]]) -> List[str]:
    violations = []
    for category, words in keywords.items():
        for word in words:
            if word.lower() in text.lower():
                violations.append(f"{category}: {word}")
    return violations

async def check_policies(session: aiohttp.ClientSession, text: str) -> List[str]:
    system_content = "You are an AI assistant that checks content for policy violations."
    user_content = f"""Analyze the following text and determine if it violates any of the Meta Advertising Policies:
    - Personal Attributes
    - Illegal Products
    - Adult Content
    - Misinformation
    - Profanity

    Text: {text}

    List any policy violations found, or state "No violations" if none are found."""

    async with session.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={
            "model": "gpt-4o",
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ],
            "max_tokens": 150,
            "n": 1,
            "stop": None,
            "temperature": 0.2,
        },
    ) as response:
        if response.status == 200:
            result = await response.json()
            response_text = result['choices'][0]['message']['content'].strip()
            return [policy for policy in meta_policies if policy.lower() in response_text.lower()]
        else:
            return []

async def generate_ad(session: aiohttp.ClientSession, ad_type: str, choice: str, product_name: str, product_description: str) -> str:
    # Check for keyword violations
    keyword_violations = check_keywords(product_name + " " + product_description, prohibited_keywords)
    if keyword_violations:
        return f"Content violates Meta Advertising Policies. Violations: {', '.join(keyword_violations)}"

    # Check for policy violations
    policy_violations = await check_policies(session, product_name + " " + product_description)
    if policy_violations:
        return f"Content violates Meta Advertising Policies. Violations: {', '.join(policy_violations)}"

    # Proceed with ad generation if no violations
    if ad_type == "facebook":
        if choice == "Simple Facebook Ad":
            prompt = f"Write a creative ad for the following product to run on Facebook.\nProduct: {product_name}\nDescription: {product_description}"
        elif choice == "Advanced Facebook Ad":
            prompt = f"Write a creative ad for the following product to run on Facebook.\nProduct: {product_name}\nDescription: {product_description}\n\nPain: [Describe the pain point]\nAgitate: [Describe how the pain point affects the user]\nSolution: [Describe how the product solves the pain point]"
        elif choice == "Facebook Headlines":
            prompt = f"Write a creative ad for the following product to run on Facebook Ads.\nProduct: {product_name}\nDescription: {product_description}\n\nHeadline 1:\nHeadline 2:\nHeadline 3:"
        else:
            return "Invalid choice for Facebook ad. Please choose a valid option."
        system_content = "You are a creative ad copywriter specializing in Facebook ads."
    elif ad_type == "google":
        prompt = f"""Write a creative ad for the following product to run on Google.

Product: {product_name}
About: {product_description}

Headline 1:
Headline 2:
Headline 3:
Description 1:
Description 2:
"""
        system_content = "You are a creative ad copywriter specializing in Google ads."
    else:
        return "Invalid ad type. Please choose 'Facebook' or 'Google'."

    try:
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {openai_api_key}"},
            json={
                "model": "gpt-4o",
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 350,
                "n": 1,
                "stop": None,
                "temperature": 0.7,
            },
        ) as response:
            if response.status == 200:
                result = await response.json()
                return result['choices'][0]['message']['content'].strip()
            else:
                error_content = await response.text()
                return f"Error: API request failed with status code {response.status}. Details: {error_content}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

async def process_request(session: aiohttp.ClientSession, request: dict) -> dict:
    ad_content = await generate_ad(session, request['ad_type'], request.get('choice', ''), request['product_name'], request['product_description'])
    return {
        "ad_type": request['ad_type'],
        "product_name": request['product_name'],
        "ad_content": ad_content
    }

async def main(requests):
    async with aiohttp.ClientSession() as session:
        tasks = [process_request(session, request) for request in requests]
        results = await asyncio.gather(*tasks)
    return results

def run_async(coroutine):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coroutine)

st.title("Ad Generator with Content Moderation")

with st.form("ad_form"):
    ad_type = st.selectbox("Choose the type of ad you want to create:", ["Facebook", "Google"])
    
    if ad_type == "Facebook":
        choice = st.selectbox("Choose the type of Facebook ad:", ["Simple Facebook Ad", "Advanced Facebook Ad", "Facebook Headlines"])
    else:
        choice = ''
    
    product_name = st.text_input("Enter the product name:")
    product_description = st.text_area("Enter the product description:")
    
    submit_button = st.form_submit_button("Generate Ad")

if submit_button:
    if not product_name or not product_description:
        st.error("Please fill in all fields.")
    else:
        request = {
            "ad_type": ad_type.lower(),
            "choice": choice,
            "product_name": product_name,
            "product_description": product_description
        }
        
        with st.spinner("Generating ad and checking compliance..."):
            results = run_async(main([request]))
        
        if results:
            st.subheader("Generated Ad Content:")
            for result in results:
                st.write(f"Ad Type: {result['ad_type'].capitalize()}")
                st.write(f"Product: {result['product_name']}")
                if "violates Meta Advertising Policies" in result['ad_content']:
                    st.error(result['ad_content'])
                else:
                    st.text_area("Ad Content:", value=result['ad_content'], height=300, disabled=True)
        else:
            st.error("Failed to generate ad. Please try again.")

st.sidebar.title("About")
st.sidebar.info("This is an ad generator with content moderation using OpenAI's GPT-4 model. It can create Facebook and Google ads based on your input while ensuring compliance with Meta's advertising policies.")
st.sidebar.warning("Note: Make sure you have set up your OpenAI API key in the .env file.")

