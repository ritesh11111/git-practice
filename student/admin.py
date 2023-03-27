from django.contrib import admin
from . models import student ,MemberCommunicationType
# Register your models here.
@admin.register(MemberCommunicationType)
class Studentadmin(admin.ModelAdmin):
 list_display=['id','communication_type','subject','pn_title','template_used','enable_bcc_emails',
                  'enable_cc_emails','utm_params','send_as_async','moengage_msg','gamooga_msg','konotor_msg',
                  'deeplink','campaign_name','enable_pn_max','email_template1','email_template2','sms_template',
                  'pn_template','send_email','send_sms','sms_provider','send_pn','send_whatsapp_message',
                  'whatsapp_template_name','email_html_template','variables_used','utm_params_pn','utm_params_sms']