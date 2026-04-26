"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        file_path = sys.argv[1]

        if len(sys.argv) < 3:
            return

        command = sys.argv[2]
        tasks = read_todo_file(file_path)

        if command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)

        elif command == "add":
            if len(sys.argv) < 4:
                raise IndexError('Task description required for "add".')

            task = sys.argv[3]
            tasks.append(task)
            write_todo_file(file_path, tasks)
            print(f'Task "{task}" added.')

        elif command == "remove":
            if len(sys.argv) < 4:
                raise IndexError('Task description required for "remove".')

            task = sys.argv[3]

            try:
                tasks.remove(task)
                write_todo_file(file_path, tasks)
                print(f'Task "{task}" removed.')
            except ValueError:
                print(f'Task "{task}" not found.')

        else:
            raise ValueError("Command not found!")

    except (IndexError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()