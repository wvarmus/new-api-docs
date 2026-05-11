---
title: 速率限制与并发说明
---

为了保障整体调用体验与系统稳定性，无限星河AI 会根据上游接口的实时状态进行动态的速率限制（Rate Limits）。

作为一家聚合型 AI 算力网关，**我们的底层并发能力主要取决于各原厂上游供应商（如 OpenAI、Anthropic 等）的实时通道状态**。平台通过多节点冗余与智能路由机制，尽量提升高频调用场景下的稳定性与响应效率。

---

## 一、 核心限制指标解析

当您的请求频率过高时，通常是触发了以下两个核心指标中的某一个：

1.  **RPM (Requests Per Minute)**：每分钟最大请求次数。
2.  **TPM (Tokens Per Minute)**：每分钟最大消耗的 Token 数量（包含输入文本与生成的输出文本）。

---

## 二、 动态限流与排队机制

由于全球 AI 模型的算力需求存在高峰与低谷，我们的速率限制机制具有以下特点：

* **动态吞吐**：在原厂供应商算力充沛时，系统会自动放宽并发限制；但在全球调用晚高峰或原厂服务降级（如大模型官网宕机）时，我们将根据上游通道的实际吞吐量，实施严格的排队与限流。
* **推理模型限制更严**：请注意，当您调用推理能力较强的模型时，由于其本身消耗算力更高，上游供应商对它们的并发限制通常比基础模型更严格。

---

## 三、 遇到 429 报错该如何处理？

当您的请求频率超过当前系统的承载上限时，接口会返回 HTTP 状态码 `429 Too Many Requests`。

### 1. 错误响应示例
```json
{
  "error": {
    "message": "Rate limit reached for model claude-3-7-sonnet. Please try again in 10s.",
    "type": "requests",
    "param": null,
    "code": "rate_limit_exceeded"
  }
}
```

### 2. 开发者最佳实践：指数退避 (Exponential Backoff)
如果您是在编写自动化脚本（如批量翻译文档、高频调用 Agent 爬虫），强烈建议您在代码中加入**“指数退避算法”**。当遇到 429 报错时，不要立即死循环重试，而是应该逐次延长等待时间。

**Python 伪代码示例：**
```python
import time
import requests

def call_api_with_retry(max_retries=5):
    for attempt in range(max_retries):
        response = requests.post("https://infistar.ai/v1/chat/completions", headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()
            
        elif response.status_code == 429:
            sleep_time = (2 ** attempt)  # 依次等待 1s, 2s, 4s, 8s...
            print(f"触发限流，系统繁忙，将在 {sleep_time} 秒后自动重试...")
            time.sleep(sleep_time)
        else:
            raise Exception(f"API Error: {response.status_code}")
            
    raise Exception("已达到最大重试次数，请稍后再试")
```

---

## 四、 如何保障高频业务的最佳体验？

如果您的业务需要更稳定的高频调用，我们提供以下建议：

1. **错峰调用**：如果是跑非实时性的批处理脚本，建议将任务安排在**北京时间上午 8:00 - 12:00**（北美深夜时间），此时全球上游供应商算力最为充沛。
2. **任务分流**：对于非复杂的文字提取、格式转换等任务，可优先选择轻量或高速模型。
3. **申请企业独立通道**：如果您的商业项目即将上线，需要更稳定的高频调用能力，请通过 **[联系我们]** 页面与我们的商务专员沟通。企业客户可根据实际调用量申请独立通道或专属资源方案；并发、隔离方式和服务等级以双方确认结果为准。