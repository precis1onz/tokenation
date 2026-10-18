import re
from datetime import date, timedelta


UPDATE_RE = re.compile(r"^（更新至 (\d{4}-\d{2}-\d{2})）$")
TITLE_RE = re.compile(r"^🎁 \*\*最新有效免费 LLM API & 羊毛活动 TOP 10\*\*（(\d{4})\.(\d{2})\.(\d{2})）$")
PROVIDER_RE = re.compile(r"^(\d+)\. \*\*(.+)\*\*$")
DATE_RE = re.compile(r"^(?:\d{4}-\d{2}-\d{2}(?:（剩余超7天）)?|长期有效(?:（[^）]+）)?|开通后\d+天（剩余时间[^）]+）|新账号赠送额度自发放起\d+天（剩余时间[^）]+）)$")
URL_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")


def validate_markdown(markdown: str, today: date | None = None) -> list[str]:
    """Validate the fixed Tokenation daily Markdown contract."""
    errors: list[str] = []
    # Blank lines are visual spacing only and do not belong to entry content.
    lines = [line for line in markdown.splitlines() if line.strip()]
    if len(lines) < 4:
        return ["内容过短，无法构成10项清单"]

    update_match = UPDATE_RE.fullmatch(lines[0])
    if not update_match:
        errors.append("首行必须为（更新至 YYYY-MM-DD）")
        updated = today
    else:
        try:
            updated = date.fromisoformat(update_match.group(1))
        except ValueError:
            errors.append("更新日期无效")
            updated = today
        if today and updated != today:
            errors.append("更新日期与本次执行日期不一致")

    title_match = TITLE_RE.fullmatch(lines[1])
    if not title_match:
        errors.append("第二行主标题或日期格式错误")
    elif update_match and title_match.groups() != tuple(update_match.group(1).split("-")):
        errors.append("主标题日期与更新日期不一致")

    if len(lines) < 3 or lines[2] != "---":
        errors.append("主标题后必须紧接分隔线 ---")

    sections: list[list[str]] = []
    current: list[str] = []
    for line in lines[3:]:
        if line == "---":
            if current:
                sections.append(current)
                current = []
            else:
                errors.append("Provider 分隔线之间不得有空条目")
        else:
            current.append(line)
    if current:
        sections.append(current)

    if len(sections) != 10:
        errors.append(f"必须恰好10项，当前为{len(sections)}项")

    expected_prefixes = [
        "🏷️ **活动/类型**：",
        "⏰ **免费有效日期**：",
        "⚡ **频控限制**：",
        "🤖 **推荐免费模型**（1~3个）：",
    ]
    for index, section in enumerate(sections, start=1):
        if not section:
            continue
        provider = PROVIDER_RE.fullmatch(section[0])
        if not provider or int(provider.group(1)) != index or not provider.group(2).strip():
            errors.append(f"第{index}项首行须为“{index}. **Provider 名称**”")

        positions: dict[str, int] = {}
        for prefix in expected_prefixes:
            hits = [i for i, line in enumerate(section) if line.startswith(prefix)]
            if len(hits) != 1:
                errors.append(f"第{index}项字段缺失或重复：{prefix}")
            else:
                positions[prefix] = hits[0]
        if len(positions) == len(expected_prefixes) and list(positions.values()) != sorted(positions.values()):
            errors.append(f"第{index}项字段顺序错误")

        date_prefix = expected_prefixes[1]
        if date_prefix in positions:
            value = section[positions[date_prefix]][len(date_prefix):].strip()
            if not DATE_RE.fullmatch(value):
                errors.append(f"第{index}项有效日期格式错误")
            elif re.match(r"^\d{4}-\d{2}-\d{2}", value) and updated:
                date_text = value[:10]
                try:
                    expiry = date.fromisoformat(date_text)
                    if expiry <= updated + timedelta(days=7):
                        errors.append(f"第{index}项限时有效期必须超过7天")
                except ValueError:
                    errors.append(f"第{index}项截止日期无效")

        model_prefix = expected_prefixes[3]
        if model_prefix in positions:
            model_lines = [line for line in section[positions[model_prefix] + 1:] if line.startswith("  • 模型")]
            if not 1 <= len(model_lines) <= 3:
                errors.append(f"第{index}项须列出1至3个推荐模型")

        link_prefix = "🔗 **获取/注册链接**："
        if not section[-1].startswith(link_prefix) or not URL_RE.search(section[-1]):
            errors.append(f"第{index}项最后一行必须包含有效注册链接")

    return errors
