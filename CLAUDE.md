---
title: "Instructions for Claude AI"
description: "How Claude should interact with this Personal AI Employee system"
created: "2026-02-11"
version: "1.0"
---

# 🤖 Instructions for Claude AI

## 📂 Folder Conventions

### Purpose of Each Folder
- **Inbox/**: New tasks and information to be processed
- **Needs_Action/**: Tasks requiring processing or completion  
- **Done/**: Completed tasks (archive for reference)
- **Skills/**: Documentation of capabilities and how-tos
- **Logs/**: Activity logs and historical records
- **Pending_Approval/**: Items requiring human approval before execution
- **Briefings/**: Strategic information and company updates

### File Naming Convention
- Use descriptive names with underscores: `marketing_campaign_analysis.md`
- Include dates when relevant: `meeting_notes_2026_02_11.md`
- Use consistent prefixes for categorization: `skill_`, `log_`, `briefing_`

## 📝 Reading Files

### When to Read Files
- Always check `Dashboard.md` first for current status
- Review `Company_Handbook.md` for policy guidance
- Consult `Skills/` folder for capability references
- Check `Logs/` folder for historical context

### Reading Protocol
1. Start with `Dashboard.md` to understand current state
2. Refer to `Company_Handbook.md` for operational rules
3. Look at `Inbox/` for new tasks
4. Check `Pending_Approval/` for items awaiting authorization

## ✍️ Writing Files

### Creating New Files
- Place new tasks in `Inbox/` folder initially
- Move to `Needs_Action/` when ready to process
- Transfer to `Done/` when completed
- Add to `Logs/` for record keeping
- Use `Skills/` for documenting new capabilities
- Use `Briefings/` for strategic information

### Writing Standards
- Use proper YAML frontmatter when appropriate
- Apply markdown formatting for readability
- Include relevant emojis for visual cues
- Use callouts (```>``` or ```!!!```) for important information
- Follow the style guide in `Company_Handbook.md`

## 🔄 Processing Workflow

### Task Lifecycle
1. **Receive**: New task appears in `Inbox/`
2. **Assess**: Determine priority and approval needs
3. **Process**: Move to `Needs_Action/` and execute
4. **Approve**: If threshold exceeded, move to `Pending_Approval/`
5. **Complete**: Move to `Done/` when finished
6. **Log**: Record activity in `Logs/`
7. **Report**: Update `Dashboard.md` with status

### Decision Tree
```
New Task → Check Approval Threshold → 
├─ Below threshold → Process → Done → Update Dashboard
└─ Above threshold → Pending Approval → Wait for Authorization → Process → Done
```

## 🛡️ Safety Protocols

### Forbidden Actions
- Never delete files from `Done/` or `Logs/` without explicit permission
- Don't exceed approval thresholds without authorization
- Don't access external systems without proper credentials
- Don't share confidential information outside appropriate channels

### Error Handling
- If uncertain about a task, place in `Pending_Approval/`
- Document any unusual situations in `Logs/`
- Update `Dashboard.md` to reflect any system issues
- Follow escalation procedures in `Company_Handbook.md`

## 📊 Reporting Requirements

### Dashboard Updates
- Update status metrics daily
- Record completed tasks
- Note pending items
- Track performance indicators

### Logging Standards
- Date and time stamp all log entries
- Include task ID when applicable
- Note any deviations from standard procedure
- Record efficiency metrics