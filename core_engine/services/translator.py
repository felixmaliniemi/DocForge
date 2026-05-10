"""Translator utility using googletrans."""

from functools import lru_cache
from core_engine.utils.logger_config import setup_logger

logger = setup_logger()

TRANSLATE_ENABLED = True        # Can be manually disabled
_translation_state = {"failed": False}    # Keeps track of whether translation failed
_translator_instance = None              # Always define the variable

try:
    from googletrans import Translator

    _translator = Translator()
    TRANSLATE_AVAILABLE = True

except ImportError:
    logger.warning("⚠️ googletrans is missing. Translation will not be used.")
    TRANSLATE_AVAILABLE = False

@lru_cache(maxsize=1024)
def translate(text: str, target_language="en") -> str:
    """
        Translates text with Google Translate.

        Parameters:
        text (str): Text to be translated.
        target_language (str): Language to translate to (e.g. "en", "sv", "none").

        Returns:
        str: Translated text or original text if translation is not possible.
    """
    if not text:
        return "(no documentation found)"

    if (
        not TRANSLATE_AVAILABLE
        or not TRANSLATE_ENABLED
        or _translation_state["failed"]
        or target_language.lower() == "none"
        or _translator_instance is None
    ):
        return text

    try:
        return _translator_instance.translate(text, dest=target_language).text

    except Exception as exc:  # pylint: disable=broad-exception-caught
        logger.error(
            "❌ Translation failed for text: %r. Error: %s",
            text[:80],
            exc,
        )
        return f"{text}\n\n(translation not available)"
