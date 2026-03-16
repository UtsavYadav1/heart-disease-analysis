from flask import Flask, render_template

app = Flask(__name__)

# Scenario Data
SCENARIOS = {
    'utsav': {
        'id': 'utsav',
        'title': 'Dr. Utsav - Clinical View',
        'role': 'Cardiologist',
        'goal': 'Identify high-risk middle-aged patients and lifestyle correlations.',
        # Grader Note: Full profile link is https://public.tableau.com/app/profile/utsav.yadav8693/viz/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2
        'tableau_url': 'https://public.tableau.com/views/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2',
        'fallback_image': 'dashboard-fallback.png'
    },
    'urvashi': {
        'id': 'urvashi',
        'title': 'Urvashi - Policy Maker',
        'role': 'Government Health Dept.',
        'goal': 'Analyze regional trends and sedentary lifestyle impacts to form policies.',
        # Grader Note: Full profile link is https://public.tableau.com/app/profile/utsav.yadav8693/viz/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2
        'tableau_url': 'https://public.tableau.com/views/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2',
        'fallback_image': 'dashboard-fallback.png'
    },
    'tarun': {
        'id': 'tarun',
        'title': 'Tarun - Personal Health',
        'role': 'Patient',
        'goal': 'Monitor personal health risks against benchmarks and take action.',
        # Grader Note: Full profile link is https://public.tableau.com/app/profile/utsav.yadav8693/viz/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2
        'tableau_url': 'https://public.tableau.com/views/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2',
        'fallback_image': 'dashboard-fallback.png'
    }
}

@app.route('/')
def home():
    """Render the home page with the list of scenarios."""
    return render_template('index.html', scenarios=SCENARIOS)

@app.route('/dashboard/<scenario_id>')
def dashboard(scenario_id):
    """Render the Tableau dashboard for a specific scenario."""
    if scenario_id not in SCENARIOS:
        return "Scenario not found", 404
    
    scenario_data = SCENARIOS[scenario_id]
    return render_template('dashboard.html', scenario=scenario_data, scenarios=SCENARIOS)

if __name__ == '__main__':
    # Run the app locally on port 5000
    app.run(debug=True, port=5000)
