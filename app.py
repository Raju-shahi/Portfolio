import streamlit as st

# Set page config
st.set_page_config(page_title="Raju Shahi's Portfolio", layout="centered")

# Custom style
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .title {
            font-size: 50px;
            font-weight: 800;
            color: #1abc9c;
        }
        .section-header {
            font-size: 28px;
            color: #3498db;
            border-bottom: 2px solid #2980b9;
            padding-bottom: 5px;
            margin-bottom: 20px;
        }
        a {
            color: #e74c3c;
        }
    </style>
""", unsafe_allow_html=True)

# Profile picture and intro
st.image("DP.jpg", width=200, caption="Raju Shahi")
st.markdown('<h1 class="title">Hi, I\'m Raju Shahi 👋</h1>', unsafe_allow_html=True)
st.markdown("""
I'm currently pursuing my **M.Tech** in **Computer Engineering** at **NIT Kurukshetra**. After completing my undergrad in **Computer Science**, I’ve developed a deep fascination with **Artificial Intelligence** — especially **Machine Learning**, **Deep Learning**, **Generative AI**, **NLP**, and all things **Data Science**.

When I’m not coding or experimenting with models, you’ll find me exploring tech trends or reading research papers.
""")

# Skills section
st.markdown('<h2 class="section-header">🛠️ Skills & Tech Stack</h2>', unsafe_allow_html=True)
st.markdown("""
- **Programming**: Python, Java, C++
- **Frameworks & Libraries**: NumPy, Pandas, Scikit-learn, Gradio, LangChain, Hugging Face, TensorFlow, Keras, Streamlit
- **Database**: MySQL
- **Tools**: VS Code, Jupyter Notebook, Google Colab, Git & GitHub
- **Areas of Interest**: Machine Learning, Deep Learning, Generative AI, DSA, OOP, OS, DBMS, CN, NLP
""")

# Projects
st.markdown('<h2 class="section-header">📁 Projects</h2>', unsafe_allow_html=True)

st.subheader("1. Customer Churn Prediction App")
st.markdown("""
- Developed an **ANN-based binary classification** model to predict bank customer churn.
- Preprocessed data with **feature encoding** and **scaling**.
- Achieved high accuracy using **TensorFlow**.
- Built frontend using **Gradio** and deployed on **Hugging Face Spaces**.

🔗 [Live Demo on Hugging Face](https://huggingface.co/spaces/ShahiRaju/Churn_Prediction)
""")

st.subheader("2. Fake News Detection with LSTM")
st.markdown("""
- Built an **LSTM-based model** to classify news as real or fake.
- Used text preprocessing and **word embeddings**.
- Achieved **93% validation accuracy** on a large dataset.
""")

# Contact section
st.markdown('<h2 class="section-header">📬 Contact Me</h2>', unsafe_allow_html=True)
st.markdown("""
- 🌐 [GitHub](https://github.com/Raju-shahi)
- 💼 [LinkedIn](https://www.linkedin.com/in/raju-shahi-340554309/)
- 🧠 [LeetCode](https://leetcode.com/u/_HANUMANTH_/)
""")



# Resume
st.markdown('<h2 class="section-header">📄 Resume</h2>', unsafe_allow_html=True)
with open("Resume_solsphare.pdf", "rb") as pdf_file:
    st.download_button(
        label="⬇️ Download My Resume",
        data=pdf_file,
        file_name="Raju_Shahi_Resume.pdf",
        mime="application/pdf"
    )

# Footer
st.markdown("""
<hr />
<div style='text-align: center; font-size: small;'>
    © 2025 Raju Shahi. All rights reserved. <br />
    Connect on <a href="https://github.com/Raju-shahi">GitHub</a> | 
    <a href="https://www.linkedin.com/in/raju-shahi-340554309/">LinkedIn</a> | 
    <a href="https://leetcode.com/u/_HANUMANTH_/">LeetCode</a>
</div>
""", unsafe_allow_html=True)
