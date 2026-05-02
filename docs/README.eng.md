# dream-tracker
A simple social platform for recording and tracking sleep quality and the narratives experienced during rapid eye movement dreaming.

Read the [seed-report](/docs/seed_report.eng.md)

## Functionality
Users can
- create an account and sign in
- create new posts, and edit or delete their own posts
- view their own posts as well as posts by other users
- follow other users, receiving their posts in their feeds
- set visibility rules for each of their posts (e.g. public, private, followers only)
- assign apt categories to their own posts
- search for posts using search queries, categories and/or statistics
- view users' profile pages, which display the user's posts and some statistics
- reply to and like posts

## Notable potential improvements

A few notable improvements are possible:
- CSRF vulnerabilities should ideally be prevented in registration and sign-in forms as well. The rule of thumb is that any POST method should check the secret CSRF token.
- A marginal improvement to the usability of the site could be attained by displaying error messages on the pages that raise them, instead of redirecting to a dedicated error page. This is considered a low-priority improvement.
- Hyperlinks could be displayed in a clearer manner. The developer considers the usability of the site to be intuitive enough with the current layout and styling.
- Line breaks (and other markdown-style rendering) is only supported on post pages, and not, for instance, on the front page, user pages or comments. This is considered intentional behavior, since only the full post body is intended to be long enough for line breaks. 
- Comments on private or friends-only posts are public for all to see on the commenter's user page. However, this is not considered a critical issue, since only the title and comment content are visible (not, say, any post data or the post body itself).
- Like counting can be effectivized by methods outlined in the [seed report](/docs/seed_report.eng.md).

# Installation

1. Clone the repository and navigate to its directory with a terminal of your choice
2. Install `flask`:

```
$ pip install flask
```

or as a self-contained virtual environment

```
$ python -m venv venv
$ venv/bin/activate
$ pip install flask
```

3. Start the server and navigate to `localhost:5000` with a browser of your choice

```
$ flask run
```

The app will initialize the database and any configurations automatically.