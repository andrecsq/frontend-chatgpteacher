import json
from typer import Typer

from rich import print
from rich.prompt import Prompt

from external.gpteacher_api.gpteacher import GPTeacher
from external.objects import CorrectionPayload
from domain.style import print_full_table

app = Typer()
gpteacher = GPTeacher()


@app.command()
def run():

    while True:
        print()

        sentence_to_translate = gpteacher.get_sentence()

        translation_attempt = Prompt.ask(f"🔠 Translate [b]{sentence_to_translate}[/b] to [red]English[/red]")

        payload = CorrectionPayload(
            sentence_to_translate=sentence_to_translate,
            translation_attempt=translation_attempt
        )

        correction = gpteacher.post_correction(payload)

        correction_dict = json.loads(correction)

        if len(correction_dict['errors']) == 0:
            print("\n Congratulations! The translation is [b][green]correct[/green][/b]!")
        else:
            print_full_table(correction_dict['errors'])
    
@app.command()
def sentence():
    sentence_to_translate = gpteacher.get_sentence()

    print(sentence_to_translate)


if __name__ == "__main__":
    app()
