from typer import Typer, Argument

from external.gpteacher_api.gpteacher import GPTeacher

app = Typer()


@app.command()
def run():
    print("Running!")
    sentece = GPTeacher.get_sentence()
    ok = input("> ")
    print("ok")
    
@app.command()
def sentences(
    quant: int = Argument(10, help="The number of sentences to print")
):
    response = ", ".join([str(i) for i in range(quant)])
    print(f"Counting {response}")


if __name__ == "__main__":
    app()