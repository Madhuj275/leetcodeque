
import requests
import os
import json
import subprocess

# Set your GitHub repo details
GITHUB_USERNAME = "Madhuj275"
GITHUB_REPO = "Leetcode-DSA-Questions"
GITHUB_BRANCH = "main"  # Change if using another branch
LEETCODE_USERNAME = "madhuj27"
LEETCODE_SESSION = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTEzODExMTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkYmQ0YjcxZTY2MWNmZGYwOTAzOTliOTY5ZWI0YjMzN2QwNGMwNWU0MGY2NGIzMzdlOWIxMzVlZjI1N2IyN2E2Iiwic2Vzc2lvbl91dWlkIjoiMDZkNGM0OGIiLCJpZCI6MTEzODExMTQsImVtYWlsIjoibWFkaHVqLjIwMDRAeWFob28uY29tIiwidXNlcm5hbWUiOiJtYWRodWoyNyIsInVzZXJfc2x1ZyI6Im1hZGh1ajI3IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTc0NzEyMDQyMiwiaXAiOiI0NS4xMTYuMTQ5LjE4NiIsImlkZW50aXR5IjoiMzNkMGYyNTdhODE3ZDFjYTRjNDM4MWI4N2Y4YWQ4M2YiLCJkZXZpY2Vfd2l0aF9pcCI6WyIxZWUzNmQ5YzgyNmViN2E3NDZkNWFhYzE5MjgwYzMxNSIsIjQ1LjExNi4xNDkuMTg2Il0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.mUBe9xyvjd-jY9ehOQ2B5_cT0MO1oJQvb84uKN_f5Sk"

if not LEETCODE_SESSION:
    print("❌ LeetCode session token is missing. Please set LEETCODE_SESSION.")
    exit(1)

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}",
    "User-Agent": "Mozilla/5.0"
}

LEETCODE_SUBMISSIONS_API = "https://leetcode.com/api/submissions/"

def fetch_all_submissions():
    """Fetches all accepted submissions from LeetCode using proper pagination."""
    submissions = []
    offset = 0
    limit = 200  # API limit is 20 submissions per request

    while True:
        url = f"{LEETCODE_SUBMISSIONS_API}?offset={offset}&limit={limit}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"❌ Failed to fetch submissions. HTTP {response.status_code}")
            print(response.text)
            break

        try:
            data = response.json()
            fetched = data.get("submissions_dump", [])

            if not fetched:
                break  # Stop if no more submissions
            
            submissions.extend(fetched)
            offset += limit  # Move to the next batch

        except json.JSONDecodeError:
            print("❌ Error decoding JSON response.")
            print(response.text)
            break

    print(f"✅ Fetched {len(submissions)} submissions.")
    return submissions

def save_to_file(submission):
    """Saves a submission to a file in a structured format."""
    title_slug = submission.get('title_slug', f"unknown_{submission.get('title', 'problem')}").replace(" ", "_")
    code = submission.get('code', '')

    if not code:
        print(f"⚠️ No code found for {title_slug}, skipping...")
        return

    difficulty = submission.get("difficulty", "Unknown")
    problem_title = submission.get("title", "Unknown")

    # Create a solutions folder if it doesn't exist
    os.makedirs("solutions", exist_ok=True)

    filename = f"solutions/{title_slug}.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Problem: {problem_title}\n")
        f.write(f"# Difficulty: {difficulty}\n")
        f.write("# Solution:\n\n")
        f.write(code)

    print(f"✅ Saved: {filename}")

def sync_solutions():
    """Fetch, save, and push LeetCode submissions to GitHub."""
    submissions = fetch_all_submissions()
    if not submissions:
        print("⚠️ No submissions found.")
        return

    for sub in submissions:
        save_to_file(sub)

    # Commit and push changes to GitHub
    git_commit_and_push()

def git_commit_and_push():
    """Commits and pushes the latest changes to the GitHub repository."""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-sync LeetCode submissions"], check=True)
        subprocess.run(["git", "push", "origin", GITHUB_BRANCH], check=True)
        print("🚀 Successfully pushed to GitHub!")
    except subprocess.CalledProcessError:
        print("❌ Error pushing to GitHub. Make sure Git is installed and configured.")

if __name__ == "__main__":
    sync_solutions()
