from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.contrib import messages
from geopy.geocoders import Nominatim
import folium
from route.getroute import get_route


def index(request):
    if request.method == 'POST' and 'btn1' in request.POST:
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

    elif request.method == 'POST' and 'btn2' in request.POST:
        if HttpResponse.status_code == 200:
            from_country = request.POST.get("from_country")
            from_city = request.POST.get("from_city")
            from_street = request.POST.get('from_street')
            to_country = request.POST.get("to_country")
            to_city = request.POST.get("to_city")
            to_street = request.POST.get('to_street')
            app = Nominatim(user_agent='test')
            try:
                from_location = app.geocode(f"{from_street},{from_city}, {from_country}").raw
                to_location = app.geocode(f"{to_street},{to_city}, {to_country}").raw
                # print raw data
                figure = folium.Figure()
                lat1,long1,lat2,long2=float(from_location['lat']),float(from_location['lon']),float(to_location['lat']),float(to_location['lon'])
                route = get_route(long1,lat1,long2,lat2)
                m = folium.Map(location=[(route['start_point'][0]),
                                            (route['start_point'][1])], 
                                zoom_start=10)
                m.add_to(figure)
                folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
                figure.render()
                context={'map':figure}
                return render(request,'route/showroute.html',context)
            except:
                messages.error(request, 'Введите правильные данные')
                return render(request, 'index.html')
        else:
            return render(request, 'index.html')

    return render(request, 'index.html')