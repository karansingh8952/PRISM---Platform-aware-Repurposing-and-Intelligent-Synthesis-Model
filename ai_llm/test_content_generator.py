import sys
import time

# Ensure UTF-8 output encoding for Windows terminals
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    from ai_llm.content_generator import (
        generate_summary,
        generate_linkedin_post,
        generate_twitter_content,
        generate_instagram_caption,
        generate_youtube_content,
    )
except ImportError:
    from content_generator import (
        generate_summary,
        generate_linkedin_post,
        generate_twitter_content,
        generate_instagram_caption,
        generate_youtube_content,
    )

SOURCE_TEXT = """ Social media has become an important part of modern daily life. People use social networking platforms to
communicate with friends, share information, follow news, and discover new content.
One major benefit of social media is communication. People can stay connected with family, friends, and
professional communities even when they are in different locations. Social media also allows users to share
photos, videos, ideas, and experiences with a large audience.
Social media is also widely used for learning and information sharing. Students can discover educational
content, follow experts, participate in online communities, and access different perspectives on various topics.
However, excessive social media usage can create challenges. Spending too much time on social platforms
may reduce productivity and distract users from their daily responsibilities. Users may also encounter
misleading information, unwanted content, or privacy concerns.
Responsible usage is therefore important. Users should be careful about the information they share online,
review their privacy settings, and verify important information before accepting or sharing it with others.
Overall, social media provides useful opportunities for communication, learning, and information sharing. At
the same time, users need to maintain a healthy balance and use social platforms responsibly.
"""


def run_tests():
    summary_res = generate_summary(SOURCE_TEXT)
    time.sleep(12)
    linkedin_res = generate_linkedin_post(SOURCE_TEXT)
    time.sleep(12)
    twitter_res = generate_twitter_content(SOURCE_TEXT)
    time.sleep(12)
    instagram_res = generate_instagram_caption(SOURCE_TEXT)
    time.sleep(12)
    youtube_res = generate_youtube_content(SOURCE_TEXT)

    print("==================================================")
    print("PRISM CONTENT GENERATOR TEST")
    print("==================================================\n")

    print("========== 1. SUMMARY ==========")
    print(summary_res.get("response") or summary_res.get("error"))
    print()

    print("========== 2. LINKEDIN POST ==========")
    print(linkedin_res.get("response") or linkedin_res.get("error"))
    print()

    print("========== 3. TWITTER/X POST ==========")
    print(twitter_res.get("response") or twitter_res.get("error"))
    print()

    print("========== 4. INSTAGRAM CAPTION ==========")
    print(instagram_res.get("response") or instagram_res.get("error"))
    print()

    print("========== 5. YOUTUBE TITLE + DESCRIPTION ==========")
    print(youtube_res.get("response") or youtube_res.get("error"))
    print()

    print("==================================================")
    print("RESPONSE TIMES")
    print("==================================================")
    print(f"Summary: {summary_res.get('response_time')} seconds")
    print(f"LinkedIn: {linkedin_res.get('response_time')} seconds")
    print(f"Twitter/X: {twitter_res.get('response_time')} seconds")
    print(f"Instagram: {instagram_res.get('response_time')} seconds")
    print(f"YouTube: {youtube_res.get('response_time')} seconds")
    print()

    print("==================================================")
    print("ERROR STATUS")
    print("==================================================")
    print(f"Summary: {summary_res.get('error')}")
    print(f"LinkedIn: {linkedin_res.get('error')}")
    print(f"Twitter/X: {twitter_res.get('error')}")
    print(f"Instagram: {instagram_res.get('error')}")
    print(f"YouTube: {youtube_res.get('error')}")


if __name__ == "__main__":
    run_tests()
