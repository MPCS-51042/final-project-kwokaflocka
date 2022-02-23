    #   <!-- {% for key, value in recipe.items() %}
    #     <article class="media content-section">
    #       <div class="media-body">
    #         <div class="article-metadata">
    #           <a class="mr-2" href="#">{{ recipe.key }}</a>
    #         </div>
    #         {% for key2, value2 in value.items() %}
    #         <h2><a class="article-title" href="#">{{ value.key2 }}</a></h2>
    #         <p class="article-content">{{ value.value2 }}</p>
    #       </div>
    #   </article>
    #         {% endfor %}
    #   {% endfor %} -->

    # <article class="media content-section">
    #            <div class="media-body">
    #              <div class="article-metadata">
    #                <a class="mr-2" href="#">{{ recipe.key }}</a>
    #              </div>
    #              {% for key2, value2 in value.items() %}
    #              <h2><a class="article-title" href="#">{{ value.key2 }}</a></h2>
    #              <p class="article-content">{{ value.value2 }}</p>
    #            </div>
    #        </article>