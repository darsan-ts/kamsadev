# kamsadev 🚀

A fast, lightweight wrapper around `customtkinter` designed for rapid Python GUI development. It completely eliminates layout boilerplate by letting you pass packing, gridding, and placing parameters directly into the widget constructors!

---

## ✨ Features

- **No Boilerplate:** Create and pack/grid a widget in a single line of code.
- **Smart Layout Handling:** Built-in support for `pack`, `grid`, and `place` right inside the `__init__` constructor.
- **Batch Generation:** Quickly generate ordered lists of labels, buttons, or checkboxes inside scrollable frames with single commands.
- **Built-in Debug Mode:** Left-click anywhere on your `kamsadev` window to print instant pixel coordinates to your terminal.
- **Easter Egg Included:** Try calling `easter_egg()` for a localized surprise. 😉

---

## 📦 Installation

Install the package directly from PyPI:

```bash
pip install kamsadev
```

---

## 🚀 Quick Start (The "Kamsa" Way)

Look how clean your code becomes. No separate `.pack()` or `.grid()` calls needed!

```python
import kamsadev

# 1. Initialize the main window effortlessly
root = kamsadev.kamsadev(name="My Quick App", size="600x400", theme="dark")

# 2. Widgets automatically pack themselves by default!
title = kamsadev.kamsalabel(master=root, text="Welcome to Kamsadev", font=("Arial", 24))
btn = kamsadev.kamsabutton(master=root, text="Click Me", command=lambda: print("Clicked!"))

# 3. Start the loop
root.run()
```

---

## 🛠️ API Reference & Syntax

### 1. Main Window (`kamsadev.kamsadev`)
Inherits from `ctk.CTk`. Opens up a heavily customized window instantly.
```python
app = kamsadev.kamsadev(
    name="TS",            # Window Title
    size="1920x1080",     # Geometry size
    bg="#242424",         # Background hex
    theme="dark",         # "dark" or "light"
    resizable=True,       # Window resizing permission
    fullscreen=False,     # Launch in fullscreen mode
    transparency=1.0,     # Window alpha (0.0 to 1.0)
    topmost=False,        # Stay on top of other windows
    icon=None,            # Path to .ico file
    debug=False           # Set to True to print click coordinates instantly!
)
```

### 2. Core Widgets (`kamsalabel`, `kamsabutton`, `kamsacheckbox`, `kamsaframe`)
All core widgets accept regular `customtkinter` visual parameters, plus **Layout Arguments** directly in the constructor:

#### **Layout Control Arguments:**
* **Pack Logic:** `pack=True` (default), `side="top"`, `fill="none"`, `expand=False`, `padx=0`, `pady=10`, `pack_anchor="center"`
* **Grid Logic:** `grid=True`, `row=0`, `column=0`, `columnspan=1`, `rowspan=1`, `sticky="nsew"`, `grid_padx=0`, `grid_pady=0`
* **Place Logic:** `place=True`, `x=0`, `y=0`, `relx=0.0`, `rely=0.0`

*Example using Grid instead of Pack:*
```python
# Disables default packing and snaps strictly onto a grid layout instead
submit_btn = kamsadev.kamsabutton(master=root, text="Submit", grid=True, row=2, column=1)
```

---

## 📜 Advanced Layout Automation (`kamsascrollableframe`)

Generate large lists of UI items instantly using mass-ordering methods:

```python
import kamsadev

root = kamsadev.kamsadev()

# Create the scrollable container
scroll_frame = kamsadev.kamsascrollableframe(master=root, width=300, height=400)

# Mass generate checkboxes inside the frame instantly!
scroll_frame.ordercheckbox("Item 1", "Item 2", "Item 3", "Item 4")

# Mass generate buttons inside the frame instantly!
scroll_frame.orderbutton("Save", "Load", "Clear", "Exit")

root.run()
```

---

## 🥚 Fun Features

### Debug Coordinate Finder
Struggling to figure out where to place a widget? Turn on `debug=True` in your window. Click anywhere on your app canvas, and the terminal will output:
```text
Clicked position -> x=245, y=108
```

### The Legendary Easter Egg
Want a quick level check? Import and call the hidden module tool:
```python
import kamsadev
kamsadev.easter_egg()
```

---

## 📄 License
Distributed under the MIT License. Built with ❤️ by developers, for fast developers.
