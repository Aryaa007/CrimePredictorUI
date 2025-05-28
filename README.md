<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CrimePredictor UI</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #0f1117;
      color: #f1f1f1;
      line-height: 1.6;
      padding: 2rem;
    }
    h1, h2, h3 {
      color: #FF4B4B;
    }
    code {
      background: #1c1c1c;
      color: #90ee90;
      padding: 0.2rem 0.4rem;
      border-radius: 5px;
      font-size: 90%;
    }
    .badge-container img {
      margin-right: 8px;
    }
    .screenshot {
      width: 100%;
      max-width: 600px;
      border-radius: 10px;
      margin-top: 1rem;
    }
    .section {
      margin-bottom: 2rem;
    }
  </style>
</head>
<body>

  <h1 align="center">💀 CRIMEPREDICTORUI</h1>
  <p align="center"><em>Empowering Communities with Insightful Crime Risk Awareness</em></p>

  <div class="badge-container" align="center">
    <img src="https://img.shields.io/github/last-commit/Aryaa007/crimepredictor-ui?color=blue&label=Last%20Commit" />
    <img src="https://img.shields.io/github/languages/top/Aryaa007/crimepredictor-ui?color=orange&label=Top%20Language" />
    <img src="https://img.shields.io/github/languages/count/Aryaa007/crimepredictor-ui?color=green&label=Languages" />
  </div>

  <div class="section">
    <h2>📖 Overview</h2>
    <p><strong>CrimePredictorUI</strong> is an interactive geospatial dashboard that visualizes district-wise rape risk across India. Built with Streamlit, it overlays predictive insights on 3D maps while analyzing historical trends and demographic vulnerabilities.</p>
  </div>

  <div class="section">
    <h2>❓ Why CrimePredictor</h2>
    <p>CrimePredictor bridges the gap between data and decisions. It empowers:</p>
    <ul>
      <li>🚨 Policymakers and analysts</li>
      <li>🧠 Researchers and data scientists</li>
      <li>🗺️ NGOs and community leaders</li>
      <li>👥 Citizens and activists</li>
    </ul>
  </div>

  <div class="section">
    <h2>⚙️ Getting Started</h2>
    <h3>🧰 Prerequisites</h3>
    <ul>
      <li>Python 3.8+</li>
      <li>pip</li>
      <li>Git</li>
    </ul>

    <h3>💾 Installation</h3>
    <pre><code>git clone https://github.com/Aryaa007/crimepredictor-ui.git
cd crimepredictor-ui
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt</code></pre>

    <h3>🚀 Usage</h3>
    <pre><code>streamlit run app.py</code></pre>
    <p>Open <code>http://localhost:8501</code> in your browser.</p>
  </div>

  <div class="section">
    <h2>🧪 Testing</h2>
    <ul>
      <li>Dropdown filtering for state and district</li>
      <li>3D map column rendering</li>
      <li>Trend chart plotting</li>
      <li>Demographic analysis & smart suggestions</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧠 Technologies Used</h2>
    <ul>
      <li>Streamlit</li>
      <li>Pydeck</li>
      <li>Pandas</li>
      <li>Matplotlib</li>
      <li>NumPy</li>
      <li>Pillow</li>
    </ul>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre><code>crimepredictor-ui/
├── app.py
├── Final.csv
├── requirements.txt
├── runtime.txt
├── README.md
└── screenshots/</code></pre>
  </div>

  <div class="section">
    <h2>📸 Screenshots</h2>
    <img src="screenshots/dashboard.png" alt="Dashboard" class="screenshot" />
    <img src="screenshots/map.png" alt="3D Risk Map" class="screenshot" />
  </div>

  <div class="section">
    <h2>📬 Contact</h2>
    <p>Made with ❤️ by <a href="https://github.com/Aryaa007" target="_blank">Aryaa007</a></p>
    <p>Drop a ⭐ if this project empowered you, and feel free to fork or contribute.</p>
    <blockquote><em>"Code with purpose. Visualize with power."</em></blockquote>
  </div>

</body>
</html>
