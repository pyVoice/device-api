# admin CSV exporter
def download_csv(self, request, queryset):
    import csv
    from io import StringIO
    from django.http import HttpResponse

    f = StringIO()
    writer = csv.writer(f)
    writer.writerow(
        ['id', 'device_id', 'version', 'location', 'operating_system'])
    for s in queryset:
        writer.writerow([s.id, s.device_id, s.version, s.location, s.operating_system])

    f.seek(0)
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=devices.csv'
    return response
