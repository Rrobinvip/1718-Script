# ECE 1718 Project automated script

The goal of this script is to automate daily use cases. We plan to do the following:

* Browse 12 webpages (1 minute each)
* Watch a YouTube Video (12 minutes)
* Auto typing in Word (12 minutes)
* Zoom meeting (12 minutes)
* WeChat (12 minutes)

And we need to implement tools to watch frequency and power consumption.

## To use

Set up config in `Config.py`, such as webpages, etc.


1. Create the python3 venv with `python3 -m venv env`, and activate with `source env/bin/activate`.
2. Run pip install venv_requirements.txt.
3. Inspect packages with pip list.

### macOS

After activating the venv, simply `python macOS_auto.py`.

### Windows