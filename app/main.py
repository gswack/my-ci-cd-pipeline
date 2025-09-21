import os
import logging
import datetime
from flask import Flask, request


app = Flask(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')


@app.route('/')
def home():
    try: 
        timestamp = datetime.datetime.now().isoformat()
        client_ip = request.remote_addr
        message = f"recieved request from ip {client_ip} @{timestamp}"
        logging.info(message)
        return f"Hello, {message}"
    except Exception as e:
        logging.exception(f"Error handling request: {e}")
        # print(f"Error due to {e}")
        return "An error occurred while processing your request", 500
    

@app.route('/health')
def health():
    return "OK", 200


@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(e):
    return "Internal server error", 500
    
    # TODO add error handling
    # TODO add health endpoint

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
