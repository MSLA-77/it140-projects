"""Project Two starter for the student's text-based adventure game."""

# Student Name: Lakesha Bennett


def show_instructions():
    """Display the game objective and available commands."""
    
    print("Welcome to the Text-Based Adventure Game!")
    print("Collect all items before encountering the villain.")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get item name")

    


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    
    print("----------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    print("----------------------")



def main():
    """Run the main gameplay loop."""
    
    # Rooms and items for Escape the Haunted Hotel
    rooms = {
        "Hotel Lobby": {
            "west": "Kitchen",
            "north": "Basement"
        },
        "Kitchen": {
            "east": "Hotel Lobby",
            "north": "Dining Room",
            "item": "Flashlight"
        },
        "Dining Room": {
            "south": "Kitchen",
            "north": "Laundry Room",
            "east": "Basement",
            "item": "Key"
        },
        "Laundry Room": {
            "south": "Dining Room",
            "east": "Guest Room",
            "item": "Rope"
        },
        "Guest Room": {
            "west": "Laundry Room",
            "east": "Security Room",
            "south": "Basement",
            "item": "Cell Phone"
        },
        "Security Room": {
            "west": "Guest Room",
            "south": "Storage Room",
            "item": "Security Badge"
        },
        "Storage Room": {
            "north": "Security Room",
            "west": "Basement",
            "item": "Crowbar"
        },
        "Basement": {
            "south": "Hotel Lobby",
            "west": "Dining Room",
            "north": "Guest Room",
            "east": "Storage Room"
        }
    }


    
    current_room = "Hotel Lobby"


    
    inventory = []


    
    show_instructions()


    
    while True:
        show_status(current_room, inventory, rooms)
        
        command = input("Enter your move: ").strip()

        if command.lower().startswith("go "):
            direction = command[3:].strip().lower()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You moved to the {current_room}.")
            else:
                print("You cannot go that way!")

        elif command.lower().startswith("get "):
            item_name = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name.lower() == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print(f"You picked up the {room_item}!")
                else:
                    print("That item is not in this room.")
            else:
                print("There is no item to collect here.")

        else:
            print("Invalid command. Please try again.")


        # Check whether the player encountered the villain.
        if current_room == "Basement":
            if len(inventory) == 6:
                print("Congratulations! You collected all six items!")
                print("You escaped the Haunted Hotel! You win!")
            else:
                print("Oh no! The villain caught you in the Basement!")
                print("Game Over! You lose!")

            break


if __name__ == "__main__":
    main()
