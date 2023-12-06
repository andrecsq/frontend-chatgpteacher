from rich.table import Table
from rich import box
from rich.console import Console

def _generate_table_with_header():
    table = Table(box=box.MINIMAL)

    table.add_column("Error", style="magenta")
    table.add_column("Comment", style="cyan")

    return table

def _generate_rows(table: Table, errors: list):

    for error in errors:
        table.add_row(error['type'], error['comment'])

    return table

def _generate_full_table(errors: list):

    table = _generate_table_with_header()

    table = _generate_rows(table, errors)

    return table

def print_full_table(errors: list):
    table = _generate_full_table(errors)

    console = Console()
    console.print(table)
