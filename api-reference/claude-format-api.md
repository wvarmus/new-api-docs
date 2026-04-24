---
title: Claude 专属格式接口 (Messages API)
---

如果您现有的业务系统或软件是严格基于 Anthropic 原生规范（Messages API）开发的，可以直接使用此专属通道接入 Claude 家族模型，无需修改底层业务逻辑代码。

> **接口端点：** `POST /v1/messages`
> **关键请求头：** 必须在 Headers 中携带 `anthropic-version: 2023-06-01`
> **身份认证：** `Authorization: Bearer 您的API_KEY`

## 核心参数说明表

在发送请求时，请在请求体中提供以下参数：

| 参数名称 | 是否必填 | 参数说明 |
| :--- | :--- | :--- |
| **model** | **必填** | 必须指定 Claude 系列的模型 ID，如 `claude-3-opus-20240229`。 |
| **messages** | **必填** | 用户的提问与历史对话列表。 |
| **max_tokens** | **必填** | 注意：Claude 原生接口强制要求必须指定最大生成长度参数，且数值必须大于或等于 1。 |
| **system** | 选填 | 全局的系统提示词设定。 |
| **thinking** | 选填 | 思考过程配置（仅针对 Claude 3.5 及以上版本支持内置思考设定的模型有效）。 |