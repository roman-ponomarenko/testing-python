from playwright.sync_api import Locator, expect

from src.ui.models.badge import Badge


class ProjectCard:
    def __init__(self, root: Locator):
        self._root = root

    def __repr__(self) -> str:
        return self.title.inner_text()

    @property
    def title(self) -> Locator:
        return self._root.locator("h3")

    @property
    def test_count(self) -> Locator:
        return self._root.locator("p")

    @property
    def member_avatars(self) -> Locator:
        return self._root.locator("img")

    @property
    def extra_members_count(self) -> Locator:
        return self._root.locator("div.rounded-full")

    @property
    def badge(self) -> Locator:
        return self._root.locator(".common-badge")

    @property
    def link(self) -> Locator:
        return self._root.locator("a")

    def get_title_text(self) -> str:
        return self.title.inner_text()

    def get_badge_text(self) -> str:
        return self.badge.inner_text()

    def get_href(self) -> str | None:
        return self.link.get_attribute("href")

    def click(self) -> None:
        self.link.click()

    def verify_badge(self, badge: Badge):
        assert self.badge.inner_text() == badge.label

    def verify_test_count(self, expected_count: int) -> None:
        expect(self.test_count).to_have_text(f"{expected_count} tests")
