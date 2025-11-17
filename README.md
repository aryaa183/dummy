#  Accident Risk Predictor

**Accident Risk Predictor** is a web-based application designed to evaluate the likelihood of road accidents using driver details, route information, and environmental factors. The system also provides **emergency alerts** and **interactive visualizations** to help users make safer driving decisions.

---

##  Features

* **Accident Risk Prediction**

  * Evaluates accident risk based on driver behavior, route, and environment.
  * Classifies risk levels: Low, Medium, High.

* **Emergency Alert System**

  * Notifies pre-defined contacts automatically in case of high risk.
  * Includes driver location, ETA, and risk severity.
  * Works without third-party SMS accounts.

* **Interactive Visualizations**

  * Dynamic charts and dashboards for accident trends.
  * Component-wise risk breakdown for better understanding.

* **User-Friendly Web Interface**

  * Clean and responsive design.
  * Accessible on any modern web browser.

---

##  Technologies Used

| Layer         | Technology                     |
| ------------- | ------------------------------ |
| Backend       | Python, Flask, Pandas, NumPy   |
| Frontend      | HTML, CSS, JavaScript          |
| Visualization | Chart.js, Plotly               |
| Data          | CSV datasets of road accidents |

---

##  Project Structure

```
accident-risk-predictor/
│
├── data_refinement.py        # data refinement and cleaning
├── data_processing.py        # data cleaning and feature engineering
├── logistic_regression.py    # model testing
├── lstm_time_training.py     # Model testing
├── model_training.py         # model training and accuracy improvement using XGBoost
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/                # HTML templates
│   └── index.html
|   └── Result.html           #OutPut
├── static/
│   ├── style.css             # CSS styles
│   └── script.js             # JS for charts and alerts
├── models/                   # ML or predictive models (if any)
├── data/
│   └── accident_risk_data.csv
└── README.md
```

---

##  Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/Accident-Risk-Predictor.git
cd Accident-Risk-Predictor
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. **Open in browser**

```
http://127.0.0.1:5000
```

---

##  How It Works

1. **User Inputs**: Driver info, route details, vehicle, and environmental conditions.
2. **Risk Prediction**: The system evaluates accident risk level.
3. **Alerts**: Emergency contacts are notified if risk is high.
4. **Visualization**: Interactive dashboard shows trends and risk breakdown.

---

##  Sample Output

```
🚦 Smart Accident Risk Report
Generated at: 2025-11-17 16:07:18

Risk Level
 LOW RISK — Safe to drive

Overall Score: 20.2

 Route Details
From: Pune
To: Mumbai
Road Type: Highway
Weather: Clear
Lighting: Daylight
Speed Limit: 100 km/h
Recommended Safe Speed: 100 km/h

 Risk Breakdown
Weather Risk: 22
Road Condition Risk: 37
Time of Day Risk: 20
Driver Risk: 8
Distance/Fatigue Risk: 5

 Dynamic Weather Tips
- Maintain posted speed limit and stay alert.
- Keep a safe following distance of 2–3 seconds.
- Ensure sunglasses/visor ready for glare.

 Detected Hazards
- Known accident hotspots near expressway tolls and ghat sections.

 Vehicle Readiness Checklist
- Check tyre pressure: recommended 30–35 psi for passenger cars.
- Ensure fuel is sufficient for at least 25% extra travel time.

 Nearby Emergency Services
- Jaslok Hospital (Hospital) — ETA: 20 mins
- Mumbai Highway Patrol (Highway Patrol) — ETA: 12 mins

Frequent High-Risk Patterns Detected
- Road_Highway

 Quick Actions
 Send ETA to Family
 Emergency SOS
```

###  What This Shows

* **Risk Level & Score**: Overall risk assessment for the journey.
* **Route Details**: Info about origin, destination, road type, weather, and speed.
* **Risk Breakdown**: Component-wise risk evaluation.
* **Safety Tips**: Weather and driving guidance.
* **Detected Hazards**: Alerts for known high-risk areas.
* **Vehicle Readiness**: Checklist to prepare the car for the journey.
* **Emergency Services**: Nearby hospitals and highway patrol with ETAs.
* **Quick Actions**: Options to send alerts or SOS.

---

##  Future Enhancements

* Real-time **GPS tracking** for dynamic risk alerts.
* **Voice command integration** for hands-free emergency notifications.
* Incorporate **traffic, weather, and road condition data** for more accurate predictions.
* Develop a **mobile version** for on-the-go use.

---

##  Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Make changes and commit (`git commit -m "Add feature xyz"`)
4. Push to branch (`git push origin feature-xyz`)
5. Create a Pull Request

---

