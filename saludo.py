import os


def set_github_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as gh_out:
        print(f"{output_name}={output_value}", file=gh_out)
        

def run():
    name = os.getenv("INPUT_NAME", "Pepe")
    set_github_action_output("greeting", f"Hola, {name}!")


if __name__ == "__main__":
    run()
