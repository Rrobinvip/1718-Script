import os
import subprocess


print(" * Automated script started..")


# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "browse_web.py")

print(" - Process 1 starting.. (Browsing webpage)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 1 has finished.")


# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "youtube.py")

print(" - Process 2 starting.. (Playing YouTube)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 2 has finished.")