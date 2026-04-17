# Responses API 接口

高级对话接口。基于最新的 Responses 规范，专门为需要多轮复杂交互、工具调用和深层推理记忆的开发场景而设计。

> **接口端点：** `POST /v1/responses`
> **身份认证：** `Authorization: Bearer 您的API_KEY`

## 核心参数说明表

在发送请求时，请在请求体中提供以下参数：

| 参数名称 | 是否必填 | 参数说明 |
| :--- | :--- | :--- |
| **model** | **必填** | 指定的模型标识符（例如 `gpt-4o` 等）。 |
| **input** | 选填 | 用户本次输入的文本或多模态内容。 |
| **instructions** | 选填 | 系统级指令（等同于传统接口的 system prompt），用于设定 AI 的全局角色或行为准则。 |
| **previous_response_id** | 选填 | 上一轮对话的响应 ID。填入此 ID 可让 AI 自动在服务端回忆起上一轮的上下文，显著节省每次都上传全部历史记录的 Token 费用。 |
| **truncation** | 选填 | 截断方式策略，可选 `auto` 或 `disabled`。 |