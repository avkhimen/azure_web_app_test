from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Azure App Service Demo</title>
    </head>
    <body>
        <h1>🚀 Hello from Azure App Service</h1>

        <p>This Flask application is running successfully in Azure.</p>

        <p>This is Vadim's app.</p>

        <p>✅ Deployment Successful</p>

        <h2>Features</h2>

        <ul>
            <li>Python Flask backend</li>
            <li>Hosted on Azure App Service</li>
            <li>Simple HTML page</li>
            <li>Ready for further development</li>
        </ul>

        <p>Powered by Flask and Azure</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()