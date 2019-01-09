from django.core.management import BaseCommand

from base import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('---------------------------------------')
        print('Generating tags...')
        print('---------------------------------------')

        def create_tags(tags, type, parent):
            for tag in tags:
                tag_obj = models.Tag.objects.create(name=tag['name'], type=type, parent=parent)

                if tag.get('synonyms'):
                    for synonym in tag['synonyms']:
                        models.Synonym.objects.create(name=synonym, type=type, master=tag_obj)

                if tag.get('children'):
                    create_tags(tag['children'], type, tag_obj)


        regions = ({
            'name': 'russia', 'synonyms': ('russian-federation',), 'children': ({
                'name': 'bashkortostan', 'children': (
                    {'name': 'ufa'},
                    {'name': 'salavat'},
                    {'name': 'belebey'},
                    {'name': 'neftekamsk'},
                ),
            }, {
                'name': 'tatarstan', 'children': (
                    {'name': 'kazan'},
                    {'name': 'bugulma'},
                    {'name': 'naberezhnye-chelny'},
                ),
            }, {
                'name': 'krasnodar', 'children': (
                    {'name': 'anapa'},
                    {'name': 'belorechensk'},
                    {'name': 'gelendzhik'},
                    {'name': 'sochi'},
                ),
            }),
        }, {
            'name': 'united-states', 'synonyms': ('usa','united-states-of-america'), 'children': ({
                'name': 'california', 'children': (
                    {'name': 'los-angeles'},
                    {'name': 'san-diego'},
                    {'name': 'san-francisco'},
                    {'name': 'sacramento'},
                    {'name': 'windsor'},
                ),
            }, {
                'name': 'florida', 'children': (
                    {'name': 'miami'},
                    {'name': 'orlando'},
                    {'name': 'tallahassee'},
                    {'name': 'palm-beach'},
                ),
            }),
        }, {
            'name': 'australia', 'children': ({
                'name': 'new-south-wales', 'children': (
                    {'name': 'newcastle'},
                    {'name': 'sydney'},
                    {'name': 'albury'},
                ),
            }, {
                'name': 'queensland', 'children': (
                    {'name': 'brisbane'},
                    {'name': 'gold-coast'},
                    {'name': 'logan'},
                    {'name': 'redcliffe-city'},
                ),
            }),
        })

        create_tags(regions, 'region', None)


        organisms = (
            {'name': 'animal', 'children': (
                {'name': 'chordate', 'children': (
                    {'name': 'reptile', 'children': (
                        {'name': 'turtle'},
                        {'name': 'lizard'},
                    )},

                    {'name': 'mammal', 'children': (
                        {'name': 'cat'},
                        {'name': 'dog'},
                        {'name': 'chimpanzee'},
                    )},

                    {'name': 'bird', 'children': (
                        {'name': 'pigeon'},
                        {'name': 'parrot'},
                    )},

                    {'name': 'amphibia', 'children': (
                        {'name': 'frog'},
                        {'name': 'salamander'},
                    )},
                )},

                {'name': 'arthropod', 'children': (
                    {'name': 'arachnid', 'children': (
                        {'name': 'spider'},
                        {'name': 'scorpion'},
                    )},

                    {'name': 'insect', 'children': (
                        {'name': 'beetle'},
                        {'name': 'ladybug'},
                    )},
                )},
            )},
        )

        create_tags(organisms, 'organism', None)


        genres = (
            {'name': 'comedy'},
            {'name': 'drama'},
            {'name': 'epic'},
            {'name': 'romance'},
            {'name': 'satire'},
            {'name': 'tragedy'},
            {'name': 'tragicomedy'},
        )

        create_tags(genres, 'genre', None)


        occupations = (
            {'name': 'historian'},
            {'name': 'philosopher'},
            {'name': 'mathematician'},
            {'name': 'programmer', 'synonyms': ('coder','developer')},
            {'name': 'scientist'},
            {'name': 'accountant'},
            {'name': 'physicist'},
            {'name': 'engineer'},

            {'name': 'artist', 'children': (
                {'name': 'musician'},
                {'name': 'actor'},
                {'name': 'dancer', 'synonyms': ('choreographer','ballet-dancer')},
                {'name': 'singer', 'synonyms': ('vocalist',)},
                {'name': 'painter'},
                {'name': 'sculptor'},
                {'name': 'photographer'},
            )},

            {'name': 'sportsman', 'children': (
                {'name': 'football-player'},
                {'name': 'tennis-player'},
                {'name': 'wrestler'},
                {'name': 'skier'},
            )},
        )

        create_tags(occupations, 'occupation', None)

        print('---------------------------------------')
        print('Done generating tags...')
        print('---------------------------------------')
