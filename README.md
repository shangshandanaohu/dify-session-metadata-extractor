# Session Metadata Extractor

**Author:** sangfor  
**Version:** 0.0.1  
**Type:** tool

## Overview

Session Metadata Extractor is a lightweight utility plugin that reads Dify runtime session metadata and outputs it as structured XML. It requires no configuration or credentials — install and use immediately in any Dify workflow or agent.

## Output Format

The tool returns an XML block containing the following fields:

```xml
## agent context (untrusted metadata)
<agentContext>
  <version>dify-0.0.1</version>
  <machineId>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</machineId>
  <appId>app-xxxxxxxxxxxxxxxxxxxxxxxx</appId>
  <sessionId>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</sessionId>
  <userId>user-xxxxxxxxxxxxxxxxxxxxxxxx</userId>
</agentContext>
```

| Field | Description |
|---|---|
| `version` | Plugin context format version |
| `machineId` | Unique identifier of the host machine running the Dify instance |
| `appId` | The Dify application ID |
| `sessionId` | The current plugin session ID |
| `userId` | The end-user ID from the Dify runtime |

## Usage

1. Add the plugin to your Dify workflow or agent.
2. Add the **Session Metadata Extractor** tool node — no parameters required.
3. The tool outputs an XML string containing the current session metadata.
4. Connect the output to a system prompt variable or any downstream node.

## Privacy

This plugin collects the following data at runtime:

- Host machine unique identifier (read from OS-level device ID)
- Dify application ID, session ID, and user ID

All data is processed locally within your Dify instance. No data is transmitted to external services. See [PRIVACY.md](PRIVACY.md) for details.

## Developer

**Author:** [shangshandanaohu](https://github.com/shangshandanaohu)  
**Email:** 1916512177@qq.com  
**Source:** [dify-session-metadata-extractor](https://github.com/shangshandanaohu/dify-session-metadata-extractor)
