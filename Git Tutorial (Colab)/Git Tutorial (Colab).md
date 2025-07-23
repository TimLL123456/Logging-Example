# Set your Git config info
```bash
!git config --global user.email "your_email@example.com"
!git config --global user.name "your_github_username"
```

# Define variables
```bash
GITHUB_USERNAME = "your_github_username"
GITHUB_TOKEN = "your_personal_access_token"   # Create one in GitHub Settings > Developer Settings > Personal access tokens
REPO_NAME = "your_repo_name"
BRANCH = "main"  # or "master"
```

# Clone your repo (if not cloned yet)
```bash
!git clone https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git
%cd {REPO_NAME}
```

# Make your changes here or upload files to repo folder

# Add and commit
```bash
!git add .
!git commit -m "Your commit message"
```

# Push changes
```bash
!git push https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git {BRANCH}
```