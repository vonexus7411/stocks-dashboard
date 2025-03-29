import pytest
import tkinter as tk
from tkinter import ttk
from ui.components.frames import StockGridApp

@pytest.fixture
def root():
    """Fixture to create and destroy a tk root window"""
    root = tk.Tk()
    yield root
    root.destroy()

def test_stock_grid_app_initialization(root):
    """Test basic initialization of StockGridApp"""
    app = StockGridApp(root)
    assert app.root.title() == "Stock Grid Application"
    assert isinstance(app.main_frame, ttk.Frame)

def test_grid_configuration(root):
    """Test grid configuration and weights"""
    app = StockGridApp(root)
    
    # Test column configuration
    for i in range(4):
        weight = app.main_frame.grid_columnconfigure(i, 'weight')
        assert weight == 1
        
    # Test row configuration
    for i in range(3):
        weight = app.main_frame.grid_rowconfigure(i, 'weight')
        assert weight == 1

def test_frame_creation(root):
    """Test creation of all frames"""
    app = StockGridApp(root)
    
    # Test top frames
    assert isinstance(app.top_left, ttk.Frame)
    assert isinstance(app.top_center_left, ttk.Frame)
    assert isinstance(app.top_center_right, ttk.Frame)
    assert isinstance(app.top_right, ttk.Frame)
    
    # Test center frame
    assert isinstance(app.center_frame, ttk.Frame)
    
    # Test bottom frames
    assert isinstance(app.bottom_left, ttk.Frame)
    assert isinstance(app.bottom_center_left, ttk.Frame)
    assert isinstance(app.bottom_center_right, ttk.Frame)
    assert isinstance(app.bottom_right, ttk.Frame)

def test_frame_grid_placement(root):
    """Test grid placement of frames"""
    app = StockGridApp(root)
    
    # Test top row placement
    assert app.top_left.grid_info()['row'] == 0
    assert app.top_left.grid_info()['column'] == 0
    
    # Test center frame placement
    assert app.center_frame.grid_info()['row'] == 1
    assert app.center_frame.grid_info()['columnspan'] == 4
    
    # Test bottom row placement
    assert app.bottom_right.grid_info()['row'] == 2
    assert app.bottom_right.grid_info()['column'] == 3

def test_window_dimensions(root):
    """Test window dimensions configuration"""
    app = StockGridApp(root)
    
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Get window geometry
    geometry = root.geometry()
    dimensions = geometry.split('+')[0]
    width, height = map(int, dimensions.split('x'))
    
    assert width == screen_width
    assert height == screen_height