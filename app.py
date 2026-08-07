from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1 + num2
        except ValueError:
            result = "Please enter valid numbers."

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vadim's Calculator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f7fa;
                padding-top: 50px;
            }}
            .container {{
                background: white;
                width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            input {{
                padding: 10px;
                margin: 10px;
                width: 120px;
            }}
            button {{
                padding: 10px 20px;
                background: #0078D4;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background: #005A9E;
            }}
            .result {{
                margin-top: 20px;
                font-size: 1.5em;
                color: green;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Azure Flask Calculator</h1>

            <form method="POST">
                <input type="number" step="any" name="num1" placeholder="First Number" required>
                <input type="number" step="any" name="num2" placeholder="Second Number" required>
                <br>
                <button type="submit">Add Numbers</button>
            </form>

            <div class="result">
                {"Result: " + str(result) if result is not None else ""}
            </div>

            <p>Powered by Flask and Azure</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()