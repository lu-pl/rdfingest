from pathlib import Path


pass_config_yamls = Path().rglob("config_pass_*.yaml")
fail_config_yamls = Path().rglob("config_fail_*.yaml")

pass_registry_yamls = Path().rglob("registry_pass_*.yaml")
fail_registry_yamls = Path().rglob("registry_fail_*.yaml")
