# Personal AI Employee - Bronze Tier

A complete file-based AI employee system that automates task processing and workflow management using a simple folder structure and markdown files.

## 🚀 Overview

The Personal AI Employee Bronze Tier implements a robust automation system that monitors an Inbox folder for new files, processes them according to predefined rules, and manages workflow through a structured folder system. The system includes:

- **File System Watcher**: Monitors Inbox for new files and processes them automatically
- **Three-Tier Workflow**: Inbox → Needs_Action → Done for task management
- **Skill-Based Architecture**: Modular skills for different capabilities
- **Dashboard Monitoring**: Real-time status updates and metrics
- **Comprehensive Logging**: Full audit trail of all activities

## 📁 Folder Structure

```
Project Root/
├── Inbox/                 # New files dropped here for processing
├── Needs_Action/          # Files requiring processing or completion
├── Done/                  # Completed tasks (archived)
├── Skills/                # Documentation of capabilities and how-tos
│   ├── vault-manager/     # File organization and movement
│   ├── dashboard-updater/ # Status monitoring and reporting
│   └── file-drop-processor/ # Inbox file processing
├── Logs/                  # Activity logs and historical records
├── Pending_Approval/      # Items requiring human approval
└── Briefings/             # Strategic information and updates
```

## 🛠️ Components

### File System Watcher
- Located at: `watchers/file-system-watcher.py`
- Monitors the Inbox folder for new files
- Creates structured markdown summaries with YAML frontmatter
- Moves original files to Done folder after processing
- Logs all activities to `Logs/watcher.log`

### Skills System
- **vault-manager**: Manages folder creation and file movement between workflow stages
- **dashboard-updater**: Monitors system state and updates Dashboard.md with current status
- **file-drop-processor**: Processes new files from Inbox, creates markdown summaries

### Dashboard
- Real-time status updates in `Dashboard.md`
- Tracks pending tasks, recent activity, and system health
- Automatically updated when workflows are completed

## 📋 Requirements

- Python 3.7+
- `watchdog` library (install via `pip install -r requirements.txt`)

## 🚦 Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the file system watcher:
   ```bash
   python watchers/file-system-watcher.py
   ```
4. The system will begin monitoring the Inbox folder automatically

## 🎯 Usage

1. **Drop files in Inbox/**: Place any file in the Inbox folder to initiate processing
2. **Monitor Needs_Action/**: Check this folder for structured markdown summaries of your files
3. **Review Done/**: Find original files that have been processed and archived
4. **Check Dashboard.md**: View real-time status and metrics
5. **Manual triggers**: After watcher processes files, manually trigger Claude with "Check /Needs_Action and update Dashboard.md"

## 📝 Company Handbook

Refer to `Company_Handbook.md` for:
- Communication style guidelines
- Approval thresholds ($200+ requires human approval)
- Priority rules and urgent keywords
- Forbidden actions and compliance requirements

## 🏷️ YAML Frontmatter

Processed files include structured metadata:
```yaml
---
type: file_drop
original_name: "filename.ext"
size_bytes: 1234
mime_type: "application/pdf"
dropped_at: "2026-02-11T10:30:00"
status: pending
priority: medium
---
```

## 🔄 Workflow

1. **Inbox**: New files are dropped for processing
2. **Needs_Action**: System creates markdown summary with metadata
3. **Processing**: Tasks are completed according to defined procedures
4. **Done**: Completed tasks are archived for reference
5. **Dashboard**: Status is updated automatically

## 🛡️ Safety Protocols

- Files over $200 in value require human approval
- Social media posting requires explicit authorization
- Professional communication standards enforced
- Complete audit trail maintained in Logs/

## 🤖 Interacting with Claude

The `CLAUDE.md` file contains instructions for AI assistants on how to interact with this system, including:
- Folder conventions and purpose
- Reading and writing protocols
- Processing workflows
- Safety protocols

## 📊 Monitoring

The system provides real-time monitoring through:
- Dashboard.md with status metrics
- Activity logs in Logs/ folder
- File counts in each workflow stage
- System health indicators

## 🚀 Next Steps

This Bronze Tier implementation can be extended with:
- Email integration (Gmail watcher)
- Calendar synchronization
- API integrations
- Advanced analytics and reporting
- Custom skill development

## 📜 License

This project is open source and available under the MIT License.