# Privacy Policy

**Plugin:** Session Metadata Extractor  
**Author:** sangfor  
**Last updated:** 2026-04-07

## Data Collected

This plugin collects the following data during execution:

| Data | Source | Purpose |
|---|---|---|
| Host machine unique identifier (`machineId`) | OS-level device ID (Linux: `/etc/machine-id`, Windows: registry `MachineGuid`, macOS: `IOPlatformUUID`) | Identifies the physical or virtual host running the Dify instance |
| Dify application ID (`appId`) | Dify session runtime | Identifies which Dify application triggered the tool |
| Plugin session ID (`sessionId`) | Dify session runtime | Identifies the current plugin execution session |
| Dify user ID (`userId`) | Dify runtime | Identifies the end user associated with the current request |

## How Data Is Used

All collected data is used solely to construct a structured XML context block that is returned as the tool's output. This output may be used by the workflow or agent that invokes the tool — for example, to inject session metadata into LLM system prompts, to write audit logs, or to pass identifiers to downstream nodes.

## Data Storage and Transmission

- This plugin does **not** store any collected data persistently.
- This plugin does **not** transmit any data to external servers or third-party services.
- All data remains within your Dify instance and is subject to your own infrastructure's security controls.

## Third-Party Services

This plugin does not integrate with or send data to any third-party service.

## User Control

The `machineId` is derived from the OS at plugin load time and cannot be changed by end users. The remaining fields (`appId`, `sessionId`, `userId`) are provided by the Dify runtime and reflect the active session context. Users who do not wish to expose these identifiers should not use the output of this tool in externally visible prompts or logs.

## Contact

For questions or concerns about this privacy policy, please open an issue at the plugin repository.
