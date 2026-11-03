---
name: sync-youtube
description: Fetch latest YouTube uploads and update event pages.
---

# sync-youtube

This skill provides the instructions for synchronizing the latest YouTube uploads from the Gdańsk Embedded Meetup channel with the local documentation.

**Note**: Videos are typically uploaded a couple of weeks after the meeting. Some sessions may not be recorded at all. The goal is strictly to add URLs found in the YouTube metadata to their corresponding event entries.

## Instructions

To synchronize the YouTube URLs, execute the following command to fetch the latest metadata:

```bash
uvx --with deno --with yt-dlp-ejs yt-dlp --skip-download --max-downloads 10 --print "%(webpage_url)s :  %(upload_date)s %(title)s" https://www.youtube.com/@gdanskembeddedmeetup 2>/dev/null
```

## Manual Update Workflow

Once you have the output from the command above, follow these steps:

1. **Identify Targets**: Search for recent presentation files that are missing a YouTube link. Use this command to find files using the presentation template that do not have a `youtube_url` field:
   ```bash
   find content/events -name "index.md" -exec grep -l "template: presentation.html" {} + | xargs grep -L "youtube_url:"
   ```
   *Note: If you want to find files where the field exists but is set to `TBD`, use:*
   ```bash
   find content/events -name "index.md" -exec grep -l "template: presentation.html" {} + | xargs grep -lE "youtube_url: (TBD|)"
   ```

2. **Match Uploads**: Match the video title from the `uvx` output to the `title` field in the frontmatter of these identified files. **CRITICAL: Before applying any changes, verify that the video title and/or speaker name matches the event's schedule in the parent `index.md`, and that the YouTube upload date is strictly AFTER the event date to avoid matching videos from previous meetups.**
3. **Verify Continuity**: Ensure the YouTube upload date is reasonably recent and follows the event date.
4. **Update Frontmatter**: For each match, update the `youtube_url` field in that file's frontmatter with the provided URL.
5. **Verify**: Check that the Markdown file still parses correctly and the new URL is present.
