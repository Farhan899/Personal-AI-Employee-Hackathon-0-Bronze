---
name: "dashboard-updater"
description: "Monitors the system state and updates Dashboard.md with current status, pending items, and recent activity"
when_to_use: "After completing tasks, at scheduled intervals, or when status information needs refreshing"
version: "1.0"
author: "Personal AI Employee"
tags: ["monitoring", "reporting", "status", "dashboard"]
---

# 📊 Dashboard Updater Skill

## Description
The dashboard-updater skill continuously monitors the Personal AI Employee system and maintains an accurate representation of current status in Dashboard.md. It reads the state of various folders, counts pending tasks, summarizes recent activity, and presents this information in a clear, actionable format.

## Capabilities

### Status Monitoring
- Count files in Needs_Action folder (pending tasks)
- Track recently completed items in Done folder
- Monitor Pending_Approval folder for items awaiting authorization
- Check Inbox for new unprocessed items

### Dashboard Updates
- Update status summary tables with current counts
- Generate recent activity logs from Logs folder
- Refresh pending tasks section with current Needs_Action items
- Update metrics and KPIs based on system activity

### Data Aggregation
- Compile statistics from multiple sources
- Format data into readable tables and lists
- Calculate metrics like completion rates and average processing time
- Extract relevant information from file metadata

## Examples

### Updating Task Counts
```
Input: Scan system folders
Action: Count files in each workflow stage
Result: 
- Inbox: 3 items
- Needs_Action: 7 items  
- Pending Approval: 2 items
- Done (today): 5 items
Dashboard updated with these numbers
```

### Adding Recent Activity
```
Input: Check Logs/ folder for recent entries
Action: Extract latest 5 log entries
Result: Recent Activity section updated with latest actions
```

### Generating Status Summary
```
Input: Current system state
Action: Create summary table
Result: Updated metrics table showing system health
```

## Best Practices

### Frequency of Updates
- Update immediately after completing a task
- Perform comprehensive update at start of each day
- Refresh before generating reports
- Update when requested by other skills

### Data Presentation
- Use consistent table formats
- Highlight urgent or overdue items
- Show trends over time when possible
- Include timestamps for recent activities
- Use emojis for quick visual scanning

### Accuracy
- Verify file counts before updating
- Cross-reference with other system components
- Flag inconsistencies for manual review
- Maintain historical data for trend analysis

## Integration Points

### With Other Skills
- Receives notifications from file-drop-processor when new items arrive
- Gets updates from vault-manager when files are moved
- Coordinates with custom skills to include specialized metrics

### Trigger Events
- File movement between workflow stages
- Completion of processing tasks
- Scheduled intervals (hourly, daily)
- Manual requests from system administrator

## Limitations
- May have slight delays if system is busy
- Cannot predict future tasks or workload
- Depends on other skills properly updating file locations
- Requires read access to all monitored folders