```
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint, pformat

from . import models


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').strip()
        any = request.GET.get('any') == 'on'

        tag_pair_strings = query.split()
        tag_pairs = tuple(map(lambda tag_pair: tag_pair.split(':'), tag_pair_strings))

        tags = set()
        synonyms = set()
        not_found = None

        for tag_pair in tag_pairs:
            found_tags = models.Tag.objects.none()

            if len(tag_pair) == 2:
                if tag_pair[0] and tag_pair[1]:
                    found_tags = models.Tag.objects.filter(type__iexact=tag_pair[0], name__iexact=tag_pair[1])
                elif tag_pair[0]:
                    found_tags = models.Tag.objects.filter(type__iexact=tag_pair[0])
                elif tag_pair[1]:
                    found_tags = models.Tag.objects.filter(name__iexact=tag_pair[1])
            else:
                found_tags = models.Tag.objects.filter(name__iexact=tag_pair[0])

            for tag in found_tags:
                tags.add(tag)


            if len(tag_pair) == 2:
                found_synonyms = models.Synonym.objects.none()

                if tag_pair[0] and tag_pair[1]:
                    found_synonyms = models.Synonym.objects.filter(type__iexact=tag_pair[0], name__iexact=tag_pair[1])
                elif tag_pair[0]:
                    found_synonyms = models.Synonym.objects.filter(type__iexact=tag_pair[0])
                elif tag_pair[1]:
                    found_synonyms = models.Synonym.objects.filter(name__iexact=tag_pair[1])
            else:
                found_synonyms = models.Synonym.objects.filter(name__iexact=tag_pair[0])

            for synonym in found_synonyms:
                tags.add(synonym.master)
                synonyms.add(synonym)

            if not found_tags and not found_synonyms:
                not_found = True

        if any:
            notes = set()

            for tag in tags:
                notes.update(models.Note.objects.filter(
                    tags__lft__gte=tag.lft,
                    tags__rght__lte=tag.rght,
                    tags__tree_id=tag.tree_id,
                ))
        else:
            notes = models.Note.objects.all()

            if not_found:
                notes = notes.none()
            else:
                for tag in tags:
                    notes = notes.filter(
                        tags__lft__gte=tag.lft,
                        tags__rght__lte=tag.rght,
                        tags__tree_id=tag.tree_id,
                    )

                notes = notes.distinct()

            if not tags:
                notes = notes.none()

        return render(request, self.template_name, {
            'notes': notes,
            'query': query,
            'any': any,
            'tags': tags,
        })
```

```
<form style="display: flex; align-items: center; margin-bottom: 10px" action="{% url 'home' %}" method="GET" novalidate>
    <input style="flex-grow: 1; margin-right: 10px" type="text" name="q" value="{{ query }}">

    <label style="margin-right: 10px; white-space: nowrap; cursor: pointer">
        <input type="checkbox" name="any" {% if any %}checked {% endif %}> Any
    </label>

    <button type="submit">Find</button>
</form>

{% if notes|length > 0 %}
    <p style="margin-bottom: 20px; font-size: 18px; color: #999">
        {{ notes|length }} items found by {{ tags|length }} tags
    </p>

    <ul>
        {% for note in notes %}
            <li>
                <p>{{ note.name }}</p>

                <p style="font-size: 18px; color: #ccc">
                    {% for note_tag in note.tags.all %}
                        {% is_descendant_of_any note_tag tags as is_descendant %}

                        {% if note_tag in tags %}
                            <b style="color: #f90" title="{{ note_tag.type }}">{{ note_tag.name }}</b>
                        {% elif is_descendant %}
                            <span style="color: #eb8" title="{{ note_tag.type }}">{{ note_tag.name }}</span>
                        {% else %}
                            <span title="{{ note_tag.type }}">{{ note_tag.name }}</span>
                        {% endif %}
                    {% endfor %}
                </p>

                <br>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p style="margin-bottom: 20px; font-size: 18px; color: #999">
        {% if query == "" %}
            Type something into the search field
        {% else %}
            Nothing found [{{ tags|length }} tags]
        {% endif %}
    </p>
{% endif %}
```


---------------------------------------

## tags__id=17

{
    "count": 9,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2
        },
        {
            "id": 30
        },
        {
            "id": 32
        },
        {
            "id": 47
        },
        {
            "id": 57
        },
        {
            "id": 7
        },
        {
            "id": 71
        },
        {
            "id": 75
        },
        {
            "id": 90
        }
    ]
}

----------------------------------------
