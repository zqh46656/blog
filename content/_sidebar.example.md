
    {% set groups = ['tag', 'archive', 'author'] %}
{% for group in groups %}

##### {{group}}s

{% for name, items in group(kind=group) -%}
- [{{name}}]({{group}}-{{name | slugify}}.html)
{% endfor %}

{% endfor %}

#### Streams

{% for name, items in group(kind='stream') -%}

- [{{name}}]({{name | slugify}}.html)

{% endfor %}

