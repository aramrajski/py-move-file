import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 and parts[0] == "mv":
        return
    _, source, destination = parts
    if not os.path.exists(source):
        return

    directory, filename = os.path.split(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with open(source, "r") as src_file:
            content = src_file.read()

        with open(destination, "w") as dst_file:
            dst_file.write(content)

    except Exception as e:
        print(f"Błąd podczas przenoszenia: {e}")

    os.remove(source)
