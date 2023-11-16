---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about_cust.biography
    id: about
    content:
      title: About me
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block:
    id: news
    content:
      title: Recent news
      subtitle: "[All news>>](/news)"
      text: |-
        {{< readfromfile "/content/newslist.dat" 5 >}}
    design:
      columns: '2'
      spacing:
        padding: 30px 0 30px 0;
  - block: people
    content:
      title: Meet the Team
      subtitle: "Note: I have recently acquired more funding, for 2 postdocs and 2 more PhD students. Stay tuned for recruitment ads!"
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Postdocs
          - PhD Students
          - Administration
          - Researchers
          - Visitors
          - Alumni
      sort_by: Params.user_groups
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: false
      columns: '2'
---