# Python Command-line Interface Libraries

Below are detailed descriptions and usage examples for key Python standard libraries related to command-line interfaces.

---

## argparse — Parser for Command-line Options, Arguments and Subcommands

**Description:**  
Provides a powerful parser for command-line options, arguments, and subcommands.

**Usage Example:**
```python
import argparse

parser = argparse.ArgumentParser(description='Example CLI')
parser.add_argument('--name', type=str, help='Your name')
args = parser.parse_args(['--name', 'Alice'])
print(args.name)  # Alice
```

---

## optparse — Parser for Command Line Options

**Description:**  
Legacy module for parsing command-line options (deprecated in favor of argparse).

**Usage Example:**
```python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--name", dest="name")
(options, args) = parser.parse_args(['--name', 'Alice'])
print(options.name)  # Alice
```

---

## getpass — Portable Password Input

**Description:**  
Provides a way to securely prompt the user for a password without echoing.

**Usage Example:**
```python
import getpass

password = getpass.getpass('Enter password: ')
print('Password entered:', '*' * len(password))
```

---

## fileinput — Iterate Over Lines from Multiple Input Streams

**Description:**  
Allows iteration over lines from multiple input streams (files or stdin).

**Usage Example:**
```python
import fileinput

for line in fileinput.input(['file1.txt', 'file2.txt']):
	print(line.strip())
```

---

## curses — Terminal Handling for Character-cell Displays

**Description:**  
Provides terminal handling for character-cell displays, supporting windowing and keyboard input.

**Usage Example:**
```python
import curses

def main(stdscr):
	stdscr.addstr(0, 0, "Hello, curses!")
	stdscr.refresh()
	stdscr.getkey()

curses.wrapper(main)
```

---

## curses.textpad — Text Input Widget for Curses Programs

**Description:**  
Implements a text input widget for curses programs.

**Usage Example:**
```python
import curses
import curses.textpad

def main(stdscr):
	win = curses.newwin(3, 30, 2, 2)
	box = curses.textpad.Textbox(win)
	stdscr.addstr(0, 0, "Enter text:")
	stdscr.refresh()
	text = box.edit()
	stdscr.addstr(4, 0, f"You entered: {text}")
	stdscr.refresh()
	stdscr.getkey()

curses.wrapper(main)
```

---

## curses.ascii — Utilities for ASCII Characters

**Description:**  
Provides utilities for working with ASCII characters.

**Usage Example:**
```python
import curses.ascii

print(curses.ascii.isdigit('5'))  # True
print(curses.ascii.isupper('A'))  # True
```

---

## curses.panel — A Panel Stack Extension for Curses

**Description:**  
Adds support for panel stacks (overlapping windows) in curses.

**Usage Example:**
```python
import curses
import curses.panel

def main(stdscr):
	win1 = curses.newwin(5, 20, 2, 2)
	win2 = curses.newwin(5, 20, 4, 4)
	panel1 = curses.panel.new_panel(win1)
	panel2 = curses.panel.new_panel(win2)
	curses.panel.update_panels()
	stdscr.refresh()
	stdscr.getkey()

curses.wrapper(main)
```

---

## cmd — Support for Line-oriented Command Interpreters

**Description:**  
Provides a simple framework for writing line-oriented command interpreters.

**Usage Example:**
```python
import cmd

class HelloCmd(cmd.Cmd):
	prompt = '> '
	def do_greet(self, line):
		print('Hello,', line)
	def do_exit(self, line):
		return True

if __name__ == '__main__':
	HelloCmd().cmdloop()
```

---
