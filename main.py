import subprocess
import os
from datetime import datetime, timedelta
import random

# -------- CONFIG --------
TARGET_DATES = ["2025-05-13", "2025-05-15"]
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 5, 10)  # exclude 13, 15
GITHUB_BRANCH = "main"
# ------------------------

def run(cmd, **kwargs):
    """Run subprocess command and return output or raise error."""
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kwargs)

def git_stash():
    print("📦 Stashing current changes...")
    subprocess.run(["git", "stash", "--include-untracked", "-m", "pre-redistribution-backup"], check=True)

def git_stash_pop():
    print("♻️ Restoring previous changes...")
    subprocess.run(["git", "stash", "pop"], check=True)

def get_files_from_dates():
    files = set()
    for date in TARGET_DATES:
        try:
            out = run(["git", "log", "--since", f"{date} 00:00", "--until", f"{date} 23:59",
                       "--pretty=format:", "--name-only"]).stdout
            for line in out.splitlines():
                path = line.strip()
                if path and os.path.isfile(path):
                    files.add(path)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error fetching commits for {date}")
            print(e.stderr)
    return list(files)

def random_dates(n):
    all_days = [(START_DATE + timedelta(days=i)) for i in range((END_DATE - START_DATE).days + 1)]
    return random.sample(all_days, min(n, len(all_days)))

def recommit(files, dates):
    for file, date in zip(files, dates):
        dt_str = date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = dt_str
        env["GIT_COMMITTER_DATE"] = dt_str

        try:
            subprocess.run(["git", "add", file], check=True)
            subprocess.run(["git", "commit", "-m", f"Redistributed {file}"], check=True, env=env)
            print(f"✅ Committed {file} on {date.date()}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to commit {file}")

def main():
    try:
        git_stash()
        files = get_files_from_dates()
        print(f"📁 Found {len(files)} files to redistribute")

        if not files:
            print("⚠️ No files found.")
            return

        new_dates = random_dates(len(files))
        recommit(files, new_dates)

        print("\n🚀 Push with:\n   git push origin", GITHUB_BRANCH)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        git_stash_pop()

if __name__ == "__main__":
    main()
