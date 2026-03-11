---
layout: page
title: 🏢 Weekly OH
description: The weekly event schedule.
nav_order: 2
---

{: .warning }
⚠️ This content is archived as of March 2026 and is retained exclusively for reference. [Find current offerings.](https://data8.org/)

# **Weekly Office Hours**

We use an [online sign-up system](https://oh.data8.org/) to help keep track of everyone.

{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}
