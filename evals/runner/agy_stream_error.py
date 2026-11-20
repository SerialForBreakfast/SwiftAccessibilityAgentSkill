"""Recognize a terminal AGY service interruption without accepting partial output."""


def interrupted_stream(result, rc, process, log_path):
    if not (
        rc == 0
        and process == "exited"
        and result.get("status") == "ERROR"
        and result.get("finished_reason") == "error"
        and result.get("error") == "The stream was interrupted. Please continue the task you were working on."
    ):
        return False
    return "UNAVAILABLE (code 503)" in log_path.read_text(errors="replace")
