# Chap 1 practice set
# TASK 1 
print(
    """
    this is multi line string
      in print statement
    """
)

# TASK 2 
import math
print(math.pi)

# TASK 3 
import pyjokes
print(pyjokes.get_joke())

# TASK 4
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, welcome to the world of programming")
engine.runAndWait()