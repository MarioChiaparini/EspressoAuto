import click 

@click.command()
@click.option("--name", prompt="Enter Your name", help="Name of the user")
def hello(name):
    click.hello(f"Hello {name}!")

PRIORITIES = {
    "o":"Optional",
    "l":"Low",
    "m":"Medium"
}
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.PATH(exists=False), required=0)
@click.argument("-n", "--name", prompt="Enter todo name", help="Name of todo file")
@click.argument("-d", "--desc", prompt="Enter todo description", help="Description of todo file")
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} : {description} [Priority : {PRIORITIES[priority]}]")

if __name__ == "main":
    hello()