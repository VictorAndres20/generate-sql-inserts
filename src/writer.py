def write_code(path, content):
    content += "\n\n-- Generated by https://github.com/VictorAndres20 generate sql inserts"
    with open(path, "w") as f:
        f.write(content)