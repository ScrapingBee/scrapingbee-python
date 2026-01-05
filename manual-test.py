import os
from scrapingbee import ScrapingBeeClient

API_KEY = os.environ.get("SCRAPINGBEE_API_KEY")
client = ScrapingBeeClient(API_KEY)


# ============================================
# Helper Functions
# ============================================

def assert_test(condition, message):
    if not condition:
        raise AssertionError(message)


# ============================================
# HTML API Tests (Legacy)
# ============================================

def test_html_get():
    print("=== Testing HTML API - GET ===")
    try:
        response = client.get(
            url="https://httpbin.org/get",
            params={"render_js": False}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.text, "Response is empty")
        assert_test("httpbin" in response.text, "Response does not contain expected content")

        print(f"Status: {response.status_code}")
        print("✅ HTML GET test passed!\n")
    except Exception as e:
        print(f"❌ HTML GET test failed: {e}\n")
        raise


def test_html_post():
    print("=== Testing HTML API - POST ===")
    try:
        response = client.post(
            url="https://httpbin.org/post",
            params={"render_js": False},
            data={"test": "data"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.text, "Response is empty")
        assert_test("test" in response.text, "Response does not contain posted data")

        print(f"Status: {response.status_code}")
        print("✅ HTML POST test passed!\n")
    except Exception as e:
        print(f"❌ HTML POST test failed: {e}\n")
        raise


# ============================================
# HTML API Tests (New)
# ============================================

def test_html_api_get():
    print("=== Testing HTML API (New) - GET ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/get",
            method="GET",
            params={"render_js": False}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.text, "Response is empty")
        assert_test("httpbin" in response.text, "Response does not contain expected content")

        print(f"Status: {response.status_code}")
        print("✅ HTML API GET test passed!\n")
    except Exception as e:
        print(f"❌ HTML API GET test failed: {e}\n")
        raise


def test_html_api_post():
    print("=== Testing HTML API (New) - POST ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/post",
            method="POST",
            params={"render_js": False},
            data={"test": "data"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.text, "Response is empty")
        assert_test("test" in response.text, "Response does not contain posted data")

        print(f"Status: {response.status_code}")
        print("✅ HTML API POST test passed!\n")
    except Exception as e:
        print(f"❌ HTML API POST test failed: {e}\n")
        raise


def test_html_api_extract_rules():
    print("=== Testing HTML API - Extract Rules ===")
    try:
        response = client.html_api(
            url="https://www.scrapingbee.com/blog/",
            params={
                "render_js": False,
                "extract_rules": {
                    "title": "h1",
                    "posts": {
                        "selector": ".container > div > div > div",
                        "type": "list",
                        "output": {
                            "title": "h4",
                            "link": "a@href"
                        }
                    }
                }
            }
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("title"), "Extracted title is missing")
        assert_test(isinstance(data.get("posts"), list), "Extracted posts is not a list")
        assert_test(len(data.get("posts", [])) > 0, "No posts extracted")

        print(f"Status: {response.status_code}")
        print(f"Extracted title: {data.get('title')}")
        print(f"Extracted posts count: {len(data.get('posts', []))}")
        print("✅ HTML API Extract Rules test passed!\n")
    except Exception as e:
        print(f"❌ HTML API Extract Rules test failed: {e}\n")
        raise


def test_html_api_js_scenario():
    print("=== Testing HTML API - JS Scenario ===")
    try:
        response = client.html_api(
            url="https://www.scrapingbee.com",
            params={
                "render_js": True,
                "js_scenario": {
                    "instructions": [
                        {"wait": 1000},
                        {"scroll_y": 500},
                        {"wait": 500}
                    ]
                }
            }
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.text, "Response is empty")

        print(f"Status: {response.status_code}")
        print(f"Content: {response.text[:300]}")  # ← Fixed: Match Node.js output
        print("✅ HTML API JS Scenario test passed!\n")
    except Exception as e:
        print(f"❌ HTML API JS Scenario test failed: {e}\n")
        raise


def test_html_api_screenshot():
    print("=== Testing HTML API - Screenshot ===")
    try:
        response = client.html_api(
            url="https://www.scrapingbee.com",
            params={
                "render_js": True,
                "screenshot": True,
                "window_width": 1920,
                "window_height": 1080
            }
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test(response.content, "Response is empty")
        assert_test(len(response.content) > 10000, "Screenshot seems too small")

        # Check PNG signature
        png_signature = b'\x89PNG\r\n\x1a\n'
        assert_test(response.content[:8] == png_signature, "Response is not a valid PNG")

        print(f"Status: {response.status_code}")
        print(f"Screenshot size: {len(response.content)} bytes")
        print("✅ HTML API Screenshot test passed!\n")
    except Exception as e:
        print(f"❌ HTML API Screenshot test failed: {e}\n")
        raise


def test_html_api_json_response():
    print("=== Testing HTML API - JSON Response ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/get",
            params={
                "render_js": False,
                "json_response": True
            }
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("body") is not None, "JSON response missing body field")
        assert_test(data.get("xhr") is not None, "JSON response missing xhr field")

        # Handle body as string or object
        body = data.get("body")
        body_preview = body[:300] if isinstance(body, str) else str(body)[:300]

        print(f"Status: {response.status_code}")
        print(f"Content: {body_preview}")
        print("✅ HTML API JSON Response test passed!\n")
    except Exception as e:
        print(f"❌ HTML API JSON Response test failed: {e}\n")
        raise


def test_html_api_with_headers():
    print("=== Testing HTML API - Custom Headers ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/headers",
            params={"render_js": False},
            headers={"X-Custom-Header": "CustomValue123"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test("CustomValue123" in response.text, "Custom header not forwarded")

        print(f"Status: {response.status_code}")
        print("✅ HTML API Custom Headers test passed!\n")
    except Exception as e:
        print(f"❌ HTML API Custom Headers test failed: {e}\n")
        raise


def test_html_api_with_cookies():
    print("=== Testing HTML API - Custom Cookies ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/cookies",
            params={"render_js": False},
            cookies={"session_id": "abc123", "user_token": "xyz789"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test("abc123" in response.text or "xyz789" in response.text, "Cookies not forwarded")

        print(f"Status: {response.status_code}")
        print("✅ HTML API Custom Cookies test passed!\n")
    except Exception as e:
        print(f"❌ HTML API Custom Cookies test failed: {e}\n")
        raise


def test_html_api_post_with_headers_and_cookies():
    print("=== Testing HTML API - POST with Headers + Cookies ===")
    try:
        response = client.html_api(
            url="https://httpbin.org/post",
            method="POST",
            params={"render_js": False},
            headers={"X-Test-Header": "TestValue"},
            cookies={"session": "mysession123"},
            data={"action": "submit"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")
        assert_test("submit" in response.text, "Posted data not in response")

        print(f"Status: {response.status_code}")
        print("✅ HTML API POST with Headers + Cookies test passed!\n")
    except Exception as e:
        print(f"❌ HTML API POST with Headers + Cookies test failed: {e}\n")
        raise


# ============================================
# Google Search API
# ============================================

def test_google_search():
    print("=== Testing Google Search API ===")
    try:
        response = client.google_search(
            search="scrapingbee",
            params={"language": "en", "country_code": "us"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("organic_results"), "Missing organic_results in response")
        assert_test(isinstance(data.get("organic_results"), list), "organic_results is not a list")
        assert_test(len(data.get("organic_results", [])) > 0, "No organic results found")

        print(f"Status: {response.status_code}")
        print(f"Results found: {len(data.get('organic_results', []))}")
        print("✅ Google Search test passed!\n")
    except Exception as e:
        print(f"❌ Google Search test failed: {e}\n")
        raise


# ============================================
# Amazon API
# ============================================

def test_amazon_search():
    print("=== Testing Amazon Search API ===")
    try:
        response = client.amazon_search(
            query="laptop",
            params={"domain": "com", "pages": 1}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("products"), "Missing products in response")
        assert_test(isinstance(data.get("products"), list), "products is not a list")
        assert_test(len(data.get("products", [])) > 0, "No products found")

        print(f"Status: {response.status_code}")
        print(f"Results found: {len(data.get('products', []))}")
        print("✅ Amazon Search test passed!\n")
    except Exception as e:
        print(f"❌ Amazon Search test failed: {e}\n")
        raise


def test_amazon_product():
    print("=== Testing Amazon Product API ===")
    try:
        response = client.amazon_product(
            query="B0D2Q9397Y",
            params={"domain": "com"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("title"), "Missing product title in response")

        print(f"Status: {response.status_code}")
        print(f"Product title: {data.get('title', '')[:50]}")
        print("✅ Amazon Product test passed!\n")
    except Exception as e:
        print(f"❌ Amazon Product test failed: {e}\n")
        raise


# ============================================
# Walmart API
# ============================================

def test_walmart_search():
    print("=== Testing Walmart Search API ===")
    try:
        response = client.walmart_search(
            query="laptop",
            params={"device": "desktop", "sort_by": "best_match"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("products"), "Missing products in response")
        assert_test(isinstance(data.get("products"), list), "products is not a list")
        assert_test(len(data.get("products", [])) > 0, "No products found")

        print(f"Status: {response.status_code}")
        print(f"Results found: {len(data.get('products', []))}")
        print("✅ Walmart Search test passed!\n")
    except Exception as e:
        print(f"❌ Walmart Search test failed: {e}\n")
        raise


def test_walmart_product():
    print("=== Testing Walmart Product API ===")
    try:
        response = client.walmart_product(
            product_id="454408250",
            params={"device": "desktop"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("title"), "Missing product title in response")

        print(f"Status: {response.status_code}")
        print(f"Product title: {data.get('title', '')[:50]}")
        print("✅ Walmart Product test passed!\n")
    except Exception as e:
        print(f"❌ Walmart Product test failed: {e}\n")
        raise


# ============================================
# YouTube API
# ============================================

def test_youtube_search():
    print("=== Testing YouTube Search API ===")
    try:
        response = client.youtube_search(
            search="web scraping tutorial",
            params={"sort_by": "relevance", "type": "video"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("results"), "Missing results in response")
        assert_test(isinstance(data.get("results"), list), "results is not a list")
        assert_test(len(data.get("results", [])) > 0, "No results found")

        print(f"Status: {response.status_code}")
        print(f"Results found: {len(data.get('results', []))}")
        print("✅ YouTube Search test passed!\n")
    except Exception as e:
        print(f"❌ YouTube Search test failed: {e}\n")
        raise


def test_youtube_metadata():
    print("=== Testing YouTube Metadata API ===")
    try:
        response = client.youtube_metadata(video_id="dQw4w9WgXcQ")

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("title") or data.get("like_count") is not None, "Missing expected metadata fields")

        print(f"Status: {response.status_code}")
        print(f"Like count: {data.get('like_count')}")
        print("✅ YouTube Metadata test passed!\n")
    except Exception as e:
        print(f"❌ YouTube Metadata test failed: {e}\n")
        raise


def test_youtube_transcript():
    print("=== Testing YouTube Transcript API ===")
    try:
        response = client.youtube_transcript(
            video_id="sfyL4BswUeE",
            params={"language": "en"}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("text") or data.get("transcript"), "Missing transcript in response")

        transcript_preview = (data.get("text") or str(data.get("transcript", "")))[:100]
        print(f"Status: {response.status_code}")
        print(f"Transcript preview: {transcript_preview}")
        print("✅ YouTube Transcript test passed!\n")
    except Exception as e:
        print(f"❌ YouTube Transcript test failed: {e}\n")
        raise


def test_youtube_trainability():
    print("=== Testing YouTube Trainability API ===")
    try:
        response = client.youtube_trainability(video_id="dQw4w9WgXcQ")

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("permitted") is not None, "Missing permitted field in response")

        print(f"Status: {response.status_code}")
        print(f"Permitted: {data.get('permitted')}")
        print("✅ YouTube Trainability test passed!\n")
    except Exception as e:
        print(f"❌ YouTube Trainability test failed: {e}\n")
        raise


# ============================================
# ChatGPT API
# ============================================

def test_chatgpt():
    print("=== Testing ChatGPT API ===")
    try:
        response = client.chatgpt(
            prompt="What is web scraping? Answer in one sentence.",
            params={"search": True}
        )

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("results_text") or data.get("results_markdown"), "Missing response text")

        response_text = (data.get("results_text") or data.get("results_markdown", ""))[:100]
        print(f"Status: {response.status_code}")
        print(f"Response: {response_text}")
        print("✅ ChatGPT test passed!\n")
    except Exception as e:
        print(f"❌ ChatGPT test failed: {e}\n")
        raise


# ============================================
# Usage API
# ============================================

def test_usage():
    print("=== Testing Usage API ===")
    try:
        response = client.usage()

        assert_test(response.status_code == 200, f"Expected status 200, got {response.status_code}")

        data = response.json()
        assert_test(data.get("max_api_credit") is not None, "Missing max_api_credit")
        assert_test(data.get("used_api_credit") is not None, "Missing used_api_credit")
        assert_test(data.get("max_concurrency") is not None, "Missing max_concurrency")

        print(f"Status: {response.status_code}")
        print(f"Max API credits: {data.get('max_api_credit')}")
        print(f"Used API credits: {data.get('used_api_credit')}")
        print(f"Max concurrency: {data.get('max_concurrency')}")
        print("✅ Usage test passed!\n")
    except Exception as e:
        print(f"❌ Usage test failed: {e}\n")
        raise


# ============================================
# Run All Tests
# ============================================

def run_tests():
    print("\n🚀 Starting ScrapingBee Python SDK Tests\n")

    tests = [
        # Legacy HTML API
        test_html_get,
        test_html_post,

        # New HTML API
        test_html_api_get,
        test_html_api_post,
        test_html_api_extract_rules,
        test_html_api_js_scenario,
        test_html_api_screenshot,
        test_html_api_json_response,
        test_html_api_with_headers,
        test_html_api_with_cookies,
        test_html_api_post_with_headers_and_cookies,

        # Other APIs
        test_google_search,
        test_amazon_search,
        test_amazon_product,
        test_walmart_search,
        test_walmart_product,
        test_youtube_search,
        test_youtube_metadata,
        test_youtube_transcript,
        test_youtube_trainability,
        test_chatgpt,
        test_usage,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception:
            failed += 1

    print("🏁 All tests completed!")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {len(tests)}\n")

    if failed > 0:
        exit(1)


if __name__ == "__main__":
    run_tests()
