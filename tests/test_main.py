# tests/test_main.py
from app.main import home
from datetime import datetime
import io
import sys


def test_home_route():
    with home.test_client() as client: 
        response = client.get('/')
        assert response.status_code == 200
        assert "Hello, received request from ip" in response.data.decode()
    # Capture stdout
    # captured_output = io.StringIO()
    # sys.stdout = captured_output

    # home()
    # sys.stdout = sys.__stdout__  # Reset redirect
    # output = captured_output.getvalue().strip()
    # assert output.startswith("received")

    # # Extract the time string
    # time_str = output.replace("received", "").strip()

    # # Try parsing the time string to validate format
    # try:
    #     datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    # except ValueError:
    #     assert False, "Time format is incorrect"
