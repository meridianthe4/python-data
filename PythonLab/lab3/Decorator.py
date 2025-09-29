# Q.4. Decorate the display_greeting() function using a decorator so that greeting is displayed in uppercase

def greetings_upper(inner):
    def wrapper(*args):
        txt = "".join(args)
        return inner(txt).upper()
    return wrapper

@greetings_upper
def greetings(name):
    return f"{name}!, Welcome to Dubai."

print(greetings("Mrugank"))