import os

def make_commits(filename="commit_dates.txt"):
    with open(filename, "r") as file:
        commit_dates = [line.strip().split() for line in file.readlines()]
    
    for commit_date, num_commits in commit_dates:
        num_commits = int(num_commits)
        for i in range(num_commits):
            with open("commit_log.txt", "a") as log_file:
                log_file.write(f"{commit_date} commit {i}\n")
            os.system("git add commit_log.txt")
            os.system(f"GIT_COMMITTER_DATE='{commit_date}T12:00:00' git commit --date='{commit_date}T12:00:00' -m 'Auto commit {i}'")

def push_commits():
    os.system("git pull origin main")  # Assicura di avere l'ultima versione del repo
    os.system("git push origin main")

# Esegui il processo
if __name__ == "__main__":
    make_commits()  # Legge dal file e crea i commit
    push_commits()
