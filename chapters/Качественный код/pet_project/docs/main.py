from rich import pretty, print as print_pretty


def prrich():
    pretty.install()
    print_pretty([2, 2, 2, 2])


print(2, 2, 2, 2)
prrich()
