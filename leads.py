import pandas as pd
import numpy as np

leads_cols = ['id', 'email', 'acquisition_channel', 'mms_backup_status', 'mms', 'first_name', 'last_name', 'job_title', 'company_name', 'acquisition_date', 'sfdc_campaigns']
leads = pd.read_csv('reports/all_leads.csv', names=leads_cols).dropna(subset=['email'])
print leads.head()

sfdc_nn = leads.dropna(subset=['sfdc_campaigns'])

sfdc_oe = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Online Education' in x)]
sfdc_oe_final = sfdc_oe.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_oe_final.to_csv('reports/sfdc_oe.csv')

sfdc_cert = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Certification' in x)]
sfdc_cert_final = sfdc_cert.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_cert_final.to_csv('reports/sfdc_cert.csv')

sfdc_mongocon = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'MongoCon' in x)]
sfdc_mongocon_final = sfdc_mongocon.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_mongocon_final.to_csv('reports/sfdc_mongocon.csv')

sfdc_webinar = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Webinar' in x)]
sfdc_webinar_final = sfdc_webinar.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_webinar_final.to_csv('reports/sfdc_webinar.csv')

sfdc_newsletter = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Newsletter' in x)]
sfdc_newsletter_final = sfdc_webinar.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_newsletter_final.to_csv('reports/sfdc_newsletter.csv')

sfdc_enterprise = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'MongoDB Enterprise Edition' in x)]
sfdc_enterprise_final = sfdc_webinar.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_enterprise_final.to_csv('reports/sfdc_enterprise.csv')

sfdc_content = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Content Download' in x)]
sfdc_content_final = sfdc_webinar.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_content_final.to_csv('reports/sfdc_content.csv')

sfdc_webform = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Webform' in x)]
sfdc_webform_final = sfdc_webinar.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_webform_final.to_csv('reports/sfdc_webform.csv')

sfdc_training = sfdc_nn[sfdc_nn['sfdc_campaigns'].apply(lambda x: 'Public Training' in x)]
sfdc_training_final = sfdc_training.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
sfdc_training_final.to_csv('reports/sfdc_training.csv')

mms = leads.dropna(subset=['mms'])
mms_final = mms.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
mms_final.to_csv('reports/mms.csv')

mms_backup = leads.dropna(subset=['mms_backup_status'])
mms_backup_final = mms_backup.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
mms_backup_final.to_csv('reports/mms_backup.csv')

acqui_nn = leads.dropna(subset=['acquisition_channel'])

acqui_ppc = acqui_nn[acqui_nn['acquisition_channel'].apply(lambda x: 'PPC' in x)]
acqui_ppc_final = acqui_ppc.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
acqui_ppc_final.to_csv('reports/acqui_ppc.csv')

acqui_organic = acqui_nn[acqui_nn['acquisition_channel'].apply(lambda x: 'Organic' in x)]
acqui_organic_final = acqui_organic.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
acqui_organic_final.to_csv('reports/acqui_organic.csv')

acqui_social = acqui_nn[acqui_nn['acquisition_channel'].apply(lambda x: 'Social' in x)]
acqui_social_final = acqui_social.drop(['acquisition_channel', 'mms_backup_status', 'mms',  'sfdc_campaigns'], axis=1)
acqui_social_final.to_csv('reports/acqui_social.csv')


