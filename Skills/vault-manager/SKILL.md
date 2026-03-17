---
name: "vault-manager"
description: "Manages the vault structure by creating folders and moving files between Inbox, Needs_Action, and Done folders"
when_to_use: "When organizing files, creating new directories, or moving files between workflow stages"
version: "1.0"
author: "Personal AI Employee"
tags: ["file-management", "organization", "workflow"]
---

# 🗂️ Vault Manager Skill

## Description
The vault-manager skill handles all file organization tasks within the Personal AI Employee system. It creates new folders as needed, moves files between the different workflow stages (Inbox → Needs_Action → Done), lists directory contents, and reads file contents for processing.

## Capabilities

### Directory Management
- Create new folders with proper naming conventions
- List contents of any directory
- Check if folders exist before creating

### File Movement
- Move files from Inbox to Needs_Action when ready for processing
- Move completed files from Needs_Action to Done
- Copy files when preservation is needed
- Handle file conflicts appropriately

### Content Reading
- Read file contents for analysis
- Extract metadata from files
- Parse structured content (markdown, YAML, etc.)

## Examples

### Moving a Task Through Workflow
```
Input: File "new_client_request.md" in Inbox/
Action: Move to Needs_Action/
Result: File moved, ready for processing
```

### Creating New Category Folder
```
Input: Need to create "Marketing/" folder
Action: Create Marketing/ folder in root
Result: New folder created, ready for marketing-related files
```

### Reading File for Processing
```
Input: Read "Q4_budget_proposal.md" for analysis
Action: Retrieve file contents
Result: Content extracted and ready for analysis
```

## Best Practices

### File Movement
- Always verify destination folder exists before moving
- Maintain original filename unless transformation is needed
- Log all movements in the system for audit trail
- Check for duplicate filenames before moving

### Directory Creation
- Use descriptive, lowercase names with hyphens
- Follow existing naming conventions
- Create parent directories if they don't exist
- Update Dashboard.md when new categories are added

### Error Handling
- If move operation fails, attempt copy then delete
- If directory creation fails, check permissions
- If read fails, verify file exists and has proper permissions
- Always preserve original files until movement is confirmed

## Integration Points

### With Other Skills
- Works with file-drop-processor to organize incoming files
- Collaborates with dashboard-updater to maintain accurate status
- Coordinates with custom skills to store specialized outputs

### Workflow Dependencies
- Called before processing files in Needs_Action
- Used after completion to archive in Done/
- Invoked when creating space for new project categories

## Limitations
- Cannot move files that are locked or in use
- Does not validate file contents during movement
- Relies on proper naming conventions for correct routing
- Cannot undo operations without manual intervention