"""Platform Content Generators for PRISM.

Provides 5 platform-specific content generation functions powered by LLM.
"""

from typing import Any, Dict, Optional

try:
    from ai_llm.llm_service import generate_content
except ImportError:
    from llm_service import generate_content


def _validate_source_text(source_text: Optional[str]) -> Optional[Dict[str, Any]]:
    """Validate that source_text is non-empty.

    If empty or None, return an error dictionary without calling the LLM.
    """
    if not source_text or not str(source_text).strip():
        return {
            "response": "Source text is required.",
            "response_time": 0.0,
            "error": "Source text is required.",
        }
    return None


def generate_summary(source_text: str) -> Dict[str, Any]:
    """Generate a concise summary with 3-5 key points from the source text."""
    error_res = _validate_source_text(source_text)
    if error_res:
        return error_res

    prompt = f"""You are a content summarizer. Summarize the following source text.

Requirements:
- Generate a concise summary.
- Return exactly 3 to 5 key points in a numbered list.
- Preserve the original meaning.
- Do not invent facts, statistics, names, dates, URLs, or claims.
- Do not add information that is not present in the source text.
- Use clear and simple language.
- Do not add any intro, outro, explanations, or disclaimers outside the requested format.

Required output format:

SUMMARY:
1. ...
2. ...
3. ...

Source Text:
{source_text}"""

    return generate_content(prompt)


def generate_linkedin_post(source_text: str) -> Dict[str, Any]:
    """Generate a professional LinkedIn post based on the source text."""
    error_res = _validate_source_text(source_text)
    if error_res:
        return error_res

    prompt = f"""You are an expert social media strategist writing a LinkedIn post based ONLY on the source text below.

Requirements:
- Professional LinkedIn tone.
- Start with a strong hook under HOOK:.
- Use short readable paragraphs under POST:.
- Extract the important ideas from the source text.
- Make the post engaging but strictly factual.
- Include a natural call-to-action under CTA:.
- Add 3 to 5 relevant hashtags under HASHTAGS:.
- Do not invent statistics, facts, names, dates, URLs, or claims.
- Do not provide posting tips or extra commentary outside the requested structure.
- Return ONLY the final LinkedIn post structure.

Required structure:

HOOK:
...

POST:
...

CTA:
...

HASHTAGS:
#... #... #...

Source Text:
{source_text}"""

    return generate_content(prompt)


def generate_twitter_content(source_text: str) -> Dict[str, Any]:
    """Generate concise Twitter/X post based on the source text."""
    error_res = _validate_source_text(source_text)
    if error_res:
        return error_res

    prompt = f"""You are a social media copywriter creating a Twitter/X post based ONLY on the source text below.

Requirements:
- Concise Twitter/X style.
- Strong opening hook.
- Keep the content short and easy to scan.
- Preserve important information from the source text.
- Use a natural call-to-action when appropriate.
- Use a maximum of 3 relevant hashtags under HASHTAGS:.
- Do not invent facts, statistics, names, dates, URLs, or claims.
- Do not add explanations or posting tips.

Required output structure:

TWITTER/X:
...

HASHTAGS:
#... #...

Source Text:
{source_text}"""

    return generate_content(prompt)


def generate_instagram_caption(source_text: str) -> Dict[str, Any]:
    """Generate an engaging Instagram caption based on the source text."""
    error_res = _validate_source_text(source_text)
    if error_res:
        return error_res

    prompt = f"""You are an Instagram content creator writing a caption based ONLY on the source text below.

Requirements:
- Engaging Instagram style.
- Strong opening line.
- Short readable paragraphs under CAPTION:.
- Capture the main idea of the source text.
- Include a natural call-to-action under CTA:.
- Add 5 to 8 relevant hashtags under HASHTAGS:.
- Do not use irrelevant or excessive hashtags.
- Do not invent facts, statistics, names, dates, URLs, or claims.
- Do not add posting tips or explanations outside the requested structure.
- Return only the final caption structure.

Required output structure:

CAPTION:
...

CTA:
...

HASHTAGS:
#... #... #... #... #...

Source Text:
{source_text}"""

    return generate_content(prompt)


def generate_youtube_content(source_text: str) -> Dict[str, Any]:
    """Generate YouTube title, description, key points, and CTA based on source text."""
    error_res = _validate_source_text(source_text)
    if error_res:
        return error_res

    prompt = f"""You are a YouTube video strategist creating video title and description content based ONLY on the source text below.

Requirements:
- Generate an SEO-friendly YouTube title relevant to the source text under TITLE:.
- Title must be clear and relevant to the source text.
- Generate a useful YouTube description under DESCRIPTION:.
- Include 3 concise key points under KEY POINTS:.
- Include a natural call-to-action under CTA:.
- Do not invent facts, statistics, names, dates, URLs, or claims.
- Do not add unrelated information.
- Do not add anything before TITLE: or after CTA:.

Required structure MUST be followed exactly:

TITLE:
...

DESCRIPTION:
...

KEY POINTS:
1. ...
2. ...
3. ...

CTA:
...

Source Text:
{source_text}"""

    return generate_content(prompt)
