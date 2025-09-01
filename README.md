`
## 🧰 task-cli: A Simple Command-Line ToDo Manager

task-cli is a lightweight command-line tool for managing tasks directly from your terminal. Add, update, delete, and track tasks with ease — no GUI required.
This project was built as a sample solution to the thttps://github.com/Mezie-Gift/task-cli  project of roadmap.sh

---

## 🚀 Installation Guide

#### 📦 Prerequisites

- Python 3.6 or higher
- Git
- Unix-like environment (Linux, macOS, or Termux on Android)

---

#### 🛠️ Installation Steps

`bash

1. Clone the repository
```
git clone https://github.com/Mezie-Gift/task-cli.git
cd task-cli
```
2. Make the CLI script executable
chmod +x task-cli

3. (Optional) Install system-wide
sudo mv task-cli /usr/local/bin/task-cli
`

> ✅ After installation, you can run commands like:
> `bash
>
```
task-cli add "Buy groceries"
task-cli list
```
> `

---

## 📚 Available Commands

| Command                        | Description                          |
|-------------------------------|--------------------------------------|
| add "task"                  | Add a new task                       |
| update <id> "task"          | Update an existing task              |
| delete <id>                 | Delete a task                        |
| mark-done <id>              | Mark a task as done                  |
| mark-in-progress <id>       | Mark a task as in progress           |
| list                        | List all tasks                       |
| list done                   | List completed tasks                 |
| list todo                   | List pending tasks                   |
| list in-progress           | List tasks in progress               |

---

## 🧪 Testing the CLI

Try running:

```bash
task-cli list
```

If it displays your tasks, you're good to go!

---

## 🧰 Troubleshooting

- If you get command not found, make sure /usr/local/bin is in your $PATH.
- If you're on Windows, consider using WSL or Git Bash.

---

## 💡 Contributing

Pull requests are welcome! If you have suggestions for improvements or new features, feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

`
