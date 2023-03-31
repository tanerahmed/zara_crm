from django.contrib import admin
from .models import User, Company, Client, Distributors, Sold, Product, Article
from django.contrib.auth.admin import UserAdmin


class CompanyAdmin(admin.ModelAdmin):
    list_per_page = 15

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Избери Компания за промяна.'}
        return super(CompanyAdmin, self).changelist_view(request, extra_context=extra_context)

    list_display = ('name', 'address', 'category', 'work_with_us')
    list_filter = ('category', 'work_with_us', 'address')


class ClientAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Избери Клиент за промяна.'}
        return super(ClientAdmin, self).changelist_view(request, extra_context=extra_context)
    list_display = ('first_name', 'last_name', 'birthday')


class SoldAdmin(admin.ModelAdmin):
    list_per_page = 10
    # list_max_show_all = 5
    list_display = ('company_buyer', 'product', 'items', 'sold_price',
                    'delivery_price', 'profit', 'date_custom', 'we_delivered', 'sold')
    readonly_fields = ('profit',)
    list_filter = ('product', 'created_at', 'sold', 'we_delivered', 'company_buyer__name',)
    list_editable = ("sold",)

    def date_custom(self, obj):
        return obj.created_at.strftime("%d.%m.%Y ")
    # date_custom.admin_order_field = 'timefield'
    date_custom.short_description = 'Date'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_address')
    list_filter = ('company',)


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Distributors)
admin.site.register(Product)
admin.site.register(Sold, SoldAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.site_header = 'Zara Computers'
