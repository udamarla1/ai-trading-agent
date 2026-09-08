import os
import logging
from typing import List, Dict, Optional

from openai import OpenAI

logger = logging.getLogger(__name__)


_CLIENT: Optional[OpenAI] = None


def _get_client() -> OpenAI:
    """Lazily initialize and return an OpenAI client (v1+ Python SDK)."""
    global _CLIENT
    if _CLIENT is not None:
        return _CLIENT
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    _CLIENT = OpenAI(api_key=key)
    return _CLIENT


def chat_completion(messages: List[Dict[str, str]], model: str = "gpt-3.5-turbo", temperature: float = 0.7, max_tokens: int = 512) -> str:
    """Call the OpenAI Chat Completions API (new client) and return assistant text.

    This uses the openai.OpenAI client (`client.chat.completions.create(...)`).
    The function attempts to robustly extract text from the returned object.
    """
    client = _get_client()
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        # Try to extract assistant content in a few sensible ways.
        choice = None
        try:
            choice = resp.choices[0]
        except Exception:
            choice = None

        if choice is not None:
            # choice.message may be an object or dict
            msg = None
            if hasattr(choice, "message"):
                msg = choice.message
            elif isinstance(choice, dict):
                msg = choice.get("message")

            if msg is not None:
                # msg might expose .content or be a dict with 'content'
                content = None
                if hasattr(msg, "content"):
                    content = msg.content
                elif isinstance(msg, dict):
                    # some responses nest content under different keys
                    content = msg.get("content") or msg.get("text")

                if isinstance(content, list):
                    # sometimes content is a list of parts
                    content = "".join([c.get("text") if isinstance(c, dict) else str(c) for c in content])

                if content:
                    return str(content).strip()

        # Fallbacks: try resp.choices[0].text or resp.output_text-ish
        try:
            if choice is not None and hasattr(choice, "text") and choice.text:
                return str(choice.text).strip()
        except Exception:
            pass

        # As a last resort, stringify the response
        return str(resp).strip()

    except Exception as e:
        logger.exception("OpenAI request failed")
        raise


def prompt_to_text(prompt: str, **kwargs) -> str:
    """Convenience wrapper for a single-user prompt."""
    messages = [{"role": "user", "content": prompt}]
    return chat_completion(messages, **kwargs)
