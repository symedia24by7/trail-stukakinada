from django.shortcuts import render, redirect
import smtplib
from django.contrib import messages
# Create your views here.


def raiseIssue(request):
    TO = "beautiful19900g@gmail.com"
    SUBJECT = "STUKAKINANDA Issue From User"
    if request.method == "POST":
        issue_title = request.POST["issue_title"]
        issue_body = request.POST["issue_body"]
        issue_contact = request.POST["issue_contact"]

        if issue_body and issue_title and issue_contact:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login('symedia24by7@gmail.com', 'mjrzzmuwpwcswevd')
            message = "Issue Title: " + issue_title + "\n" + "Issue Body: " + issue_body + "\n" + "Sent From: " + issue_contact
            BODY = '\r\n'.join(['To: %s' % TO,
                               'From: symedia24by@gmail.com',
                               'Subject: %s' % SUBJECT,
                               '', message])
            s.sendmail('symedia24by7@gmail.com',TO, BODY)
            s.quit()
            messages.success(request, "Issue Sent!")
            return render(request, "issues.html")
    else:
        return redirect("issue")


def issues(request):
    return render(request, 'issues.html')
