from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives


class Home(TemplateView):
    template_name = 'index.html'

    def post(self, request):

        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email = 'khester.company@gmail.com'
        subject1 = f'{subject}'
        from_email = request.POST.get('email')
        text_content = ''
        html_content = ''

        html_content += f'''<h1>Здравстуйте, я {name},
        (сообщение: {message}), (email: {from_email})</h1>'''
        msg = EmailMultiAlternatives(
            subject1, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        email = request.POST.get('email')
        subject = 'Ваше письмо доставлено!'
        from_email = request.POST.get('email')
        text_content = ''
        html_content = ''

        html_content += f'''<h1>Привет! Ваше письмо:"{subject1}" было успешно получено, мы ответим Вам уже совсем скоро!</h1>'''
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return redirect('index')
