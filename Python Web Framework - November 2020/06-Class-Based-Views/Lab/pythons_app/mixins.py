from django.shortcuts import render


class GroupRequiredMixin:
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        all_user_groups = {group.name for group in request.user.groups.all()}

        if len(all_user_groups.intersection(self.group_required)) <= 0 and not request.user.is_superuser:
            return render(request, 'unauthorized.html')

        return super().dispatch(request, *args, **kwargs)
