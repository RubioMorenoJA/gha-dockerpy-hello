import os
import random


def set_github_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as gh_out:
        print(f"{output_name}={output_value}", file=gh_out)

def run():
    dices_order = os.getenv("INPUT_DICES_ORDER", "two")
    set_github_action_output("dice1", f"{random.randint(1, 6)}")
    if dices_order == "two":
        set_github_action_output("dice2", f"{random.randint(1, 6)}")


if __name__ == "__main__":
    run()
