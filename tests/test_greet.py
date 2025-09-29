import sys
sys.path.insert(0, "./src")

from textanalysis_tool import greet

result = greet("My Name")

if result == "Hello My Name! \n It's nice to meet you!":
    print("Test passed!")
else:
    print("Test failed!")