import subprocess

def git_commit_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Respaldar cambios automáticamente"])
    subprocess.run(["git", "push", "origin", "main"])

git_commit_push()
