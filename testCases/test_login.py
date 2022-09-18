from PageObjects.loginpage import Login
from utilities import customlogger

class Test_1:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

#pim
    firstname = "kalai"
    lastName = "vani"

#personal details
    otherid = "123"
    licenseno = "456"
    expirydate = "2025-05-10"
    ssn = "867"
    sin = "909"
    dob = "1998-08-17"
    militaryservice = "no"
#contact details
    street1 = "No.6,vinayager kovil street"
    street2 = "vengathur village"
    city = "Thiuvallur "
    state = "Tamilnadu"
    pincode = "602002"
    homephno = "9784356920"
    mobileno = "9865436789"
    work = "12345"
    email = "admin57@gmail.com"
    otheremail = "klph@gmail.com"
#emergency details
    name = "deepa"
    relationship = "Mother"
    mobileno = "7895306459"
    workno = "9004683432"
#dependent
    name="deepa"
    relation = "child"
    dob = "2019-5-8"
#immigration
    number = "9087634909"
    issueddate = "2010-05-10"
    expirydate = "2025-05-10"
    eligiblestatus = "Eligible"
    reviewdate = "2020-05-10"
    command = "success"
#job
    joineddate = "2015-09-7"
#salary details
    salcomponent = "hike"
    amount1 = "40000"
    comments = "this is my ssl"
    acountno = "123456789743"
    routingno = "564"
    amount2 = "40000"
#tax
    fedexamption = "23"
    stateexemption = "34"
#report to
    suprname = "a"
    subname = "Pe"

#qualification(workexperience)
    company = "abcorganisation"
    jobtitle = "adminofficer"
    fromdate = "2020-01-10"
    todate = "2022-01-10"
    comments= "this is my work experience"
#qualification(eduction)
    institute ="pbccollege"
    major = "ece"
    year = "2019"
    gpa = "90"
    startdate = "2015-05-10"
    enddate = "2019-05-10"
#qualification(skills)
    yearofexp = "2"
    comments = "skills i haved"
#qualification(language)
    comments = "laguages i known"
#qualification(license)
    licenseno = "309"
    issueddate = "2015-05-10"
    expirydate = "2025-05-10"

#membership
    supsamount = "20000"
    supscommencedate = "2020-05-10"
    renewaldate = "2025-05-10"
#admin
    empname = "kalai"
    username1 = "vaniNK199817"
    password1 ="K@l@!v@n!1"
    cnfrmpassword = "K@l@!v@n!1"
#search
    Username = "vaniNK199817"
#again login
    username2="vaniNK199817"
    password2="K@l@!v@n!1"
    logger = customlogger.test_logDemo()
    def test_user_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        loginPageObj = Login(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        loginPageObj.setlogin(self.username,self.password)
        loginPageObj.pim(self.firstname,self.lastName)
        self.logger.info("************* New employee is Added ***********")
        loginPageObj.peronal_details(self.otherid,self.licenseno,self.expirydate,self.ssn,self.sin,self.dob,self.militaryservice)
        self.logger.info("------ Personal Details is Added ---------")
        self.driver.execute_script("window.scrollBy(0,-2000)", "")
        loginPageObj.contact_details(self.street1,self.street2,self.city,self.state,self.pincode,self.homephno,self.mobileno,self.work,self.email,self.otheremail)
        self.logger.info("------ Contact  Details is Added ---------")
        loginPageObj.Emergency_details(self.name,self.relationship,self.mobileno,self.workno)
        self.logger.info("------ Emergency  Details is Added ---------")
        loginPageObj.Dependend(self.name,self.dob)
        self.logger.info("------ dependent is Added ---------")
        loginPageObj.immigration(self.number,self.issueddate,self.expirydate,self.eligiblestatus,self.reviewdate,self.command)
        self.logger.info("------ Immigration details are  is Added ---------")
        loginPageObj.job_details(self.joineddate)
        self.logger.info("------ job details is Added properly---------")
        loginPageObj.salary_details(self.salcomponent,self.amount1,self.comments,self.acountno,self.routingno,self.amount2)
        self.logger.info("------ salary details also Added properly---------")
        loginPageObj.tax_details(self.fedexamption,self.stateexemption)
        self.logger.info("------ tax details also Added properly---------")
        loginPageObj.report_to(self.suprname, self.subname)
        self.logger.info("------ report also included--------")
        loginPageObj.qualification_wrk_experience(self.company,self.jobtitle,self.fromdate,self.todate,self.comments)
        self.logger.info("-----qualification work experience is added------")
        loginPageObj.qualification_education(self.institute,self.major,self.year,self.gpa,self.startdate,self.enddate)
        self.logger.info("--------- qualificatin education is added-----------")
        loginPageObj.qualification_skills(self.yearofexp,self.comments)
        self.logger.info("-------qualification skills  are added properly------")
        loginPageObj.qualification_language(self.comments)
        self.logger.info("------- qualification language is added------")
        loginPageObj.qualification_license(self.licenseno,self.issueddate,self.expirydate)
        self.logger.info("--------qualification license is added----------")
        self.driver.execute_script("window.scrollBy(0,-2000)", "")
        loginPageObj.membership(self.supsamount,self.supscommencedate,self.renewaldate)
        self.logger.info("---------- membership is added---------")

        loginPageObj.Admin_add(self.username1, self.password1, self.cnfrmpassword, self.empname)
        self.logger.info("--------- admin added------------")
        loginPageObj.search_user_name(self.Username)
        username = loginPageObj.check_customer_added()
        print(username)
        if username == "vaniNK199817":
            self.logger.info("--- the username is correct------")
            print("customer successfully added")
        else:
            self.logger.info("------ the username is wrong--------------")
            print("customer not added")
        loginPageObj.logout()

    def test_Admin(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        loginPageObj = Login(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        loginPageObj.Again_login(self.username2, self.password2)