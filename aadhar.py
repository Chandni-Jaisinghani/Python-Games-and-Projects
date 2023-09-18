from flask import Flask, request, render_template

app = Flask(__name__)

import re

def is_valid_aadhaar_number(aadhaar_number):
    regex = "^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$"
    pattern = re.compile(regex)

    return re.match(pattern, aadhaar_number) is not None

@app.route('/', methods=['GET', 'POST'])
def validate_aadhaar():
    result = None
    if request.method == 'POST':
        aadhaar_number = request.form['aadhar_number']
        if is_valid_aadhaar_number(aadhaar_number):
            result = f"{aadhaar_number} is a valid Aadhaar number."
        else:
            result = f"{aadhaar_number} is not a valid Aadhaar number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
