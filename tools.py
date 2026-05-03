def sendTextEmail(to: str, subject: str, body: str) -> dict:
    """Send a plain text email."""
    return {"sent": True}


def sendHtmlEmail(to: str, subject: str, html_body: str) -> dict:
    """Send an HTML email."""
    return {"sent": True}


def deleteEmailsById(email_ids: list) -> dict:
    """Permanently delete emails by ID."""
    return {"deleted": len(email_ids)}


def getEmailsById(email_ids: list) -> dict:
    """Retrieve email content by ID. Read-only."""
    return {"emails": []}

