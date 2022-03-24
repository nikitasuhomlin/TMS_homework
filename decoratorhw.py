def wrap(func):
    def wrapper(*args, **kwargs):
        print("[red]*обертка*[/red]")
        func(*args, **kwargs)
    return wrapper


@wrap
def gift(something):
    print(something)


