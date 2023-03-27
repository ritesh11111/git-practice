from django.db import models

# Create your models here.
class student(models.Model) :
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    
class MemberCommunicationType(models.Model):

    communication_type = models.CharField(max_length=100)
    # BB-18249 MemberCommunication Revamp changes
    # level-1 reasons
    subject = models.CharField(max_length=25, null=True, blank=True)
    pn_title = models.CharField(max_length=25, null=True, blank=True,
                                help_text="Push notification title used only for Unified channel")
    template_used = models.CharField(max_length=10, null=True, blank=True)
    enable_bcc_emails = models.BooleanField(
        default=False,help_text="If enabled, will send copy of email "
                                "to ADMIN email-ids mentioned in settings.py file. Don't enable"
                                "this for loyalty emails.")
    enable_cc_emails = models.BooleanField(
        default=True, help_text="If enabled, will send copy of email "
                                "to email ids provided in cc_email in bind_vars")
    utm_params = models.CharField(max_length=50, null=True, blank=True)
    send_as_async = models.BooleanField(default=False,
                                        help_text="If enabled, will send async mail using queue")
    moengage_msg = models.CharField(max_length=20, blank=True, null=True)
    gamooga_msg = models.CharField(max_length=20, blank=True, null=True)
    # konotor_msg field is deprecated
    konotor_msg = models.CharField(max_length=20, blank=True, null=True,
                                   help_text="Deprecated no need to provide this")
    deeplink = models.CharField(max_length=10, blank=True, null=True)
    pn_project = models.CharField( blank=True, null=True, max_length=50)
    campaign_name = models.CharField(max_length=25, blank=True, null=True)
    enable_pn_max = models.BooleanField(default=False, help_text="If enabled, any number of PNs can be send")

    # BB-18249 MemberCommunication Revamp changes
    # content to use in emails
    email_template1 = models.CharField(max_length=50, null=True, blank=True)
    email_template2 = models.CharField(max_length=50, null=True, blank=True)

    # content to use in sms
    sms_template = models.CharField(max_length=10, null=True, blank=True)

    # content to use in push notifications
    pn_template = models.CharField(max_length=10, null=True, blank=True)

    send_email = models.BooleanField(default=False)
    send_sms = models.BooleanField(default=False)
    sms_provider = models.IntegerField(null=True)
    send_pn = models.BooleanField(default=False)
    send_whatsapp_message = models.BooleanField(default=False)
    whatsapp_template_name = models.CharField(max_length=50, null=True, blank=True)
    email_html_template = models.TextField(null=True, blank=True)
    variables_used = models.CharField(max_length=50, blank=True, null=True)
    utm_params_pn = models.CharField(max_length=50, blank=True, null=True)
    utm_params_sms = models.CharField(max_length=50, blank=True, null=True)
