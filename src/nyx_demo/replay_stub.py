"""Replay a tiny synthetic Nyx drill card.

This file is intentionally shallow. It exists so reviewers can see the intended
shape of the demo without exposing a production rule base.
"""

from .action_card_templates import hold_verify, route_realign


def choose_card(event):
    if event.get("last_verified_checkpoint") == "stale":
        return route_realign()
    return hold_verify()


if __name__ == "__main__":
    print(choose_card({"last_verified_checkpoint": "stale"}))

