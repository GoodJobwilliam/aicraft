"""Small sample used by the MCP Code Review team trial."""

import os


def run_report(user_input: str) -> None:
    # Deliberately unsafe example: the trial should flag this before merge.
    os.system(user_input)
    print("report generated")
