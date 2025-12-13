#!/usr/bin/env python3
"""
Web Crawler v2 - Playwright + EasyOCR (100% Free & Open Source)

Features:
- Playwright: JavaScript SPA 완벽 지원 (GPTers 등)
- EasyOCR: 무료 OCR (한국어/영어 지원)
- API 비용 0원
- 기본 저장: imi-workspace/Inbox/

Usage:
  python web-crawler-v2.py <URL> [output_file.md]

Examples:
  python web-crawler-v2.py https://www.gpters.org/member/6dtzZyRgED
  python web-crawler-v2.py https://example.com result.md
"""

import sys
import os
import asyncio
import tempfile
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin

# 기본 저장 경로 (PKM Inbox)
# scripts -> web-crawler-ocr -> skills -> .claude -> workspace root -> imi-workspace/00-inbox
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = SCRIPT_DIR.parent.parent.parent.parent  # .claude/skills/web-crawler-ocr/scripts -> root
DEFAULT_OUTPUT_DIR = WORKSPACE_ROOT / "imi-workspace" / "00-inbox"

# Lazy imports for better error messages
def check_dependencies():
    """Check and report missing dependencies"""
    missing = []

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        missing.append("playwright (pip install playwright && playwright install chromium)")

    try:
        import easyocr
    except ImportError:
        missing.append("easyocr (pip install easyocr)")

    if missing:
        print("\n[!] Missing dependencies:")
        for dep in missing:
            print(f"    - {dep}")
        print("\nInstall with:")
        print("  pip install playwright easyocr")
        print("  playwright install chromium")
        sys.exit(1)

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_status(msg, color=Colors.BLUE):
    print(f"{color}{msg}{Colors.END}")

def print_success(msg):
    print_status(f"[OK] {msg}", Colors.GREEN)

def print_warn(msg):
    print_status(f"[!] {msg}", Colors.YELLOW)

def print_error(msg):
    print_status(f"[X] {msg}", Colors.RED)

class WebCrawlerV2:
    def __init__(self):
        self.ocr_reader = None
        self.temp_dir = Path(tempfile.mkdtemp(prefix="crawler_"))

    def init_ocr(self):
        """Initialize EasyOCR (lazy loading)"""
        if self.ocr_reader is None:
            print_status("[*] Initializing EasyOCR (first run may download models)...")
            import easyocr
            self.ocr_reader = easyocr.Reader(['ko', 'en'], gpu=False)
            print_success("EasyOCR ready")
        return self.ocr_reader

    async def crawl_page(self, url: str) -> dict:
        """Crawl page with Playwright (handles JavaScript/SPA)"""
        from playwright.async_api import async_playwright

        print_status(f"[*] Crawling: {url}")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = await context.new_page()

            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(2)  # Wait for dynamic content

                # Get page info
                title = await page.title()
                content = await page.content()

                # Extract text content
                text_content = await page.evaluate('''() => {
                    const article = document.querySelector('article') ||
                                   document.querySelector('main') ||
                                   document.querySelector('.content') ||
                                   document.body;
                    return article ? article.innerText : document.body.innerText;
                }''')

                # Extract all links
                links = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('a[href]')).map(a => ({
                        href: a.href,
                        text: a.innerText.trim().substring(0, 100)
                    })).filter(l => l.href && l.text);
                }''')

                # Extract post links (for GPTers-like sites)
                post_links = await page.query_selector_all('a[href*="/post/"]')
                posts = []
                for link in post_links:
                    href = await link.get_attribute('href')
                    text = await link.inner_text()
                    if href and text.strip():
                        full_url = urljoin(url, href)
                        posts.append({'url': full_url, 'title': text.strip()[:100]})

                # Extract images
                images = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('img[src]')).map(img => ({
                        src: img.src,
                        alt: img.alt || ''
                    })).filter(img => img.src && !img.src.includes('data:'));
                }''')

                # Take screenshot
                screenshot_path = self.temp_dir / "screenshot.png"
                await page.screenshot(path=str(screenshot_path), full_page=False)

                print_success(f"Page loaded: {title}")
                print_success(f"Found {len(posts)} post links, {len(images)} images")

                return {
                    'url': url,
                    'title': title,
                    'text': text_content,
                    'html': content,
                    'links': links[:50],  # Limit
                    'posts': posts,
                    'images': images[:20],  # Limit
                    'screenshot': screenshot_path
                }

            except Exception as e:
                print_error(f"Crawl failed: {e}")
                return None
            finally:
                await browser.close()

    def download_image(self, url: str, index: int) -> Path:
        """Download image for OCR"""
        import requests

        try:
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'Mozilla/5.0'
            })
            response.raise_for_status()

            # Determine extension
            content_type = response.headers.get('content-type', '')
            ext = '.jpg'
            if 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            elif 'webp' in content_type:
                ext = '.webp'

            filepath = self.temp_dir / f"image_{index}{ext}"
            filepath.write_bytes(response.content)
            return filepath
        except Exception as e:
            print_warn(f"Image download failed: {url[:50]}... ({e})")
            return None

    def ocr_image(self, image_path: Path) -> str:
        """Run OCR on image using EasyOCR"""
        try:
            reader = self.init_ocr()
            results = reader.readtext(str(image_path))

            if results:
                texts = [r[1] for r in results]
                return '\n'.join(texts)
            return ""
        except Exception as e:
            print_warn(f"OCR failed: {e}")
            return ""

    def generate_markdown(self, data: dict, image_ocr_results: list) -> str:
        """Generate final markdown output"""

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        md = f"""# {data['title']}

> **URL**: {data['url']}
> **Crawled**: {timestamp}
> **Tool**: Playwright + EasyOCR (Open Source)

---

## Text Content

{data['text'][:5000]}{'...(truncated)' if len(data['text']) > 5000 else ''}

"""

        # Add post links if found
        if data.get('posts'):
            md += "\n---\n\n## Post Links Found\n\n"
            for i, post in enumerate(data['posts'][:20], 1):
                md += f"{i}. [{post['title'][:60]}...]({post['url']})\n"

        # Add OCR results
        if image_ocr_results:
            md += "\n---\n\n## Image OCR Results (EasyOCR)\n\n"
            for i, ocr in enumerate(image_ocr_results, 1):
                if ocr['text']:
                    md += f"### Image {i}\n\n"
                    md += f"**URL**: {ocr['url']}\n\n"
                    md += f"**Extracted Text**:\n```\n{ocr['text']}\n```\n\n"

        return md

    async def process(self, url: str, output_file: str = None) -> Path:
        """Main processing pipeline"""

        print_status("\n" + "="*60)
        print_status(f"{Colors.BOLD}Web Crawler v2 - Playwright + EasyOCR{Colors.END}")
        print_status("="*60 + "\n")

        # 1. Crawl page
        data = await self.crawl_page(url)
        if not data:
            print_error("Crawling failed")
            return None

        # 2. OCR images
        image_ocr_results = []
        images_to_process = data['images'][:10]  # Limit to 10

        if images_to_process:
            print_status(f"\n[*] Processing {len(images_to_process)} images with OCR...")

            for i, img in enumerate(images_to_process, 1):
                print(f"    [{i}/{len(images_to_process)}] {img['src'][:60]}...")

                # Download
                img_path = self.download_image(img['src'], i)
                if not img_path:
                    continue

                # OCR
                ocr_text = self.ocr_image(img_path)
                if ocr_text:
                    image_ocr_results.append({
                        'url': img['src'],
                        'alt': img['alt'],
                        'text': ocr_text
                    })
                    print_success(f"    OCR extracted {len(ocr_text)} chars")

        # 3. Generate markdown
        markdown = self.generate_markdown(data, image_ocr_results)

        # 4. Save output
        if not output_file:
            domain = urlparse(url).netloc.replace('www.', '')
            safe_domain = re.sub(r'[^\w\-]', '_', domain)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{safe_domain}_{timestamp}.md"

            # 기본 저장 경로 사용 (Inbox)
            DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output_path = DEFAULT_OUTPUT_DIR / filename
        else:
            output_path = Path(output_file)

        output_path.write_text(markdown, encoding='utf-8')

        print_status("\n" + "="*60)
        print_success(f"Output saved: {output_path.absolute()}")
        print_status("="*60 + "\n")

        # Summary
        print(f"Summary:")
        print(f"  - Text: {len(data['text'])} characters")
        print(f"  - Post links: {len(data.get('posts', []))}")
        print(f"  - Images processed: {len(image_ocr_results)}")
        print(f"  - Output: {output_path}")

        return output_path

def main():
    check_dependencies()

    if len(sys.argv) < 2:
        print("Usage: python web-crawler-v2.py <URL> [output_file.md]")
        print("\nExamples:")
        print("  python web-crawler-v2.py https://www.gpters.org/member/6dtzZyRgED")
        print("  python web-crawler-v2.py https://example.com result.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    crawler = WebCrawlerV2()
    result = asyncio.run(crawler.process(url, output_file))

    if result:
        print(f"\nDone! Read with: cat {result}")

if __name__ == "__main__":
    main()
