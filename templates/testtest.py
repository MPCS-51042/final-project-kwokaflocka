

    # {% for recipe, ingredients in recipes.items() %}
    #     <article class="media content-section">
    #       <div class="media-body">
    #         <div class="article-metadata">
    #           <a class="mr-2" href="#">{{ recipe }}</a>
    #         </div>
    #         <h2><a class="article-title" href="#">{{ recipe }}</a></h2>
    #           {% for ingredient, amount_unit in ingredients.items() %}
    #             <p class="article-content">{{ingredient}}: {{ amount_unit }}</p>
    #           {% endfor %}
    #       </div>
    #   </article>
    # {% endfor %}

    #  {% for recipe, ingredients in recipes.items() %}
    #   <div>{{ recipe }}</div>
    #   {% for ingredient, amount_unit in ingredients.items() %}
    #     <div>
    #       <span>{{ ingredient }}: {{ amount_unit }}</span>
    #     </div>
    #   {% endfor %}
    # {% endfor %}