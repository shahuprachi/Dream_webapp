
from flask import Flask, render_template, request, redirect, url_for
from dream_analysis import analyze_dream

app = Flask(__name__)

dreams = []  # Temporary in-memory storage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        dream_text = request.form['dream']
        analysis = analyze_dream(dream_text)
        dreams.append({
            'text': dream_text,
            'analysis': analysis
        })
        return redirect(url_for('dashboard'))
    return render_template('journal.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', dreams=dreams)

if __name__ == '__main__':
    app.run(debug=True)
