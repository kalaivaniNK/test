from selenium.webdriver.common.by import By
import time

class Login:
    txtbx_email_xpath = "//input[@placeholder='Username']"
    txtbx_password_xpath = "//input[@placeholder='Password']"
    btn_login_button = "//button[normalize-space()='Login']"
#pim
    pim_add_xpath = "//button[normalize-space()='Add']"
    emp_frst_name = "//input[@placeholder='First Name']"
    emp_last_name = "//input[@placeholder='Last Name']"
    pim_save_button = "//form/div[2]//button[@type='submit']"

#personal details locators
    other_id_xpath = "//div[2]/div[1]/div[2]//div[2]/input[@class='oxd-input oxd-input--active']"
    license_no_path = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    expiry_date =  "//form/div[2]//div[2]//div/input[@placeholder='yyyy-mm-dd']"
    ssn_xpath = "//div[3]/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    sin_xpath = "//div[3]/div[2]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    date_of_birth = "//form/div[3]/div[2]//div/input[@placeholder='yyyy-mm-dd']"
    gender_xpath = "//label[normalize-space()='Female']"
    select_nationality_xpath = "//div[@class='oxd-form-row']/div[1]/div[1]//div[@clear]"
    select_nationality_click = "//*[contains(text(),'Indian')]"
    select_married_status = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_married_status_click =  "//*[contains(text(),'Single')]"
    military_service_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//div[5]/button[@type='submit']"
    blood_xpath = "//form/div[1]//div[2]//div[@class='oxd-select-text oxd-select-text--active']"
    select_blood_group ="//*[contains(text(),'A+')]"
    save_button1_xpath = "//form/div[2]/button[@type='submit']"
#contact details
    click_contact = "//a[contains(text(),'Contact Details')]"
    street1_xpath = "//form/div[1]/div/div[1]//div[2]/input[@class='oxd-input oxd-input--active']"
    street2_xpath = "//form/div[1]//div[2]//div[2]/input"
    city_xpath =  "//form[@class='oxd-form']/div[1]//div[3]//div[2]/input"
    state_xpath = "//form//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    pincode_xpath = "//form[@class='oxd-form']//div[1]//div[5]//div[2]/input"
    country_path_select = "//*[contains(text(),'-- Select --')]"
    country_click_path = "//*[text()='India']"
    txt_homenumber_xpath = "//form[@class='oxd-form']/div[2]//div[1]/div/div[2]/input"
    txt_mobile_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_work_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_workemail_xpath = "//form[@class='oxd-form']/div[3]/div/div[1]//input"
    txt_othermail_xpath = "//form[@class='oxd-form']/div[3]/div/div[2]//input"
    txt_contactsave_xpath = "//form[@class='oxd-form']/div[4]//button"

#emergency details locators
    emergency_contact_click = "//a[normalize-space()='Emergency Contacts']"
    add_contact = "//div/div[2]/div[1]/div/button"
    Name_path = "//form/div[1]/div/div[1]//input"
    realationship_path = "//form/div[1]/div/div[2]//input"
    mobile1_no_path = "//form/div[2]/div/div[2]//input"
    work_no_path = "//form/div[2]/div/div[3]//input"
    save_emergency_cotact ="//button[normalize-space()='Save']"
#dependent locators
    dependent_click = "//a[normalize-space()='Dependents']"
    add_dependent_path = "//div[2]/div//div[2]/div[1]//button"
    add_name = "//div[2]/input"
    drp_relation_path = "//form/div//div[2]//div[2]/div"
    drp_relation_click_path = "//*[contains(text(),'Child')]"
    add_dob = "//input[@placeholder='yyyy-mm-dd']"
    save_dependent = "//button[@type='submit']"

#Immigration
    immigration_click = "//a[normalize-space()='Immigration']"
    add_immigration =  "//div[2]/div[1]/div/button[@class='oxd-button oxd-button--medium oxd-button--text']"
    add_number = "//form/div[2]/div/div[1]//input"
    issued_date =  "//form/div[2]//div[2]//div[2]//input[@placeholder='yyyy-mm-dd']"
    expiry_date_enter = "//div[3]//div[2]//input[@placeholder='yyyy-mm-dd']"
    eligible_status = "//form[@class='oxd-form']/div[2]//div[4]//input"
    drp_issued_by = "//div[contains(text(),'-- Select --')]"
    select_issued_by = "//*[contains(text(),'India')]"
    eligible_review_date =  "//div[6]//div[2]//input[@placeholder='yyyy-mm-dd']"
    command_path = "//textarea[@placeholder='Type Comments here']"
    save_immigration = "//form/div[3]/button[2]"

#job
    job_click = "//a[normalize-space()='Job']"
    joined_date = "//input[@placeholder='yyyy-mm-dd']"
    drp_job_title_path = "//div[2]/div/div[2]//div[@tabindex='0']"
    select_job_title = "//*[contains(text(),'Chief Technical Officer')]"
    drp_job_categery = "//div[4]/div/div[2]//div[@tabindex='0']"
    select_job_categery ="//*[contains(text(),'Professionals')]"
    sub_unit = "//div[5]/div/div[2]//div[@tabindex='0']"
    select_sub_unit = "//*[contains(text(),'Administration')]"
    location_path = "//div[6]/div/div[2]//div[@tabindex='0']"
    select_location_path = "//*[contains(text(),'HQ - CA, USA')]"
    employement_status = "//div[7]/div/div[2]//div[@tabindex='0']"
    click_employee_status = "//*[contains(text(),'Full-Time Permanent')]"
    save_job = "//div[3]/button[@type='submit']"
#salary locators
    salary_click = "//a[normalize-space()='Salary']"
    ad_salary = "//div[2]//div[1]//div[2]/div[1]//button[@type='button']"
    salary_component = "//div[1]/div/div[2]/input"
    pay_grade = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_pay_grade = "//*[contains(text(),'Grade 2')]"
    pay_frequency = "//div[3]/div/div[2]//div[@class='oxd-select-text-input']"
    select_pay_frequency = "//*[contains(text(),'Monthly')]"
    currency_path = "//div[4]/div/div[2]//div[@class='oxd-select-text-input']"
    select_currency = "//*[contains(text(),'United States Dollar')]"
    amount_path =  "//div[5]/div/div[2]/input"
    salary_command = "//textarea"
    include_account = "//label/span"
    account_no_path = "//form/div[4]/div[1]/div[1]/div/div[2]/input"
    acount_type = "//form/div[4]//div[2]//div[@class='oxd-select-text-input']"
    select_account_type = "//*[contains(text(),'Savings')]"
    routing_no = "//form/div[4]/div[2]/div[1]/div/div[2]/input"
    amount_xpath = "//div[2]/div/div[2]/input"
    save_salary = "//button[normalize-space()='Save']"

#tax

    tax_btn_xpath = "//a[normalize-space()='Tax Exemptions']"
    fede_drp_status_xpath = "//form/div[1]//div[2]//div[@tabindex='0']"
    fede_drp_sta_sel_xpath = "//*[contains(text(),'Single')]"
    fede_exemption_xpath = "//div[2]/div/div[2]//input"
    state_drp_xpath = "//div[2]/div/div[1]/div/div[2]/div/div/div[@tabindex='0']"
    state_drp_select_xpath = "//*[contains(text(),'Alaska')]"
    status_drp_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    status_drp_select_xpath = "//div[2]/div/div[2]//*[contains(text(),'Single')]"
    state_txt_input = "//div[3]//div[2]/input"
    unemp_drp_xpath = "//form//div[4]//div[2]//div[@tabindex='0']"
    unemp_select_xpath = "//*[contains(text(),'New York')]"
    work_state_drp_xpath = "//form//div[5]//div[2]//div[@tabindex='0']"
    work_select_drp_xpath = "//*[contains(text(),'Montana')]"
    tax_save_xpath = "//button[normalize-space()='Save']"
#report locators
    click_report = "//a[normalize-space()='Report-to']"
    add_report = "//div/div[2]/div[1]/div/button"
    add_supervisr_name = "//input[@placeholder='Type for hints...']"
    select1_name = "//*[contains(text(),'Odis  Adalwin')]"
    drp_reporting_method = "//form/div[1]//div[2]//div[@tabindex='0']"
    select_reporting_method = "//*[contains(text(),'Direct')]"
    save_supervisor = "//button[normalize-space()='Save']"
    add_suborinate_path = "//div/div[3]/div[1]/div/button"
    subordinate_name = "//input[@placeholder='Type for hints...']"
    select2_name = "//*[contains(text(),'Cassidy  Hope')]"
    drp_reporting1_method = "//*[contains(text(),'-- Select --')]"
    select_report_method =  "//*[contains(text(),'Indirect')]"
    save_subordinate = "//button[normalize-space()='Save']"
#Qualification(work experience)
    click_qualification = "//a[normalize-space()='Qualifications']"
    add_work_exp = "//div[2]/div[2]/div[1]/div/button"
    wrkexp_add_cmpny = "//div[1]/div/div[2]/input"
    wrkexp_job_title = "//form[@class='oxd-form']/div[1]//div[2]//div[2]/input"
    from_xpath = "//form/div[2]/div/div[1]//div[2]//input"
    to_xpath = "//form/div[2]//div[2]//div[2]//input[@placeholder='yyyy-mm-dd']"
    wrkexp_comments = "//textarea"
    save_work_exp = "//form/div[4]/button[2]"
#qualification(Education)
    add_education =  "//div[3]/div[1]//button[@type='button']"
    leve_path = "//form/div[1]//div[2]//div[@tabindex='0']"
    select_level_path = "//*[contains(text(),'College Undergraduate')]"
    institute_path = "//div[1]/div/div[2]/div/div[2]/input"
    major_path = "//div[3]/div/div[2]/input"
    year_path = "//form/div[1]//div[4]//div[2]/input"
    gpa_path = "//div[5]/div/div[2]/input"
    start_date_path = "//form/div[2]/div/div[1]//div[2]//input[@placeholder='yyyy-mm-dd']"
    end_date_path = "//div[2]/div/div[2]//div/input[@placeholder='yyyy-mm-dd']"
    save_education = "//button[normalize-space()='Save']"
#qualification(skills)
    add_skills = "//div[4]/div[1]/div/button"
    drp_skill_path = "//form/div[1]//div[2]//div[@tabindex='0']"
    select_skill_path = "//*[contains(text(),'Python')]"
    year_of_experience = "//div[2]/div[2]//input"
    skill_comments = "//textarea"
    save_skills = "//button[normalize-space()='Save']"
#qualification(language)
    add_language_button = "//div[5]/div[1]/div/button"
    drp_language_xpath = "//form/div[1]/div/div[1]//div[@tabindex='0']"
    select_language = "//*[contains(text(),'English')]"
    drp_fluency = "//form/div[1]/div/div[2]//div[@tabindex='0']"
    select_fluency = "//*[contains(text(),'Writing')]"
    drp_competency = "//form/div[1]/div/div[3]//div[@tabindex='0']"
    select_competency = "//*[contains(text(),'Good')]"
    language_comments = "//textarea"
    save_language = "//button[normalize-space()='Save']"
#qualification(license)
    add_license = "//div[6]/div[1]/div/button"
    license_type = "//form/div[1]/div/div[1]//div[@tabindex='0']"
    select_license_type = "//*[contains(text(),'Certified Information Security Manager')]"
    license_no_xpath = "//div[2]//div[2]/input"
    license_issued_date = "//form/div[2]/div/div[1]//input"
    license_expiry_date = "//form/div[2]/div/div[2]//input"
    save_license = "//button[normalize-space()='Save']"
#membership
    add_membership = "//a[normalize-space()='Memberships']"
    mem_add_xpath = "//div[1]/div/div[2]/div[1]/div/button"
    drp_memership_xpath = "//form/div/div/div[1]//div[@tabindex='0']"
    mem_drp_xpath = "//*[contains(text(),'ACCA')]"
    drp_subscription_xpath = "//form/div/div/div[2]//div[@tabindex='0']"
    mem_subscription_xpath = "//*[contains(text(),'Company')]"
    subscription_amt_xpath = "//div[3]//div[2]//input"
    drp_currency_xpath = "//form/div/div/div[4]//div[@tabindex='0']"
    mem_currency_xpath = "//*[contains(text(),'Indian Rupee')]"
    sub_commence_date_xpath = "//div[5]//input[@placeholder='yyyy-mm-dd']"
    sub_renewal_date_xpath = "//div[6]//input[@placeholder='yyyy-mm-dd']"
    membership_save_xpath = "//button[normalize-space()='Save']"




#admin page
    Admin_click_path = "//span[normalize-space()='Admin']"
    add_admin_path = "//button[normalize-space()='Add']"
    drp_userrole_path =  "//div[1]/div/div[2]/div/div/div[@class='oxd-select-text-input']"
    click_user_role = "//*[contains(text(),'Admin')]"
    emp_name_path =  "//input[@placeholder='Type for hints...']"
    click_emp_name = "//*[contains(text(),'kalai')]"
    drp_status_path = "//div[3]/div/div[2]/div/div/div[@class='oxd-select-text-input']"
    click_status_path = "//*[contains(text(),'Enabled')]"
    username_path = "//div[1]//div[4]//input"
    password_path = "//div[1]/div/div[2]/input"
    confirm_password = "//div[2]/div/div[2]/input"
    save_admin = "//button[normalize-space()='Save']"







#search for the user

    username1_path = "//form/div[1]/div//div[2]/input"
    search_button = "//button[normalize-space()='Search']"
#name
    name_search = "//div[@class='oxd-table-card']//div//div[2]"
#logout
    click_profile = "//i/preceding::p"
    logout_path = "//a[text()='Logout']"

#again login
    txtbx1_email_xpath = "//input[@placeholder='Username']"
    txtbx1_password_xpath = "//input[@placeholder='Password']"
    btn1_login_button = "//button[normalize-space()='Login']"








    def __init__(self, driver):
        self.driver = driver

    def setlogin(self, username,password):
        self.driver.find_element(By.XPATH,self.txtbx_email_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,self.txtbx_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH,self.btn_login_button).click()

    def pim(self,firstName,lastName):
        self.driver.find_element(By.XPATH,self.pim_add_xpath).click()
        self.driver.find_element(By.XPATH,self.emp_frst_name).send_keys(firstName)
        self.driver.find_element(By.XPATH,self.emp_last_name).send_keys(lastName)
        self.driver.find_element(By.XPATH,self.pim_save_button).click()
    def peronal_details(self,otherid,licenseno,expirydate,ssn,sin,dob,militaryservice):
        self.driver.find_element(By.XPATH,self.other_id_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH,self.license_no_path).send_keys(licenseno)
        self.driver.find_element(By.XPATH,self.expiry_date).send_keys(expirydate)
        self.driver.find_element(By.XPATH,self.ssn_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH,self.sin_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH,self.date_of_birth).send_keys(dob)
        self.driver.find_element(By.XPATH,self.gender_xpath).click()
        self.driver.find_element(By.XPATH,self.select_nationality_xpath).click()
        self.driver.find_element(By.XPATH,self.select_nationality_click).click()
        self.driver.find_element(By.XPATH,self.select_married_status).click()
        self.driver.find_element(By.XPATH,self.select_married_status_click).click()
        self.driver.find_element(By.XPATH,self.military_service_xpath).send_keys(militaryservice)
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()
        self.driver.find_element(By.XPATH,self.blood_xpath).click()
        self.driver.find_element(By.XPATH,self.select_blood_group).click()
        self.driver.find_element(By.XPATH,self.save_button1_xpath).click()
        time.sleep(5)

    def contact_details(self,street1,street2,city,state,pincode,homephno,mobileno,work,email,otheremail):

        self.driver.find_element(By.XPATH,self.click_contact).click()
        self.driver.find_element(By.XPATH,self.street1_xpath).send_keys(street1)
        self.driver.find_element(By.XPATH,self.street2_xpath).send_keys(street2)
        self.driver.find_element(By.XPATH,self.city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH,self.state_xpath).send_keys(state)
        self.driver.find_element(By.XPATH,self.pincode_xpath).send_keys(pincode)
        self.driver.find_element(By.XPATH,self.country_path_select).click()
        self.driver.find_element(By.XPATH,self.country_click_path).click()
        self.driver.find_element(By.XPATH,self.txt_homenumber_xpath).send_keys(homephno)
        self.driver.find_element(By.XPATH,self.txt_mobile_xpath).send_keys(mobileno)
        self.driver.find_element(By.XPATH,self.txt_work_xpath).send_keys(work)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.txt_workemail_xpath).send_keys(email)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.txt_othermail_xpath).send_keys(otheremail)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.txt_contactsave_xpath).click()
        time.sleep(3)


    def Emergency_details(self,name,relationship,mobileno,workno):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.emergency_contact_click).click()
        self.driver.find_element(By.XPATH,self.add_contact).click()
        self.driver.find_element(By.XPATH,self.Name_path).send_keys(name)
        self.driver.find_element(By.XPATH,self.realationship_path).send_keys(relationship)
        self.driver.find_element(By.XPATH,self.mobile1_no_path).send_keys(mobileno)
        self.driver.find_element(By.XPATH,self.work_no_path).send_keys(workno)
        self.driver.find_element(By.XPATH,self.save_emergency_cotact).click()

    def Dependend(self,name,dob):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.dependent_click).click()
        self.driver.find_element(By.XPATH,self.add_dependent_path).click()
        self.driver.find_element(By.XPATH,self.add_name).send_keys(name)
        self.driver.find_element(By.XPATH,self.drp_relation_path).click()
        self.driver.find_element(By.XPATH,self.drp_relation_click_path).click()
        self.driver.find_element(By.XPATH,self.add_dob).send_keys(dob)
        self.driver.find_element(By.XPATH,self.save_dependent).click()

    def immigration(self,number,issueddate,expirydate,eligiblestatus,reviewdate,command):
        self.driver.find_element(By.XPATH,self.immigration_click).click()
        self.driver.find_element(By.XPATH,self.add_immigration).click()
        self.driver.find_element(By.XPATH,self.add_number).send_keys(number)
        self.driver.find_element(By.XPATH,self.issued_date).send_keys(issueddate)
        self.driver.find_element(By.XPATH,self.expiry_date_enter).send_keys(expirydate)
        self.driver.find_element(By.XPATH,self.eligible_status).send_keys(eligiblestatus)
        self.driver.find_element(By.XPATH,self.drp_issued_by).click()
        self.driver.find_element(By.XPATH,self.select_issued_by).click()
        self.driver.find_element(By.XPATH,self.eligible_review_date).send_keys(reviewdate)
        self.driver.find_element(By.XPATH,self.command_path).send_keys(command)
        self.driver.find_element(By.XPATH,self.save_immigration).click()
    def job_details(self,joineddate):

        self.driver.find_element(By.XPATH,self.job_click).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.joined_date).send_keys(joineddate)
        self.driver.find_element(By.XPATH,self.drp_job_title_path).click()
        self.driver.find_element(By.XPATH,self.select_job_title).click()
        self.driver.find_element(By.XPATH,self.drp_job_categery).click()
        self.driver.find_element(By.XPATH,self.select_job_categery).click()
        self.driver.find_element(By.XPATH,self.sub_unit).click()
        self.driver.find_element(By.XPATH,self.select_sub_unit).click()
        self.driver.find_element(By.XPATH,self.location_path).click()
        self.driver.find_element(By.XPATH,self.select_location_path).click()
        self.driver.find_element(By.XPATH,self.employement_status).click()
        self.driver.find_element(By.XPATH,self.click_employee_status).click()
        self.driver.find_element(By.XPATH,self.save_job).click()

    def salary_details(self,salcomponent,amount1,comments,acountno,routingno,amount2):
        self.driver.find_element(By.XPATH,self.salary_click).click()
        self.driver.find_element(By.XPATH,self.ad_salary).click()
        self.driver.find_element(By.XPATH,self.salary_component).send_keys(salcomponent)
        self.driver.find_element(By.XPATH,self.pay_grade).click()
        self.driver.find_element(By.XPATH, self.select_pay_grade).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.pay_frequency).click()
        self.driver.find_element(By.XPATH, self.select_pay_frequency).click()
        self.driver.find_element(By.XPATH, self.currency_path).click()
        self.driver.find_element(By.XPATH, self.select_currency).click()
        self.driver.find_element(By.XPATH,self.amount_path).send_keys(amount1)
        self.driver.find_element(By.XPATH,self.salary_command).send_keys(comments)
        self.driver.find_element(By.XPATH, self.include_account).click()
        self.driver.find_element(By.XPATH,self.account_no_path).send_keys(acountno)
        self.driver.find_element(By.XPATH,self.acount_type).click()
        self.driver.find_element(By.XPATH, self.select_account_type).click()
        self.driver.find_element(By.XPATH, self.routing_no).send_keys(routingno)
        self.driver.find_element(By.XPATH, self.amount_xpath).send_keys(amount2)
        self.driver.find_element(By.XPATH,self.save_salary).click()

    def tax_details(self,fedexamption,stateexemption):
        self.driver.find_element(By.XPATH,self.tax_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.fede_drp_status_xpath).click()
        self.driver.find_element(By.XPATH, self.fede_drp_sta_sel_xpath).click()
        self.driver.find_element(By.XPATH, self.fede_exemption_xpath).send_keys(fedexamption)
        self.driver.find_element(By.XPATH, self.state_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.state_drp_select_xpath).click()
        self.driver.find_element(By.XPATH, self.status_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.status_drp_select_xpath).click()
        self.driver.find_element(By.XPATH, self.state_txt_input).send_keys(stateexemption)
        self.driver.find_element(By.XPATH, self.unemp_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.unemp_select_xpath).click()
        self.driver.find_element(By.XPATH, self.work_state_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.work_select_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.tax_save_xpath).click()

    def report_to(self,suprname,subname):
        self.driver.find_element(By.XPATH,self.click_report).click()
        self.driver.find_element(By.XPATH,self.add_report).click()

        self.driver.find_element(By.XPATH,self.add_supervisr_name).send_keys(suprname)

        self.driver.find_element(By.XPATH,self.select1_name).click()
        self.driver.find_element(By.XPATH,self.drp_reporting_method).click()
        self.driver.find_element(By.XPATH,self.select_reporting_method).click()
        self.driver.find_element(By.XPATH,self.save_supervisor).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.add_suborinate_path).click()
        self.driver.find_element(By.XPATH,self.subordinate_name).send_keys(subname)
        self.driver.find_element(By.XPATH,self.select2_name).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,self.drp_reporting1_method).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.select_report_method).click()
        self.driver.find_element(By.XPATH,self.save_subordinate).click()


    def qualification_wrk_experience(self,company,jobtitle,fromdate,todate,comments):
        self.driver.find_element(By.XPATH,self.click_qualification).click()
        self.driver.find_element(By.XPATH,self.add_work_exp).click()
        self.driver.find_element(By.XPATH,self.wrkexp_add_cmpny).send_keys(company)
        self.driver.find_element(By.XPATH,self.wrkexp_job_title).send_keys(jobtitle)
        self.driver.find_element(By.XPATH,self.from_xpath).send_keys(fromdate)
        self.driver.find_element(By.XPATH,self.to_xpath).send_keys(todate)
        self.driver.find_element(By.XPATH,self.wrkexp_comments).send_keys(comments)
        self.driver.find_element(By.XPATH,self.save_work_exp).click()

    def qualification_education(self,institute,major,year,gpa,startdate,enddate):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.add_education).click()
        self.driver.find_element(By.XPATH,self.leve_path).click()
        self.driver.find_element(By.XPATH,self.select_level_path).click()
        self.driver.find_element(By.XPATH,self.institute_path).send_keys(institute)
        self.driver.find_element(By.XPATH,self.major_path).send_keys(major)
        self.driver.find_element(By.XPATH,self.year_path).send_keys(year)
        self.driver.find_element(By.XPATH,self.gpa_path).send_keys(gpa)
        self.driver.find_element(By.XPATH,self.start_date_path).send_keys(startdate)
        self.driver.find_element(By.XPATH,self.end_date_path).send_keys(enddate)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.save_education).click()
    def qualification_skills(self,yearofexp,comments):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.add_skills).click()
        self.driver.find_element(By.XPATH,self.drp_skill_path).click()
        self.driver.find_element(By.XPATH,self.select_skill_path).click()
        self.driver.find_element(By.XPATH,self.year_of_experience).send_keys(yearofexp)
        self.driver.find_element(By.XPATH,self.skill_comments).send_keys(comments)
        self.driver.find_element(By.XPATH,self.save_skills).click()

    def qualification_language(self,comments):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.add_language_button).click()
        self.driver.find_element(By.XPATH,self.drp_language_xpath).click()
        self.driver.find_element(By.XPATH,self.select_language).click()
        self.driver.find_element(By.XPATH,self.drp_fluency).click()
        self.driver.find_element(By.XPATH,self.select_fluency).click()
        self.driver.find_element(By.XPATH,self.drp_competency).click()
        self.driver.find_element(By.XPATH,self.select_competency).click()
        self.driver.find_element(By.XPATH,self.language_comments).send_keys(comments)
        self.driver.find_element(By.XPATH,self.save_language).click()
    def qualification_license(self,licenseno,issueddate,expirydate):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.add_license).click()
        self.driver.find_element(By.XPATH,self.license_type).click()
        self.driver.find_element(By.XPATH,self.select_license_type).click()
        self.driver.find_element(By.XPATH,self.license_no_xpath).send_keys(licenseno)
        self.driver.find_element(By.XPATH,self.license_issued_date).send_keys(issueddate)
        self.driver.find_element(By.XPATH,self.license_expiry_date).send_keys(expirydate)
        self.driver.find_element(By.XPATH,self.save_license).click()
    def membership(self,supsamount,supscommencedate,renewaldate):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.add_membership).click()
        self.driver.find_element(By.XPATH, self.mem_add_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_memership_xpath).click()
        self.driver.find_element(By.XPATH, self.mem_drp_xpath).click()
        self.driver.find_element(By.XPATH, self.drp_subscription_xpath).click()
        self.driver.find_element(By.XPATH, self.mem_subscription_xpath).click()
        self.driver.find_element(By.XPATH, self.subscription_amt_xpath).send_keys(supsamount)
        self.driver.find_element(By.XPATH, self.drp_currency_xpath).click()
        self.driver.find_element(By.XPATH, self.mem_currency_xpath).click()
        self.driver.find_element(By.XPATH, self.sub_commence_date_xpath).send_keys(supscommencedate)
        self.driver.find_element(By.XPATH, self.sub_renewal_date_xpath).send_keys(renewaldate)
        self.driver.find_element(By.XPATH, self.membership_save_xpath).click()
        time.sleep(5)

    def Admin_add(self,username1,password1,cnfrmpassword,empname):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.Admin_click_path).click()
        self.driver.find_element(By.XPATH,self.add_admin_path).click()
        self.driver.find_element(By.XPATH,self.drp_userrole_path).click()
        self.driver.find_element(By.XPATH,self.click_user_role).click()
        element = self.driver.find_element(By.XPATH,self.emp_name_path)
        element.send_keys(empname)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.click_emp_name).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.drp_status_path).click()
        self.driver.find_element(By.XPATH,self.click_status_path).click()
        self.driver.find_element(By.XPATH,self.username_path).send_keys(username1)
        self.driver.find_element(By.XPATH,self.password_path).send_keys(password1)
        self.driver.find_element(By.XPATH, self.confirm_password).send_keys(cnfrmpassword)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.save_admin).click()

    def search_user_name(self,Username):
        time.sleep(10)
        self.driver.find_element(By.XPATH,self.username1_path).send_keys(Username)
        self.driver.find_element(By.XPATH,self.search_button).click()

    def check_customer_added(self):
        return self.driver.find_element(By.XPATH,self.name_search).text
    def logout(self):
        self.driver.find_element(By.XPATH,self.click_profile).click()
        self.driver.find_element(By.XPATH,self.logout_path).click()
        time.sleep(5)

    def Again_login(self,username2,password2):
        self.driver.find_element(By.XPATH,self.txtbx1_email_xpath).send_keys(username2)
        self.driver.find_element(By.XPATH,self.txtbx1_password_xpath).send_keys(password2)
        self.driver.find_element(By.XPATH,self.btn1_login_button).click()