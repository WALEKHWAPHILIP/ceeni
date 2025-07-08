

````markdown
# 🧱 CEENI Project Setup & Git Initialization Guide

This guide documents all foundational steps taken to set up the CEENI project — from creating the local project structure to initializing Git and pushing to GitHub. It is meant to be a clean, repeatable reference in case the project ever needs to be recreated from scratch.

---

## 📁 1. Create Project Folder Structure

We chose `C:\apps\ceeni` as the working path.

```bash
mkdir C:\apps\ceeni
cd C:\apps\ceeni
````

---

## 🐍 2. Create and Activate Virtual Environment

A virtual environment ensures isolation from global Python packages.

```bash
python -m venv ceeni_venv
ceeni_venv\Scripts\activate
```

Once activated, you should see the prompt like:

```
(ceeni_venv) C:\apps\ceeni>
```

---

## 🌿 3. Initialize Git Repository

Run the following to start version control in the project directory:

```bash
git init
```

This creates the `.git/` directory and prepares Git to track files.

---

## 📄 4. Add a Clean `.gitignore` File

Download the official Python `.gitignore` template from GitHub:

```bash
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
```

Then open the file in Notepad:

```bash
notepad .gitignore
```

At the bottom, append CEENI-specific entries:

```gitignore
# CEENI project-specific additions
ceeni_venv/      # Local virtual environment folder
static/          # Collected static files (if generated)
media/           # Uploaded media files
*.sqlite3        # SQLite databases
*.sql            # SQL dump files
.vscode/         # Visual Studio Code settings folder
```

These exclusions prevent unnecessary or sensitive files from being tracked.

---

## ⚖️ 5. Normalize Line Endings with `.gitattributes`

To avoid CRLF vs LF issues across operating systems, normalize line endings using:

```bash
echo * text=auto > .gitattributes
```

This file tells Git to automatically handle line endings consistently.

---

## ⚙️ 6. Configure Global Git Settings (Windows-Friendly)

Run the following **only once** to set up Git globally:

```bash
git config --global core.autocrlf true         # Prevent line ending conflicts
git config --global pull.rebase true           # Avoid messy merge commits
git config --global init.defaultBranch main    # Default to main branch
```

---

## ✅ 7. Stage and Commit Initial Files

Add the `.gitignore` and `.gitattributes` to version control:

```bash
git add .gitignore .gitattributes
git commit -m "Add .gitattributes and CEENI-optimized .gitignore"
```

This creates the first commit (root commit) of your project history.

---

## ☁️ 8. Connect to GitHub

Your GitHub repository URL is:

```
https://github.com/WALEKHWAPHILIP/ceeni.git
```

Add it as the remote origin:

```bash
git remote add origin https://github.com/WALEKHWAPHILIP/ceeni.git
```

If you made a mistake earlier:

```bash
git remote set-url origin https://github.com/WALEKHWAPHILIP/ceeni.git
```

Check it with:

```bash
git remote -v
```

Expected output:

```
origin  https://github.com/WALEKHWAPHILIP/ceeni.git (fetch)
origin  https://github.com/WALEKHWAPHILIP/ceeni.git (push)
```

---

## 🚀 9. Push to GitHub and Set Upstream

Push the main branch and set it to track GitHub:

```bash
git push --set-upstream origin main
```

If successful, you'll see:

```
branch 'main' set up to track 'origin/main'.
```

---

## ✅ Final Status

At this point:

* [x] Local Git repository is initialized
* [x] Python-specific `.gitignore` is added and customized for CEENI
* [x] `.gitattributes` normalizes cross-platform line endings
* [x] Project is committed and pushed to GitHub under `main` branch
* [x] You are ready to begin Django scaffolding

---

## ⏭️ Next Step

Create the Django project inside the same folder:

```bash
django-admin startproject config .
```

This will create:

* `config/` folder for Django settings
* `manage.py` in the root directory

---

## 🗃️ Appendix: File Structure So Far

```
ceeni/
├── .git/                  # Git internal data
├── .gitignore             # Ignored files list
├── .gitattributes         # Line ending normalization
├── ceeni_venv/            # Virtual environment (excluded from Git)
└── (manage.py + config/)  # To be created in the next step
```

---

## 📘 Notes

* This setup is ideal for collaborative development
* Your documentation folder (`/docs/`) should be tracked in Git
* Never include `.env`, secrets, or venvs in version control

---

Let CEENI be born.
Let equity be law.
Let justice be measured.

```


