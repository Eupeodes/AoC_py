import sys
import importlib

if len(sys.argv) < 4:
    print("Gebruik: python AoC.py <action> <year> <dag>")
    sys.exit(1)

action = sys.argv[1]
year = sys.argv[2]
day = sys.argv[3]

match action:
    case 'run':
        module = importlib.import_module(f'solution.{year}.{day}')

        solution = module.Solution()
        solution.run()

    case 'init':
       
        from init import fetch_input
        fetch_input(int(year), int(day))

    case _:
        print(f"Onbekende actie: {action}")
