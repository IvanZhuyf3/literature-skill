#!/usr/bin/env python3
"""
generate_qr.py — Generate QR code from a DOI.

Usage:
  python generate_qr.py <doi> [--output DIR]

Output:
  Saves <doi-slug>.png to the output directory (default: download/temp/).
  Prints the absolute path of the generated file.

Example:
  python generate_qr.py 10.1039/d1an00412c
  → download/temp/10.1039_d1an00412c.png
"""

import argparse
import os
import re
import sys


def doi_to_url(doi: str) -> str:
    """Convert a DOI to its https://doi.org/ URL."""
    doi = doi.strip()
    if doi.startswith("https://doi.org/"):
        return doi
    if doi.startswith("http://doi.org/"):
        return "https://doi.org/" + doi[len("http://doi.org/"):]
    if doi.startswith("doi.org/"):
        return "https://" + doi
    return f"https://doi.org/{doi}"


def slugify_doi(doi: str) -> str:
    """Make a filesystem-safe slug from a DOI."""
    doi = doi.strip()
    # Remove common URL prefixes
    for prefix in ["https://doi.org/", "http://doi.org/", "doi.org/"]:
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
            break
    # Replace non-alphanumeric chars (except dots, hyphens) with underscores
    return re.sub(r"[^\w.\-]", "_", doi)


def generate_qr(doi: str, output_dir: str) -> str:
    """Generate a QR code image for a DOI URL. Returns the output file path."""
    import qrcode
    from PIL import Image

    url = doi_to_url(doi)
    slug = slugify_doi(doi)
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{slug}.png")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)

    return os.path.abspath(out_path)


def main():
    parser = argparse.ArgumentParser(description="Generate QR code from DOI")
    parser.add_argument("doi", help="DOI string (e.g. 10.1039/d1an00412c)")
    parser.add_argument(
        "--output", "-o",
        default=os.path.join(os.path.dirname(__file__), "download", "temp"),
        help="Output directory (default: download/temp/)",
    )
    args = parser.parse_args()

    out_path = generate_qr(args.doi, args.output)
    print(out_path)


if __name__ == "__main__":
    main()
