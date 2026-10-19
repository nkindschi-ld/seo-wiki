# GitHub Docs — Searching for repositories (+ topic rules)

Source: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
Secondary: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics (topic rules only; see end of file)
Author: GitHub (first-party documentation)
Published: undated living documentation
Type: official platform documentation
Retrieved: 2026-10-19

Note: added by Claude during the GitHub SEO ingest (2026-10-19) with the user's go-ahead, as first-party verification of practitioner claims. Example-query tables flattened in conversion.

# Searching for repositories

You can search for repositories on GitHub and narrow the results using these repository search qualifiers in any combination.

## In this article

You can search for repositories globally across all of GitHub, or search for repositories within a particular organization. For more information, see About searching on GitHub.

To include forks in the search results, you will need to add `fork:true` or `fork:only` to your query. For more information, see Searching in forks.

Tip

- This article contains links to example searches on the GitHub.com website, but you can use the same search filters in any GitHub platform. In the linked example searches, replace `github.com` with the hostname for your GitHub platform.
- For a list of search syntaxes that you can add to any search qualifier to further improve your results, see Understanding the search syntax.
- Use quotations around multi-word search terms. For example, if you want to search for issues with the label "In progress," you'd search for `label:"in progress"`. Search is not case sensitive.

## Search by repository name, description, or contents of the README file

With the `in` qualifier you can restrict your search to the repository name, repository description, repository topics, contents of the README file, or any combination of these. When you omit this qualifier, only the repository name, description, and topics are searched.

QualifierExample

`in:name`**jquery in:name** matches repositories with "jquery" in the repository name.

`in:description`**jquery in:name,description** matches repositories with "jquery" in the repository name or description.

`in:topics`**jquery in:topics** matches repositories labeled with "jquery" as a topic.

`in:readme`**jquery in:readme** matches repositories mentioning "jquery" in the repository's README file.

`repo:owner/name`**repo:octocat/hello-world** matches a specific repository name.

## Search based on the contents of a repository

You can find a repository by searching for content in the repository's README file using the `in:readme` qualifier. For more information, see About the repository README file.

Besides using `in:readme`, it's not possible to find repositories by searching for specific content within the repository. To search for a specific file or content within a repository, you can use the file finder or code-specific search qualifiers. For more information, see Finding files on GitHub and Understanding GitHub Code Search syntax.

QualifierExample

`in:readme`**octocat in:readme** matches repositories mentioning "octocat" in the repository's README file.

## Search within a user's or organization's repositories

To search in all repositories owned by a certain user or organization, you can use the `user` or `org` qualifier.

QualifierExample

`user:USERNAME`**user:defunkt forks:>100** matches repositories from @defunkt that have more than 100 forks.

`org:ORGNAME`**org:github** matches repositories from GitHub.

## Search by repository size

The `size` qualifier finds repositories that match a certain size (in kilobytes), using greater than, less than, and range qualifiers. For more information, see Understanding the search syntax.

QualifierExample

`size:n`**size:1000** matches repositories that are 1 MB exactly.

`size:>n`**size:>=30000** matches repositories that are at least 30 MB.

`size:<n`**size:<50** matches repositories that are smaller than 50 KB.

`size:n..n`**size:50..120** matches repositories that are between 50 KB and 120 KB.

## Search by number of followers

You can filter repositories based on the number of users who follow the repositories, using the `followers` qualifier with greater than, less than, and range qualifiers. For more information, see Understanding the search syntax.

QualifierExample

`followers:>=n`**node followers:>=10000** matches repositories with 10,000 or more followers mentioning the word "node".

`followers:n..n`**styleguide linter followers:1..10** matches repositories with between 1 and 10 followers, mentioning the word "styleguide linter."

## Search by number of forks

The `forks` qualifier specifies the number of forks a repository should have, using greater than, less than, and range qualifiers. For more information, see Understanding the search syntax.

QualifierExample

`forks:n`**forks:5** matches repositories with only five forks.

`forks:>n`**forks:>=205** matches repositories with at least 205 forks.

`forks:<n`**forks:<90** matches repositories with fewer than 90 forks.

`forks:n..n`**forks:10..20** matches repositories with 10 to 20 forks.

## Search by number of stars

You can search repositories based on the number of stars the repositories have, using greater than, less than, and range qualifiers. For more information, see Saving repositories with stars and Understanding the search syntax.

QualifierExample

`stars:n`**stars:500** matches repositories with exactly 500 stars.

`stars:n..n` `size:<n`**stars:10..20 size:<1000** matches repositories 10 to 20 stars, that are smaller than 1000 KB.

`stars:>=n` `fork:true` `language:LANGUAGE`**stars:>=500 fork:true language:php** matches repositories with the at least 500 stars, including forked ones, that are written in PHP.

## Search by when a repository was created or last updated

You can filter repositories based on time of creation or time of last update. For repository creation, you can use the `created` qualifier; to find out when a repository was last updated, you'll want to use the `pushed` qualifier. The `pushed` qualifier will return a list of repositories, sorted by the most recent commit made on any branch in the repository.

Both take a date as a parameter. Date formatting must follow the ISO8601 standard, which is `YYYY-MM-DD` (year-month-day). You can also add optional time information `THH:MM:SS+00:00` after the date, to search by the hour, minute, and second. That's `T`, followed by `HH:MM:SS` (hour-minutes-seconds), and a UTC offset (`+00:00`).

When you search for a date, you can use greater than, less than, and range qualifiers to further filter results. For more information, see Understanding the search syntax.

QualifierExample

`created:<YYYY-MM-DD`**webos created:<2011-01-01** matches repositories with the word "webos" that were created before 2011.

`pushed:>YYYY-MM-DD`**css pushed:>2013-02-01** matches repositories with the word "css" that were pushed to after January 2013.

`pushed:>=YYYY-MM-DD` `fork:only`**case pushed:>=2013-03-06 fork:only** matches repositories with the word "case" that were pushed to on or after March 6th, 2013, and that are forks.

## Search by language

You can search repositories based on the language of the code in the repositories.

QualifierExample

`language:LANGUAGE`**`rails language:javascript`** matches repositories with the word "rails" that are written in JavaScript.

## Search by topic

You can find all of the repositories that are classified with a particular topic. For more information, see Classifying your repository with topics.

QualifierExample

`topic:TOPIC`**`topic:jekyll`** matches repositories that have been classified with the topic "Jekyll."

## Search by number of topics

You can search repositories by the number of topics that have been applied to the repositories, using the `topics` qualifier along with greater than, less than, and range qualifiers. For more information, see Classifying your repository with topics and Understanding the search syntax.

QualifierExample

`topics:n`**topics:5** matches repositories that have five topics.

`topics:>n`**topics:>3** matches repositories that have more than three topics.

## Search by license

You can search repositories by the type of license in the repositories. You must use a license keyword to filter repositories by a particular license or license family. For more information, see Licensing a repository.

QualifierExample

`license:LICENSE_KEYWORD`**license:apache-2.0** matches repositories that are licensed under Apache License 2.0.

## Search by repository visibility

You can filter your search based on the visibility of the repositories. For more information, see About repositories.

QualifierExample

`is:public`**is:public org:github** matches public repositories owned by GitHub.

`is:private`**is:private pages** matches private repositories that you can access and contain the word "pages."

## Search based on repository custom property

You can filter repositories based on custom properties using the `props.` prefixed qualifiers. For more information, see Managing custom properties for repositories in your organization.

For these qualifiers to work, the search must be limited to a single organization. Otherwise, `props.` qualifiers are ignored.

QualifierExample

`props.PROPERTY:VALUE`**org:github props.environment:production** matches repositories from the `github` organization that have the custom property `environment` set to `production`.

## Search based on whether a repository is a mirror

You can search repositories based on whether the repositories are mirrors and hosted elsewhere. For more information, see Finding ways to contribute to open source on GitHub.

QualifierExample

`mirror:true`**mirror:true GNOME** matches repositories that are mirrors and contain the word "GNOME."

`mirror:false`**mirror:false GNOME** matches repositories that are not mirrors and contain the word "GNOME."

## Search based on whether a repository is a template

You can search repositories based on whether the repositories are templates. For more information, see Creating a template repository.

QualifierExample

`template:true`**template:true GNOME** matches repositories that are templates and contain the word "GNOME".

`template:false`**template:false GNOME** matches repositories that are not templates and contain the word "GNOME".

## Search based on whether a repository is archived

You can search repositories based on whether or not the repositories are archived. For more information, see Archiving repositories.

QualifierExample

`archived:true`**archived:true GNOME** matches repositories that are archived and contain the word "GNOME."

`archived:false`**archived:false GNOME** matches repositories that are not archived and contain the word "GNOME."

## Search based on number of issues with `good first issue` or `help wanted` labels

You can search for repositories that have a minimum number of issues labeled `help-wanted` or `good-first-issue` with the qualifiers `help-wanted-issues:>n` and `good-first-issues:>n`. For more information, see Encouraging helpful contributions to your project with labels.

QualifierExample

`good-first-issues:>n`**good-first-issues:>2 javascript** matches repositories with more than two issues labeled `good-first-issue` and that contain the word "javascript."

`help-wanted-issues:>n`**help-wanted-issues:>4 react** matches repositories with more than four issues labeled `help-wanted` and that contain the word "React."

## Search based on ability to sponsor

You can search for repositories whose owners can be sponsored on GitHub Sponsors with the `is:sponsorable` qualifier. For more information, see About GitHub Sponsors.

You can search for repositories that have a funding file using the `has:funding-file` qualifier. For more information, see Displaying a sponsor button in your repository.

QualifierExample

`is:sponsorable`**is:sponsorable** matches repositories whose owners have a GitHub Sponsors profile.

`has:funding-file`**has:funding-file** matches repositories that have a FUNDING.yml file.

## Search based on deployment context

If your organization has added records to the linked artifacts page, you can use this data to filter lists of repositories, such as the organization's "Repositories" page. For more information, see About linked artifacts.

QualifierDescription

`deployable:true`There is an active **storage record** for the repository in the linked artifacts page.

`deployed:true`There is an active **deployment record** for the repository in the linked artifacts page.

---

## Excerpt — "Classifying your repository with topics" (retrieved 2026-10-19)

Topic rules as stated on the page:
- "Add no more than 20 topics."
- "Use lowercase letters, numbers, and hyphens."
- "Use 50 characters or less."
- "To browse the most used topics, go to github.com/topics/."
- "You can contribute to GitHub's set of featured topics" (via the github/explore repository).
- Clicking a topic shows related topics and other repositories with that topic.
