import json
import tkinter as tk
from tkinter import scrolledtext

class CookieFormatConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Format Converter")

        self.create_widgets()

    def create_widgets(self):
        self.create_string_to_json_widgets()
        self.create_json_to_string_widgets()

    def create_string_to_json_widgets(self):
        self.string_input = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.string_output = scrolledtext.ScrolledText(self.root, width=40, height=10)

        string_to_json_btn = tk.Button(self.root, text="Convert to JSON", command=self.on_string_to_json)

        self.string_input.grid(row=0, column=0, padx=10, pady=10)
        self.string_output.grid(row=1, column=0, padx=10, pady=10)
        string_to_json_btn.grid(row=2, column=0, padx=10, pady=5)

    def create_json_to_string_widgets(self):
        self.json_input = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.json_output = scrolledtext.ScrolledText(self.root, width=40, height=10)

        json_to_string_btn = tk.Button(self.root, text="Convert to String", command=self.on_json_to_string)

        self.json_input.grid(row=0, column=1, padx=10, pady=10)
        self.json_output.grid(row=1, column=1, padx=10, pady=10)
        json_to_string_btn.grid(row=2, column=1, padx=10, pady=5)

    def on_string_to_json(self):
        string_cookies = self.string_input.get("1.0", "end-1c")
        json_cookies = convert_to_json(string_cookies)
        self.json_output.delete("1.0", "end")
        self.json_output.insert("1.0", json_cookies)

    def on_json_to_string(self):
        json_cookies = self.json_input.get("1.0", "end-1c")
        string_cookies = convert_to_string(json_cookies)
        self.string_output.delete("1.0", "end")
        self.string_output.insert("1.0", string_cookies)

def convert_to_json(cookie_text):
    try:
        cookies_list = []
        cookies = cookie_text.split('; ')
        for cookie in cookies:
            name, value = cookie.split('=')
            cookies_list.append({
                "name": name.strip(),
                "value": value.strip()
            })
        formatted_cookies = json.dumps(cookies_list, indent=4)
    except Exception as e:
        print("Error converting to JSON:", e)
        formatted_cookies = ""
    return formatted_cookies

def convert_to_string(cookies_json):
    try:
        cookies_list = json.loads(cookies_json)
        formatted_cookies = ""
        for cookie in cookies_list:
            formatted_cookies += f"{cookie['name']}={cookie['value']}; "
        formatted_cookies = formatted_cookies.strip()
    except Exception as e:
        print("Error converting to string:", e)
        formatted_cookies = ""
    return formatted_cookies

if __name__ == "__main__":
    root = tk.Tk()
    app = CookieFormatConverterApp(root)
    root.mainloop()
