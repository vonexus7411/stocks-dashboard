import pytest
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ui.components.charts import create_chart, create_main_chart

@pytest.fixture
def root():
    """Fixture to create and destroy a tk root window"""
    root = tk.Tk()
    yield root
    root.destroy()

@pytest.fixture
def frame(root):
    """Fixture to create a frame for testing"""
    return ttk.Frame(root)

def test_create_chart(frame):
    """Test chart creation with basic parameters"""
    create_chart(frame, "Test Chart", "Y Label")
    
    # Verify chart components
    children = frame.winfo_children()
    assert len(children) == 1
    assert isinstance(children[0], FigureCanvasTkAgg().get_tk_widget().__class__)

def test_create_chart_dimensions(frame):
    """Test chart dimensions and properties"""
    create_chart(frame, "Test Chart", "Y Label")
    canvas = frame.winfo_children()[0]
    
    # Verify chart is configured to fill frame
    pack_info = canvas.pack_info()
    assert pack_info['fill'] == 'both'
    assert pack_info['expand'] == True

def test_create_main_chart(frame):
    """Test main chart creation"""
    create_main_chart(frame)
    
    # Verify label creation
    children = frame.winfo_children()
    assert len(children) == 1
    assert isinstance(children[0], ttk.Label)
    assert children[0].cget('text') == "Main Chart Area"

def test_create_chart_with_invalid_frame():
    """Test chart creation with invalid frame"""
    with pytest.raises(AttributeError):
        create_chart(None, "Test Chart", "Y Label")