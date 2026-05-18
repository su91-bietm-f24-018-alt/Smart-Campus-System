import gradio as gr


# Login Function
def login(username, password):

    if username == "Ameer Hamza" and password == "018":
        return "✅ Login Successful! Welcome to Smart Campus System"

    return "❌ Invalid Username or Password"


# Chatbot Function
def chatbot(message):

    msg = message.lower()

    if "attendance" in msg:
        return "📊 Your current attendance is 80%"

    elif "exam" in msg:
        return "📝 Your next exam starts on 21 May 2026"

    elif "notification" in msg:
        return "🔔 Assignment deadline: 19 May 2026"

    elif "timetable" in msg:
        return """
📅 Today's Timetable

9:00 AM - Software Engineering
11:00 AM - Web 1
1:00 PM - Technical Report Writting
"""

    elif "fee" in msg:
        return "💳 Fee Status: Paid"

    return "Ask about attendance, exam, fee, timetable or notification"


with gr.Blocks(title="Smart Campus System") as demo:

    gr.Markdown("# 🎓 Superior University Lahore")
    gr.Markdown("## AI Chatbot for Student Queries")

    with gr.Tab("Login Screen"):

        username = gr.Textbox(label="Username")

        password = gr.Textbox(
            label="Password",
            type="password"
        )

        btn = gr.Button("Login")

        output = gr.Textbox(label="Status")

        btn.click(
            login,
            [username, password],
            output
        )


    with gr.Tab("AI Chatbot"):

        gr.ChatInterface(
            fn=lambda x,history:
            chatbot(x)
        )

if __name__ == "__main__":
    demo.launch()