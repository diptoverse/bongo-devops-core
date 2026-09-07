# Git & GitHub Mastery

A practical collection of must use Git and GitHub tasks designed to build hands on experience through real world workflows.

## Task 1: **First Impression**

### Objective

Complete the first Git workflow:

▪ Initialize the repository  
▪ Configure commit identity  
▪ Create `README.md`  
▪ Stage the file  
▪ Create the first commit

### Concept

▪ To get started with Git, we need to initialize a repository in our local directory.

▪ Git also needs to know who is making the changes, so we configure the commit identity with a name and email.

▪ Once that is set, we create our first file, stage it, and commit the change to Git history.

### Commands

| Command | Purpose |
|---|---|
| `git init` | Initialize the repository |
| `git config user.name "Your Name"` | Configure the commit author name |
| `git config user.email "your@email.com"` | Configure the commit author email |
| `touch README.md` | Create the README file |
| `git add README.md` | Stage the file |
| `git commit -m "Initial commit"` | Create the first commit |

### Workflow

`git init` → `git config` → `touch README.md` → `git add` → `git commit`

> Every project we want tracked by Git needs a starting point and git init is that one. Every change needs an owner and git config gives that unique identity.

## Task 2: **The Safe Space**

### Objective

Complete the Git ignore workflow:

▪ Create a `.env` file with a fake password  
▪ Create a `.gitignore` file  
▪ Configure Git to ignore `.env`  
▪ Verify that `.env` is not tracked by Git

### Concept

▪ Software engineers handle secrets like API keys and DB passwords that are not meant to be tracked by Git or pushed to GitHub.

▪ That's why we use a `.env` file to store these values locally and a `.gitignore` file to tell Git not to track `.env`.

▪ This keeps sensitive files out of Git and prevents them from being pushed to GitHub.

### Commands

| Command | Purpose |
|---|---|
| `touch .env` | Create the environment file |
| `echo "PASSWORD=fakepassword" > .env` | Add a fake password to the `.env` file |
| `touch .gitignore` | Create the Git ignore file |
| `echo ".env" >> .gitignore` | Tell Git to ignore the `.env` file |
| `git status` | Verify that `.env` is not listed as an untracked file |

### Workflow

`touch .env` → `touch .gitignore` → `echo ".env" >> .gitignore` → `git status`

> Some files should never be tracked by Git or pushed to GitHub. That's why we use `.gitignore` to keep them out.

## Task 3: **The Parallel Universe**

### Objective

Complete the Git branching workflow:

▪ Create a new branch called `feature/system-optimization`  
▪ Switch to the new branch  
▪ Create `kernel_tuning.txt`  
▪ Commit the file  
▪ Switch back to `main` and observe the file is not there

### Concept

▪ Git branches allow us to work on different changes without affecting the main branch.

▪ We create a separate branch for the system optimization work, add and commit the new file there.

▪ When we switch back to `main`, the file disappears because that commit exists only in the feature branch.

### Commands

| Command | Purpose |
|---|---|
| `git branch feature/system-optimization` | Create the feature branch |
| `git switch feature/system-optimization` | Switch to the feature branch |
| `touch kernel_tuning.txt` | Create the kernel tuning file |
| `git add kernel_tuning.txt` | Stage the file |
| `git commit -m "Add kernel tuning"` | Commit the file to the feature branch |
| `git switch main` | Switch back to the main branch |

### Workflow

`git branch` → `git switch` → `touch kernel_tuning.txt` → `git add` → `git commit` → `git switch main`

> We use branches to work on changes separately without affecting the main branch.

## Task 4: **The Selective Memory**

### Objective

Complete the Git staging workflow:

▪ Create `web_fix.conf` and `db_fix.conf`  
▪ Stage only `web_fix.conf`  
▪ Commit `web_fix.conf`  
▪ Stage and commit `db_fix.conf` separately

### Concept

▪ Git allows us to choose which changes should be included in a commit.

▪ Instead of committing every changed file together, we can stage specific files and keep each commit focused on a particular change.

▪ This helps us maintain a clean and meaningful Git history.

### Commands

| Command | Purpose |
|---|---|
| `touch web_fix.conf db_fix.conf` | Create both configuration files |
| `git add web_fix.conf` | Stage only `web_fix.conf` |
| `git commit -m "Add web fix"` | Commit `web_fix.conf` |
| `git add db_fix.conf` | Stage `db_fix.conf` |
| `git commit -m "Add database fix"` | Commit `db_fix.conf` separately |

### Workflow

`touch` → `git add web_fix.conf` → `git commit` → `git add db_fix.conf` → `git commit`

> We can choose specifically which file to stage and commit.

## Task 5: **The Cloud Connection**

### Objective

Complete the GitHub connection workflow:

▪ Create a repository on GitHub  
▪ Connect the local repository to GitHub  
▪ Push the `main` branch  
▪ Verify the Git history in the browser

### Concept

▪ A local Git repository tracks changes on our machine, but GitHub allows us to store and share that repository remotely.

▪ We can connect a local repository to GitHub using different methods such as HTTPS or SSH. Here, we connect it using an SSH URL.

▪ Once the remote is configured, we push the `main` branch and can view our Git history directly from GitHub.

### Commands

| Command | Purpose |
|---|---|
| `git remote add origin <ssh-repository-url>` | Connect the local repository to GitHub using SSH |
| `git remote -v` | Verify the remote repository |
| `git push -u origin main` | Push the `main` branch to GitHub |

### Workflow

`git remote add origin` → `git remote -v` → `git push -u origin main` → GitHub

> To store our changes remotely, we need to connect our local repository to a remote repository. One of the most common ways is using SSH.


## Task 6: **The History Detective**

### Objective

Complete the Git investigation:

▪ Find the commit that changed the port number  
▪ Identify who made the change  
▪ Identify when the change was made  
▪ Verify the change using `git log -p` or `git blame`

### Concept

▪ Git history allows us to investigate who changed a file, what they changed, and when the change was made.

▪ For this investigation, we made the configuration change and committed it under a different commit identity so the change could be traced through Git history.

▪ Using `git log -p` and `git blame`, we can identify the exact commit, author, date, and change made to the port configuration.

### How I Did It

▪ I created a separate branch for the investigation and made the required port configuration change.

▪ I first created a commit using my original Git identity, then changed the local commit identity and created the commit containing the port change.

▪ After the investigation, I restored my original Git identity and used `git log -p` and `git blame db_fix.conf` to trace the change.

### Investigation

The investigation showed that the port was changed from `8080` to `8083`.

The change was made in commit `d9cb8378` by `wrong_person` on September 4, 2026 at 15:34:12 +0600.

### Commands

| Command | Purpose |
|---|---|
| `git log -p` | Show commit history with the changes introduced by each commit |
| `git blame db_fix.conf` | Show which commit and author last changed each line |
| `git log` | View the commit history and identify commit details |

### Workflow

`git log -p` → Find the port change → `git blame db_fix.conf` → Identify the commit and author

> When something changes unexpectedly, Git history helps us find who changed it, what changed, and when.