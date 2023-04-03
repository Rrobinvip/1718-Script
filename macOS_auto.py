import os, time
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

time.sleep(5)

# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "youtube.py")

print(" - Process 2 starting.. (Playing YouTube)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 2 has finished.")

time.sleep(5)

# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "word.py")

print(" - Process 3 starting.. (Typing in Word)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 3 has finished.")

time.sleep(5)

# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "zoom.py")

print(" - Process 4 starting.. (Zoom meeting)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 4 has finished.")

time.sleep(5)

# get the path to your Python script relative to the current working directory
script_path = os.path.join("macOS_scripts", "qq.py")

print(" - Process 5 starting.. (QQ chating)")
# execute the script as a child process
process = subprocess.Popen(["python", script_path])

# wait for the child process to finish
process.wait()

# the parent process will resume here once the child process has finished
print(" - Process 5 has finished.")


print(" - All tasks finished without any error.")