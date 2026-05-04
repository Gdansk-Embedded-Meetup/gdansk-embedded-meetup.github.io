---
name: scrape-event
description: Scrape event information from meetup.com and add it to the repository
---

Given a link to a meetup.com event, scrape the event information and add it to the repository.
After each of these steps let the user know that you followed it exactly before continuing.

1. Read the mkdocs configuration file to understand the configured locations that can be referenced
1. Save the webpage content to a temporary file `event.html` in the repository for later reference, since the webpage can be too big for the context. Do not fetch the webpage directly to context.
1. Extract event description, time and date information and location from the webpage content
1. Copy the template folder `template_event/2099-01-01_999` to `content/events/<year>/<yyyy-mm-dd>_<event_number>`. Do not skip this step.
1. Download the webp cover image in high resolution and place in the new folder in the `static` subfolder (you need to create that folder)
    1. The link should look like `https://secure.meetupstatic.com/photos/event/1/0/b/c/highres_533404284.webp`
        1. If it's jpeg and not webp just change the last part to `.webp` and try that
        1. If changing the link to webp doesn't work and you have a link to a highres jpeg image, use that
        1. If not sure which photo to use, get the one that is linked most often
    1. Verify that the image was saved correctly
1. Using the last event as reference if needed, fill the event description and the talks in the subfolders in the directory copied from the template
    1. Add appropriate tags to each talk, use something like `grep --recursive --no-filename -A5 tags content/events | uniq` to find the tags used in the previous events, as not all of them are mentioned in the mkdocs configuration, and there is quite a lot of them
        1. Make sure to get all the tags and filter out all the noise.
        1. Use ripgrep if available
        1. If there are no fitting tags, add just the tag `random` and let the user know about that. Propose some options as well.
    1. Do not alter the text nor skip any parts, just reformat it fully into the repository format, modifying just the formatting if needed
    1. Make sure to format any lists as proper markdown lists
1. Verify that no parts of the description were omitted.
1. Run `uv run mkdocs serve --strict` to verify the site builds correctly
1. If everything went well, remove the downloaded page content

