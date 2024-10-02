from rich.console import Console
from rich.table import Table

# Create a Console instance to print formatted text
console = Console()

dream_cars = [
    {
        "Make": "Honda",
        "Model": "Civic",
        "Year": 2006,
        "Cost": 4500
    },
    {
        "Make": "Toyota",
        "Model": "Camry",
        "Year": 1999,
        "Cost": 1200
    },
    {
        "Make": "Honda",
        "Model": "Accord",
        "Year": 2000,
        "Cost": 2000
    },
    {
        "Make": "Smart",
        "Model": "Fortwo",
        "Year": 2000,
        "Cost": 2024
    }
]

console.print("Hello. I am conducting a survey on individual's dream cars. Here are mine first!", style="bold cyan")

def print_cars():
    console.print("\n[bold cyan]My dream cars:[/bold cyan]")
    for car in dream_cars:
        console.print("\n")
        for field, value in car.items():
            console.print(f"[magenta]{field}[/magenta]: {value}")

print_cars()

def prompt(): 
    console.print("Would you like to add more, or view the updated list? ", style="bold cyan")
    next = input("ADD/VIEW/EXIT: ")

    while next != "ADD" and next != "VIEW" and next != "EXIT":
        console.print("Wrong answer.", style="bold cyan")
        next = input("ADD/VIEW/EXIT: ")

    if next == "VIEW":
        print_cars()
        prompt()
    if next == "ADD":
        addCar()
        prompt()
    if next == "EXIT":
        console.print("Thanks for viewing.", style = "bold cyan")

def addCar():
    console.print("What is the make of your dream car?", style="bold cyan")
    make = input("Make: ")

    console.print("What is the model of your dream car?", style="bold cyan")
    model = input("Model: ")

    console.print("What is the year of your dream car?", style="bold cyan")
    year = input("Year: ")

    console.print("What is the cost of your dream car?", style="bold cyan")
    cost = input("Cost: ")

    dream_car = {"Make": make, "Model": model, "Year": year, "Cost": cost}


    console.print("Is this correct?", style="bold cyan")


    for field, value in dream_car.items():
        console.print(f"[magenta]{field}[/magenta]: {value}")
    response = input("Y/N: ")
    if response == "Y":
        dream_cars.append(dream_car)
        prompt()
    else:
        addCar()

console.print("Would you care to share your dream cars? Please respond Y/N", style="bold cyan")
y_n = input("Y/N: ")


while y_n != "Y":
    console.print("Wrong answer!", style="bold cyan")
    y_n = input("Y/N: ")

addCar()
