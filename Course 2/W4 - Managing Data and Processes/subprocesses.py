import subprocess

subprocess.run(["date"])
subprocess.run(["sleep","2"])
subprocess.run(["ls","file_not_exist"])



result = subprocess.run(["ping","8.8.8.8"],capture_output=True)

print(result.stdout.decode())

result = subprocess.run(["rm","not_exist_file"], capture_output=True)
print(type(result))
print(result.returncode)
print(result.stdout.decode())
print(result.stderr.decode())

