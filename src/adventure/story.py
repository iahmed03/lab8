from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event


if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Intro panel
    console.print(Panel.fit(
        Text("🌲 You wake up in a dark forest. You can go left or right. 🌲", style="bold green"),
        title="The Adventure Begins",
        border_style="green"
    ))

    while True:
        choice = Prompt.ask(
            "[bold cyan]Which direction do you choose?[/bold cyan]",
            choices=["left", "right", "exit"],
            default="left"
        ).lower().strip()

        if choice == "exit":
            # Console-styled farewell
            console.print("\n[bold yellow]You decide to leave the forest...[/bold yellow]")
            console.print(Panel.fit(
                Text(
                    "🌅 The sunlight greets you as you find your way home.\n\n"
                    "[bold green]Thank you for playing![/bold green]",
                    justify="center"
                ),
                title="Farewell, Traveler",
                border_style="yellow"
            ))

            print("Goodbye!")
            break

        result = step(choice, events)
        console.print(Panel(result, border_style="blue", title="Your Journey Continues"))
