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

SOURCE_TEXT = """ Cybersecurity has become an important part of modern digital systems. 
As businesses and individuals increasingly use online services, protecting 
digital information from unauthorized access has become more important.

One common cybersecurity threat is phishing. In phishing attacks, attackers 
may send fake emails or messages designed to trick users into sharing 
passwords, financial information, or other sensitive data.

Strong passwords are another important part of cybersecurity. Using unique 
passwords for different accounts can reduce the risk of multiple accounts 
being affected if one password is compromised. Multi-factor authentication 
can provide an additional layer of security.

Organizations also need to keep their software and systems updated. Software 
updates can include security fixes that protect systems against known 
vulnerabilities.

Employee awareness is equally important. Regular cybersecurity training can 
help employees recognize suspicious emails, unsafe links, and other potential 
security threats.

Overall, cybersecurity requires a combination of technology, secure 
practices, regular updates, and user awareness. Both organizations and 
individuals have a role to play in protecting digital information."""


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
