from flask import Flask
import os
import subprocess
import signal

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"


def kill_process_on_port(port):
    try:
        result = subprocess.run(['lsof', '-t', '-i', f':{port}'], capture_output=True, text=True, check=True)
        pids = result.stdout.strip().split()
        for pid in pids:
            os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        return True
    except Exception as e:
        return False
    return True

def start():
    app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    try:
        start()
    except:
        if not kill_process_on_port(5000):
            print("Another error")
    start()
