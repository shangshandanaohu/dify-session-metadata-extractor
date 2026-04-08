# 会话元数据提取器

**作者：** sangfor  
**版本：** 0.0.1  
**类型：** 工具

## 简介

会话元数据提取器是一个轻量级工具插件，用于读取 Dify 运行时的会话元数据并以结构化 XML 格式输出。无需任何配置或凭证，安装后即可在任意 Dify 工作流或智能体中直接使用。

## 输出格式

工具返回包含以下字段的 XML 块：

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

| 字段 | 说明 |
|---|---|
| `version` | 插件上下文格式版本 |
| `machineId` | 运行 Dify 实例的宿主机唯一标识符 |
| `appId` | Dify 应用 ID |
| `sessionId` | 当前插件会话 ID |
| `userId` | 来自 Dify 运行时的终端用户 ID |

## 使用方法

1. 将插件添加到 Dify 工作流或智能体中。
2. 添加 **会话元数据提取器** 工具节点，无需填写任何参数。
3. 工具输出包含当前会话元数据的 XML 字符串。
4. 将输出连接到系统提示变量或任意下游节点。

## 隐私

本插件在运行时会收集以下数据：

- 宿主机唯一标识符（从操作系统设备 ID 读取）
- Dify 应用 ID、会话 ID 及用户 ID

所有数据均在您的 Dify 实例本地处理，不会传输至任何外部服务。详见 [PRIVACY_zh.md](PRIVACY_zh.md)。

## 开发者

**作者：** [shangshandanaohu](https://github.com/shangshandanaohu)  
**邮箱：** 1916512177@qq.com  
**源代码：** [dify-session-metadata-extractor](https://github.com/shangshandanaohu/dify-session-metadata-extractor)