from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('sms_spam_model.pkl')
vectorizer = joblib.load('sms_spam_vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_input = request.form.get('message')
        user_input_vectorized = vectorizer.transform([user_input])
        prediction = model.predict(user_input_vectorized)
        prediction = 'Spam' if prediction[0] == 1 else 'Ham'

        return render_template('sms_spam.html', prediction=prediction)
    return render_template('sms_spam.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)