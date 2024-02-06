class Console:
    def __init__(self) -> None:
        self.prompt = 'geocalc1.0> '
        # Initialize an empty array for storing points.
        self.points = []

    def run(self) -> None:
        while True:
            try:
                command = input(self.prompt)
                # Exit commands.
                if command.lower() in ['exit', 'quit']:  
                    print("Exiting the console.")
                    break
                elif command.startswith('add_point'):
                    self.handle_add_point(command)
                elif command.startswith('remove_point'):
                    self.handle_remove_point(command)
                elif command.startswith('clear_points'):
                    self.handle_clear_points(command)
                else:
                    # Print user error in yellow.
                    print("\033[93m" + "Unknown command." + "\033[0m")
            except KeyboardInterrupt:
                print("\nExiting the console (interrupted).")
                break
            except EOFError:
                print("\nExiting the console (EOF).")
                break

    def handle_add_point(self, command) -> None:
        try:
            # Assuming the command format is "add_point x y"
            _, x, y = command.split()
            # Convert strings to integers and create an array.
            point = [int(x), int(y)]
            # Add the point to the points array.
            self.points.append(point)
            # Print a success message in green.
            print("\033[92m" + f"Point {point} added." + "\033[0m")
        except ValueError:
            # Print a user error in yellow.
            print("\033[93m" + "Invalid point format. Usage: add_point x y"
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error adding point: {e}" + "\033[0m")

    def handle_remove_point(self, command) -> None:
        try:
            # Assuming the command format is "remove_point x y"
            _, x, y = command.split()
            # Convert strings to integers and create an array.
            point = [int(x), int(y)]
            try:
                # Find the index of the point in points array.
                index = self.points.index(point)
                # Remove the point from the points array.
                del self.points[index]
                # Print a success message in green.
                print("\033[92m" + f"Point {point} removed." + "\033[0m")
            except ValueError:
                # Print an error in red.
                print("\033[91m" + f"Point entered does not exist." + "\033[0m")
        except ValueError:
            # Print an error in yellow.
            print("\033[93m" + "Invalid point format. Usage: remove_point x y"
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error removing point: {e}" + "\033[0m")
        
    def handle_clear_points(self, command) -> None:
        try:
            # Assuming the command format is "clear_points"
            _, = command.split()
            # Clear the list of points.
            self.points = []
            # Print a success message in green.
            print("\033[92m" + "Points cleared." + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error clearing points: {e}" + "\033[0m")


console = Console()
console.run()