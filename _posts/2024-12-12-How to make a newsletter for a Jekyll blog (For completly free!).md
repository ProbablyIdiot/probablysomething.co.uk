---
layout: post
author: ProbablyIdiot
mainTitle: BlogZilla beta2-2024.08.14
mainIco: /assets/images/w98-icons/executable_script-0.png
---

This is one of the most overly complex and undocumented jekyll problems I've come across so far (apart from pagination - but I try to block that out of my memory). I'll try to make this short and easy to follow, but no promises.

### Step 1 - Install `jekyll-feed`

You might think "Why would I want an RSS feed? I want a newsletter!". However, this is the simplest way of doing it. At the moment there are no plugins or tutorials for directly sending emails from your jekyll site (or none that I could find), therefore, the easiest way to make a newsletter is to copy your RSS feed.

Just follow the instructions on the [jekyll-feed Github](https://github.com/jekyll/jekyll-feed) to install the plugin, and check that it works by going to `yoururl.com/feed.xml`. If it worked, you should see something like this, with the text containing all blog posts you have previously made.![](/assets/postImages/feedXml.png)

### Step 2 - Setup a mailing website to mirror your RSS feed

This is the step that has taken forever to figure out. The most popular option for setups like this is [Intuit Mailchimp](https://mailchimp.com), however, they can get quite pricey and I prefer something open-source. At first I tried the [RSS2Newsletter]([GitHub - ElliotKillick/rss2newsletter: Convert RSS/Atom feed to email newsletters](https://github.com/ElliotKillick/rss2newsletter)) project, however I could not manage to get it to install on my raspberry pi. I then spent ages looking through google for a free alternative. This is when I stumbled upon [rssto.email](https://rssto.email). A FOSS project hosted on Github that will convert any RSS feed into a newsletter and deliver it straight to your inbox. They have a simple user interface, and allow you to embed a link for your RSS feed straight into your blog. This can be annoying to setup, however, so look at step 3 for how to do that.

### Step 3 - Setting up a link for `rssto.email`

Head to their website, and click the EMBED ON YOUR BLOG button. Input the link to your RSS feed and then copy the link.

![](/assets/postImages/rssToEmail.png)

Then use this code (replacing `yourURL.com` with the link you copied) to create a newsletter button on your blog:

```html
<form action="https://rssto.email" method="GET" target="_blank">
    <input type="hidden" name="url" value="yourURL.com">
    <button type="submit">Sign up to the newsletter!</button>
</form>
```

There you go! You should now have a fully functional newsletter for your users to keep up with all your blog posts. My next blog should be on adding comments, so keep an eye out for that.
