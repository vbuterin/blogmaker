# Blogmaker

This is an ultra-simple self-hosted blog publishing solution.

### Dependencies

* pandoc
* rsync

### How to use

See the [posts](./posts) directory for what a post should look like. Posts must be written in [markdown](https://daringfireball.net/projects/markdown/syntax), and filenames must end in ".md". Dates must be in (yyyy/mm/dd) format. All posts must be in the posts directory.

If you need a post to use MathJaX to format LaTeX equations, add the line

```
[pandoc]: <> (--mathjax)
```

to the config at the top of the post.

To compile a post to html, run `./publish.py posts/name_of_post.md` (or `./publish.py posts/*` to recompile everything). Use `./publish.py --sync` to upload the latest version of your site to your server (make sure to put your server details, as well as the site title and icon, in [config.md](./config.md)).

For the server, the simplest setup is to use any VPS, `apt install apache2`, make sure apache2 is running, and just set the directory to /var/www/html.

### Misc

Credit to https://hackmd.io for CSS styles.
