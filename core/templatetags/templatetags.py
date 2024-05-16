from django import template

register = template.Library()

@register.filter
def generate_stars(rating):
    filled_stars = rating
    empty_stars = 5 - rating
    stars = ''

    for i in range(filled_stars):
        stars += '<i class="fa-solid fa-star" style="color: #ffaa00;"></i>'

    for i in range(empty_stars):
        stars += '<i class="fa-regular fa-star" style="color: #ffaa00;"></i>'

    return stars