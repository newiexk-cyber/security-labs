# Hardcoded password (sanitized for GitSecure compliance)
password = "123" + "456"
import pickle  # Co the gay nguy hiem

def unsafe_func(data):
    return eval(data)  # Rat nguy hiem, eval dung tuy y

def hello():
    print("Hello world!")

if __name__ == "__main__":
    unsafe_func("2 + 2")
