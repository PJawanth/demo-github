def greet(name: str = "World") -> str:
    """Return a hello message for name."""
    return f"Hello, {name}!"


def main() -> None:
    """Simple CLI: prints a greeting to stdout."""
    import argparse

    parser = argparse.ArgumentParser(description="Hello World CLI")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
