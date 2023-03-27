from django.test import TestCase,Client
from . models import student,MemberCommunicationType
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase,APIClient
from rest_framework import status
# Create your tests here.

# class StudentTest(TestCase):
#     def test_name(self):
#         obj=student(name='ravi')
#         self.assertEquals(str(obj),'ravi')
#     def test_roll(self):
#         obj= student(roll="102")
#         self.assertEquals(obj.roll,"102")
#     def test_city_name(self):
#         obj=student(city="varansi")
#         self.assertEquals(obj.city,'varansi')    

# TEST URL OF DJANGO
# two methods
# class Test_Url(TestCase):  
    # def test_URL(self):
    #     response=self.client.get('/get_api')
    #     self.assertEquals(response.status_code,200)

    # def test_views(self):
    #     client=Client()
    #     response= self.client.get('/student/')
    #     self.assertEquals(response.status_code,200)

# API TESTING 

# class ApiTesting(APITestCase):
    # def test_api(self):
        
    #     response = self.client.get('/student/',format='json')
    #     self.assertAlmostEqual(response.status_code,status.HTTP_200_OK)
# class Api_testing(APITestCase):
#     def setUp(self):
#        self.client = Client()

#     def test_api_get(self):
#         student.objects.create(name='Himanshu', roll= "103", city="varanasi" )
#         response= self.client.get('/getpost')
#         self.assertEquals(response.status_code,status.HTTP_200_OK)
#         self.assertEquals(len(response.data),1)
#         self.assertEquals(response.data[0]['name'],'Himanshu')

class TestApi(TestCase):
    
    def setUp(self):
        self.client=APIClient()

    def test_post_request(self):
        data = {
             'communication_type':'oreder_delever',
             'subject': 'subject is here',
             'pn_title':'push notification',
             'template_used': 'this',
             'enable_bcc_emails': True,
             'enable_cc_emails': True,
             'utm_params' : 'this is utm para',
             'send_as_async':True,
             'moengage_msg':'yes',
             'gamooga_msg':'no',
             'konotor_msg':'konotor',
             'deeplink':'www.deep',
             'campaign_name':'campaign',
             'enable_pn_max': True,
             'email_template1':'this is template one',
             'email_template2':'this is template two',
             'sms_template':'sms',
             'pn_template':'pn',
             'send_email': True,
             'send_sms': True,
             'sms_provider': 3,
             'send_pn': True,
             'send_whatsapp_message': True,
             'whatsapp_template_name':'this is whatsapp template',
             'email_html_template':'email html field',
             'variables_used':'character',
             'utm_params_pn':'utm Push Notification',
             'utm_params_sms': 'utm sms',
        }
        response=self.client.post('/getpost',data,format='json')
        print(response.data)
        self.assertEquals(MemberCommunicationType.objects.get().communication_type,"oreder_delever")
        self.assertEquals(MemberCommunicationType.objects.get().utm_params_sms,"utm sms")
        self.assertEquals(MemberCommunicationType.objects.get().enable_pn_max,True)
        self.assertEquals(MemberCommunicationType.objects.get().send_sms, True)