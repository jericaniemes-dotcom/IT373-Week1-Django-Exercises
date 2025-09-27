from django.shortcuts import render

# Dummy data to render the template
ANNOUNCEMENTS = [
    {'id': 1, 'title': 'Welcome', 'content': 'Welcome to the announcements board!'},
    {'id': 2, 'title': 'Exam', 'content': 'Exam on Friday. Study hard!'},
]

def announcement_list(request):
    return render(request, 'announcements/list.html', {'announcements': ANNOUNCEMENTS})

def announcement_detail(request, pk):
    ann = next((a for a in ANNOUNCEMENTS if a['id'] == int(pk)), None)
    return render(request, 'announcements/detail.html', {'announcement': ann})
