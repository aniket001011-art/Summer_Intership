def read_config():
    try: 
        open("the safe divider.py",'r')
    except FileNotFoundError:
        print("Error: The file [filename] was not found.")
    finally:
        print("File operations check complete.")
x = read_config()
print(x)