#!/usr/bin/env python3
"""
Local test script that runs zotero-arxiv-daily without sending emails.
Instead, it prints the email content to the console.

Usage:
    python test_no_email.py

This script patches the send_email function to preview the email content
instead of actually sending it via SMTP.
"""
import sys
import os
import datetime
from omegaconf import DictConfig

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def preview_send_email(config: DictConfig, html: str):
    """Preview email instead of sending"""
    print("\n" + "="*80)
    print("📧 EMAIL PREVIEW - NOT SENT")
    print("="*80)
    print(f"TO: {config.email.receiver}")
    print(f"FROM: {config.email.sender}")
    today = datetime.datetime.now().strftime('%Y/%m/%d')
    print(f"SUBJECT: Daily arXiv {today}")
    print("="*80)
    print("HTML CONTENT:")
    print("-" * 80)
    # Print the HTML content (truncated if too long)
    max_show = 8000
    if len(html) > max_show:
        print(html[:max_show] + f"\n\n... [truncated, total {len(html)} chars]")
    else:
        print(html)
    print("-" * 80)
    print("✅ Email would have been sent successfully (test mode)")
    print("="*80 + "\n")


# Patch the modules before importing main
import zotero_arxiv_daily.utils as utils
import zotero_arxiv_daily.executor as executor

utils.send_email = preview_send_email
executor.send_email = preview_send_email

# Now run main
from zotero_arxiv_daily.main import main

if __name__ == '__main__':
    print("🚀 Running zotero-arxiv-daily in test mode (no emails will be sent)")
    print("="*80)
    main()
