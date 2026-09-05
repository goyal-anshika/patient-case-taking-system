from pathlib import Path
import subprocess


class OCRProcessingError(RuntimeError):
    """Raised when OCR processing fails."""


def extract_text(image_path: str) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Tesseract must be installed separately on Windows.
    """

    path = Path(image_path)

    if not path.exists():
        raise OCRProcessingError(
            f"File not found: {image_path}"
        )

    try:
        result = subprocess.run(
            [
                "tesseract",
                str(path),
                "stdout",
                "--psm",
                "6",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
            check=False,
        )

    except FileNotFoundError as exc:
        raise OCRProcessingError(
            "Tesseract OCR is not installed or "
            "is not available in PATH."
        ) from exc

    except subprocess.TimeoutExpired as exc:
        raise OCRProcessingError(
            "OCR processing timed out."
        ) from exc

    if result.returncode != 0:
        raise OCRProcessingError(
            result.stderr.strip()
            or "OCR processing failed."
        )

    return result.stdout.strip()