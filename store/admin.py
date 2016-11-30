from django.contrib import admin
from store.models import Book, Buty

# Login : Admin         |  All
# Password zaq12wsx     |

# Login : Michau        |  Books
# Password : zaq12wsx   |

# Login : Michau        |  Buty
# Password : zaq12wsx   |


class bookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date", "price", "stock")

class butyAdmin(admin.ModelAdmin):
    list_display = ("brand", "name", "description", "size", "price")

admin.site.register(Book,bookAdmin)
admin.site.register(Buty,butyAdmin)
