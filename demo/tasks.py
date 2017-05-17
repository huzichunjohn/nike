# -*- coding: utf-8 -*-
from celery import task
import subprocess
import os

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="uptime")
def uptime():
    p = subprocess.Popen(["uptime"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    stdout, stderr = p.communicate()
    result = {
        "stdout": stdout.decode('utf-8'),
        "stderr": stderr.decode('utf-8')
    }
    return result

@task(name="ping")
def ping():
    p = subprocess.Popen(["ansible-playbook", "-i", "/vagrant/src/hosts", "/vagrant/src/ping.yml", "-e",
                          "ansible_python_interpreter=/vagrant/src/venv/bin/python3.5", "-f", "3"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, env={**os.environ, "TASK_ID": "007"})
    stdout, stderr = p.communicate()
    if stdout:
        stdout_lines = stdout.decode('utf-8').split('\n')
        for line in stdout_lines:
            print(line)
    if stderr:
        stderr_lines = stderr.decode('utf-8').split('\n')
        for line in stderr_lines:
            print(line)

@task(name="ansible")
def ansible():
    p = subprocess.Popen(["ansible", "all", "-m", "ping", "-e",
                          "ansible_python_interpreter=/vagrant/src/venv/bin/python3.5", "-f", "3"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    stdout, stderr = p.communicate()
    if stdout:
        stdout_lines = stdout.decode('utf-8').split('\n')
        for line in stdout_lines:
            print(line)
    if stderr:
        stderr_lines = stderr.decode('utf-8').split('\n')
        for line in stderr_lines:
            print(line)
