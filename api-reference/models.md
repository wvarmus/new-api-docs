---
title: 模型列表接口 (Models)
---

此接口用于动态获取您当前账户有权限调用的所有模型名称及其基本信息。建议开发者在应用初始化时调用此接口，以动态渲染软件中的模型选择下拉菜单。

> **接口端点：** `GET /v1/models`
> **身份认证：** `Authorization: Bearer 您的API_KEY`

## 接口说明

本接口具备**智能格式识别**特性，会根据您的请求头自动返回不同格式的列表：

* **OpenAI 格式 (默认)**：直接请求，返回兼容 OpenAI 标准的模型列表。

* **Anthropic 格式**：如果在请求头中携带了 `anthropic-version` 字段，系统将自动返回 Claude 格式的模型列表。

* **Gemini 格式**：如果请求头中包含 `x-goog-api-key`，系统将返回兼容 Google Gemini 格式的列表。

> $$
> $$
