from object_serializer.serializer_factory import SerializerFactory
from typer import Typer

app = Typer()


@app.command()
def converter(file_from: str, file_to: str, format_from: str, format_to: str):
    from_serializer = SerializerFactory.create_serializer(format_from)
    to_serializer = SerializerFactory.create_serializer(format_to)

    with open(file_from, "r") as rfile, open(file_to, "w") as wfile:
        obj = from_serializer.load(rfile)
        print(f"Object was read from {file_from}")
        to_serializer.dump(obj, wfile)
        print(f"Object was saved to {file_to}")


if __name__ == "__main__":
    app()
