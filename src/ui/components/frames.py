from tkinter import ttk
from ui.components.charts import create_chart, create_main_chart


class StockGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Grid Application")

        # Configure window to use full screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Create and configure main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure grid layout
        for i in range(4):
            self.main_frame.grid_columnconfigure(i, weight=1, uniform="col")
        for i in range(3):
            self.main_frame.grid_rowconfigure(i, weight=1, uniform="row")

        # ===== TOP LEFT FRAME =====
        self.top_left = ttk.Frame(self.main_frame)
        self.top_left.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        create_chart(self.top_left, "Top Left Chart", "Stock Performance")

        # ===== TOP CENTER-LEFT FRAME =====
        self.top_center_left = ttk.Frame(self.main_frame)
        self.top_center_left.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
        create_chart(self.top_center_left, "Volume Analysis", "Daily Volume")

        # ===== TOP CENTER-RIGHT FRAME =====
        self.top_center_right = ttk.Frame(self.main_frame)
        self.top_center_right.grid(row=0, column=2, padx=2, pady=2, sticky="nsew")
        create_chart(self.top_center_right, "Market Trends", "Sector Analysis")

        # ===== TOP RIGHT FRAME =====
        self.top_right = ttk.Frame(self.main_frame)
        self.top_right.grid(row=0, column=3, padx=2, pady=2, sticky="nsew")
        create_chart(self.top_right, "Price Indicators", "Technical Analysis")

        # ===== CENTER FRAME =====
        self.center_frame = ttk.Frame(self.main_frame)
        self.center_frame.grid(
            row=1, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )
        create_main_chart(self.center_frame)

        # ===== BOTTOM LEFT FRAME =====
        self.bottom_left = ttk.Frame(self.main_frame)
        self.bottom_left.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")
        create_chart(self.bottom_left, "Volume Analysis", "Daily Volume")

        # ===== BOTTOM CENTER-LEFT FRAME =====
        self.bottom_center_left = ttk.Frame(self.main_frame)
        self.bottom_center_left.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.bottom_center_left, text="Bottom Center-Left").pack(expand=True)

        # ===== BOTTOM CENTER-RIGHT FRAME =====
        self.bottom_center_right = ttk.Frame(self.main_frame)
        self.bottom_center_right.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.bottom_center_right, text="Bottom Center-Right").pack(
            expand=True
        )

        # ===== BOTTOM RIGHT FRAME =====
        self.bottom_right = ttk.Frame(self.main_frame)
        self.bottom_right.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.bottom_right, text="Bottom Right").pack(expand=True)

        # Configure root grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
