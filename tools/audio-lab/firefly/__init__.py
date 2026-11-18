"""Read-only ingestion of owner-generated Adobe Firefly sound effects."""

def main(argv=None):
    from .cli import main as cli_main
    return cli_main(argv)
