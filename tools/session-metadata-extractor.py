import platform
import re
import subprocess
import xml.etree.ElementTree as ET
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


CONTEXT_VERSION = "0.0.1"

_machine_id_cache: str | None = None


def _get_machine_id() -> str:
    """跨平台获取机器唯一 ID，对齐 node-machine-id machineIdSync(true) 行为"""
    global _machine_id_cache
    if _machine_id_cache is not None:
        return _machine_id_cache

    system = platform.system()
    result = ""
    try:
        if system == "Linux":
            for path in ("/var/lib/dbus/machine-id", "/etc/machine-id"):
                try:
                    with open(path) as f:
                        result = f.read().strip().lower()
                        break
                except OSError:
                    continue
        elif system == "Windows":
            output = subprocess.check_output(
                ["REG", "QUERY", r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography", "/v", "MachineGuid"],
                stderr=subprocess.DEVNULL,
            ).decode()
            match = re.search(r"MachineGuid\s+REG_SZ\s+(\S+)", output)
            if match:
                result = match.group(1).lower()
        elif system == "Darwin":
            output = subprocess.check_output(
                ["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"],
                stderr=subprocess.DEVNULL,
            ).decode()
            match = re.search(r'IOPlatformUUID"\s*=\s*"([^"]+)"', output)
            if match:
                result = match.group(1).lower()
    except Exception:
        pass

    _machine_id_cache = result
    return result


def _build_context_xml(session, runtime) -> str:
    """将平台元数据构建为 XML 格式字符串，仅包含平台级字段，不含用户输入"""
    root = ET.Element("agentContext")
    ET.SubElement(root, "version").text = f"dify-{CONTEXT_VERSION}"
    ET.SubElement(root, "machineId").text = _get_machine_id()
    ET.SubElement(root, "appId").text = session.app_id or ""
    ET.SubElement(root, "sessionId").text = session.session_id or ""
    ET.SubElement(root, "userId").text = runtime.user_id or ""
    ET.indent(root, space="  ")
    xml_str = ET.tostring(root, encoding="unicode", xml_declaration=False)
    return "## agent context (untrusted metadata)\n" + xml_str


class SessionMetadataExtractorTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        yield self.create_text_message(_build_context_xml(self.session, self.runtime))
