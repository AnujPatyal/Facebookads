<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ad Generator with Content Moderation</title>
</head>
<body>

<h1>📝 Ad Generator with Content Moderation</h1>

<p><strong>A streamlined solution for generating ad content that adheres to Meta's Advertising Policies, using OpenAI's GPT-4.</strong><br>
Effortlessly create ad copies for Facebook and Google while ensuring compliance with advertising guidelines.</p>

<img src="https://link-to-your-image.com/banner.png" alt="Ad Generator Banner">
<!-- Include a relevant banner image or GIF to visually represent your project. -->

<hr>

<h2>📋 Table of Contents</h2>
<ul>
  <li><a href="#about-the-project">About the Project</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#demo">Demo</a></li>
  <li><a href="#getting-started">Getting Started</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#technologies">Technologies</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contact">Contact</a></li>
</ul>

<hr>

<h2 id="about-the-project">📖 About the Project</h2>
<p>This project provides a user-friendly interface to generate creative ad content for Facebook and Google while checking compliance with key Meta Advertising Policies. Using OpenAI's GPT-4 model, it flags prohibited keywords and policies, ensuring that ad content meets standards for personal attributes, adult content, misinformation, and more.</p>

<hr>

<h2 id="features">✨ Features</h2>
<ul>
  <li><strong>Ad Generation for Facebook and Google</strong>: Generate different types of Facebook ads (Simple, Advanced, Headlines) and Google ad formats.</li>
  <li><strong>Policy Compliance Check</strong>: Detects violations based on Meta’s Advertising Policies, flagging keywords related to personal attributes, adult content, misinformation, and profanity.</li>
  <li><strong>User-Friendly Interface</strong>: Uses Streamlit to provide a simple, interactive form for creating ads.</li>
  <li><strong>Asynchronous Processing</strong>: Handles API requests concurrently for efficient ad generation and policy compliance checks.</li>
</ul>

<hr>

<h2 id="demo">🎥 Demo</h2>
<img src="https://link-to-demo-gif.com/demo.gif" alt="Demo GIF">
<!-- A quick demo showing ad generation and content moderation in action. -->

<hr>

<h2 id="getting-started">🏁 Getting Started</h2>
<p>These instructions will help you set up and run the project locally.</p>

<h3>Prerequisites</h3>
<ul>
  <li><strong>Python 3.8 or higher</strong></li>
  <li><strong>OpenAI API key</strong> (set up in a <code>.env</code> file)</li>
  <li><strong>Git</strong> (optional, for cloning the repository)</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/your-username/ad-generator-moderation.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd ad-generator-moderation</code></pre>
  </li>
  <li>Create a virtual environment and activate it:
    <pre><code>python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Set up the OpenAI API Key:
    <ul>
      <li>Create a <code>.env</code> file in the project root directory.</li>
      <li>Add your OpenAI API key to this file:
        <pre><code>API_KEY=your_openai_api_key_here</code></pre>
      </li>
    </ul>
  </li>
</ol>

<hr>

<h2 id="usage">🚀 Usage</h2>
<p>To run the application, simply execute the following command:</p>
<pre><code>streamlit run usemodel.py</code></pre>

<ol>
  <li><strong>Select Ad Type</strong>: Choose between "Facebook" and "Google" ads.</li>
  <li><strong>Input Details</strong>:
    <ul>
      <li>For <strong>Facebook</strong>: Select ad type (Simple Ad, Advanced Ad, Headlines).</li>
      <li>Enter the <strong>Product Name</strong> and <strong>Description</strong>.</li>
    </ul>
  </li>
  <li><strong>Generate Ad</strong>: Click "Generate Ad" to create ad content and check compliance.</li>
  <li><strong>View Results</strong>: Review generated ad copy along with any flagged policy violations.</li>
</ol>

<hr>

<h2 id="technologies">🛠️ Technologies</h2>
<ul>
  <li><strong>Python</strong>: Core programming language</li>
  <li><strong>Streamlit</strong>: For creating an interactive UI</li>
  <li><strong>OpenAI GPT-4</strong>: Model for ad generation and moderation</li>
  <li><strong>Aiohttp</strong>: To handle asynchronous HTTP requests</li>
  <li><strong>Dotenv</strong>: For environment variable management</li>
</ul>

<hr>

<h2 id="contributing">🤝 Contributing</h2>
<p>Contributions are welcome! Please follow these steps to contribute:</p>
<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch (<code>git checkout -b feature/YourFeature</code>).</li>
  <li>Commit your changes (<code>git commit -m 'Add feature'</code>).</li>
  <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
  <li>Open a Pull Request.</li>
</ol>

<hr>

<h2 id="license">📝 License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>

<hr>

<h2 id="contact">📞 Contact</h2>
<p><strong>Your Name</strong><br>
  - GitHub: <a href="https://github.com/your-username">your-username</a><br>
  - Email: <a href="mailto:your-email@example.com">your-email@example.com</a>
</p>

<hr>

<h2>🎉 Acknowledgements</h2>
<ul>
  <li><a href="https://openai.com">OpenAI</a> for GPT-4.</li>
  <li><a href="https://streamlit.io">Streamlit</a> for easy app creation.</li>
  <li><a href="https://www.facebook.com/business/help/">Meta's Advertising Policies</a>.</li>
</ul>

</body>
</html>
