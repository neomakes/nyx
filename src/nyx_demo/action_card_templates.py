"""Small action-card templates for the public Nyx demo."""


def route_realign():
    return {
        "status": "RE-ORIENT / REALIGN",
        "next_actions": [
            "Recover the last verified checkpoint.",
            "Match two independent landmarks.",
            "Prepare handoff if the route still conflicts.",
        ],
    }


def hold_verify():
    return {
        "status": "HOLD / VERIFY",
        "next_actions": [
            "Hold position and keep distance.",
            "Collect a second independent cue.",
            "Mark for handoff if confidence stays low.",
        ],
    }

