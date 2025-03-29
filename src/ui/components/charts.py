import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def create_chart(frame, title, ylabel):
    """Helper method to create charts for frames"""
    fig = Figure(figsize=(4, 3))
    ax = fig.add_subplot(111)

    data = np.random.rand(5) * 100
    x_pos = range(len(data))
    labels = ["A", "B", "C", "D", "E"]

    ax.bar(x_pos, data, align="center")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title(title)
    ax.set_ylabel(ylabel)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def create_main_chart(frame):
    """Helper method to create the main center chart"""
    ttk.Label(frame, text="Main Chart Area").pack(expand=True)
