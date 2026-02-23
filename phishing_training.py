import tkinter as tk
from tkinter import messagebox

# ---------------------------
# Main Application Class
# ---------------------------
class PhishingTrainingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Awareness Training")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f4f7")

        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "You receive an email asking for your bank password urgently. What should you do?",
                "options": [
                    "Reply with your password",
                    "Ignore and delete the email",
                    "Click the link and login",
                    "Forward to friends"
                ],
                "answer": 1
            },
            {
                "question": "Which is a sign of phishing?",
                "options": [
                    "Official domain email",
                    "Spelling mistakes and urgent tone",
                    "Secure HTTPS and correct URL",
                    "Email from known contact"
                ],
                "answer": 1
            },
            {
                "question": "What should you check before clicking a link?",
                "options": [
                    "Sender name only",
                    "URL carefully",
                    "Email color theme",
                    "Nothing"
                ],
                "answer": 1
            }
        ]

        self.create_main_menu()

    # ---------------------------
    # Main Menu
    # ---------------------------
    def create_main_menu(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Phishing Awareness Training",
                         font=("Arial", 22, "bold"), bg="#f0f4f7")
        title.pack(pady=20)

        buttons = [
            ("What is Phishing?", self.show_phishing_info),
            ("Recognizing Phishing Emails", self.show_email_info),
            ("Fake Websites", self.show_fake_website_info),
            ("Social Engineering", self.show_social_engineering),
            ("Best Practices", self.show_best_practices),
            ("Real World Examples", self.show_examples),
            ("Take Quiz", self.start_quiz)
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, width=35, height=2,
                      command=command, bg="#1976D2", fg="white",
                      font=("Arial", 12)).pack(pady=8)

    # ---------------------------
    # Content Display
    # ---------------------------
    def show_content(self, title_text, content_text):
        self.clear_screen()

        tk.Label(self.root, text=title_text,
                 font=("Arial", 20, "bold"),
                 bg="#f0f4f7").pack(pady=20)

        text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        text_area.insert("1.0", content_text)
        text_area.config(state="disabled")
        text_area.pack(expand=True, fill="both", padx=20, pady=10)

        tk.Button(self.root, text="Back to Menu",
                  command=self.create_main_menu,
                  bg="gray", fg="white").pack(pady=10)

    # ---------------------------
    # Training Sections
    # ---------------------------
    def show_phishing_info(self):
        content = """
Phishing is a cyber attack where attackers impersonate trusted entities
to steal sensitive information like passwords, credit card numbers, or personal data.

Common Targets:
- Banking credentials
- Social media accounts
- Corporate login systems
- OTP codes

Phishing attacks often create urgency and fear.
        """
        self.show_content("What is Phishing?", content)

    def show_email_info(self):
        content = """
How to Recognize Phishing Emails:

- Suspicious sender address
- Urgent language (e.g., "Act Now!")
- Spelling and grammar mistakes
- Unexpected attachments
- Requests for sensitive information

Always verify before clicking any link.
        """
        self.show_content("Recognizing Phishing Emails", content)

    def show_fake_website_info(self):
        content = """
How to Identify Fake Websites:

- Check URL spelling carefully
- Look for HTTPS and padlock symbol
- Avoid shortened links
- Verify domain name

Example:
Real: www.amazon.com
Fake: www.amaz0n-security.com
        """
        self.show_content("Fake Websites", content)

    def show_social_engineering(self):
        content = """
Social Engineering Tactics:

- Impersonation (pretending to be IT support)
- Creating urgency
- Emotional manipulation
- Authority exploitation
- Baiting (offering fake rewards)

Attackers manipulate human psychology.
        """
        self.show_content("Social Engineering", content)

    def show_best_practices(self):
        content = """
Best Practices to Stay Safe:

- Never share passwords
- Enable 2-Factor Authentication (2FA)
- Verify suspicious emails
- Keep software updated
- Report phishing attempts
- Use antivirus software

Stay alert and think before you click.
        """
        self.show_content("Best Practices", content)

    def show_examples(self):
        content = """
Real World Examples:

1. Fake bank email asking to verify account.
2. Fake job offer requesting payment.
3. WhatsApp message claiming lottery win.
4. Fake IT support asking for OTP.

Always verify with official sources.
        """
        self.show_content("Real World Examples", content)

    # ---------------------------
    # Quiz Section
    # ---------------------------
    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()

        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]

            tk.Label(self.root, text="Quiz",
                     font=("Arial", 20, "bold"),
                     bg="#f0f4f7").pack(pady=20)

            tk.Label(self.root, text=q["question"],
                     font=("Arial", 14),
                     bg="#f0f4f7").pack(pady=10)

            self.selected_option = tk.IntVar()

            for idx, option in enumerate(q["options"]):
                tk.Radiobutton(self.root, text=option,
                               variable=self.selected_option,
                               value=idx,
                               font=("Arial", 12),
                               bg="#f0f4f7").pack(anchor="w", padx=200)

            tk.Button(self.root, text="Submit",
                      command=self.check_answer,
                      bg="#388E3C", fg="white").pack(pady=20)

        else:
            messagebox.showinfo("Quiz Completed",
                                f"Your Score: {self.score}/{len(self.questions)}")
            self.create_main_menu()

    def check_answer(self):
        selected = self.selected_option.get()
        correct = self.questions[self.current_question]["answer"]

        if selected == correct:
            self.score += 1

        self.current_question += 1
        self.show_question()

    # ---------------------------
    # Utility
    # ---------------------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------------------------
# Run Application
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingTrainingApp(root)
    root.mainloop()