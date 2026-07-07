"""
Intentionally vulnerable Python code for SAST testing.
Do NOT use in production.
"""
import os
import sqlite3
import pickle
import hashlib
from flask import Flask

API_KEY = "1234567890abcdef1234567890abcdef"
DB_PASSWORD = "SuperSecretPassword123!"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def ping(host):
    os.system("ping -c 4 " + host)

def load_data(data):
    return pickle.loads(data)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def calculate(expression):
    return eval(expression)

def execute(code):
    exec(code)

import subprocess
def run_command(cmd):
    subprocess.call(cmd, shell=True)

import ssl
def insecure_ssl():
    return ssl._create_unverified_context()

import yaml
def parse_yaml(data):
    return yaml.load(data, Loader=yaml.Loader)

import random
def generate_token():
    return str(random.randint(100000, 999999))

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

import os
def create_world_writable():
    filename = "public.txt"
    with open(filename, "w") as f:
        f.write("hello")
    os.chmod(filename, 0o777)

try:
    import requests
    def download(url):
        return requests.get(url, verify=False)
except ImportError:
    pass

if __name__ == "__main__":
    app.run(debug=True)
