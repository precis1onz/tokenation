import unittest
from datetime import date, timedelta

from scripts.validate_readme import validate_markdown


def make_report(today: date, expiry_days: int = 30) -> str:
    expires = (today + timedelta(days=expiry_days)).isoformat()
    sections = []
    for index in range(1, 11):
        sections.append(
            f"{index}. **Provider {index}**\n"
            "🏷️ **活动/类型**：常态免费Tier\n"
            f"⏰ **免费有效日期**：{expires}（剩余超7天）\n"
            "⚡ **频控限制**：官方未公布\n"
            "🤖 **推荐免费模型**（1~3个）：\n"
            "  • 模型1：model-id（通用）\n"
            "🔗 **获取/注册链接**：[官方链接](https://example.com)"
        )
    return (
        f"（更新至 {today.isoformat()}）\n"
        f"🎁 **最新有效免费 LLM API & 羊毛活动 TOP 10**（{today:%Y.%m.%d}）\n"
        "---\n" + "\n---\n".join(sections) + "\n"
    )


class ValidateReadmeTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 10, 18)
        self.markdown = make_report(self.today)

    def test_accepts_ten_well_formed_entries(self):
        self.assertEqual(validate_markdown(self.markdown, self.today), [])

    def test_rejects_wrong_count(self):
        shortened = self.markdown.replace("\n---\n10. **Provider 10**", "", 1)
        self.assertTrue(any("恰好10项" in error for error in validate_markdown(shortened, self.today)))

    def test_rejects_expiry_with_seven_or_fewer_days_remaining(self):
        report = make_report(self.today, expiry_days=7)
        self.assertTrue(any("超过7天" in error for error in validate_markdown(report, self.today)))

    def test_rejects_missing_required_field(self):
        report = self.markdown.replace("⚡ **频控限制**：官方未公布\n", "", 1)
        self.assertTrue(any("频控限制" in error for error in validate_markdown(report, self.today)))

    def test_rejects_unrequested_preface(self):
        report = "每日整理如下：\n" + self.markdown
        self.assertTrue(any("首行必须" in error for error in validate_markdown(report, self.today)))

    def test_accepts_blank_lines_after_provider_separators(self):
        report = self.markdown.replace("\n---\n", "\n---\n\n")
        self.assertEqual(validate_markdown(report, self.today), [])

    def test_accepts_account_dependent_expiry_without_treating_it_as_a_date(self):
        report = self.markdown.replace(
            "长期有效", "新账号赠送额度自发放起30天（剩余时间因账号或活动而异）", 1
        )
        self.assertEqual(validate_markdown(report, self.today), [])


if __name__ == "__main__":
    unittest.main()
