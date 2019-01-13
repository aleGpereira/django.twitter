
# Documentation

**Example Django project connected to twitter. ReactJS front-end available.**

# Overview

This is a sample Django project to get data from a twitter account. Also gives *ReactJS* and classic template front-end support.

# How to use

Once the repository is cloned, run migrations commands:

    cd django
    ./manage.py makemigrations
    ./manage.py migrate

Then run the server:

    ./manage.py runserver

In your browser you can go to `localhost:8000/tweets_list` to get your current stored tweets. No tweets will be available in first time access.

An api is defined to manage tweets. Current endpoints are:

* `/tweets`
* `/tweets/update`

All will respond in a JSON format. If we access them through the browser it will open a `django-rest-framework` default view that it'll contain the response. The endpoint `/tweets/update`  will fetch more tweets.

You can access them locally by:
    
* `localhost:8000/api/v1/tweets`
* `localhost:8000/api/v1/tweets/update`

Twitter account must be configured in `django/twitter_stuff/settings.py`. The constant that need to be modified is `TWITTER_SETTINGS`. The same must be a tuple with the keys (same order):

* api_key.
* api_secret_key
* access_token
* access_token_secret

These keys are provider by setting an app in your twitter account. If you don't have an app configured, please follow the steps described [here](https://python-twitter.readthedocs.io/en/latest/getting_started.html#create-your-app).

# ReactJS front end

Default configuration is layered with a base `webpack.base.config.js` and a local `webpack.local.config.js` configuration files. The ReactJS entry is set as `TwitterStuff`. Bundles will be stored at `django/twitter_stuff/static/bundles/local/`. The template that will load `TwitterStuff` to render a list of tweets is at `django/twitter_stuff/templates/tweets_list.html`.

There's also a default django view which uses the `django/twitter_stuff/templates/hello.html` template.

All ReacjJS related files are keeped at `django/reactjs`.

# Tests

Only the django app `tweets` is under tests. To run them just do:

    cd django
    ./manage.py test

Once tests ran, the result will show in terminal. Also, a `cover` folder will be created. The same contains a html report with the tests and code coverage results. You can display it by opening the `cover/index.html` file in a browser.


# Requeriments

* django 1.9.3
* django-webpack-loader 0.2.4
* python-twitter 3.5
* djangorestframework 3.6.4
* django-nose 1.4.3 or higher
* coverage 4.5.2 or higher
* mock 2.0.0