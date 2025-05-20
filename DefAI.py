import os
import tkinter as tk
import subprocess
import time
import threading
import queue
import shutil
from tkinter import messagebox

output_queue = queue.Queue()
current_directory = os.getcwd()
split_path = current_directory.split(os.sep)
first_three_parts = os.sep.join(split_path[:3])

def toggle_fullscreen(event=None):
    root.state('zoomed')

def exit_fullscreen(event=None):
    root.state('normal')

def fabric_setup():
    fabric_directory = first_three_parts + r'\.config\fabric'
    fabric_setup_source = current_directory + r'\fabric_env'

    if os.path.exists(fabric_directory):
        shutil.copytree(fabric_setup_source, fabric_directory, dirs_exist_ok=True)

def add_patterns():
    pattern_directory = first_three_parts + r'\.config\fabric\patterns'
    patterns_source = current_directory + r'\patterns'

    os.makedirs(pattern_directory, exist_ok=True)
    shutil.copytree(patterns_source, pattern_directory, dirs_exist_ok=True)

def setup_fabric(root):
    fabric_directory = first_three_parts + r'\.config\fabric'
    os.makedirs(fabric_directory, exist_ok=True)

    def submit_form():
        api_key = api_key_entry.get().strip()
        selected_model = model_var.get()

        if not api_key:
            messagebox.showwarning("Input Error", "Please enter an API key.")
            fabric_window.lift()
            return

        if not selected_model or selected_model not in model_options:
            messagebox.showwarning("Input Error", "Please select a valid model.")
            fabric_window.lift()
            return

        config_lines = [
            "DEFAULT_VENDOR=OpenAI",
            f"DEFAULT_MODEL={selected_model}",
            "PATTERNS_LOADER_GIT_REPO_URL=https://github.com/danielmiessler/fabric.git",
            "PATTERNS_LOADER_GIT_REPO_PATTERNS_FOLDER=patterns",
            "PROMPT_STRATEGIES_GIT_REPO_URL=https://github.com/danielmiessler/fabric.git",
            "PROMPT_STRATEGIES_GIT_REPO_STRATEGIES_FOLDER=strategies",
            f"OPENAI_API_KEY={api_key}",
            "OPENAI_API_BASE_URL=https://api.openai.com/v1"
        ]

        with open("fabric_env/.env", "w") as f:
            f.write("\n".join(config_lines))

        threading.Thread(target=fabric_setup(), daemon=True).start()
        threading.Thread(target=add_patterns(), daemon=True).start()
        time.sleep(2)

        fabric_window.destroy()

    def on_model_select(event):
        selected_index = model_listbox.curselection()
        if selected_index:
            selected_model = model_listbox.get(selected_index)
            model_var.set(selected_model)

    fabric_window = tk.Toplevel(root)
    fabric_window.title("AI Vendor Setup")

    window_width = 500
    window_height = 400
    screen_width = fabric_window.winfo_screenwidth()
    screen_height = fabric_window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    fabric_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(fabric_window, text="API Key:").pack(pady=(30, 5), anchor='w', padx=20)
    api_key_entry = tk.Entry(fabric_window, show="*")
    api_key_entry.pack(fill=tk.X, padx=20)

    tk.Label(fabric_window, text="Select Default Model:").pack(pady=(20, 5), anchor='w', padx=20)

    model_var = tk.StringVar()

    model_options = [
        "babbage-002",
        "davinci-002",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0125",
        "gpt-3.5-turbo-1106",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-instruct",
        "gpt-3.5-turbo-instruct-0914",
        "gpt-4.1",
        "gpt-4.1-2025-04-14",
        "gpt-4.1-mini",
        "gpt-4.1-mini-2025-04-14",
        "gpt-4.1-nano",
        "gpt-4.1-nano-2025-04-14",
        "gpt-4.5-preview",
        "gpt-4.5-preview-2025-02-27",
        "gpt-4o",
        "gpt-4o-2024-05-13",
        "gpt-4o-2024-08-06",
        "gpt-4o-2024-11-20",
        "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18",
        "gpt-4o-mini-search-preview",
        "gpt-4o-mini-search-preview-2025-03-11",
        "gpt-4o-search-preview",
        "gpt-4o-search-preview-2025-03-11",
        "o1-mini",
        "o1-mini-2024-09-12",
        "o1-preview",
        "o1-preview-2024-09-12",
    ]

    model_var.set(model_options[0])

    frame = tk.Frame(fabric_window)
    frame.pack(fill=tk.X, padx=20, pady=5)

    scrollbar = tk.Scrollbar(frame, orient="vertical")

    model_listbox = tk.Listbox(frame, height=10, selectmode=tk.SINGLE)
    for model in model_options:
        model_listbox.insert(tk.END, model)

    model_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=model_listbox.yview)

    model_listbox.bind("<<ListboxSelect>>", on_model_select)

    model_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tk.Button(fabric_window, text="Submit", command=submit_form).pack(pady=30)

    fabric_window.update_idletasks()
    fabric_window.deiconify()
    fabric_window.lift()
    fabric_window.focus_force()

def startup(root):
    fabric_env = first_three_parts + r'\.config\fabric\.env'

    if not os.path.isfile(fabric_env):
        setup_fabric(root)

def create_section(parent, title, elements):
    title_frame = tk.Frame(parent, bg="#e0e0e0")
    title_frame.pack(fill="x", padx=20, pady=(10, 5))

    label = tk.Label(title_frame, text=title, font=("Arial", 18, "bold"), bg="#e0e0e0", fg="black", padx=10, pady=10)
    label.pack(fill="x", expand=True)

    input_options = {
        "Program": ["Program File Path:"],
        "Network Vulnerability": ["Nmap Results File Path:"],
        "Network Traffic": ["Network Traffic Capture File Path:"],
        "Behavior": ["Username:", "Log File Path:"],
        "Nmap": ["Flags:", "IP Address:"],
        "CVE": ["CVE ID (CVE-2025-47419):"]
    }

    button_frame = tk.Frame(parent, bg="#e0e0e0")
    button_frame.pack(fill="x", padx=20, pady=5)

    for i in range(len(elements)):
        button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(0, weight=1)

    for i, element in enumerate(elements):
        btn = tk.Button(
            button_frame,
            text=element,
            font=("Arial", 12),
            width=20,
            height=2,
            bg="black",
            fg="white",
            command=lambda e=element: open_new_window(e, input_options.get(e, [])))
        btn.grid(row=i, column=0, sticky="ew", pady=2)

def open_new_window(title, inputs):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("500x250")

    new_window.update_idletasks()
    window_width = 500
    window_height = 200
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(new_window, text=f"{title} Window", font=("Arial", 16))
    label.pack(pady=10)

    entry_widgets = []
    for input_label in inputs:
        frame = tk.Frame(new_window)
        frame.pack(pady=5)

        label = tk.Label(frame, text=input_label, font=("Arial", 12))
        label.pack(side="left", padx=5)
        entry = tk.Entry(frame, font=("Arial", 12))
        entry.pack(side="right", padx=5)
        entry_widgets.append(entry)

    def submit_action():
        inputs = [entry.get().strip() for entry in entry_widgets]
        user_input = " ".join(inputs)

        if title == "Program":
            handle_program(user_input)
        elif title == "Network Vulnerability":
            handle_network_vulnerability(user_input)
        elif title == "Network Traffic":
            handle_network_traffic(user_input)
        elif title == "Behavior":
            handle_behavior(user_input)
        elif title == "Nmap":
            handle_nmap(user_input)
        elif title == "CVE":
            handle_cve(user_input)

        new_window.destroy()

    submit_button = tk.Button(
        new_window,
        text="Submit",
        font=("Arial", 12),
        command=submit_action
    )
    submit_button.pack(pady=20)

def handle_program(user_input):
    def run_subprocess():
        try:
            with open(user_input, "r", encoding="utf-8", errors="replace") as f:
                ser_input = f.read()
        except Exception as e:
            output_queue.put(f"Error reading file: {e}")
            return

        try:
            process = subprocess.Popen(
                [".\\fabric-windows-amd64.exe", "/s", "/p", "program"],
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding="utf-8",
                errors="replace"
            )

            if process.stdin:
                process.stdin.write(ser_input)
                process.stdin.flush()
                process.stdin.close()

            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    output_queue.put(output)
        except Exception as e:
            output_queue.put(f"Subprocess error: {e}")

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def handle_network_vulnerability(user_input):
    def run_subprocess():
        try:
            with open(user_input, "r", encoding="utf-8", errors="replace") as f:
                ser_input = f.read()
        except Exception as e:
            output_queue.put(f"Error reading file: {e}")
            return

        try:
            process = subprocess.Popen(
                [".\\fabric-windows-amd64.exe", "/s", "/p", "network_vulnerability"],
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding="utf-8",
                errors="replace"
            )

            if process.stdin:
                process.stdin.write(ser_input)
                process.stdin.flush()
                process.stdin.close()

            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    output_queue.put(output)
        except Exception as e:
            output_queue.put(f"Subprocess error: {e}")

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def handle_network_traffic(user_input):
    def run_subprocess():
        try:
            with open(user_input, "r", encoding="utf-8", errors="replace") as f:
                ser_input = f.read()
        except Exception as e:
            output_queue.put(f"Error reading file: {e}")
            return

        try:
            process = subprocess.Popen(
                [".\\fabric-windows-amd64.exe", "/s", "/p", "network_traffic"],
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding="utf-8",
                errors="replace"
            )

            if process.stdin:
                process.stdin.write(ser_input)
                process.stdin.flush()
                process.stdin.close()

            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    output_queue.put(output)
        except Exception as e:
            output_queue.put(f"Subprocess error: {e}")

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def handle_behavior(user_input):
    def run_subprocess():
        try:
            try:
                username, file_path = map(str.strip, user_input.split(" ", 1))
            except ValueError:
                print(user_input)
                output_queue.put("Invalid input format. Expected: 'username, path_to_log_file'")
                return

            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                ser_input = f.read()
        except Exception as e:
            output_queue.put(f"Error reading file: {e}")
            return

        try:
            process = subprocess.Popen(
                [".\\fabric-windows-amd64.exe", "/s", "/p", "behavior"],
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding="utf-8",
                errors="replace"
            )

            if process.stdin:
                process.stdin.write("The username of the user I want a behavior analysis of is " + username + ". This is the contents of the user actions log: " + ser_input)
                process.stdin.flush()
                process.stdin.close()

            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    output_queue.put(output)
        except Exception as e:
            output_queue.put(f"Subprocess error: {e}")

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()


def handle_nmap(user_input):
    def run_subprocess():
        process = subprocess.Popen(
            ["./Nmap/nmap.exe", *user_input.split()],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            encoding="utf-8",
            errors="replace",
        )

        output_path = os.path.abspath("nmap_output.txt")

        with open(output_path, "w", encoding="utf-8") as f:
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    output_queue.put(output)
                    f.write(output)
                    f.flush()

        output_queue.put(f"\nNmap results saved to: {output_path}\n")

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def handle_cve(user_input):
    def run_subprocess():
        process = subprocess.Popen(
            [".\\fabric-windows-amd64.exe", "/s", "/p", "cve"],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            encoding="utf-8",
            errors="replace"
        )

        if process.stdin:
            process.stdin.write("Tell me about" + user_input + "\n")
            process.stdin.flush()
            process.stdin.close()

        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                output_queue.put(output)

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def ask_cyber_question_pattern(user_input):
    def run_subprocess():
        process = subprocess.Popen(
            [".\\fabric-windows-amd64.exe", "/s", "/p", "ask_cyber_question"],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            encoding="utf-8",
            errors="replace"
        )

        if process.stdin:
            process.stdin.write(user_input + "\n")
            process.stdin.flush()
            process.stdin.close()

        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                output_queue.put(output)

    thread = threading.Thread(target=run_subprocess, daemon=True)
    thread.start()

def check_output_queue():
    try:
        while True:
            output = output_queue.get_nowait()

            if output.strip().endswith("INPUT:"):
                output = output.strip()[:-6].rstrip()

            if output.strip():
                response_box_main.insert(tk.END, output + "\n")
                response_box_main.see(tk.END)
    except queue.Empty:
        pass

    root.after(10, check_output_queue)

def talk_to_defai_send(user_input):
    ask_cyber_question_pattern(user_input)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("DefAI")
root.geometry("1920x1080")
root.configure(bg="#e0e0e0")
root.state('zoomed')
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=30)
root.grid_rowconfigure(2, weight=30)
root.grid_rowconfigure(3, weight=30)
root.grid_rowconfigure(4, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

header = tk.Frame(root, bg="black", height=10)
header.grid(row=0, column=0, columnspan=2, sticky="nsew")
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=8)
header.grid_columnconfigure(2, weight=0)
header.grid_columnconfigure(3, weight=0)
header.grid_columnconfigure(4, weight=0)

dashboard_label = tk.Label(header, text="          DefAI", font=("Arial", 20, "bold"), bg="black", fg="white")
dashboard_label.grid(row=0, column=1, sticky="nsew")

btn_fabric_setup = tk.Button(header, text="Setup Fabric", font=("Arial", 12), bg="white", fg="black", borderwidth=0, width=12, height=1, command=lambda: setup_fabric(root))
btn_fabric_setup.grid(row=0, column=5, padx=10)

frame_left = tk.Frame(root, bg="#e0e0e0")
frame_left.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
create_section(frame_left, "Analysis", ["Program", "Network Vulnerability", "Network Traffic", "Behavior"])

frame_center = tk.Frame(root, bg="#e0e0e0")
frame_center.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
create_section(frame_center, "Information", ["Nmap", "CVE"])

frame_right = tk.Frame(root, bg="#e0e0e0")
frame_right.grid(row=1, column=1, rowspan=3, padx=20, pady=20, sticky="nsew")

frame_right.grid_rowconfigure(0, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

response_frame = tk.Frame(frame_right, bg="#e0e0e0")
response_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

response_box_main = tk.Text(response_frame, font=("Arial", 12), height=5, bg="white", relief="sunken", wrap="word")
response_box_main.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(response_frame, command=response_box_main.yview)
scrollbar.pack(side="right", fill="y")

response_box_main.config(yscrollcommand=scrollbar.set)

frame_talk = tk.Frame(root, bg="#e0e0e0")
frame_talk.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

label_talk = tk.Label(frame_talk, text="Talk to DefAI", font=("Arial", 20, "bold"), bg="#e0e0e0", fg="black", padx=10, pady=10)
label_talk.pack(fill="x", padx=20, pady=(10, 20))

entry = tk.Entry(frame_talk, font=("Arial", 14), width=40)
entry.pack(pady=10, fill="x", padx=20)

send_button = tk.Button(frame_talk, text="Send", font=("Arial", 14), bg="black", fg="white", command=lambda: talk_to_defai_send(entry.get()))
send_button.pack(pady=10, fill="x", padx=20)

root.after(100, check_output_queue)

startup(root)

root.mainloop()