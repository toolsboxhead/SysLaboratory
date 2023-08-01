import subprocess

def git_commit_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Respaldar cambios automáticamente"])
    

git_commit_push()
