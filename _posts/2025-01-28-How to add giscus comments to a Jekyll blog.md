---
layout: post
author: ProbablyIdiot
mainTitle: BlogZilla rc1-2025.01.01
mainIco: /assets/images/w98-icons/executable_script-0.png
---

This is actually quite easy, but there are a few steps required before just adding the code to your web page. 

### Step 1 - Enable GH discussions

The way that giscus works is by creating GitHub discussion posts for each page and then displaying that discussion on the webpage. To enable GH discussions, head to your repo's settings page, and scroll down to the features section. From there, simply enable discussions.

![](/assets/postImages/GHdiscussSetup.png)

You may want to clear out the extra categories here, but make sure you leave at least one announcements channel, as that's what you'll want to use for giscus.

### Step 2 - Generate giscus code

Head to the [giscus website](https://giscus.app/) and follow the instructions there. Then select the discussion category as the announcements one you setup earlier and copy the code.

### Step 3 - Insert into blog

Now, head to your website's code, and scroll to the bottom of your posts template. Here, insert the code you generated earlier, and you're good to go! Hope this helped, make sure to leave a comment if so.
