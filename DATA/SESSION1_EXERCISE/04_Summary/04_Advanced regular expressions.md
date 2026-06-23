# Advanced regular expressions

Type: Article

Here you will find some useful regular expressions. Apart from this, do experiment with [https://regex101.com/](https://regex101.com – on the right a detailed explanation of how the computer understood your regex is displayed - this makes it much easier to look for errors.

## Useful regexes

- `\d+` - a number (at least one digit)
- `\d+[,.]\d+` - a number with a comma (or a dot)
- `[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}` - simplified regex for finding email addresses
- `https?:\/\/[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#()?&//=]*)` - URL addresses (with an `http` or `https` prefix)
- `[12]\d{3}-\d{1,2}-\d{1,2}` - YEAR-MONTH-DAY formatted date
- `\d{1,2}\.\d{1,2}\.\d{4}` - DAY.MONTH.YEAR formatted date
- `[^/\\]+\.[a-zA-Z0-9]{3}` - filename with a 3-character extension (eg. `.jpg`)
