import json
from subprocess import check_output

def get_processes():
    """
    Wywołuje moduł C++ do uzyskania listy procesów.
    """
    output = check_output(["./scripts/system_monitor"])
    return json.loads(output)
