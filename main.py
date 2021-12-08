import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Nissi#3/Documents/Testing/webdriver/chromedriver")


driver.maximize_window()
driver.get('https://staging.interraneuro.com')
time.sleep(5)

email = "admin@medris.ai"
email_element = driver.find_element_by_xpath('//*[@id="Username"]')
email_element.send_keys(email)
time.sleep(1)

password = "Admin@123"
password_element = driver.find_element_by_xpath('//*[@id="Password"]')
password_element.send_keys(password)
time.sleep(1)

login = driver.find_element_by_xpath('/html/body/div/div[1]/form/div[3]/button')
login.click()
time.sleep(1)

# forgot_password = driver.find_element_by_xpath('/html/body/div/div[1]/form/div[3]/div/button')
# forgot_password.click()
# time.sleep(4)
#
# forgot_email = "dharmik6610@gmail.com"
# forgot_email_element = driver.find_element_by_xpath('//*[@id="Username"]')
# forgot_email_element.send_keys(forgot_email)
# time.sleep(1)




#add hospital



hospital_site = driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[4]/a/span')
hospital_site.click()
time.sleep(9)

hospital_site_add_hospital = driver.find_element_by_xpath('//*[@id="btnAdd"]')
hospital_site_add_hospital.click()
time.sleep(5)





hosp_site_name = "NH5"
hosp_site_name_element = driver.find_element_by_xpath('//*[@id="HospitalSiteName"]')
hosp_site_name_element.send_keys(hosp_site_name)
time.sleep(2)

hosp_site_Latitude = "35"
hosp_site_Latitude_element = driver.find_element_by_xpath('//*[@id="Latitude"]')
hosp_site_Latitude_element.send_keys(hosp_site_Latitude)
time.sleep(2)


hosp_site_Longitude = "38"
hosp_site_Longitude_element = driver.find_element_by_xpath('//*[@id="Longitude"]')
hosp_site_Longitude_element.send_keys(hosp_site_Longitude)
time.sleep(2)


hosp_site_CartLocation = "Bengaluru"
hosp_site_CartLocation_element = driver.find_element_by_xpath('//*[@id="CartLocation"]')
hosp_site_CartLocation_element.send_keys(hosp_site_CartLocation)
time.sleep(2)


hosp_site_HospitalNumber = "765432189"
hosp_site_HospitalNumber_element = driver.find_element_by_xpath('//*[@id="HospitalNumber"]')
hosp_site_HospitalNumber_element.send_keys(hosp_site_HospitalNumber)
time.sleep(2)


hosp_site_EDNumber = "765438922"
hosp_site_EDNumber_element = driver.find_element_by_xpath('//*[@id="EDNumber"]')
hosp_site_EDNumber_element.send_keys(hosp_site_EDNumber)
time.sleep(2)

hosp_site_HouseNurseNumber = "625872367"
hosp_site_HouseNurseNumber_element = driver.find_element_by_xpath('//*[@id="HouseNurseNumber"]')
hosp_site_HouseNurseNumber_element.send_keys(hosp_site_HouseNurseNumber)
time.sleep(2)

save_element = driver.find_element_by_xpath('//*[@id="form0"]/div/div[8]/input')
save_element.click()
time.sleep(3)

# cancel = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/button')
# cancel.click()
# time.sleep(1)


next = driver.find_element_by_xpath('//*[@id="DefaultDatatable_paginate"]/ul/li[4]/a')
next.click()
time.sleep(3)

edit = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[3]/td[6]/a[1]')
edit.click()
time.sleep(3)



hosp_site_name_edit = "NH5"
hosp_site_name_edit_element = driver.find_element_by_xpath('//*[@id="HospitalSiteName"]')
hosp_site_name_edit_element.send_keys(hosp_site_name_edit)
time.sleep(2)

hosp_site_Latitude_edit = ""
hosp_site_Latitude_edit_element = driver.find_element_by_xpath('//*[@id="Latitude"]')
hosp_site_Latitude_edit_element.send_keys(hosp_site_Latitude_edit)
time.sleep(2)


hosp_site_Longitude_edit = ""
hosp_site_Longitude_edit_element = driver.find_element_by_xpath('//*[@id="Longitude"]')
hosp_site_Longitude_edit_element.send_keys(hosp_site_Longitude_edit)
time.sleep(2)


hosp_site_CartLocation_edit = "Bengaluru"
hosp_site_CartLocation_edit_element = driver.find_element_by_xpath('//*[@id="CartLocation"]')
hosp_site_CartLocation_edit_element.send_keys(hosp_site_CartLocation_edit)
time.sleep(2)


hosp_site_HospitalNumber_edit = "765432189"
hosp_site_HospitalNumber_edit_element = driver.find_element_by_xpath('//*[@id="HospitalNumber"]')
hosp_site_HospitalNumber_edit_element.send_keys(hosp_site_HospitalNumber_edit)
time.sleep(2)


hosp_site_EDNumber_edit = "765438922"
hosp_site_EDNumber_edit_element = driver.find_element_by_xpath('//*[@id="EDNumber"]')
hosp_site_EDNumber_edit_element.send_keys(hosp_site_EDNumber_edit)
time.sleep(2)

hosp_site_HouseNurseNumber_edit = "625872367"
hosp_site_HouseNurseNumber_edit_element = driver.find_element_by_xpath('//*[@id="HouseNurseNumber"]')
hosp_site_HouseNurseNumber_edit_element.send_keys(hosp_site_HouseNurseNumber_edit)
time.sleep(2)

save_element = driver.find_element_by_xpath('//*[@id="form0"]/div/div[8]/input')
save_element.click()
time.sleep(3)

hosp_site_HouseNurseNumber_edit = "NH"
hosp_site_HouseNurseNumber_edit_element = driver.find_element_by_xpath('//*[@id="DefaultDatatable_filter"]/label/input')
hosp_site_HouseNurseNumber_edit_element.send_keys(hosp_site_HouseNurseNumber_edit)
time.sleep(2)

delete = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[3]/td[6]/a[2]')
delete.click()
time.sleep(2)


delete_yes = driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[1]')
delete_yes.click()
time.sleep(2)







#add hospital contact


hospital_contact = driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[5]/a/span')
hospital_contact.click()
time.sleep(2)


add_hospital_contact = driver.find_element_by_xpath('//*[@id="btnAdd"]')
add_hospital_contact.click()
time.sleep(2)


add_hospital_contact = driver.find_element_by_xpath('//*[@id="HospitalSiteId"]/option[3]')
add_hospital_contact.click()
time.sleep(2)

add_hospital_contact = driver.find_element_by_xpath('//*[@id="ContactType"]/option[3]')
add_hospital_contact.click()
time.sleep(2)

extra_comment = "uiefgsi"
extra_comment_element = driver.find_element_by_xpath('//*[@id="ExtraComment"]')
extra_comment_element.send_keys(extra_comment)
time.sleep(1)

contact = "7276567"
contact_element = driver.find_element_by_xpath('//*[@id="ContactNumber"]')
contact_element.send_keys(contact)
time.sleep(1)

save= driver.find_element_by_xpath('//*[@id="form0"]/div/div[5]/input')
save.click()
time.sleep(10)

edit= driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[2]/td[4]/a[1]')
edit.click()
time.sleep(2)

save= driver.find_element_by_xpath('//*[@id="form0"]/div/div[5]/input')
save.click()
time.sleep(10)


delete= driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[2]/td[4]/a[2]')
delete.click()
time.sleep(2)

delete_yes= driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[1]')
delete_yes.click()
time.sleep(2)




# encounter type




Encounter_type = driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[4]/a/span')
Encounter_type.click()
time.sleep(2)


add_encounter_type = driver.find_element_by_xpath('//*[@id="btnAdd"]')
add_encounter_type.click()
time.sleep(10)

add_encounter_type_name = "Heartt111211232"
add_encounter_type_name_element = driver.find_element_by_xpath('//*[@id="EncounterTypeName"]')
add_encounter_type_name_element.send_keys(add_encounter_type_name)
time.sleep(1)

add_encounter_charge = "5"
add_encounter_charge_element = driver.find_element_by_xpath('//*[@id="EncounterCharges"]')
add_encounter_charge_element.send_keys(add_encounter_charge)
time.sleep(1)



select_encounter = driver.find_element_by_xpath('//*[@id="ParentEncounterTypeId"]/option[7]')
select_encounter.click()
time.sleep(1)




save = driver.find_element_by_xpath('//*[@id="form0"]/div/div[4]/input')
save.click()
time.sleep(5)

next = driver.find_element_by_xpath('//*[@id="DefaultDatatable_paginate"]/ul/li[3]/a')
next.click()
time.sleep(2)


edit = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[5]/td[3]/a[1]')
edit.click()
time.sleep(3)

encounter_type_update = "s"
encounter_type_update_element = driver.find_element_by_xpath('//*[@id="EncounterTypeName"]')
encounter_type_update_element.send_keys(encounter_type_update)
time.sleep(1)

save = driver.find_element_by_xpath('//*[@id="form0"]/div/div[4]/input')
save.click()
time.sleep(5)

delete_encounter_Type = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[5]/td[3]/a[2]')
delete_encounter_Type.click()
time.sleep(2)

delete_encounter_Type_yes = driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[1]')
delete_encounter_Type_yes.click()
time.sleep(2)


#user


# user = driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[5]/a/span  ')
# user.click()
# time.sleep(5)
#
#
# add_user = driver.find_element_by_xpath('//*[@id="btnAdd"]')
# add_user.click()
# time.sleep(5)
#
#
# user_full_name = "ss"
# user_full_name_element = driver.find_element_by_xpath('//*[@id="FullName"]')
# user_full_name_element.send_keys(user_full_name)
# time.sleep(1)
#
# user_email = "a@interraneuro.com"
# user_email_element = driver.find_element_by_xpath('//*[@id="EmailID"]')
# user_email_element.send_keys(user_email)
# time.sleep(1)
#
#
# user_contact = "+14664444567"
# user_contact_element = driver.find_element_by_xpath('//*[@id="ContactNumber"]')
# user_contact_element.send_keys(user_contact)
# time.sleep(1)
#
# user_role_add = driver.find_element_by_xpath('//*[@id="Role"]/option[5]')
# user_role_add.click()
# time.sleep(2)
#
#
# save = driver.find_element_by_xpath('//*[@id="form0"]/div/div[6]/input')
# save.click()
# time.sleep(5)






# next = driver.find_element_by_xpath('//*[@id="DefaultDatatable_next"]')
# next.click()
# time.sleep(1)

# edit = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[2]/td[6]/a[1]')
# edit.click()
# time.sleep(1)
# #
# #
# user_edit_full_name = "v"
# user_edit_full_name_element = driver.find_element_by_xpath('//*[@id="FullName"]')
# user_edit_full_name_element.send_keys(user_edit_full_name)
# time.sleep(1)
#
# user_edit_email = ""
# user_edit_email_element = driver.find_element_by_xpath('//*[@id="EmailID"]')
# user_edit_email_element.send_keys(user_edit_email)
# time.sleep(1)
#
# user_edit_role_add = "PANP"
# user_edit_role_add_element = driver.find_element_by_xpath('//*[@id="Role"]')
# user_edit_role_add_element.send_keys(user_edit_role_add)
# time.sleep(1)
#
# # pic = driver.find_element_by_xpath('//*[@id="form0"]/div/div[4]/input')
# # pic.click('Desktop/car and rental img/car/download (1).jpg')
# # time.sleep(1)
#
# save = driver.find_element_by_xpath('//*[@id="form0"]/div/div[6]/input')
# save.click()
# time.sleep(5)
#
# delete = driver.find_element_by_xpath('//*[@id="DefaultDatatable"]/tbody/tr[2]/td[6]/a[2]')
# delete.click()
# time.sleep(2)
#
# delete_yes = driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[1]')
# delete_yes.click()
# time.sleep(2)





# providers rate


provider_rate = driver.find_element_by_xpath('/html/body/div/div/div[2]/ul/li[6]/a/span')
provider_rate.click()
time.sleep(1)


select_user = driver.find_element_by_xpath('//*[@id="UserId"]/option[7]')
select_user.click()
time.sleep(1)

stroke_rate = "1"
stroke_rate_element = driver.find_element_by_xpath('//*[@id="Charges_0__EncounterCharge"]')
stroke_rate_element.send_keys(stroke_rate)
time.sleep(1)

routine_consultation_rate = "1"
routine_consultation_rate_element = driver.find_element_by_xpath('//*[@id="Charges_1__EncounterCharge"]')
routine_consultation_rate_element.send_keys(routine_consultation_rate)
time.sleep(1)

inpatient_critical_rate = "1"
inpatient_critical_rate_element = driver.find_element_by_xpath('//*[@id="Charges_2__EncounterCharge"]')
inpatient_critical_rate_element.send_keys(inpatient_critical_rate)
time.sleep(1)

inpatient_follow_rate = "1"
inpatient_follow_rate_element = driver.find_element_by_xpath('//*[@id="Charges_3__EncounterCharge"]')
inpatient_follow_rate_element.send_keys(inpatient_follow_rate)
time.sleep(1)

critical_care_follow_rate = "1"
critical_care_follow_rate_element = driver.find_element_by_xpath('//*[@id="Charges_4__EncounterCharge"]')
critical_care_follow_rate_element.send_keys(critical_care_follow_rate)
time.sleep(1)

advance_care_rate = "1"
advance_care_rate_element = driver.find_element_by_xpath('//*[@id="Charges_5__EncounterCharge"]')
advance_care_rate_element.send_keys(advance_care_rate)
time.sleep(1)

EEG = "1"
EEG_element = driver.find_element_by_xpath('//*[@id="Charges_6__EncounterCharge"]')
EEG_element.send_keys(EEG)
time.sleep(1)

EEG_report_2_12_hours_rate = "1"
EEG_report_2_12_hours_rate_element = driver.find_element_by_xpath('//*[@id="Charges_7__EncounterCharge"]')
EEG_report_2_12_hours_rate_element.send_keys(EEG_report_2_12_hours_rate)
time.sleep(1)

EEG_report_12_26_hours_rate = "1"
EEG_report_12_26_hours_rate_element = driver.find_element_by_xpath('//*[@id="Charges_8__EncounterCharge"]')
EEG_report_12_26_hours_rate_element.send_keys(EEG_report_12_26_hours_rate)
time.sleep(1)

EEG_report_36_60_hours_rate = "1"
EEG_report_36_60_hours_rate_element = driver.find_element_by_xpath('//*[@id="Charges_9__EncounterCharge"]')
EEG_report_36_60_hours_rate_element.send_keys(EEG_report_36_60_hours_rate)
time.sleep(1)

EEG_report_60_84_hours_rate = "1"
EEG_report_60_84_hours_rate_element = driver.find_element_by_xpath('//*[@id="Charges_10__EncounterCharge"]')
EEG_report_60_84_hours_rate_element.send_keys(EEG_report_60_84_hours_rate)
time.sleep(1)

EEG_report_more_than_84_hours_rate = "1"
EEG_report_more_than_84_hours_rate_element = driver.find_element_by_xpath('//*[@id="Charges_11__EncounterCharge"]')
EEG_report_more_than_84_hours_rate_element.send_keys(EEG_report_more_than_84_hours_rate)
time.sleep(1)

outpatient_rate = "1"
outpatient_rate_element = driver.find_element_by_xpath('//*[@id="Charges_12__EncounterCharge"]')
outpatient_rate_element.send_keys(outpatient_rate)
time.sleep(1)


extra = "1"
extra_element = driver.find_element_by_xpath('//*[@id="Charges_13__EncounterCharge"]')
extra_element.send_keys(extra)
time.sleep(1)

extra = "1"
extra_element = driver.find_element_by_xpath('//*[@id="Charges_14__EncounterCharge"]')
extra_element.send_keys(extra)
time.sleep(1)

save = driver.find_element_by_xpath('//*[@id="form0"]/div/div[18]/input')
save.click()
time.sleep(1)







#billing report


billing_report = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[7]/a/span')
billing_report.click()
time.sleep(1)

billing_start_date = "03/10/2021"
billing_start_date_element = driver.find_element_by_xpath('//*[@id="txtStartDate"]')
billing_start_date_element.send_keys(billing_start_date)
time.sleep(4)

billing_report = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div')
billing_report.click()
time.sleep(4)

billing_end_date = "04/08/2021"
billing_end_date_element = driver.find_element_by_xpath('//*[@id="txtEndDate"]')
billing_end_date_element.send_keys(billing_end_date)
time.sleep(4)

billing_report = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/h5')
billing_report.click()
time.sleep(1)

billing_all_site = "Hazard ARH"
billing_all_site_element = driver.find_element_by_xpath('//*[@id="drpHospital"]')
billing_all_site_element.send_keys(billing_all_site )
time.sleep(1)

billing_all_consultation = "Inpatient Follow Up"
billing_all_consultation_element = driver.find_element_by_xpath('//*[@id="drpEncounterType"]')
billing_all_consultation_element.send_keys(billing_all_consultation )
time.sleep(1)

billing_all_user = "Indira"
billing_all_user_element = driver.find_element_by_xpath('//*[@id="drpUsers"]')
billing_all_user_element.send_keys(billing_all_user )
time.sleep(1)

billing_select_patient = "Joe Dirt"
billing_select_patient_element = driver.find_element_by_xpath('//*[@id="PatientId"]')
billing_select_patient_element.send_keys(billing_select_patient )
time.sleep(1)

billing_view_port = driver.find_element_by_xpath('//*[@id="btnView"]')
billing_view_port.click()
time.sleep(1)



#providers invoice



providers_invoice = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[8]/a/span')
providers_invoice.click()
time.sleep(1)

billing_start_date = "03/10/2021"
billing_start_date_element = driver.find_element_by_xpath('//*[@id="txtStartDate"]')
billing_start_date_element.send_keys(billing_start_date)
time.sleep(1)

billing_report = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/h5')
billing_report.click()
time.sleep(1)

billing_end_date = "04/08/2021"
billing_end_date_element = driver.find_element_by_xpath('//*[@id="txtEndDate"]')
billing_end_date_element.send_keys(billing_end_date)
time.sleep(1)

billing_report1 = driver.find_element_by_xpath('//*[@id="DefaultDatatable_info"]')
billing_report1.click()
time.sleep(1)

billing_all_site = "Hazard ARH"
billing_all_site_element = driver.find_element_by_xpath('//*[@id="drpHospital"]')
billing_all_site_element.send_keys(billing_all_site)
time.sleep(1)

billing_all_consultation = "Inpatient Follow Up"
billing_all_consultation_element = driver.find_element_by_xpath('//*[@id="drpEncounterType"]')
billing_all_consultation_element.send_keys(billing_all_consultation)
time.sleep(1)

billing_all_user = "Naren"
billing_all_user_element = driver.find_element_by_xpath('//*[@id="drpUsers"]')
billing_all_user_element.send_keys(billing_all_user)
time.sleep(1)

billing_select_patient = "patel"
billing_select_patient_element = driver.find_element_by_xpath('//*[@id="PatientId"]')
billing_select_patient_element.send_keys(billing_select_patient)
time.sleep(1)

billing_view_port = driver.find_element_by_xpath('//*[@id="btnView"]')
billing_view_port.click()
time.sleep(1)






#appointment


appointment = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[9]/a')
appointment.click()
time.sleep(1)


add_appointment = driver.find_element_by_xpath('//*[@id="btnAdd"]')
add_appointment.click()
time.sleep(1)

select_site = driver.find_element_by_xpath('//*[@id="HospitalSiteId"]/option[3]')
select_site.click()
time.sleep(1)

select_patient = driver.find_element_by_xpath('//*[@id="PatientId"]/option[4]')
select_patient.click()
time.sleep(1)

select_appo_type = driver.find_element_by_xpath('//*[@id="AppointmentTypeId"]/option[2]')
select_appo_type.click()
time.sleep(1)

contact_no = "+19659347458"
contact_no_element = driver.find_element_by_xpath('//*[@id="ContactNumber"]')
contact_no_element.send_keys(contact_no)
time.sleep(1)


note = "87437875"
note_element = driver.find_element_by_xpath('//*[@id="DoctorNote"]')
note_element.send_keys(note)
time.sleep(1)

save = driver.find_element_by_xpath('//*[@id="frmAddPatient"]/div/div[6]/input')
save.click()
time.sleep(1)


appointment_start_date = "03/10/2021"
appointment_start_date_element = driver.find_element_by_xpath('//*[@id="txtStartDate"]')
appointment_start_date_element.send_keys(appointment_start_date)
time.sleep(1)


appointment_end_date = "03/10/2021"
appointment_end_date_element = driver.find_element_by_xpath('//*[@id="txtEndDate"]')
appointment_end_date_element.send_keys(appointment_end_date)
time.sleep(1)

appoin_touch = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div/div[2]')
appoin_touch.click()
time.sleep(2)


all_site= driver.find_element_by_xpath('//*[@id="drpHospital"]/option[3]')
all_site.click()
time.sleep(2)

select_appoin= driver.find_element_by_xpath('//*[@id="drpAppointmentType"]/option[2]')
select_appoin.click()
time.sleep(2)

filter= driver.find_element_by_xpath('//*[@id="btnView"]')
filter.click()
time.sleep(2)





#rounds




rounds= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[10]/a')
rounds.click()
time.sleep(2)


capture_list= driver.find_element_by_xpath('//*[@id="btnCapture"]')
capture_list.click()
time.sleep(2)

capture_list_yes= driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[1]')
capture_list_yes.click()
time.sleep(2)


reset_todays_capture_list= driver.find_element_by_xpath('//*[@id="btnResetCapture"]')
reset_todays_capture_list.click()
time.sleep(2)

reset_todays_capture_list_yes= driver.find_element_by_xpath('/html/body/div[4]/div[3]/button[1]')
reset_todays_capture_list_yes.click()
time.sleep(2)

select_round_date = "05/05/2021"
select_round_date_element = driver.find_element_by_xpath('//*[@id="txtStartDate"]')
select_round_date_element.send_keys(select_round_date)
time.sleep(1)

view_previous_current_round_list= driver.find_element_by_xpath('//*[@id="btnView"]')
view_previous_current_round_list.click()
time.sleep(2)


clear_selection = driver.find_element_by_xpath('//*[@id="btnClear"]')
clear_selection.click()
time.sleep(2)





#all patiennt




all_patient = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[11]/a')
all_patient.click()
time.sleep(0)

add_in_all_patient = driver.find_element_by_xpath('//*[@id="btnAdd"]')
add_in_all_patient.click()
time.sleep(0)

mrn = "12"
mrn_element = driver.find_element_by_xpath('//*[@id="MRN"]')
mrn_element.send_keys(mrn)
time.sleep(0)


first_name = "1kkk"
first_name_element = driver.find_element_by_xpath('//*[@id="FirstName"]')
first_name_element.send_keys(first_name)
time.sleep(0)

last_name = "ke"
last_name_element = driver.find_element_by_xpath('//*[@id="LastName"]')
last_name_element.send_keys(last_name)
time.sleep(0)

gender = "Male"
gender_element = driver.find_element_by_xpath('//*[@id="Gender"]')
gender_element.send_keys(gender)
time.sleep(0)

billing_start_date = "02-16-2021"
billing_start_date_element = driver.find_element_by_xpath('//*[@id="Dob"]')
billing_start_date_element.send_keys(billing_start_date)
time.sleep(0)

simply = driver.find_element_by_xpath('//*[@id="frmAddPatient"]/div')
simply.click()
time.sleep(0)

billing_all_site = "NH3"
billing_all_site_element = driver.find_element_by_xpath('//*[@id="HospitalSiteId"]')
billing_all_site_element.send_keys(billing_all_site)
time.sleep(1)

select_provides = "Indira"
select_provides_element = driver.find_element_by_xpath('//*[@id="ProviderId"]')
select_provides_element.send_keys(select_provides)
time.sleep(1)

select_patient = driver.find_element_by_xpath('//*[@id="PatientType"]/option[2]')
select_patient.click()
time.sleep(0)

select_status= driver.find_element_by_xpath('//*[@id="PatientStatus"]/option[2]')
select_status.click()
time.sleep(0)



save = driver.find_element_by_xpath('//*[@id="frmAddPatient"]/div/div[10]/input')
save.click()
time.sleep(0)

# all patient filter

billing_all_site = "Hazard ARH"
billing_all_site_element = driver.find_element_by_xpath('//*[@id="drpHospital"]')
billing_all_site_element.send_keys(billing_all_site)
time.sleep(0)

first_name = "k"
first_name_element = driver.find_element_by_xpath('//*[@id="txtFirstName"]')
first_name_element.send_keys(first_name)
time.sleep(0)

first_name = "1"
first_name_element = driver.find_element_by_xpath('//*[@id="txtLastName"]')
first_name_element.send_keys(first_name)
time.sleep(0)

gender = "Male"
gender_element = driver.find_element_by_xpath('//*[@id="drpGender"]')
gender_element.send_keys(gender)
time.sleep(0)

filtter = driver.find_element_by_xpath('//*[@id="btnView"]')
filtter.click()
time.sleep(0)




#all encounter



all_encounter = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[12]/a')
all_encounter.click()
time.sleep(1)

add_in_all_encounter = driver.find_element_by_xpath('//*[@id="btnAdd"]')
add_in_all_encounter.click()
time.sleep(2)




add_in_all_encounter = driver.find_element_by_xpath('//*[@id="HospitalSiteId"]/option[13]')
add_in_all_encounter.click()
time.sleep(4)

select_patient = "ke"
select_patient_element = driver.find_element_by_xpath('//*[@id="PatientId"]')
select_patient_element.send_keys(select_patient)
time.sleep(2)

add_in_all_encounter = driver.find_element_by_xpath('//*[@id="EncounterFor"]/option[2]')
add_in_all_encounter.click()
time.sleep(1)

add_in_all_encounter = driver.find_element_by_xpath('//*[@id="EncounterTypeId"]/option[2]')
add_in_all_encounter.click()
time.sleep(1)

add_in_all_encounter = driver.find_element_by_xpath('//*[@id="PrimaryDiagnosis"]/option[2]')
add_in_all_encounter.click()
time.sleep(1)

add_in_all_encounter = driver.find_element_by_xpath('//*[@id="TransferStatus"]/option[2]   ')
add_in_all_encounter.click()
time.sleep(1)

select_patient = "03-10-2021 08:54 PM"
select_patient_element = driver.find_element_by_xpath('//*[@id="txtEncounterOn"]')
select_patient_element.send_keys(select_patient)
time.sleep(2)



add_in_all_encounter = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/h4')
add_in_all_encounter.click()
time.sleep(1)



add_in_all_encounter = driver.find_element_by_xpath('//*[@id="ProviderId"]/option[5]')
add_in_all_encounter.click()
time.sleep(1)


save = driver.find_element_by_xpath('//*[@id="frmAddPatient"]/div/div[10]/input')
save.click()
time.sleep(1)

#encounter filter

start_date = "02-17-2021"
start_date_element = driver.find_element_by_xpath('//*[@id="txtStartDate"]')
start_date_element.send_keys(start_date)
time.sleep(1)

end_date = "04-15-2021"
end_date_element = driver.find_element_by_xpath('//*[@id="txtEndDate"]')
end_date_element.send_keys(end_date)
time.sleep(1)

billing_all_site = "Hazard ARH"
billing_all_site_element = driver.find_element_by_xpath('//*[@id="drpHospital"]')
billing_all_site_element.send_keys(billing_all_site)
time.sleep(1)

select_consultation = "Inpatient Follow Up"
select_consultation_element = driver.find_element_by_xpath('//*[@id="drpEncounterType"]')
select_consultation_element.send_keys(select_consultation)
time.sleep(1)

filtter = driver.find_element_by_xpath('//*[@id="btnView"]')
filtter.click()
time.sleep(0)



# action = drive.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[3]')
# action.click()
# time.sleep(0)

# logout = drive.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[4]/ul/li[2]/a/span')
# logout.click()
# time.sleep(0)

























































