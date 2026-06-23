# Exercise 1

Type: Exercise

# Exercise 1 – done with the lecturer

Open the [socialblade.com](https://socialblade.com/) website and find your favorite YouTuber. If you do not have one, you can use  [featony](https://socialblade.com/youtube/user/featony).

## Search for a bar with general statistics.

Use devtools to find an element where the `id` attribute has the value of `"YouTubeUserTopInfoBlock"`.

> **Hint:**
> 
> You can do this by going to the **Console** tab and typing the command:
> 
> 
> 
> ``` js
> document.querySelectorAll('#YouTubeUserTopInfoBlock');
> ```

How many elements were found?

## Search for the total number of displays

Use devtools to find a `<span>` tag containing the total number of views of all videos.

> **Hint:**
> 
> First find the number on the website, right-click and choose **Inspect element** – look at the element and its surroundings and try to write a selector that finds **only one `<span>` – the one that we seek**.

Useful selector syntax:

- `x > y` - find `y` tags that are children of `x` tags,
- `x:nth-child(99)` - find the `x` tags that **are** ninety-ninth children of their parents.

These syntaxes can be mixed, e.g. `x:nth-child(42) > y`.
