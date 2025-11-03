# Movie-Recommender-System
# 🎬 Movie Recommender System

An intelligent **content-based Movie Recommendation Web App** built using **Streamlit**, **Python**, and **TMDB API**.  
This project recommends 5 similar movies based on the movie you select and displays their posters fetched in real-time.

---

## 📘 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [TMDB API Key Setup](#️-tmdb-api-key-setup)
- [How to Run](#-how-to-run)
- [How It Works](#-how-it-works)
- [Example Output](#-example-output)
- [File Structure](#-file-structure)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🧩 Overview

This **Movie Recommender System** uses a **content-based filtering** technique to suggest movies that are similar to the one selected by the user.  
It relies on precomputed **cosine similarity scores** between movies and utilizes **The Movie Database (TMDB) API** to display posters dynamically.

The system is deployed locally using **Streamlit**, providing a simple, interactive web-based interface.

---

## 🚀 Features

✅ Recommends **5 similar movies** based on the selected film  
✅ Displays **movie posters** using the TMDB API  
✅ Simple, interactive **Streamlit web interface**  
✅ Precomputed **similarity matrix** for fast recommendations  
✅ **Lightweight and modular** Python code  

---

## 💻 Tech Stack

| Category | Technologies Used |
|-----------|-------------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Data Handling** | Pandas, Pickle |
| **API** | TMDB (The Movie Database) |
| **Environment** | Virtualenv (venv) |

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally on your system:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/CoderNived/Movie-Recommender-.git
cd Movie-Recommender-
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
3️⃣ Activate the Virtual Environment
Windows (CMD):

bash
Copy code
venv\Scripts\activate
PowerShell:

bash
Copy code
.\venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
4️⃣ Install Dependencies
If you have a requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Otherwise, install them manually:

bash
Copy code
pip install streamlit pandas requests
5️⃣ Add Dataset Files
Place your pre-trained Pickle files inside your project directory:

Copy code
movies.pkl
similarity.pkl
⚠️ Note: These files are large (>100MB) and are not uploaded to GitHub due to file size restrictions.
You can regenerate them from your data preprocessing notebook or request them separately.

🔑 TMDB API Key Setup
This project uses The Movie Database (TMDB) to fetch movie posters.

Steps to Get Your API Key:
Go to TMDB API

Create an account or log in.

Apply for a Developer API Key (free).

Copy your API Key.

Then, open your app.py file and replace this line:

python
Copy code
API_KEY = "your_tmdb_api_key_here"
with your actual API key.

▶️ How to Run
After setup, run the following command in your terminal:

bash
Copy code
streamlit run app.py
You should see output like this:

nginx
Copy code
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
Open the Local URL in your browser to launch the web app.

⚙️ How It Works
1. Data Loading
movies.pkl contains all movie metadata such as titles and genres.

similarity.pkl contains the precomputed cosine similarity matrix between movies.

2. Recommendation Logic
When you select a movie, its similarity scores are retrieved.

The top 5 most similar movies are identified (excluding the selected one).

3. Poster Fetching
Each recommended movie’s title is passed to the TMDB API.

The corresponding poster URL is fetched dynamically.

If the poster is unavailable, a placeholder image is displayed.

4. UI Display
Streamlit displays the recommended movies and their posters in a clean 5-column layout.

🧠 Example Output
If you select “Inception”, you might see something like this:

Poster	Movie
Interstellar
Shutter Island
The Prestige
The Matrix
Memento

📂 File Structure
bash
Copy code
Movie-Recommender-System/
│
├── app.py                 # Main Streamlit app
├── movies.pkl             # Movie metadata (not on GitHub)
├── similarity.pkl         # Cosine similarity matrix (not on GitHub)
├── requirements.txt       # Python dependencies
├── README.md              # Documentation file
└── venv/                  # Virtual environment (optional)
💡 Future Enhancements
🚀 Add collaborative filtering for hybrid recommendations
🌐 Deploy the app on Streamlit Cloud or Render
🎭 Include filters by genre, rating, and year
⚡ Cache API responses to improve performance
📊 Visualize similarity scores and genre distributions

👨‍💻 Author
🧑‍💻 Nived Shenoy
🎓 Electronics & Telecommunication Engineer | AI & ML Enthusiast

📎 Links

GitHub

LinkedIn

🏁 Requirements File Example
If you don’t have a requirements.txt yet, create one with the following content:

txt
Copy code
streamlit
pandas
requests
pickle-mixin
⭐ If you found this project helpful, please give it a star on GitHub!
Your support encourages more open-source work like this.

yaml
Copy code

---

Would you like me to tailor this `README.md` so it also includes a **“How to regenerate movies.pkl 
