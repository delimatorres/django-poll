from django.contrib import admin
from poll.models import Poll, Item, Queue, Vote, Choice
from django.utils.translation import ugettext_lazy as _


class PollItemInline(admin.TabularInline):
    model = Item
    max_num = 10
    fields = ('userbox', 'value', 'subtitle', 'index', 'vote_count',)
    readonly_fields = ('vote_count',)


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'queue', 'startdate', 'polltype', 'vote_count',
                    'publish')
    inlines = [
        PollItemInline,
    ]

    fieldsets = (
                 (None, {'fields': ('title',)}),
                 (_('Options'), {'fields': ('publish', 'polltype', 'queue',
                                            'startdate',)}),
                 )


class VoteChoiceItemInline(admin.TabularInline):
    model = Choice
    max_num = 10
    readonly_fields = ('item', 'uservalue')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'ip', 'user', 'datetime')
    list_filter = ('poll', 'datetime')
    inlines = [
        VoteChoiceItemInline,
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Queue, admin.ModelAdmin)
admin.site.register(Vote, VoteAdmin)
