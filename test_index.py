import re
from playwright.sync_api import Page, expect
import pytest

from pathlib import Path

file_url = Path("index.html").resolve().as_uri()

@pytest.fixture
def index(page: Page):
    page.goto(f"{file_url}")

    return page

def test_add(index):
    index.get_by_text("1").click()
    index.get_by_text("2").click()
    index.get_by_text("3").click()
    index.get_by_text("4").click()
    index.get_by_text("5").click()
    index.get_by_text("+").click()
    index.get_by_text("6").click()
    index.get_by_text("7").click()
    index.get_by_text("8").click()
    index.get_by_text("9").click()
    index.get_by_text("0").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("80235")).to_be_visible()

def test_sub(index):
    index.get_by_text("9").click()
    index.get_by_text("0").click()
    index.get_by_text("-").click()
    index.get_by_text("5").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("85")).to_be_visible()

def test_mul(index):
    index.get_by_text("8").click()
    index.get_by_text("x").click()
    index.get_by_text("7").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("56")).to_be_visible()

def test_div(index):
    index.get_by_text("1").click()
    index.get_by_text("2").click()
    index.get_by_text("8").click()
    index.get_by_text("/").click()
    index.get_by_text("4").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("32")).to_be_visible()

def test_div_frac(index):
    index.get_by_text("8").click()
    index.get_by_text("/").click()
    index.get_by_text("5").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("1.6")).to_be_visible()

def test_decimal(index):
    index.get_by_text("1").click()
    index.get_by_text(".").click()
    index.get_by_text("2").click()
    index.get_by_text("+").click()
    index.get_by_text("5").click()
    index.get_by_text(".").click()
    index.get_by_text("3").click()
    index.get_by_text("=").click()
    expect(index.get_by_text("6.5")).to_be_visible()
