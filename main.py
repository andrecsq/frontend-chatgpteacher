from typer import Typer

from external.gpteacher_api.gpteacher import GPTeacher

app = Typer()

gpteacher = GPTeacher()


@app.command()
def run():
    sentence_to_translate = gpteacher.get_sentence()
    print(f"Translate this Sentence: {sentence_to_translate}")

    translation_attempt = input("> ")

    correction = GPTeacher.get_correction(translation_attempt=translation_attempt)
    print("Correction:")
    print(correction)
    
@app.command()
def sentence():
    sentence_to_translate = gpteacher.get_sentence()

    print(sentence_to_translate)


if __name__ == "__main__":
    app()
