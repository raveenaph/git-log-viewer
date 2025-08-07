import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from git import Repo
from datetime import datetime

root = tk.Tk()
root.title("Git Log Viewer")
root.geometry("800x600")

repo_path = tk.StringVar()
commit_count = tk.IntVar(value="5")

def choose_folder():
    folder = filedialog.askdirectory(initialdir=r"C:/Users/ravee/PROJECTS")
    if(folder):
        repo_path.set(folder)

tk.Label(root, text="Repo path: ").pack()
tk.Entry(root, textvariable=repo_path, width="80").pack()
tk.Button(root, text="Browse", command=choose_folder).pack()
tk.Label(root, text="Number of Commits: ").pack()
tk.Entry(root, textvariable=commit_count).pack()

output_box = tk.Text(root, wrap="word")
output_box.pack(fill="both", expand=True)

def get_commit_logs(repo_path, count): 

    repo = Repo(repo_path)
    assert not repo.bare

    last_commits = list(repo.iter_commits("main", max_count=count))

    output = "" 

    for commit in last_commits: 
        output += f"Commit: {commit.hexsha}\n"
        output += f"Committer: {commit.author}\n"
        output += f"Message: {commit.message.strip()}\n"
        output += f"Date: {datetime.fromtimestamp(commit.committed_date).strftime('%Y-%m-%d %H:%M:%S')}\n"

        diffs = commit.diff(commit.parents[0]) if commit.parents else []
        if diffs:
            output += "Files changed:\n"
            for diff in diffs:
                output += f"  - {diff.a_path}\n"
        else:
            output += "Files changed: None\n"
    return output

def run_log():
    try:
        path = repo_path.get()
        count = int(commit_count.get())
        result = get_commit_logs(path,count)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Get Commits", command=run_log).pack()

root.mainloop()
#
# repo.index.diff(None)
#does only list files that have not been staged

#repo.index.diff('Head')
#does only list files that have been staged
# #