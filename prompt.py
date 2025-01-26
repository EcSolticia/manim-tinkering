
from click.testing import CliRunner
from manim.cli.render.commands import render

def render_scene_from_script():
    runner = CliRunner()

    arguments = [
        "test.py",  # script
        "Bye",    # class name
        "-pqh",
        "--renderer=opengl"
    ]

    # Simulate calling the `render` CLI command
    result = runner.invoke(render, arguments)

    # Print/handle output
    if result.exit_code == 0:
        print("Render successful!")
    else:
        print(f"Render failed: {result.output}")
        print(f"Error details: {result.exc_info}")

if __name__ == "__main__":
    render_scene_from_script()
