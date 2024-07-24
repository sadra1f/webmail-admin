from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from panel.models import EmailAccount


@admin.register(EmailAccount)
class EmailAccountAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    list_display = ["user", "view_in_roundcube"]

    @admin.display(description="Roundcube")
    def view_in_roundcube(self, obj):
        return format_html(
            """
                <button
                    type="button"
                    class="admin-action-submit"
                    onclick="POSTRedirect(
                        {{
                            'action': '{}',
                            'method': 'post',
                            'target': '_blank'
                        }},
                        {{ '_user': '{}', '_pass': '{}' }}
                    )"
                >
                    <span> View in Roundcube </span>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25
                            21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21
                            3v5.25"
                        />
                    </svg>
                </button>
            """,
            settings.ROUNDCUBE_LOGIN_URL,
            obj.user,
            obj.password,
        )
