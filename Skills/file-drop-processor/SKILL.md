---
name: "file-drop-processor"
description: "Processes new files that appear in the Inbox folder, creates clean markdown summaries in Needs_Action, and archives originals in Done"
when_to_use: "Whenever new files appear in the Inbox folder that need processing"
version: "1.0"
author: "Personal AI Employee"
tags: ["file-processing", "inbox-management", "summarization"]
---

# 📥 File Drop Processor Skill

## Description
The file-drop-processor skill monitors the Inbox folder for new files and automatically processes them. It creates clean, structured markdown summaries in the Needs_Action folder with appropriate metadata, then moves the original files to the Done folder for archiving. This skill serves as the entry point for new tasks into the Personal AI Employee workflow.

## Capabilities

### Inbox Monitoring
- Detect new files in the Inbox folder
- Identify file types and content structure
- Prioritize files based on type, size, or metadata
- Queue files for processing in appropriate order

### Content Processing
- Extract key information from various file types
- Convert non-markdown files to clean markdown format
- Identify important elements like dates, names, and action items
- Preserve essential content while removing formatting clutter

### Summary Creation
- Generate structured markdown summaries with proper headers
- Include relevant metadata in YAML frontmatter
- Create actionable task descriptions
- Format content for easy reading and processing

### File Management
- Move processed files from Inbox to Done
- Place summaries in Needs_Action for further processing
- Maintain original file relationships when needed
- Log processing activities in the system

## Examples

### Processing a Meeting Transcript
```
Input: "team_sync_2026_02_11.txt" in Inbox/
Action: Extract action items, decisions, and follow-ups
Output: 
- Summary "action-items-team-sync.md" in Needs_Action/
- Original file moved to Done/
- YAML frontmatter includes date, participants, priority
```

### Processing an Email Forward
```
Input: "client_request.eml" in Inbox/
Action: Extract client name, request details, deadline
Output:
- Summary "follow-up-client-request.md" in Needs_Action/
- Original email moved to Done/
- Priority set to High based on client importance
```

### Processing a PDF Document
```
Input: "contract_proposal.pdf" in Inbox/
Action: Extract parties, terms, deadlines, and key clauses
Output:
- Summary "review-contract-proposal.md" in Needs_Action/
- Original PDF moved to Done/
- Tags added for legal review and approval threshold
```

## Best Practices

### Content Extraction
- Focus on actionable items rather than full reproduction
- Identify and highlight deadlines and important dates
- Extract contact information for follow-up
- Preserve context while reducing noise

### Metadata Standards
- Include source file name in metadata
- Set appropriate priority levels
- Add relevant tags for categorization
- Include estimated processing time

### Quality Control
- Verify summaries contain sufficient detail for action
- Check that important information isn't lost in processing
- Ensure summaries are grammatically correct and clear
- Flag complex files for manual review if needed

### File Handling
- Preserve original file format and content
- Use descriptive names for summary files
- Maintain chronological order when possible
- Handle large files appropriately (chunking if necessary)

## Integration Points

### With Other Skills
- Hands off processed summaries to appropriate specialists
- Works with vault-manager to organize files properly
- Updates dashboard-updater with new task notifications
- Coordinates with custom skills for specialized processing

### Workflow Integration
- Acts as the first step in the processing pipeline
- Determines next steps based on content analysis
- Sets priority and category for downstream processing
- Triggers notifications for urgent items

## Limitations
- May struggle with heavily formatted or corrupted files
- Cannot process password-protected documents
- Accuracy depends on original file quality and structure
- Complex documents may require manual review
- Limited ability to interpret handwritten or scanned content