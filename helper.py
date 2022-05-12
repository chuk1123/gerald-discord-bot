def get_day():  
    with open('var.txt', 'r') as f:
        return f.read()

def update_day(val):
    with open('var.txt', 'r+') as f:
        f.truncate(0)
        f.write(str(val))

