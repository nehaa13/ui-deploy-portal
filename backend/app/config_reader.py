import json
import os
from typing import List

# Path where JSONs are mounted/cloned
CONFIG_BASE_PATH = "/configs"   # later: git clone or volume mount


def _load_json(lob: str, env: str) -> dict:
    """
    Example path:
    /configs/omniexpress/dev.json
    """
    file_path = f"{CONFIG_BASE_PATH}/{lob}/{env.lower()}.json"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config not found: {file_path}")

    with open(file_path, "r") as f:
        return json.load(f)


# -----------------------
# Public API functions
# -----------------------

def list_lobs() -> List[str]:
    """Return all LOBs"""
    return sorted([
        d for d in os.listdir(CONFIG_BASE_PATH)
        if os.path.isdir(os.path.join(CONFIG_BASE_PATH, d))
    ])


def list_envs(lob: str) -> List[str]:
    """Return environments for a LOB"""
    lob_path = f"{CONFIG_BASE_PATH}/{lob}"

    if not os.path.exists(lob_path):
        return []

    envs = []
    for f in os.listdir(lob_path):
        if f.endswith(".json"):
            envs.append(f.replace(".json", "").upper())

    return sorted(envs)


def list_packages(lob: str, env: str) -> List[str]:
    """Return rule packages"""
    data = _load_json(lob, env)

    key = f"{lob}_{env}"
    return data.get("RULE_PACKAGE_LISTS", {}).get(key, [])


def list_servers(lob: str, env: str) -> List[str]:
    """Return GRE servers"""
    data = _load_json(lob, env)

    key = f"{lob}_{env}"
    return data.get("GRE_SERVER_LISTS", {}).get(key, [])
