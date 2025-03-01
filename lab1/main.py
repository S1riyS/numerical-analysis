from cli.commands import FileCommand, RandomCommand, StdinCommand
from cli.console.printer import Printer


def main():
    commands = [
        StdinCommand(),
        FileCommand(),
        RandomCommand(),
    ]

    is_command_valid = False
    while not is_command_valid:
        Printer.header("Выберите режим работы:")
        # List possible commands
        for i, command in enumerate(commands):
            Printer.info(f"{i + 1}. {command.get_name()}")

        # Read command
        try:
            command_number = int(input("Введите номер команды: "))
            command_index = command_number - 1
            if command_index < 0 or command_index >= len(commands):
                raise ValueError

            # Execute command
            Printer.new_line()
            commands[command_index].execute()
            is_command_valid = True

        except ValueError:
            Printer.error("Команды с таким номером не существует")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Printer.warning("\nРабота программы прервана")
