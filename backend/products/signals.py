from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from algoliasearch_django import raw_search
from algoliasearch_django import algolia_engine
from .models import Product


# def index_to_algolia(self):
#     index = algolia_engine.client.init_index("cfe_Product")
#     index.save_object(
#         {
#             "objectID": self.pk,
#             "title": self.title,
#             "content": self.content,
#             "price": str(self.price),
#             "public": self.public,
#             "user": self.user.id if self.user else None,
#             "tags": self.get_tags_list(),
#         }
#     )


# def remove_from_algolia(self):
#     index = algolia_engine.client.init_index("your_index_name")
#     index.delete_object(self.pk)


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, **kwargs):
    instance.index_to_algolia()


@receiver(post_delete, sender=Product)
def post_delete_product(sender, instance, **kwargs):
    instance.remove_from_algolia()
