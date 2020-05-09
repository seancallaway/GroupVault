from django import template

register = template.Library()


def build_limb(folders):
    output = ''
    for folder in folders:
        if not folder.sub_folders.all():
            output += f'<li><a href="#">{folder.name}</a></li>\n'
        else:
            output += f'<li><a href="#">{folder.name}</a>\n<ul>\n'
            output += build_limb(folder.sub_folders.all())
            output += '</ul>\n</li>\n'

    return output


@register.filter(is_safe=True)
def tree_list(value):
    if value:
        return build_limb(value)
    else:
        return '<p>There are no folders here.</p>\n<p>An admin needs to create at least one root folder.</p>'
