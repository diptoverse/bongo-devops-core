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

## Task 7: **The Safety Net**

### Objective

▪ Create 5 lines of work in progress in `feature.py` without committing.

▪ Use `git stash` to temporarily hide the unfinished work.

▪ Fix the bug in `main.py`, commit and push the fix.

▪ Use `git stash pop` to restore the unfinished work.

### Concept

▪ `git stash` temporarily saves uncommitted changes so we can switch context without committing incomplete work.

▪ After fixing the urgent change, `git stash pop` restores the stashed work back to the working directory.

▪ This allows us to handle urgent fixes without losing our work in progress.

### How I Did It

▪ I created `main.py` on the `main` branch with intentional mistakes, committed it, and pushed it to GitHub.

▪ I created and switched to the `feature/recovery` branch and added 5 lines of code to `feature.py` without committing.

▪ I used a named stash to temporarily hide the unfinished work.

▪ I switched back to `main`, fixed `main.py`, committed the fix, and pushed it.

▪ I verified the stash with `git stash list` and confirmed that `feature.py` was not present before restoring the stash.

▪ I used `git stash pop` to restore `feature.py`, then committed and pushed the recovered work to the feature branch.

### Commands

| Command | Purpose |
|---|---|
| `git stash push -m "stash-name"` | Stash the uncommitted work with a message |
| `git stash list` | View the available stashes |
| `git stash pop` | Restore the latest stash and remove it from the stash list |
| `git status` | Check the current working tree |

### Workflow

`feature/recovery` → create `feature.py` → `git stash` → `main` → fix `main.py` → `git commit` → `git push` → `git stash list` → `git stash pop` → commit recovered work

> Git stash lets us temporarily put unfinished work aside so an urgent change can be handled without losing the current work.

## Task 8: **The Clean Merge**

### Objective

Complete the Git squash workflow:

▪ Make 3 small commits on `feature/system-optimization`

▪ Merge the feature branch into `main` using `git merge --squash`

▪ Create one clean commit on `main`

### Concept

▪ During development, a feature branch can contain multiple small commits that are useful while working but not necessary in the final history.

▪ `git merge --squash` combines the changes from those commits without bringing their individual commit history into `main`.

▪ We can then create one clean commit on `main` containing all the feature changes.

### How I Did It

▪ I made 3 small changes to `kernel_tuning.txt` on the `feature/system-optimization` branch and committed each change separately.

▪ I switched back to `main` and used `git merge --squash feature/system-optimization` to combine the changes.

▪ I created one clean commit on `main` and pushed the updated history to GitHub.

### Commands

| Command | Purpose |
|---|---|
| `git switch feature/system-optimization` | Switch to the feature branch |
| `git add kernel_tuning.txt` | Stage the changes |
| `git commit -m "..."` | Create each of the 3 feature commits |
| `git switch main` | Switch back to the main branch |
| `git merge --squash feature/system-optimization` | Combine the feature changes without the individual commits |
| `git commit -m "..."` | Create one clean commit on `main` |
| `git push origin main` | Push the clean commit to GitHub |

### Workflow

`feature/system-optimization` → 3 small commits → `git switch main` → `git merge --squash` → one clean commit → `git push origin main`

> Squash merging lets us keep the development history on the feature branch while keeping `main` clean and focused.

## Task 9: **The Conflict Resolution**

### Objective

▪ Create conflicting changes on the same line in two branches.

▪ Merge the branches and resolve the merge conflict.

▪ Complete the merge after resolving the conflict.

### Concept

▪ A merge conflict happens when two branches modify the same part of a file differently.

▪ Git cannot decide which change to keep, so we manually resolve the conflict.

▪ After resolving the conflict, we stage the file and commit the merge.

### Problem Faced

▪ The first two attempts resulted in a fast-forward merge instead of a conflict because `main` had no new commit after the branch was created.

### How I Solved It

▪ I made a separate commit on `main` with different text on the same line after creating the feature branch.

▪ This caused both branches to diverge from the same point and triggered the merge conflict.

▪ I manually edited `optimization.txt`, removed the conflict markers, staged the resolved file, and completed the merge.

### Commands

| Command | Purpose |
|---|---|
| `git merge conflict/optimization-test` | Merge the branch and trigger the conflict |
| `git status` | Check the conflicted file |
| `git add optimization.txt` | Mark the conflict as resolved |
| `git commit` | Complete the merge |

### Workflow

`create branch` → make conflicting changes → `git merge` → conflict → resolve manually → `git add` → `git commit`

> Merge conflicts are not errors to avoid. They are situations where Git needs us to decide which changes should remain.

## Task 10: **The Time Machine**

### Objective

Complete the Git recovery workflow:

▪ Make a commit

▪ Move `HEAD` back using `git reset --hard HEAD~1`

▪ Use `git reflog` to find the lost commit hash

▪ Move `HEAD` back to the lost commit and recover it

### Concept

▪ `HEAD` is Git's pointer to the commit we are currently on. When we make a new commit, `HEAD` moves forward to that commit.

▪ `git reset` moves the branch pointer and `HEAD` to another commit. With `--hard`, the working directory and staging area are also updated to match that commit.

▪ `HEAD~1` means the commit one step before the current `HEAD`. So `git reset --hard HEAD~1` moves `HEAD` back by one commit.

▪ `git reflog` keeps a record of where `HEAD` has pointed, which allows us to find a commit that is no longer visible in the normal Git history.

▪ Once we find the lost commit hash, `git reset --hard <hash>` moves `HEAD` and the branch pointer back to that commit and brings the work back.

### How I Did It

▪ I created and committed a test file, then used `git reset --hard HEAD~1` to move `HEAD` back and remove the commit from the normal history.

▪ I used `git reflog` to find the hash of the lost commit and verified it before recovering it.

▪ I used `git reset --hard <hash>` to move `HEAD` back to the lost commit and confirmed that the commit and file were restored.

### Commands

| Command                   | Purpose                                                         |
| ------------------------- | --------------------------------------------------------------- |
| `git commit -m "..."`     | Create the commit to be recovered                               |
| `git reset --hard HEAD~1` | Move `HEAD` and the branch pointer back by one commit           |
| `git reflog`              | Show previous positions of `HEAD` and find the lost commit      |
| `git show <hash>`         | Inspect the lost commit                                         |
| `git reset --hard <hash>` | Move `HEAD` and the branch pointer back to the recovered commit |
| `git log --oneline`       | Verify that the recovered commit is back in the history         |
                           |

### Workflow

`git commit` → `git reset --hard HEAD~1` → `git reflog` → find lost commit hash → `git reset --hard <hash>` → verify recovery

> Git can move `HEAD` and branch pointers backward, but reflog keeps track of where `HEAD` was so a lost commit can often be recovered.


## Conclusion

This assignment took Git from basic version control to real workflow situations: branching, investigation, context switching, clean history, conflict resolution, and recovery.

▪ Git is not just about saving code. It's about knowing where your work is, how it got there, and how to recover when something goes wrong.

▪ The commands may change from task to task, but the idea stays the same: make changes intentionally, keep history useful, and know how to get back when needed.

> An effective Git workflow is less about remembering commands and more about knowing what state your repository is in.
