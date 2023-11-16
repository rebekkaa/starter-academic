---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: All
          tag: '*'
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      view: showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
  - block: collection
    id: posts
    content:
      title: News
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: compact
      columns: '2'
  - block: people
    content:
      title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - PI
          - Postdocs
          - Researchers
          - PhD Students
          - Administration
          - Visitors
          - Alumni
      sort_by: Params.user_groups
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
  - block: accomplishments
    content:
      # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
      title: 'Accomplish&shy;ments'
      subtitle:
      # Date format: https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Accomplishments.
      #   Add/remove as many `item` blocks below as you like.
      #   `title`, `organization`, and `date_start` are the required parameters.
      #   Leave other parameters empty if not required.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - date_end: ''
          date_start: '2021-01-25'
          description: ''
          icon: coursera
          organization: Coursera
          organization_url: https://www.coursera.org
          title: Neural Networks and Deep Learning
          url: ''
        - date_end: ''
          date_start: '2021-01-01'
          description: Formulated informed blockchain models, hypotheses, and use cases.
          icon: edx
          organization: edX
          organization_url: https://www.edx.org
          title: Blockchain Fundamentals
          url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
        - date_end: '2020-12-21'
          date_start: '2020-07-01'
          description: ''
          icon: datacamp
          organization: DataCamp
          organization_url: https://www.datacamp.com
          title: 'Object-Oriented Programming in R'
          url: ''
    design:
      columns: '2'
      view: compact
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: All
          tag: '*'
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      view: showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: 5
  - block: collection
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation



  - block: markdown
    design:
      columns: '2'
    content:
      title: Research
      text: "I am interested in human-on-the-loop autonomous systems. These systems adapt their behavior or structure in response to changes in their environment. They commonly interact with humans. Self-adaptive systems make a lot of decisions autonomously. It is still desirable to involve humans and help them make decisions that are difficult to automate. Those decisions are often connected to tradeoffs, e.g., when deciding how much to prioritize different competing quality attributes (such as security, performance, and cost). It is often difficult for humans to understand the consequences of decisions and to specify decision criteria. When is it worth it to ramp up security features, although that might compromise performance? Those trade-offs depend on the current context of the system and what is desirable might change over time.

To address these issues, I create techniques to explain self-adaptive systems and to capture people’s (potentially changing) preferences. I also do empirical research to study these problems in large-scale industrial settings.

My research focuses on the following questions:

* How can we elicit preferences and goals that people deem important in self-adaptive systems? [[REFSQ 2021](/publication/wohlrab-2021-refsq/)[, REJ 2022](/publication/wohlrab-2021-rej/)]

* How can we improve the quality of self-adaptive systems and ensure that systems meet humans’ needs over time? [[SEAMS 2022]](/publication/wohlrab-2022-seams/)

* How can quality tradeoffs be explained to humans, so that it is easier to understand how self-adaptive systems behave? [[JSS 2023 (Wohlrab et al.)]](/publication/wohlrab-2023-jss/)

* How can systems be monitored to ensure that safety and security constraints are fulfilled, but so that we can reduce energy consumption and required bandwidth? [[CNS'22](/publication/vierhauser-2022-cns/)[, JSS 2023 (Vierhauser et al.)](/publication/vierhauser-2023-jss/)]

* How can human engineers in large organizations share knowledge effectively over time?
[[JSME 2019](/publication/wohlrab-2019-jsme/)[, ICSA 2019](/publication/wohlrab-2019-icsa-survey/)[, JSS 2020](/publication/wohlrab-2020-jss/)]"
  - block: markdown
    design:
      columns: '2'
    content:
      title: Accomplishments
      text: "
* [* ECSA'23 Best Paper Award*](https://rebekkaa.github.io/files/DiazPace2023-ECSA.pdf), co-authored with J. Andres Diaz-Pace and David Garlan.
* [Pedagogical Prize](https://www.medarbetarportalen.gu.se/internt-itufak/undervisning-pedagogik/pedagogiskt-pris/?languageId=100001)
* [*PROFES'19 Best Paper Award*](https://link.springer.com/chapter/10.1007/978-3-030-35333-9_26), co-authored with Jan-Philipp Steghöfer, Eric Knauss, and Jennifer Horkoff.
* [*ICSA'19 Best Paper Award*](https://ieeexplore.ieee.org/abstract/document/8703919),  co-authored with Ulf Eliasson, Patrizio Pelliccione, Rogardt Heldal.
* [*ICSSP'18 Best Paper Award*](https://dl.acm.org/doi/10.1145/3202710.3203155), co-authored with Patrizio Pelliccione, Eric Knauss, and Mats Larsson
"
---