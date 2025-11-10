from tkinter import *

# Word lists
positive_words = [
    "good", "excellent", "amazing", "happy", "satisfied", "love", "great", 
    "awesome", "fantastic", "wonderful", "outstanding", "superb", "brilliant",
    "perfect", "nice", "pleasant", "delighted", "pleased", "impressed",
    "recommend", "best", "fine", "smooth", "easy", "helpful", "friendly",
    "quick", "fast", "reliable", "worth", "valuable", "useful", "effective"
]

negative_words = [
    "bad", "poor", "terrible", "unhappy", "worst", "hate", "disappointed",
    "awful", "horrible", "dislike", "horrendous", "useless", "waste",
    "broken", "damaged", "defective", "faulty", "slow", "difficult",
    "complicated", "confusing", "frustrating", "annoying", "angry",
    "ridiculous", "stupid", "pointless", "rubbish", "trash", "junk"
]

def feedback_analyze(feedback):
    feedback = feedback.lower()
    for word in positive_words:
        if word in feedback: return "Positive"
    for word in negative_words:
        if word in feedback: return "Negative"
    return "Neutral"

# Menu functions
def dummy_command(): pass
def exit_app(): root.quit()

# GUI Setup
root = Tk()
root.title("Customer Feedback Analyzer")
root.geometry("600x400")

# Menu Bar
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=dummy_command)
file_menu.add_command(label="Open", command=dummy_command)
file_menu.add_command(label="Save", command=dummy_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Counters
positive_count = negative_count = neutral_count = 0

def analyze_feedback():
    global positive_count, negative_count, neutral_count
    feedback = feedback_entry.get()
    if not feedback.strip():
        result_label.config(text="Please enter some feedback!")
        return
    
    category = feedback_analyze(feedback)
    result_label.config(text=f"Feedback classified as: {category}")
    
    if category == "Positive": positive_count += 1
    elif category == "Negative": negative_count += 1
    else: neutral_count += 1
    
    update_summary()
    feedback_entry.delete(0, END)

def update_summary():
    summary_label.config(text=f"Summary:\nPositive: {positive_count}\nNegative: {negative_count}\nNeutral: {neutral_count}")

# GUI Widgets
title_label = Label(root, text="Customer Feedback Analyzer", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

feedback_label = Label(root, text="Enter Feedback:")
feedback_label.pack()

feedback_entry = Entry(root, width=60)
feedback_entry.pack()

analyze_button = Button(root, text="Analyze Feedback", command=analyze_feedback, bg="#2196F3", fg="white")
analyze_button.pack(pady=5)

result_label = Label(root, text="")
result_label.pack()

summary_label = Label(root, text="Summary:\nPositive: 0\nNegative: 0\nNeutral: 0")
summary_label.pack(pady=5)


# ------------------------------------------------------------------
# DATA VISUALIZATION
# ------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# DataFrame for manipulation
def get_feedback_dataframe():
    data = {
        "Sentiment": ["Positive", "Negative", "Neutral"],
        "Count": [positive_count, negative_count, neutral_count]
    }
    return pd.DataFrame(data)

# Visualization Functions
def show_bar_chart():
    df = get_feedback_dataframe()
    plt.bar(df["Sentiment"], df["Count"], color=["green", "red", "gray"])
    plt.title("Customer Feedback Sentiment Distribution")
    plt.xlabel("Sentiment Category")
    plt.ylabel("Number of Feedbacks")
    plt.show()

def show_pie_chart():
    df = get_feedback_dataframe()
    plt.pie(df["Count"], labels=df["Sentiment"], autopct='%1.1f%%',
            colors=["#4CAF50", "#F44336", "#9E9E9E"], startangle=90)
    plt.title("Sentiment Proportion (Visual Summary)")
    plt.show()

def show_trend_prediction():
    df = get_feedback_dataframe()
    x = np.array([1, 2, 3])  # categories
    y = np.array(df["Count"])
    
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    line = slope * x + intercept
    
    plt.scatter(x, y, color='blue')
    plt.plot(x, line, color='orange', linestyle='--')
    plt.title("Sentiment Trend Prediction")
    plt.xlabel("Sentiment Type (1=Pos, 2=Neg, 3=Neu)")
    plt.ylabel("Count of Feedbacks")
    plt.show()

# Visualization Buttons
visual_frame = Frame(root)
visual_frame.pack(pady=10)

bar_btn = Button(visual_frame, text="Show Bar Chart", command=show_bar_chart, bg="#4CAF50", fg="white")
bar_btn.grid(row=0, column=0, padx=10)

pie_btn = Button(visual_frame, text="Show Pie Chart", command=show_pie_chart, bg="#9C27B0", fg="white")
pie_btn.grid(row=0, column=1, padx=10)

trend_btn = Button(visual_frame, text="Predict Trend", command=show_trend_prediction, bg="#FF9800", fg="white")
trend_btn.grid(row=1, column=0, columnspan=2, pady=5)
# ------------------------------------------------------------------

root.mainloop()
