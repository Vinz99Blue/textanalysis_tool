import sys
sys.path.insert(0, "./src")

from textanalysis_tool import hello

def greet(name: str = "User") -> str:
    return f"{hello("My Name")} \nIt's nice to meet you!"