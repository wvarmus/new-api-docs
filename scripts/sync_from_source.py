from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "文档"

CHINESE_NUMERALS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
}


def strip_chapter_prefix(name: str) -> str:
    return re.sub(r"^[一二三四五六七八九十]+、\s*", "", name.strip())


def strip_file_prefix(name: str) -> str:
    return re.sub(r"^\d+\.\s*", "", name.strip())


def chapter_key(name: str):
    match = re.match(r"^([一二三四五六七八九十]+)、", name.strip())
    if match:
        return (0, CHINESE_NUMERALS.get(match.group(1), 999), name)
    return (1, 999, name)


def file_key(name: str):
    stripped = name.strip()
    match = re.match(r"^(\d+)", stripped)
    if match:
        return (0, int(match.group(1)), stripped)
    return (1, stripped)


CHAPTER_SLUGS = {
    "平台接入概览": "getting-started",
    "电商平台兑换指南": "ecommerce-redemption",
    "技术对接规范": "integration-guides",
    "接口参考手册": "api-reference",
    "软件与客户端集成": "client-integrations",
    "企业与开发者生态": "enterprise-developers",
    "技术支持与排错": "troubleshooting",
    "联系方式与反馈": "contact-feedback",
}

PAGE_SLUGS = {
    "关于我们与服务优势": "about-service-advantages",
    "平台通用使用流程": "platform-workflow",
    "计费逻辑深度解析": "billing-logic",
    "充值与财务管理": "recharge-finance",
    "快速上手指南": "quickstart",
    "适用平台与防骗提醒": "supported-platforms-anti-fraud",
    "保姆级兑换步骤": "redemption-steps",
    "电商用户常见问题": "ecommerce-faq",
    "网关配置": "gateway-config",
    "身份认证与权限管理": "authentication-permissions",
    "高级功能与特性支持": "advanced-features",
    "模型列表": "models",
    "聊天补全": "chat-completions",
    "Responses API": "responses-api",
    "Claude专属格式接口": "claude-format-api",
    "Gemini专属接口": "gemini-api",
    "文本嵌入": "embeddings",
    "文档重排序": "document-rerank",
    "内容安全审查": "moderation",
    "图像生成": "image-generation",
    "文本转语音": "text-to-speech",
    "音频转录": "audio-transcription",
    "视频生成": "video-generation",
    "实时语音": "realtime-audio",
    "错误码说明": "error-codes",
    "企业与开发者生态": "enterprise-developers",
    "常见 HTTP 状态码与故障排查": "http-status-troubleshooting",
    "速率限制与并发说明": "rate-limits-concurrency",
    "联系方式与反馈": "contact-feedback",
    "Chatbox": "chatbox",
    "Cherry Studio": "cherry-studio",
    "Claude Code": "claude-code",
    "Crush": "crush",
    "Cursor": "cursor",
    "LobeChat": "lobechat",
    "NextChat": "nextchat",
    "OpenClaw": "openclaw",
    "OpenCode": "opencode",
    "SillyTavern (酒馆)": "sillytavern",
    "VS Code": "vs-code",
}

DOC_CHAPTER_DIRS = set(CHAPTER_SLUGS.values())


def chapter_slug(chapter_name: str) -> str:
    return CHAPTER_SLUGS.get(chapter_name, chapter_name)


def page_slug(page_name: str) -> str:
    return PAGE_SLUGS.get(page_name, page_name)


RESERVED_API_FILES = {
    "api-reference": {
        "realtime-audio.mdx": "---\ntitle: 实时语音\ndescription: WebSocket 实时语音接口说明。\n---\n\n# 实时语音\n\n建立 WebSocket 连接用于实时对话交互。\n\n## 接口信息\n\n- **协议**：`WSS`\n- **端点**：`/v1/realtime?model=gpt-4o-realtime`\n- **认证**：`Authorization: Bearer {api_key}`\n\n## JavaScript 示例\n\n```javascript\nconst ws = new WebSocket('ws://infistar.ai/v1/realtime?model=gpt-4o-realtime', {\n  headers: { Authorization: 'Bearer sk-xxx' }\n});\n\nws.onopen = () => {\n  console.log('Connected');\n  ws.send(JSON.stringify({\n    type: 'conversation.item.create',\n    content: { type: 'input_text', text: '你好' }\n  }));\n};\n\nws.onmessage = (event) => {\n  const data = JSON.parse(event.data);\n  console.log(data);\n};\n```\n",
        "error-codes.mdx": "---\ntitle: 错误码说明\ndescription: 常见错误码与统一错误响应格式说明。\n---\n\n# 错误码说明\n\n| 错误码 | 说明 |\n| --- | --- |\n| 400 | 请求参数错误 |\n| 401 | 未授权 / API Key 无效 |\n| 403 | 权限不足 |\n| 404 | 资源不存在 |\n| 429 | 请求过于频繁（速率限制） |\n| 500 | 服务器内部错误 |\n| 501 | 接口未实现 |\n\n## 错误响应格式\n\n```json\n{\n  \"error\": {\n    \"message\": \"错误信息\",\n    \"type\": \"invalid_request_error\",\n    \"code\": \"invalid_api_key\"\n  }\n}\n```\n\n## 速率限制\n\n根据您的套餐等级，默认限制可能有所不同。具体限制可在个人中心查看。\n"
    }
}


def chapter_dirs(root: Path):
    return sorted(
        [p for p in root.iterdir() if p.is_dir() and p.name != "scripts"],
        key=lambda p: chapter_key(p.name),
    )


def transform_markdown(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "<br />", text, flags=re.IGNORECASE)

    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body = "\n".join(lines[2:]).lstrip("\n")
        frontmatter = f"---\ntitle: {title}\n---\n\n"
        return frontmatter + body

    return text


def sync_docs():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source docs directory not found: {SOURCE}")

    source_chapters = chapter_dirs(SOURCE)

    for dirname in DOC_CHAPTER_DIRS:
        existing = ROOT / dirname
        if existing.exists():
            shutil.rmtree(existing, ignore_errors=True)

    for chapter in source_chapters:
        chapter_name = strip_chapter_prefix(chapter.name)
        target_chapter = ROOT / chapter_slug(chapter_name)
        target_chapter.mkdir(parents=True, exist_ok=True)
        reserved_in_chapter = RESERVED_API_FILES.get(target_chapter.name, {})
        for existing_file in target_chapter.iterdir():
            if existing_file.is_file() and existing_file.name in reserved_in_chapter:
                continue
            if existing_file.is_file():
                existing_file.unlink()
        for source_md in sorted(chapter.glob("*.md"), key=lambda p: file_key(p.stem)):
            page_name = strip_file_prefix(source_md.stem)
            target_md = target_chapter / f"{page_slug(page_name)}.md"
            target_md.write_text(transform_markdown(source_md.read_text(encoding="utf-8")), encoding="utf-8")
        for filename, content in reserved_in_chapter.items():
            (target_chapter / filename).write_text(content, encoding="utf-8")

    default_page = ROOT / "getting-started" / "about-service-advantages.md"
    index_path = ROOT / "index.mdx"
    if default_page.exists():
        index_path.write_text(default_page.read_text(encoding="utf-8"), encoding="utf-8")


PAGE_ORDER = {
    "平台接入概览": [
        "关于我们与服务优势",
        "平台通用使用流程",
        "计费逻辑深度解析",
        "充值与财务管理",
        "快速上手指南",
    ],
    "电商平台兑换指南": [
        "适用平台与防骗提醒",
        "保姆级兑换步骤",
        "电商用户常见问题",
    ],
    "技术对接规范": [
        "网关配置",
        "身份认证与权限管理",
        "高级功能与特性支持",
    ],
    "软件与客户端集成": [
        "Chatbox",
        "Cherry Studio",
        "Claude Code",
        "Crush",
        "Cursor",
        "LobeChat",
        "NextChat",
        "OpenClaw",
        "OpenCode",
        "SillyTavern (酒馆)",
        "VS Code",
    ],
    "接口参考手册": [
        "模型列表",
        "聊天补全",
        "Responses API",
        "Claude专属格式接口",
        "Gemini专属接口",
        "文本补全",
        "文本嵌入",
        "Gemini 嵌入",
        "文档重排序",
        "内容安全审查",
        "图像生成",
        "图像编辑",
        "Gemini 图像",
        "通义千问图像",
        "文本转语音",
        "音频转录",
        "音频翻译",
        "视频生成",
        "视频生成任务",
        "可灵视频",
        "即梦视频",
        "实时语音",
    ],
    "企业与开发者生态": [
        "企业与开发者生态",
    ],
    "技术支持与排错": [
        "常见 HTTP 状态码与故障排查",
        "速率限制与并发说明",
    ],
    "联系方式与反馈": [
        "联系方式与反馈",
    ],
}


def chapter_pages(chapter_name: str):
    chapter = ROOT / chapter_slug(chapter_name)
    ordered_names = PAGE_ORDER.get(chapter_name, [])
    pages = []

    for name in ordered_names:
        slug = page_slug(name)
        if (chapter / f"{slug}.md").exists() or (chapter / f"{slug}.mdx").exists():
            pages.append(f"{chapter.name}/{slug}")

    known_slugs = {page_slug(name) for name in ordered_names}
    remaining = [
        file.stem
        for file in sorted(chapter.glob("*.md"), key=lambda p: file_key(p.stem))
        if file.stem not in known_slugs
    ]
    for slug in remaining:
        pages.append(f"{chapter.name}/{slug}")

    return pages


def build_docs_json():
    docs = {
        "$schema": "https://mintlify.com/docs.json",
        "theme": "mint",
        "name": "无限星河 AI 文档",
        "logo": "/images/site-logo.svg",
        "favicon": "/images/logo.png",
        "colors": {"primary": "#0ea5e9"},
        "styling": {"css": "style.css"},
        "navbar": {
            "links": [
                {"label": "控制台", "href": "https://infistar.ai/console"},
                {"label": "模型广场", "href": "https://infistar.ai/pricing"}
            ]
        },
        "navigation": {
            "tabs": [
                {
                    "tab": "使用指南",
                    "groups": [
                        {"group": "平台介绍", "pages": chapter_pages("平台接入概览")},
                        {"group": "电商平台兑换指南", "pages": chapter_pages("电商平台兑换指南")},
                    ],
                },
                {
                    "tab": "API 文档",
                    "groups": [
                        {
                            "group": "概览",
                            "pages": [
                                "api-overview",
                                "api-reference/realtime-audio",
                                "api-reference/error-codes"
                            ]
                        },
                        {
                            "group": "技术对接规范",
                            "pages": chapter_pages("技术对接规范")
                        },
                        {
                            "group": "接口参考手册",
                            "openapi": "openapi.json"
                        }
                    ],
                },
                {
                    "tab": "软件与客户端支持",
                    "groups": [
                        {"group": "软件与客户端集成", "pages": chapter_pages("软件与客户端集成")},
                    ],
                },
                {
                    "tab": "常见问题",
                    "groups": [
                        {"group": "故障与限制", "pages": chapter_pages("技术支持与排错")},
                    ],
                },
                {
                    "tab": "联系我们",
                    "groups": [
                        {"group": "企业与开发者生态", "pages": chapter_pages("企业与开发者生态")},
                        {"group": "联系方式与反馈", "pages": chapter_pages("联系方式与反馈")},
                    ],
                },
            ]
        },
    }

    (ROOT / "docs.json").write_text(
        json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    sync_docs()
    build_docs_json()
    print("synced mintlify mirror")


if __name__ == "__main__":
    main()

