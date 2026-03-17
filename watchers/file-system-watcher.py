"""
File System Watcher for Personal AI Employee (Bronze Tier)

This script monitors the Inbox folder for new files and processes them
according to the Personal AI Employee workflow. When a new file is detected,
it creates a structured markdown summary in the Needs_Action folder with
appropriate metadata, and optionally moves the original file to Done.

Author: Personal AI Employee
Version: 1.0
"""

import os
import time
import logging
from datetime import datetime
from pathlib import Path
import mimetypes

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class InboxHandler(FileSystemEventHandler):
    """
    Event handler for monitoring the Inbox folder.
    
    Processes new files by creating markdown summaries with metadata
    and moving original files to the Done folder.
    """
    
    def __init__(self, project_root):
        """
        Initialize the InboxHandler.
        
        Args:
            project_root (str): Path to the project root directory
        """
        super().__init__()
        self.project_root = Path(project_root)
        self.inbox_path = self.project_root / "Inbox"
        self.needs_action_path = self.project_root / "Needs_Action"
        self.done_path = self.project_root / "Done"
        self.logs_path = self.project_root / "Logs"
        
        # Create directories if they don't exist
        self.needs_action_path.mkdir(exist_ok=True)
        self.done_path.mkdir(exist_ok=True)
        self.logs_path.mkdir(exist_ok=True)
        
        # Setup logger
        self.logger = self._setup_logger()
        
    def _setup_logger(self):
        """
        Setup logger for the file system watcher.
        
        Returns:
            logging.Logger: Configured logger instance
        """
        logger = logging.getLogger('FileSystemWatcher')
        logger.setLevel(logging.INFO)
        
        # Create file handler
        log_file = self.logs_path / "watcher.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            
        return logger
    
    def _generate_summary_content(self, file_path):
        """
        Generate a structured markdown summary for the given file.
        
        Args:
            file_path (Path): Path to the original file
            
        Returns:
            str: Markdown content with YAML frontmatter
        """
        # Get file stats
        stat = file_path.stat()
        file_size = stat.st_size
        mime_type, _ = mimetypes.guess_type(str(file_path))
        
        # Create YAML frontmatter
        yaml_frontmatter = f"""---
type: file_drop
original_name: "{file_path.name}"
size_bytes: {file_size}
mime_type: "{mime_type or 'unknown'}"
dropped_at: "{datetime.now().isoformat()}"
status: pending
priority: medium
tags: []
estimated_duration_minutes: 15
---

# File Drop Summary: {file_path.name}

## File Information
- **Original Name**: `{file_path.name}`
- **Size**: {file_size} bytes
- **MIME Type**: {mime_type or 'unknown'}
- **Dropped At**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Source Path**: `{file_path.relative_to(self.project_root.parent)}`
"""
        
        # Add content preview if it's a text file
        try:
            # Try to read as text
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                preview = f.read(500)  # First 500 characters
                
            # Clean up preview text
            preview = preview.strip()
            if len(preview) >= 500:
                preview += "\n\n... (truncated)"
                
            if preview:
                yaml_frontmatter += f"\n## Content Preview\n\n```\n{preview}\n```\n"
        except Exception:
            # If not a text file, just note that
            yaml_frontmatter += f"\n## Content Preview\n\n*Non-text file ({mime_type})*\n"
        
        # Add processing instructions
        yaml_frontmatter += f"""
## Processing Instructions

1. Review the content above
2. Determine appropriate next steps
3. Update status to reflect progress
4. Add any relevant tags or metadata
5. Estimate completion time if different from default

## Action Items

- [ ] Review content and determine priority
- [ ] Assign to appropriate team member if needed
- [ ] Set realistic deadline
- [ ] Update status as work progresses
"""
        
        return yaml_frontmatter
    
    def on_created(self, event):
        """
        Handle file creation events in the Inbox folder.
        
        Args:
            event: File system event object
        """
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        
        # Only process files in the Inbox folder (not subfolders)
        if file_path.parent == self.inbox_path:
            self.process_new_file(file_path)
    
    def on_moved(self, event):
        """
        Handle file move events in the Inbox folder.
        
        Args:
            event: File system event object
        """
        if event.is_directory:
            return
            
        # The destination path is where the file was moved to
        dest_path = Path(event.dest_path)
        
        # Only process if the destination is in the Inbox folder
        if dest_path.parent == self.inbox_path:
            self.process_new_file(dest_path)
    
    def process_new_file(self, file_path):
        """
        Process a new file by creating a markdown summary and moving the original.
        
        Args:
            file_path (Path): Path to the new file in the Inbox
        """
        try:
            self.logger.info(f"Processing new file: {file_path.name}")
            
            # Generate the markdown summary
            summary_content = self._generate_summary_content(file_path)
            
            # Create a safe filename for the summary
            stem = file_path.stem.replace(' ', '_').replace('-', '_')
            summary_filename = f"{stem}_summary.md"
            summary_path = self.needs_action_path / summary_filename
            
            # Handle potential filename conflicts
            counter = 1
            original_summary_path = summary_path
            while summary_path.exists():
                name_part = original_summary_path.stem.rsplit('_', 1)[0]  # Remove counter if present
                summary_path = self.needs_action_path / f"{name_part}_{counter}.md"
                counter += 1
            
            # Write the summary to the Needs_Action folder
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary_content)
            
            self.logger.info(f"Created summary: {summary_path.name}")
            
            # Move the original file to Done folder
            done_file_path = self.done_path / file_path.name
            
            # Handle potential filename conflicts in Done folder too
            counter = 1
            original_done_path = done_file_path
            while done_file_path.exists():
                name_part = original_done_path.stem
                ext = original_done_path.suffix
                done_file_path = self.done_path / f"{name_part}_{counter}{ext}"
                counter += 1
            
            # Move the original file to Done
            file_path.rename(done_file_path)
            
            self.logger.info(f"Moved original file to Done: {done_file_path.name}")
            
            # Log successful processing
            self.logger.info(f"Successfully processed file: {file_path.name} -> {summary_path.name}")
            
            # Print instruction for manual trigger
            print(f"\n🔄 New file processed! To continue workflow:")
            print(f"   Run: \"Check /Needs_Action and update Dashboard.md\" in Claude")
            print(f"   Or manually review {summary_path.relative_to(self.project_root)}\n")
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {str(e)}")
            # Still print the instruction even if there's an error
            print(f"\n❌ Error processing {file_path.name}, see logs for details")
            print(f"   Check Logs/watcher.log for more information\n")


def main():
    """
    Main function to start the file system watcher.
    """
    # Get the project root (current directory)
    project_root = Path.cwd()
    inbox_path = project_root / "Inbox"
    
    # Verify Inbox folder exists
    if not inbox_path.exists():
        print(f"Error: Inbox folder does not exist at {inbox_path}")
        print("Please create the Inbox folder first.")
        return
    
    # Create the event handler
    event_handler = InboxHandler(project_root)
    
    # Create the observer
    observer = Observer()
    observer.schedule(event_handler, str(inbox_path), recursive=False)
    
    # Start the observer
    observer.start()
    event_handler.logger.info("File system watcher started. Monitoring Inbox folder...")
    print("📁 File system watcher started. Monitoring Inbox folder...")
    print("💡 Drop files in the Inbox folder to process them automatically.")
    print("⚠️  Press Ctrl+C to stop the watcher.\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 File system watcher stopped by user.")
    
    observer.join()


if __name__ == "__main__":
    main()